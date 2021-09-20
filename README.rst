IATI Developer Documentation
============================

Note that this documentation is currently being put together, and is not very complete. For further developer information see the `IATI wiki <http://wiki.iatistandard.org/>`_.

Viewing the Documentation
-------------------------

You can view this documentation at http://iatistandard.org/developer/ - or here on github.

Building the Documentation
--------------------------
Clone the repo:

.. code-block:: bash

   git clone git@github.com:IATI/IATI-Developer-Documentation.git

Set up a virtual environment:

.. code-block:: bash

   # Create a virtual environment (recommended)
   python3 -m venv pyenv

   # Activate the virtual environment if you created one
   # This must repeated each time you open a new shell
   source pyenv/bin/activate

   # Install python requirements (this includes Sphinx)
   pip install -r requirements.txt

This documentation uses `Sphinx <https://www.sphinx-doc.org/en/master/>`_ to 'compile' the documentation into HTML (and potentially other formats).

.. code-block:: bash

   make html

HTML documentation can then be found in the ``_build/html`` folder.

Editing the documentation
-------------------------

Fork this repository on github, edit the files, and send us a pull request. If this is too complicated, then `report an issue <https://github.com/IATI/IATI-Developer-Documentation/issues>`_ with your suggested change.

The files are in reStructuredText format, see the `Sphinx reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ for more information.
