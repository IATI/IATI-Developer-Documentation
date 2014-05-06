IATI Developer Documentation
============================

Note that this documentation is currently being put together, and is not very complete. For further developer information see the `IATI wiki <http://wiki.iatistandard.org/>`_.

Viewing the Documentation
-------------------------

You can view this documentation at http://iatistandard.org/developer/ - or here on github.

Building the Documentation
--------------------------

This documentation uses `Sphinx <http://sphinx-doc.org/>`_ to 'compile' the documentation into HTML (and potentially other formats). To do this on your own machine first install Sphinx (e.g. using your package manager), then:

.. code-block:: bash

   git clone git@github.com:IATI/IATI-Developer-Documentation.git
   make html

HTML documentation can then be found in the ``_build/html`` folder.

Editing the documentation
-------------------------

Fork this repository on github, edit the files, and send us a pull request. If this is too complicated, then `report an issue <https://github.com/IATI/IATI-Developer-Documentation/issues>`_ with your suggested change.

The files are in reStructuredText format, see the `Sphinx reStructuredText Primer <http://sphinx-doc.org/rest.html>`_ for more information.
