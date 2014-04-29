.. _xquery:

Useful XQuery queries
=====================

XQuery is a query language for querying XML files. This page provides some useful example queries for working with IATI data. A good graphical interface for running these queries is `BaseX <http://basex.org/>`_.

Many of the queries below are also valid XPath, since XPath is a subset of XQuery.

Activities missing information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Which activities are missing the Implementing Org?

.. code-block:: xquery

     //iati-activity[not(participating-org/@role='Implementing')]

Which activities are missing Commitments?

.. code-block:: xquery

     //iati-activity[not(transaction/transaction-type/@code='C')]

Counting distinct activities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Count distinct IATI Identifiers

.. code-block:: xquery

    count(distinct-values(//iati-activity/iati-identifier))

Percentage of activities with unique activity identifiers

.. code-block:: xquery

    count(distinct-values(//iati-activity/iati-identifier)) div count(//iati-activity/iati-identifier) * 100

Count distinct IATI Identifiers for a given reporting organisation

.. code-block:: xquery

    count(distinct-values(//iati-activity[reporting-org/@ref='SE-6']/iati-identifier))

Dates
^^^^^

Smallest start date

.. code-block:: xquery

   min(for $d in //activity-date[@type="start-planned" or @type="start-actual"]/@iso-date where ($d != '') return xs:date($d))

