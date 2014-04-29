IATI Code
=========

.. toctree::
   code-checklist
   :hidden:

What is IATI Code?
------------------

IATI Code is defined as code that the IATI Technical Team look after directly.

This may be custom code that has been written specifically to perform
tasks for IATI, or it could be 'off the shelf' code that we need to
maintain and update in order for it run smoothly. Some of it will be
standalone applications, some of it could be customisations to other
people's projects/code.

Some code directly powers projects/web applications. Other code may be
command line tools that, for example, process IATI data locally, or that
are 'recipes' for API's such as for communicating with the CKAN API.

There may also be code that the IATI team does not own, but makes a
commitment to contributing to. We should also bear this in mind when
talking about IATI code.

It is important for IATI to work out which code it is responsible for
resourcing.

So which code are we talking about?
-----------------------------------

Generally IATI Code can be found here:
https://github.com/IATI

There may be rare instances of code that have yet to make it into the
GitHub organisation account, but it is our desire and intention for all
IATI code to be there.

Code Checklist
--------------

We have agreed a set of 'coding principles', which provide a framework
that allows us to check that our code is being well managed. As such we
are able to audit each project that we maintain against our :doc:`IATI Code
Checklist <code-checklist>`.

Managing Code
-------------

Since we are clear about which code is ours to nurture, and with a
framework in place against which we test the health of our code, we want
to make sure our code is:

-  transferable - i.e. it could easily be handed over, or new staff
   could quickly understand it.
-  sustainable - i.e. properly resourced, future proofed, planned
-  well managed - i.e. our code is working for us

The following lays out some detail about how the IATI Technical Team has
chosen to work in order to achieve this.

GitHub
------

GitHub provides a place to 'host' code within a well known structure,
with access to key tools for managing that code:

-  issues
-  milestones
-  version control

etc - most of the things an open source code project needs (See
:ref:`code_communication` below)

Domains
-------

IATI Code often needs to be deployed on a web address. In the past IATI
has suffered from having multiple domains and it has been hard for
people to know where to find things.

Our current practices is to try to consolidate our applications,
services, etc onto iatistandard.org where practically possible.
Preferably we should be using subdomains.

Why subdomains?
^^^^^^^^^^^^^^^

When it comes to putting our work on the web we have a choice of
using subdirectories, subdomains, or a new domain.

The problem with subdirectories (e.g. /validator, /query) won't work
well as different applications need different hosting requirements.
We're always going to need to 'point' at other servers. Subdirectories
could proxy (but this is not good) or redirect (also not really very
good) to other URLs.

The problem with domains is that applications and services can end up in
many different places and therefore hard to find. New domains can be
useful to distance applications from iatistandard if needed.

Licensing
---------

IATI Code should be appropriately licensed.

Licences should be 'open' to allow re-use. The choice of licence is
something to be discussed for each project.

Documentation licensing is also important.

Branding
--------

IATI does not currently have a coherent policy on branding, but there
are some established conventions that can be followed for code 'owned' by the
Technical Team - e.g. there is a logo.

.. _code_communication:

Communicating
-------------

The IATI Technical Team needs to talk about the development of IATI Code
within the team, with other developers, bug reporters, and users of the
software.

Internally we need to talk about our code, projects, tasks, bugs, etc -
we may use third party services e.g. google group, or install third
party tools that we manage in order to do this (e.g. trac).

Current communication options with other audiences are via:

-  the IATI TAG google group,
-  the IATI Announce google group, and
-  via GitHub 'issues'
-  #iati on IRC Freenode
-  blog at `http://iati.github.io/ <http://iati.github.io/>`__

Workplans
---------

Each piece of code should have a workplan. This should be carried out
via GitHub in the form of milestones and issues, wherever possible,
keeping development, bugs etc in the public domain.

