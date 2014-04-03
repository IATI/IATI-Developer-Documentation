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

* Older versions of wget (e.g. 1.13.4) do not timeout properly if the connection hangs during the SSL/TLS certificate handshake. Additionally, even in the newest versions of wget, timeout behaviour varies depending on that SSL/TLS library is linked against. For timeouts during the handshake, the flag `--read-timeout` is needed if wget is linked against OpenSSL, whereas `--connect-timeout` is needed if wget is linked against GNUTLS.

BaseX
-----

BaseX is an XML database, with a cross platform GUI. It's useful for running xquery, see :ref:`xquery`.
