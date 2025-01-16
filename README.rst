=============
ckanext-kgcreation
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!

``ckanext-kgcreation`` is a CKAN plugin where the user is able to extend CSV datasets with existing information in the Wikidata KG. The tool applies entity linking to all concepts in the same column and enable the user to use the extracted entities to extend the dataset.


------------
Installation
------------



To install ckanext-kgcreation:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-LDM_SPARQL Python package into your virtual environment::

     pip install ckanext-falcon

3. Add ``falcon`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/ckan.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


