IATI code examples
==================

A small repository of curated code examples is maintained in order to facilitate the use of IATI APIs, data, and tools.

Setup and testing instructions for the code examples may be found in the corresponding README files:

- `Javascript <https://github.com/IATI/IATI-code-examples/blob/develop/Javascript/README.md>`__
- `Python <https://github.com/IATI/IATI-code-examples/blob/develop/Python/README.md>`__
- `R <https://github.com/IATI/IATI-code-examples/blob/develop/R/README.md>`__

The code examples include:

Applying codelist names to numerical codes
------------------------------------------

One common operation required to make semantic use of IATI data is the transformation of machine-readable codes into human-readable names. Below are some examples of how to make these transformations. These examples assume you're already familiar with the IATI Datastore API; if not, please see the documentation on the IATI API Gateway: https://developer.iatistandard.org/.

We have examples of how to download our codelist mappings, download all codelists, and match code values downloaded from the Datastore in JSON to their codelist names in the following languages:

- `Javascript <https://github.com/IATI/IATI-code-examples/blob/develop/Javascript/codelists/index.js>`__
- `Python <https://github.com/IATI/IATI-code-examples/blob/develop/Python/codelists/codelists.py>`__
- `R <https://github.com/IATI/IATI-code-examples/blob/develop/R/codelists/index.R>`__

Converting currencies
---------------------

Another common operation required to make IATI data comparable is the conversion to a common currency. IATI does not have one official source for exchange rates, but in the data folder of this repository you'll find a sample of daily exchange rates sourced from the IMF from January 1, 1994 to July 6, 2022. As the sample data we're using comes from the Datastore, all fields required are already in the correct data types, and conversion is a simple matter of looking up the appropriate rate and multiplying.

We have examples of how to convert currencies for transactions and budgets available in the following languages:

- `Javascript <https://github.com/IATI/IATI-code-examples/blob/develop/Javascript/currency/index.js>`__
- `Python <https://github.com/IATI/IATI-code-examples/blob/develop/Python/currency/currency.py>`__
- `R <https://github.com/IATI/IATI-code-examples/blob/develop/R/currency/index.R>`__
