Problems Accessing IATI Data
============================

This page details some of the common problems that developers face when accessing IATI Data, and how they can avoid some of the problems. It also provides suggestions for publishers to ensure their data is easy to access.

.. contents::

HTTPS
-----

Some publishers place their files on servers behind secure certificates. This can cause data consumers problems for a number of reasons.

Publishers can avoid these problems by not using HTTPS, although this means losing all the advantages of HTTPS. Alternatively, they should ensure that HTTPS is configured correctly, and that intermediary certificates are sent etc.

Verifying Certificates
^^^^^^^^^^^^^^^^^^^^^^

Sometimes the problem lies with verifying the certificate. This can be due to an out of date list of Certificate Authorities (CAs) on the client side, or certificate misconfiguration by the publisher.

In the first case, the client should ideally update their CA list, but this can be quite cumbersome to do.

In the case of publisher misconfiguration, this should be fixed by the publisher, but this may be difficult for us to detect and demonstrate to them, because problematic certificates may work in some applications (especially web browsers). A common problem is that the intermediary certificate is not supplied by the server.

One way for a data consumer to sidestep this problem problem, is by not verifying HTTPS certificates, but this is not an ideal response. For wget this can be achieved with the `--no-check-certificate` flag. `IATI-Registry-Refresher <https://github.com/IATI/IATI-Registry-Refresher>`__, which powers the Dashboard, uses this approach. The registry, on the other hand, does try to verify certificates when fetching metadata about a file.

Current issues:

* Intermediary certificate not supplied by server - http://data.tickets.iatistandard.org/ticket/191


Protocol Errors
^^^^^^^^^^^^^^^

Some servers have bugs in their TLS/SSL implementation. This can cause some confusing errors, because different clients may/may not have a problem with this. Currently there are no known issues of this type.

Some clients have bugs in their TLS/SSL implementation. :ref:`One such bug was encountered with Wget <wget-issues>`, but could be fixed by upgrading the software.


Connection Hangs
^^^^^^^^^^^^^^^^

Sometimes servers are misconfigured such that the connection hangs during the SSL/TLS handshake.

Wget provides flags for supplying a time out in such a case, but the relevant flag differs depending on the crypto library used, see :ref:`Wget Issues <wget-issues>`.

Currently there are no known issues of this type. Previous problems:

* https://groups.google.com/forum/#!msg/iati-technical/oHu8alQJxZQ/C-aJWw4BB-oJ

.. _block_user_agents:

Blocking User Agents
--------------------

Some publishers' web servers will block certain user agents, and sometimes IP addresses. This is probably a result of automated systems looking for "malicious" activity. This blocking is problematic, because one of the strengths of IATI data is that it can be programmatically downloaded.

Server Side Caching
-------------------

Some publishers' data is served behind caching software, most commonly `Varnish <https://www.varnish-cache.org/>`__. This can be problematic, because the most recent version may not be served.
