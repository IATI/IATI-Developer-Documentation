How is the CSV data displayed?
==============================

Formats (Choose Format options)
-------------------------------

There are three main output formats

- Activity – each row contains a unique activity. Financial information is aggregated. Budget information is excluded. Other potentially repeating fields (such as sectors) are reported in a single cell, delimited by semi-colons.
- Transaction – each row contains a unique financial transaction. The parent activity identifier and other activity-level fields are repeated for each transaction.
- Budget – each row contains a budget-period entry. Transaction data is not included. The parent activity identifier and other activity-level fields are repeated for each budget line.

Sub-formats (Repeat Row? options)
---------------------------------

In addition each of these three formats has two sub-formats which allows for analysis of percentage splits where multiple sectors or countries are reported for a single activity.

- Sector – each Activity, Transaction or Budget row is repeated for each separate Sector reported. The corresponding percentage for the sector split is reported in a separate column. This allows you to easily add arithmetic to your spreadsheet to calculate values proportionately.
- Country – each Activity, Transaction or Budget row is repeated for each separate Country reported. The corresponding percentage for the sector split is reported in a separate column. This allows you to easily add arithmetic to your spreadsheet to calculate values proportionately.

**Warning!** The standard requires that percentage splits that add up to 100% are reported whenever multiple sectors or countries are used. This rule is not enforced through validation so caution should be practiced when using these formats.

Columns
-------

Each of the above formats have a different selection of columns. This table describes the description and occurrence of columns. The sub-formats are similar to their parent format with the addition of Sector/Country and Percentage columns on the left-hand side of the sheet.

