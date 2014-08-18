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

Count number of activities

.. code-block:: xquery

    count(//iati-activity)

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

Budgets
^^^^^^^

Find budgets that have start dates after a certain date  
(replace yyyymmdd with year, month, and day. e.g. 1st Sept. 2013 would be 20130901])

.. code-block:: xquery

    //budget[number(translate(period-start/@iso-date,'-','')) > yyyymmdd]

Find the activities that have a budget with a start date after a certain date  
(append /.. )

.. code-block:: xquery
    
    //budget[number(translate(period-start/@iso-date,'-','')) > yyyymmdd]/..

Find the iati-identifiers of budgets that have start dates after a certain date

.. code-block:: xquery
    
    //budget[number(translate(period-start/@iso-date,'-','')) > yyyymmdd]/..//iati-identifier
