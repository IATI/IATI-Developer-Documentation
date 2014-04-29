Non-IATI specific tools
=======================

Wget
----

Wget is a common tool used for downloading files, including IATI data.

.. _wget-issues:

Issues
^^^^^^

* The version of Wget in Debian stable is compiled against an older version of gnutls that fails on certain https links. Update your version of libgnutls if this is a concern. However, the one publisher with a failing https link has now changed their setup such that this is no longer an issue.

* By Default Wget assumes that your filesystem can't handle unicode, and does not save unicode filenames properly. To force it to do so, use the ``--restrict-file-names=nocontrol`` flag.

* Some servers block Wget's user agent. A different user agent can be supplied with -U, but these are also sometimes blocked. (See also :ref:`block_user_agents`)

* Older versions of Wget (e.g. 1.13.4) do not timeout properly if the connection hangs during an SSL/TLS certificate handshake. Additionally, even in the newest versions of Wget, timeout behaviour varies depending on which SSL/TLS library is linked against. For timeouts during an SSL/TLS handshake, the flag ``--read-timeout`` is needed if Wget is linked against OpenSSL, whereas ``--connect-timeout`` is needed if Wget is linked against GNUTLS.

BaseX
-----

BaseX is an XML database, with a cross platform GUI. It's useful for running XQuery, see :ref:`xquery`.
