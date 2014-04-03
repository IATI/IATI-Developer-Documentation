IATI Code Checklist
^^^^^^^^^^^^^^^^^^^

About
=====

Our code checklist is based on a set of principles that provide a
framework against which code projects can be measured.

It may help to read each item as a question (that we should know the
answer to).

E.g. Is this 'our' code? Is it on our server? Does it have a licence?
etc.

The creation of this checklist allows us to:

-  communicate with new team members, external contractors,  other
   developers, about the way we do things.
-  allows us to audit current projects to find and fix gaps
-  allows us to test new work against the framework to make sure all the
   bases are covered.

Project Checklists
==================

* `IATI-Dashboard <https://github.com/IATI/IATI-Dashboard/blob/master/CHECKLIST.rst>`_


The checklist
=============

We should know which code is 'ours'
-----------------------------------

Generally IATI Code can be found here: https://github.com/IATI

There may be rare instances of code that have yet to make it into the
GitHub organisation account, but it is our desire and intention for all
IATI code to be there.

All code should have a lead person identified
---------------------------------------------

Our projects/code should be appropriately branded.
--------------------------------------------------

Our code/projects should be in version control and present links to issue trackers and source code.
---------------------------------------------------------------------------------------------------

Usually this would be in our GitHub Organisation

Code in development, where possible should also be in our GitHub
account.

If code is speculative, potentially sensitive, or has just not been
given the green light our current practice is to build it in private or
in personal developers own online repositories (GitHub, BitBucket, etc).

Each piece of code should have a document, a roadmap, and estimate of resources, and a licence.
-----------------------------------------------------------------------------------------------

Generally we're probably using a open source or free software compatible
licence.

There will usually be discussion as to whether or not we use a
permissive or copyleft licence.

We should be confident that updates to our code will not break existing functionality
-------------------------------------------------------------------------------------

Deployment of new features, especially in feature rich environments, or
of new website configurations has the potential to mess up existing
data, layouts, functionality.

Writing tests is one way of checking that large application are still
doing what they are supposed to be doing.

Does this mean everything should have a suite of tests? Probably!

It should make sense in the way people access our tools/code
------------------------------------------------------------

 - i.e. domains should make sense

- code should be kept in one place e.g. GitHub organisation

Our code should be on our servers
---------------------------------

We should be able to monitor the performance of those servers

We should be able to monitor the performance of the software

Development versions should be clearly labelled when publicly available
-----------------------------------------------------------------------

Much of our code is deployed on development servers. Some of it is actively shared (i.e. we email people links, talk about it openly), other stuff is thrown up for testing. It should be clear to visitors to those versions that they are looking at/using a development version of the software.

We should know how our code is being used - logs!
-------------------------------------------------

Issues:

Are we gathering and making use of:

- server analytics

- google analytics

- built in loggers

Our code will need to adapt with schema changes and changes to external systems upon which it relies
----------------------------------------------------------------------------------------------------

- e.g. if the datastore, or the registry change then our code should
  also change

- when creating code these dependencies should factored into the design
  and upkeep of the software.

Developers should be able to find useful resources and help easily
------------------------------------------------------------------

Developers within the existing team, externally and for anyone that
joins the team.

Each project should clearly describe how other developers can get involved
--------------------------------------------------------------------------

We should be able to communicate with the users of our code.
------------------------------------------------------------

This could be by:

- technical blog

- messages

- email

Users should be able to communicate with us about our code
----------------------------------------------------------

There should be pathways for

- technical users/queries

- non-technical users/queries

We should protect our users privacy
-----------------------------------

- good password security

- delete data that we don't need to keep

We should be clear about how we work with contractors
-----------------------------------------------------

For example:

- systems we use

- licensing

If our code works with IATI data, have we considered how it will work as the IATI datasets grow, both in terms of individual file size and as a corpus
------------------------------------------------------------------------------------------------------------------------------------------------------

It is hard to  estimate the size of data we can expect to see in e.g. 3,
6, 12 months time

We know that an example set of data may not cover all possibilities for
developers new to IATI

Our code should be secure
-------------------------

When relying on external code (e.g. wordpress) - we should be on an
alert list, we should update as soon as possible where necessary.

We should assess our own code for vulnerability

We should know that our code is working properly
------------------------------------------------

This could mean monitoring that the application is 'up' - pingdom for
example

We should know that cron jobs have run

