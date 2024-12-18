=============
ckanext-kgcreation
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!

``ckanext-kgcreation`` is a CKAN plugin that adds the ability to generate RDF triples from datasets, services, resources, and organization.
KGCreation uses SDM-RDFizer (https://github.com/SDM-TIB/SDM-RDFizer) as a knowledge graph creation engine.

------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-kgcreation:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-LDM_SPARQL Python package into your virtual environment::

     pip install ckanext-kgcreation

3. Add ``kgcreation`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/ckan.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


