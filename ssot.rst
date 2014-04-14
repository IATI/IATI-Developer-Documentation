IATI Standard (Single Source of Truth)
======================================

From 1.04, the IATI Documentation of the IATI Standard will be built from a "Single Source of Truth" (SSOT), which consists of several GitHub repositories.

See also, the original :doc:`proposal <ssot/proposal>`.

.. toctree::
   :hidden:

   ssot/proposal

Repositories
------------

* `IATI-Standard-SSOT <https://github.com/IATI/IATI-Standard-SSOT>`__ the main SSOT repository, which contains the following as submodules:
    - `IATI-Extra-Documentation <https://github.com/IATI/IATI-Extra-Documentation>`__
    - `IATI-Schemas <https://github.com/IATI/IATI-Schemas>`__
    - `IATI-Codelists <https://github.com/IATI/IATI-Codelists>`__
    - `IATI-Rulesets <https://github.com/IATI/IATI-Rulesets>`__

In addition there are codelists in another repository `IATI-Codelists-NonEmbedded <https://github.com/IATI/IATI-Codelists-NonEmbedded>`__ which are not Embedded, that is any changes to them do not need to go through the Update process. Since it is versioned seperately, this is not a submodule of the IATI-Standard-SSOT repository.

The documentation on http://dev.iatistandard.org/ is then built then built from the contents of these repositories, and also two repositories containing documentation that is not specific to a particular version of the standard: `IATI-Guidance <https://github.com/IATI/IATI-Guidance>`__ and `IATI-Developer-Documentation <https://github.com/IATI/IATI-Developer-Documentation>`__.

Finding a specific version of the SSOT
--------------------------------------

This can be done via:

* branches, which may change for typos and bugfixes e.g. ``version-1.04``, see :ref:`ssot-branches`
* tags, which point to the exact commit on the day of release e.g. ``v1.04``, see :ref:`ssot-tags`

Versions prior to 1.04
----------------------

Prior to 1.04 the only github repository was IATI-Schemas, so this is the only repository with tags and branches for 1.01, 1.02 and 1.03.

