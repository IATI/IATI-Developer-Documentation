Old Datastore (Deprecated)
=================

Between now and 22 March 2021 users can choose to either use existing API calls to return data from the old Datastore, or use a Redirect version from the Old Datastore to the new Datastore. By using this version, existing API calls will be redirected and return data from the new Datastore. After 22 March 2021, the old Datastore will be deprecated and all queries to the Old Datastore will automatically be redirected to corresponding queries on the new Datastore.

The Redirect Version of the Old Datastore is hosted at `http://datastoreredirect.iatistandard.org <http://datastoreredirect.iatistandard.org>`_. Redirects may be tested by replacing "datastore.iatistandard.org" in previous queries with "datastoreredirect.iatistandard.org." For example `http://datastore.iatistandard.org/api/1/access/activity.csv <http://datastore.iatistandard.org/api/1/access/activity.csv>`_ would become `http://datastoreredirect.iatistandard.org/api/1/access/activity.csv <http://datastoreredirect.iatistandard.org/api/1/access/activity.csv>`_.

The Datastore stores all activity data available on the IATI Registry, allowing you to query it all in one place. This data can be accessed in spreadsheet format, or in more technical formats through a standard interface (API). Please be aware that this product is considered to be in alpha (`see below <#alpha-status>`__).

* `Guidance <guidance.rst>`__
* `Reference <reference.rst>`__

IATI Datastore CSV Query Builder
--------------------------------

You can perform many common queries using the `IATI Datastore CSV Query Builder <http://datastore.iatistandard.org/query/>`__. This tool generates a Datastore query in spreadsheet (CSV) format based on the fields that you select.

Overview
--------

The Datastore has three APIs:

* `Data API <reference/data-api.rst>`__: Allows you to make queries which can output IATI data in your chosen format (CSV, XML or JSON).
* `Metadata API <reference/metadata-api.rst>`__: Allows you to find information about datasets that are contained within the Datastore.
* `Error API <reference/error-api.rst>`__: Allows you to see information about datasets that could not be successfully imported into the Datastore.

Anyone can access the Datastore – just build a query and data will be returned.

Alpha Status
------------

Please be aware that the Datastore is in alpha. This means that it may exhibit unexpected behaviour or return unexpected results. This product is intended for user testing and feedback only and should not be considered a stable product. The Datastore is not feature complete.

Current known issues include:

* Invalid publisher data causing problems with data import
* Registry failure causing problems with data import

In the meantime, we welcome code contributions from our open source community via `GitHub <https://github.com/IATI/IATI-Datastore>`__.

Quick Start
-----------

The Data API is the most commonly used API. The following examples will get you started.

**Example 1: A simple query to return data for a given country**

This URL returns all available IATI activities in Somalia using the `recipient-country` filter:

`http://datastore.iatistandard.org/api/1/access/activity.xml?recipient-country=SO <http://datastore.iatistandard.org/api/1/access/activity.xml?recipient-country=SO>`__

Values for filters come from the relevant IATI codelist. In this case, `SO` is the value for Somalia on the Country codelist.

**Example 2: A more complex query**

This URL returns all available IATI activities in multiple countries using the `recipient-country` filter – in this case, Ethopia, Somalia and Kenya – reported by multiple reporting organisation types using the `reporting-org.type` filter – in this case, international, national and regional NGOs:

`http://datastore.iatistandard.org/api/1/access/activity.xml?recipient-country=ET|SO|KE&reporting-org.type=21|22|23 <http://datastore.iatistandard.org/api/1/access/activity.xml?recipient-country=ET|SO|KE&reporting-org.type=21|22|23>`__

Next Steps
----------

The Datastore can do much more than is shown here.

* See the `Guidance <guidance.rst>`__ for a more detailed guide on querying the Datastore.
* For in-depth documentation, see the `Reference <reference.rst>`__.
