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

-  communicate with new team members, external contractors, and other
   developers, about the way we do things.
-  allows us to audit current projects to find and fix gaps.
-  allows us to test new work against the framework to make sure all the
   bases are covered.

Each code repository in our `GitHub account <https://github.com/IATI/>`_
should have a CHECKLIST.rst file

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
This makes it easy for others to work out who they might need to talk to.

Our projects/code should be appropriately branded.
--------------------------------------------------
This has been an issue for IATI as it has developed. 

Our code/projects should be in version control and present links to issue trackers and source code.
---------------------------------------------------------------------------------------------------
Usually this would be in our `GitHub account <https://github.com/IATI/>`_.

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
Essentially the domains we use to host applications should make sense.

Code should be kept in one place e.g. GitHub organisation

Our code should be on our servers
---------------------------------
As opposed to, for example, a developers personal server.

We should be able to monitor the performance of those servers

We should be able to monitor the performance of the software

Status of the software should be indicated in the deployments
-------------------------------------------------------------
For example, much of our code is deployed on development servers. 
Some of it is actively shared (i.e. we email people links, talk about
it openly), other stuff is thrown up for testing, but may still be
discoverable. It should be clear to visitors as to the status of that
software (e.g. they are using a development version of the software). 
Moreover, we may be deploying software/service that are considered
pre-Alpha, Alpha, Beta, properly stable etc..

We should know how our code is being used - logs!
-------------------------------------------------
Are we gathering and making use of:

- server analytics

- google analytics

- built in loggers

Our code will need to adapt with schema changes and changes to external systems upon which it relies
----------------------------------------------------------------------------------------------------
If, for example, the datastore, or the registry change then our code
should also change

When creating code these dependencies should factored into the design
and upkeep of the software.

Developers should be able to find useful resources and help easily
------------------------------------------------------------------
Developers within the existing team, externally and for anyone that
joins the team.

Each project should clearly describe how other developers can get involved
--------------------------------------------------------------------------
Each repository in GitHub should have a CONTRIBUTING.rst document

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
For example:

- good password security

- delete data that we don't need to keep

We should be clear about how we work with contractors
-----------------------------------------------------
For example:

- systems we use

- licensing

If our code works with IATI data, have we considered how it will work as the IATI datasets grow, both in terms of individual file size and as a corpus
------------------------------------------------------------------------------------------------------------------------------------------------------
We should be aware that it is hard to  estimate the size of data we can
expect to see in e.g. 3, 6, 12 months time.

We should also be aware know that an example set of data may not cover
all possibilities for developers new to IATI

Our code should be secure
-------------------------
When relying on external code (e.g. wordpress) - we should be on an
alert list, we should update as soon as possible where necessary.

We should assess our own code for vulnerability

We should know that our deployed code is working properly
---------------------------------------------------------
This could mean monitoring that the application is 'up' - pingdom for
example

We should know that cron jobs have run

Our code should be simple to deploy and update
----------------------------------------------
When creating an application, consideration of the ease of deployment, 
including upgrades should be considered. 

Are we using any other tools to help us monitor our code?
---------------------------------------------------------
For example, linking into webhooks or services such as Travis

Is this code language aware?
----------------------------
Can it handle unicode correctly?
Does it need to handle translations and display text in differnet scripts?
