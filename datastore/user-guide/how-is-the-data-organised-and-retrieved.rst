How is the data organised and retrieved?
========================================

Activities
----------

Each activity reported in IATI-XML format is stored as a unique record in an Activities Table. In IATI terminology an “activity” can be a project, programme, grant or any other user-defined unit of aid. The Datastore uses the <iati-identifier> element as the key to defining a unique record.

Transactions
------------

As a single activity usually contains multiple financial transactions (incoming funds, disbursements, expenditures, etc) these are stored in a separate table where each transaction is a separate record, linked to the parent activity through the <iati-identifier>. This ‘normalised’ structure makes it easy for the CSV query tool to generate spreadsheet output of transaction details with one row per transaction rather than just one row per activity.

Budgets
-------

Forward looking budgets are also stored in a separate table and are similarly accessible via CSV.

Results and geocoding
---------------------

Easy-to-use output of results and location data are not yet available in CSV format – but will be in the next iteration of the Datastore’s development. This data is available to developers through JSON and XML outputs.

Original XML data
-----------------

When data is loaded into the datastore it is deconstructed from its original XML format and saved into a database structure. During this process data may be subjected to a number of cleaning and formatting processes to enhance its usefulness. To ensure its integrity the Datastore also keeps a copy of the original XML for each individual activity.

