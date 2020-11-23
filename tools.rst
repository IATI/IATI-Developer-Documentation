Open source tools: IATI GitHub
==============================

IATI is an open data standard and all internal IATI software tools are open source and available for anyone to use from `IATI's GitHub organisation account <https://github.com/IATI>`__. Please note that some of these repositories are inactive and may exist only for archive purposes. There may be rare instances of code that have yet to make it into IATI's GitHub organisation account, but it is our desire and intention for all IATI code to be there. The following are active repositories.

- `IATI Standard SSOT <https://github.com/IATI/IATI-Standard-SSOT>`__: main repository used to collate and build the documentation pages for the IATI Standard. This also contains the rest of the submodules.
- `IATI-Schemas <https://github.com/IATI/IATI-Schemas>`__: constraints on the structure and contents of IATI XML.
- `IATI-Codelists <https://github.com/IATI/IATI-Codelists>`__: core codelists to the IATI Standard.
- `IATI-Rulesets <https://github.com/IATI/IATI-Codelists>`__: additional instructions for IATI publishers.
- `IATI-Extra-Documentation <https://github.com/IATI/IATI-Extra-Documentation>`__: additional guidance and documentation on the IATI Standard.
- `IATI-Codelists-NonCore <https://github.com/IATI/IATI-Codelists-NonEmbedded>`__: codelists used by the IATI Standard, but not subjected to the same change-control process.
- `IATI-Guidance <https://github.com/IATI/IATI-Guidance>`__: guidance and documentation that is not focused on IATI XML.
- `IATI-Upgrades <https://github.com/IATI/IATI-Upgrades>`__: record of the process for and changes made to the IATI Standard over time.
- `IATI-Standard-Website <https://github.com/IATI/IATI-Standard-Website>`__: Django and Wagtail website for IATI.
- `IATI-Dashboard <https://github.com/IATI/IATI-Dashboard>`__: dashboard for various metrics, generated nightly from IATI data.
- `IATI-Stats <https://github.com/IATI/IATI-Stats>`__: application for generating JSON stats to feed the IATI Dashboard.
- `IATI-Registry-Refresher <https://github.com/IATI/IATI-Registry-Refresher>`__: scripts to pull IATI data from the IATI registry using the CKAN API.
- `IATI-Publishing-Statistics <https://github.com/IATI/IATI-Publishing-Statistics>`__: tables and files presenting summaries of all published IATI data.
- `IATI-Website-Tests <https://github.com/IATI/IATI-Website-Tests>`__: sanity checks, smoke and integration tests for IATI tools.
- `ckanext-iati <https://github.com/IATI/ckanext-iati>`__: CKAN extension for the IATI Registry.
- `IATI-Validator <https://github.com/IATI/IATI-Validator-Actual>`__: validation and data quality checks for IATI files following Schemas, rulesets and codelists. Note the structure of the validator related repositories may change.
- `IATI-Datastore-Redirects <https://github.com/IATI/IATI-Datastore-Redirects>`__: process for redirecting old datastore API query results to new datastore API

These repositories are managed and maintained by the `IATI Technical Team <https://iatistandard.org/en/about/governance/who-runs-iati/technical-team/>`__. If you wish to contribute to them, please follow the :doc:`Developer contributions <contribute>` guidelines and, for further questions, email code@iatistandard.org.

There are additional IATI tools managed by external vendors or are not part of IATI list of repositories.

- `IATI Datastore <https://github.com/zimmerman-zimmerman/iati.cloud>`__: extracts all published IATI XML files from the IATI Registry and makes them available via an API.
- `d-portal <https://github.com/devinit/D-Portal>`__: visualisation platform for IATI data.
