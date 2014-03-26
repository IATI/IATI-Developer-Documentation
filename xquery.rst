.. _xquery:

Useful xquery queries
=====================

A good graphical interface for running these is `BaseX <http://basex.org/>`_.

Activities missing information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

which activities are missing the Implementing Org?

.. code-block:: xquery

     //iati-activity[not(participating-org/@role='Implementing')]

which activities are missing Commitments?

.. code-block:: xquery

     //iati-activity[not(transaction/transaction-type/@code='C')]

Counting distinct activities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Count distinct IATI Identifier

.. code-block:: xquery

    count(distinct-values(//iati-activity/iati-identifier))

Percentage unique activity identifiers

.. code-block:: xquery

    count(distinct-values(//iati-activity/iati-identifier)) div count(//iati-activity/iati-identifier) * 100

Count distinct IATI Identifiers for a given reporting org

.. code-block:: xquery

    count(distinct-values(//iati-activity[reporting-org/@ref='SE-6']/iati-identifier))

Dates
^^^^^

Smallest start date

.. code-block:: xquery

   min(for $d in //activity-date[@type="start-planned" or @type="start-actual"]/@iso-date where ($d != '') return xs:date($d))

