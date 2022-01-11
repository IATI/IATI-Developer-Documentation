Open source tools: IATI GitHub
==============================

IATI is an open data standard and all internal IATI software tools are open source and available for anyone to use from `IATI's GitHub organisation account <https://github.com/IATI>`__. Please note that some of these repositories are inactive and may exist only for archive purposes. There may be rare instances of code that have yet to make it into IATI's GitHub organisation account, but it is our desire and intention for all IATI code to be there. The following are active repositories.

IATI Standard repositories:
---------------------------

- `IATI-Standard-SSOT <https://github.com/IATI/IATI-Standard-SSOT>`__: main repository used to collate and build the documentation pages for the IATI Standard. This also contains the rest of the submodules.
- `IATI-Schemas <https://github.com/IATI/IATI-Schemas>`__: constraints on the structure and contents of IATI XML.
- `IATI-Codelists <https://github.com/IATI/IATI-Codelists>`__: core codelists to the IATI Standard.
- `IATI-Rulesets <https://github.com/IATI/IATI-Codelists>`__: additional instructions for IATI publishers.
- `IATI-Extra-Documentation <https://github.com/IATI/IATI-Extra-Documentation>`__: additional guidance and documentation on the IATI Standard.
- `IATI-Codelists-NonCore <https://github.com/IATI/IATI-Codelists-NonEmbedded>`__: codelists used by the IATI Standard, but not subjected to the same change-control process.
- `IATI-Guidance <https://github.com/IATI/IATI-Guidance>`__: guidance and documentation that is not focused on IATI XML.
- `IATI-Upgrades <https://github.com/IATI/IATI-Upgrades>`__: record of the process for and changes made to the IATI Standard over time.


Application layer Unified Platform repositories:
------------------------------------------------

- `IATI-refresher <https://github.com/IATI/refresher>`__

The IATI-refresher contains the applications that control the flow of the system; identifying, downloading and refreshing datasets from the Registry, and then making sure they are validated and, if appropriate, subsequently indexed into the Datastore, using services provided by the repositories below.

**Validation specific repositories:**

- `IATI-Validator_API <https://github.com/IATI/js-validator-api>`__: Pure JavaScript IATI validator implementation.
- `IATI-Validator_Services <https://github.com/IATI/validator-services>`__: Backend microservice provider for the IATI Validator on the Unified Platform.
- `IATI-Validator_Web <https://github.com/IATI/IATI-Validator-Web>`__: IATI Validator Angular Front-end application.

**Datastore specific repositories:**

- `IATI-Datastore_Services <https://github.com/IATI/datastore-services>`__: Datastore utility functions for administrators (e.g. reindex Solr).
- `IATI-Flattener <https://github.com/IATI/iati-flattener>`__: IATI document flattener, prepares IATI docs for Indexing into Solr for the IATI Datastore.

Infrastructure layer Unified Platform Repositories:
---------------------------------------------------

- `IATI-Datastore_SOLR_Configs <https://github.com/IATI/datastore-solr-configs>`__: IATI Datastore SOLR configurations, includes solr schemas and solrconfig.xml files for each collection.
- `IATI-SOLR_K8S <https://github.com/IATI/solr-k8s>`__: Kubernetes deployment manifests and information for IATI Solr Production instance
- `IATI-APIM_IATI_Gateway <https://github.com/IATI/apim-iati-gateway>`__: IATI API Management instance repo (aka IATI API gateway).


IATI tools and website not yet part of the Unified Platform
-----------------------------------------------------------

- `IATI-Standard_Website <https://github.com/IATI/IATI-Standard-Website>`__: Django and Wagtail website for IATI.
- `IATI-Dashboard <https://github.com/IATI/IATI-Dashboard>`__: dashboard for various metrics, generated nightly from IATI data.
- `IATI-Stats <https://github.com/IATI/IATI-Stats>`__: application for generating JSON stats to feed the IATI Dashboard.
- `IATI-Registry_Refresher <https://github.com/IATI/IATI-Registry-Refresher>`__: scripts to pull IATI data from the IATI registry using the CKAN API.
- `IATI-Publishing_Statistics <https://github.com/IATI/IATI-Publishing-Statistics>`__: tables and files presenting summaries of all published IATI data.
- `IATI-Website_Tests <https://github.com/IATI/IATI-Website-Tests>`__: sanity checks, smoke and integration tests for IATI tools.

These repositories are managed and maintained by the `IATI Technical Team <https://iatistandard.org/en/about/governance/who-runs-iati/technical-team/>`__. If you wish to contribute to them, please follow the :doc:`Developer contributions <contribute>` guidelines and, for further questions, email code@iatistandard.org.

Additional IATI tools managed by external vendors:
--------------------------------------------------

- `ckanext-iati <https://github.com/IATI/ckanext-iati>`__: CKAN extension for the IATI Registry.
- `d-portal <https://github.com/devinit/D-Portal>`__: visualisation platform for IATI data.
