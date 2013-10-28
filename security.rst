Security considerations
=======================

When building tools for IATI data therea are several secruity issues to be aware
of.

XML
---

When parsing XML, you should be aware of entity based attacks.

User Supplied Files
-------------------

You should make sure that

* user supplied files aren't executable (e.g. if a php file is uploaded to the
  web directory)

Fetching Remote Files
^^^^^^^^^^^^^^^^^^^^^

Working with IATI Data often involves fetching data from arbitary urls. You
should check

* The URLs don't begin file:// as this will expose data on the local filestyem
* The URLs can't point at any senstive local HTTP(S) services


