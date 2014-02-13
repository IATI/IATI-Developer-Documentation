Non-IATI specific tools
=======================

Wget
----

Wget is a common tool used for downloading files, including IATI data.

Issues
^^^^^^

* The version of wget in Debian stable is compiled against an older version of gnutls that fails on certain https links. Update your version of libgnutls if this is a concern. However, the one publisher with fialing https link has now changed their setup such that this is no longer an issue.

* By Default wget assumes that your filesystem can't handle unicode, and does not save unicode filenames properly. To force it to do so, use the --restrict-file-names=nocontrol flag.

* Some servers block wget's user agent. A different user agent can be supplied with -U, but I've also had these blocked.

BaseX
-----

BaseX is an XML database, with a cross platform GUI. It's useful for running xquery, see :ref:`xquery`.
