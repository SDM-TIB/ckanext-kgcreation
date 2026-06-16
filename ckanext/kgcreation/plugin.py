import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.kgcreation import kgcreation_cli
from ckanext.kgcreation.RDFizer_Util import RDFizer_Util
from ckanext.kgcreation.Virtuoso_Util import Virtuoso_Util
from ckan.model.group import Group
from ckan.plugins.interfaces import IDomainObjectModification
import os

import ckanext.kgcreation.dcat_utils as utils
from flask import Blueprint

import logging
log = logging.getLogger(__name__)
# HELPERS
# *******
def get_virtuoso_endpoint_URL():
    virtuoso_util = Virtuoso_Util()
    return virtuoso_util.get_virtuoso_endpoint_URL()

def get_detrusty_endpoint_URL():
    virtuoso_util = Virtuoso_Util()
    return virtuoso_util.get_detrusty_endpoint_URL()

def get_pubby_URL_for_dataset(ds_dict):
    virtuoso_util = Virtuoso_Util()
    return virtuoso_util.get_pubby_URL_for_dataset(ds_dict)


def get_show_export():
    """Helper function to check whether the metadata export options should be shown.

    The export options are only shown if the metadata of each dataset are stored.
    """
    if bool(os.getenv('SUB_KG_STORAGE')):
        return bool(os.getenv('SHOW_EXPORT'))

# ***************



class KGCreationPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IClick)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IOrganizationController, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IBlueprint)

    ## IClick
    def get_commands(self):
        return kgcreation_cli.get_commands()

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'kgcreation')

    ## IPackageController
    def after_create(self, context, pkg_dict):
        virtuoso_util = Virtuoso_Util()
        dataset_name = pkg_dict['name']

        # check if dataset is active and public and PUSH DCAT RDF to Virtuoso
        # Is this active and public?
        if virtuoso_util.dataset_should_be_included_in_graph(pkg_dict):
            dataset_name = pkg_dict['id']
            virtuoso_util.create_dataset_in_LDM(dataset_name)

    ## IPackageController
    def after_update(self, context, pkg_dict):
        '''Dataset has been created/updated. Check status of the dataset to determine if we should
        publish DOI to datacite network.
        (Note that the create method will return a dataset domain object, which may not include all fields)
        '''

        # Generate DCAT RDF nt
        virtuoso_util = Virtuoso_Util()
        dataset_name = pkg_dict['name']

        # check if dataset is active and public and PUSH DCAT RDF to Virtuoso
        # Is this active and public?
        if virtuoso_util.dataset_should_be_included_in_graph(pkg_dict):
            dataset_name = pkg_dict['id']
            virtuoso_util.update_dataset_in_LDM(dataset_name)

        return pkg_dict

    ## IOrganizationController
    def edit(self, org):
        # This is called even in Dataset change and in that case
        # the organization metadata can't be changed
        try:
            organization = toolkit.get_action('organization_show')(data_dict={'id': org.id})
            virtuoso_util = Virtuoso_Util()
            virtuoso_util.update_organization_in_graph(org.id)
        except toolkit.ObjectNotFound:
            pass

    def create(self, org):

        # This is called even in Dataset change and in that case
        # the organization metadata can't be changed
        try:
            organization = toolkit.get_action('organization_show')(data_dict={'id': org.id})
            virtuoso_util = Virtuoso_Util()
            virtuoso_util.create_organization_in_graph(org.id)
        except toolkit.ObjectNotFound:
            pass

    def get_helpers(self):
        '''Register the show_object_icon_in_package_item() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {
            'ldmsparql_get_virtuoso_endpoint_url': get_virtuoso_endpoint_URL,
            'ldmsparql_get_detrusty_endpoint_url': get_detrusty_endpoint_URL,
            'ldmsparql_get_pubby_URL_for_dataset': get_pubby_URL_for_dataset,
            'kgcreation_show_export': get_show_export,
        }

    def get_blueprint(self):
        u'''Return a Flask Blueprint object to be registered by the app.'''

        # Create Blueprint for plugin
        blueprint = Blueprint(self.name, self.__module__,)
        blueprint.template_folder = u'templates'

        # 1. rdf/xml
        # 2. xml
        # 3. n3
        # 4. ttl
        # 5. jsonld
        def download_dataset(_id, _format):
            file_format = _format

            if file_format == "rdf":
                return utils.download_dataset_rdf(_id)
            elif file_format == "xml":
                return utils.download_dataset_xml(_id)
            elif file_format == "n3":
                return utils.download_dataset_n3(_id)
            elif file_format == "ttl":
                return utils.download_dataset_ttl(_id)
            elif file_format == "jsonld":
                return utils.download_dataset_jsonld(_id)
            else:
                # If the format doesn't match, return a clean 404 page
                toolkit.abort(404, f"Format {file_format} is not supported.")

        # TODO figure out how to handle vdataset and service
        # Add plugin url rules to Blueprint object
        rules = [
            (u'/dataset/<_id>.<_format>', u'download_dataset', download_dataset),
            (u'/vdataset/<_id>.<_format>', u'download_dataset', download_dataset),
            (u'/service/<_id>.<_format>', u'download_dataset', download_dataset)
        ]

        for rule in rules:
            blueprint.add_url_rule(*rule)

        return blueprint
