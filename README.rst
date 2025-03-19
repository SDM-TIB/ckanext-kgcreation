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

4. Set up Enviroment Variables in the ``.env`` file. ``CKAN_KG_DOMAIN`` sets the value 
   for the Domain of knowledge graph. ``ENDPOINT_URL`` sets the value of the url of
   the endpoint. For ``ENDPOINT_URL``, only add the domain and port (i.e. http://localhost:8890/) including the slash (/).

5. When using the Docker image for CKAN and a docker container endpoint, you can specify the endpoint's URL using the
   container name of the endpoint, i.e., ``ENDPOINT_URL=http://endpoint:8890/`` where ``endpoint`` is the container's name.

6. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

.. Note:: ``ckanext-kgcreation`` assumes that the to be generated knowledge graph runs in Virtuoso.
