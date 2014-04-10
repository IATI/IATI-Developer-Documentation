IATI Standard (Single Source of Truth)
======================================

From 1.04, the IATI Documentation of the IATI Standard will be built from a "Single Source of Truth" (SSOT), which consists of several GitHub repositories.

Repositories
------------

* `IATI-Standard-SSOT <https://github.com/IATI/IATI-Standard-SSOT>`__ the main SSOT repository, which contains the following as submodules:
    - `IATI-Extra-Documentation <https://github.com/IATI/IATI-Extra-Documentation>`__
    - `IATI-Schemas <https://github.com/IATI/IATI-Schemas>`__
    - `IATI-Codelists <https://github.com/IATI/IATI-Codelists>`__
    - `IATI-Rulesets <https://github.com/IATI/IATI-Rulesets>`__

In addition there are codelists in another repository `IATI-Codelists-NonEmbedded <https://github.com/IATI/IATI-Codelists-NonEmbedded>`__ which are not Embedded, that is any changes to them do not need to go through the Update process. Since it is versioned seperately, this is not a submodule of the IATI-Standard-SSOT repository.

The documentation on http://dev.iatistandard.org/ is then built then built from the contents of these repositories, and also two repositories containing documentation that is not specific to a particular version of the standard: `IATI-Guidance <https://github.com/IATI/IATI-Guidance>`__ and `IATI-Developer-Documentation <https://github.com/IATI/IATI-Developer-Documentation>`__.

Branches
--------

There is no master branch, since the IATI Update process means that a "general development" branch is not really appropriate. Instead there is a branch for each version of the standard - both those that have been released, and those that are in development. These are named ``version-<version number>``, e.g. ``version-1.04`` and ``version-2.01``.

Any changes that need review should be done on feature branches.

Tags
----

Versions prior to 1.03
----------------------

These are not properly included in the Github based SSOT.

Rationale
---------

Why github?
^^^^^^^^^^^

Why multiple repositories?
^^^^^^^^^^^^^^^^^^^^^^^^^^
