# ckanext-kgcreation

``ckanext-kgcreation`` is a CKAN plugin that adds the ability to generate RDF triples from datasets, services, resources, and organization.
KGCreation uses SDM-RDFizer (https://github.com/SDM-TIB/SDM-RDFizer) as a knowledge graph creation engine.

## Installation

To install ckanext-kgcreation:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-kgcreation Python package into your virtual environment::

     pip install ckanext-kgcreation

3. Add ``kgcreation`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/ckan.ini``).

4. Set up environment variables in the ``.env`` file. ``CKAN_KG_DOMAIN`` sets the value 
   for the Domain of knowledge graph. ``ENDPOINT_URL`` sets the value of the url of
   the endpoint. For ``ENDPOINT_URL``, only add the domain and port (i.e. http://localhost:8890/) including the slash (/).

5. When using the Docker image for CKAN and a docker container endpoint, you can specify the endpoint's URL using the
   container name of the endpoint, i.e., ``ENDPOINT_URL=http://endpoint:8890/`` where ``endpoint`` is the container's name.

6. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

7. Set environment variables

   7.1 `CKAN_KG_DOMAIN`: the domain for knowledge graph. For example, https://research.tib.eu/ldm.

   7.2 `SUB_KG_STORAGE`: indicates if the individual triples of each dataset will be stored outside the knowledge graph. This is for the representation of the metadata in multiple formats. This is optional. This can be "True" or "False". If not given, it will consider false by default.

   7.3 `SHOW_EXPORT`: indicates if metadata export options should be shown on the dataset page. Requires `SUB_KG_STORAGE` to be set to "True". This is optional. This can be "True" or "False". If not given, it will consider false by default.

> [!NOTE]
> ``ckanext-kgcreation`` assumes that the to be generated knowledge graph runs in Virtuoso.

