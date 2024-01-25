Datastore and Data Pipelines
============================

This document describes what happens when a publisher publishes some new data, and how data flows through the IATI
Registry & Unified Data Pipeline to the Validator and Datastore. It is intended to help people better understand our
data pipelines, and start to think about how they can write data pipelines of their own.

Publishing new data
~~~~~~~~~~~~~~~~~~~

Firstly the publisher publishes some new data.

One way they can do this is by publishing a new file on their website. They then need to go to the IATI Registry and log
in, and tell it about this new file.

The other way they can do this is by updating a file that has already been published. In this case they don't need to
log into the Registry and edit anything. The registry will constantly check any published files and will make available
a hash for each document. This hash is a small string that is derived from the contents of the file. When the contents
of the file changes the hash changes too.

Another way of doing this is to use a publishing tool, such as Publisher or Aidstream, which will then create the file
in IATI registry automatically

Whatever method is used, anyone who wants to fetch IATI data for their own data pipeline will need to be constantly
checking the registry to find out which files they should be downloading. The file hash can be very useful here, as we
will see shortly.

The first stage of the unified data pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Unified Data Pipeline checks the Registry for all documents and their file hash. It stores details of what it has
seen before and the old file hashes. In this way it can tell straight away when some new data has been published
(because a file it hasn’t seen before appears in the registry or a file hash changes) and start processing it as fast
as it can.

This checking, and all the further stages of the Unified Data Platform happens 24/7. As soon  as the first stage has
finished its work, it waits a few minutes and then starts again. In this way the system responds really quickly when a
publisher publishes new data.

Generally during working hours (and remember in an international data standard that's working hours in many different
time zones) the unified data pipeline is always processing something, as publishers around the world update their data.

Once the unified data pipeline notices something has changed, the first step is to download the new data directly from
the publisher and store it.

Other data pipelines that do not use the file hash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Other data pipelines do not use the file hash.  However this can only mean that these data pipelines will be more
inefficient.  The only way they can tell if any data has changed is to download all the data directly from the publisher
on a regular basis.  However, this is a lot of data to download -  it will take a long time and could leave people with
a large bandwidth bill.  This means that it cannot be done regularly. Data pipelines that use this strategy tend to only
run once per day and this means they can be slow to pick up any updates.  We recommend data pipelines try and use the
file hash; it means you can build a system that responds much faster and uses much less data bandwidth.

Some other data standards do not make file hashes available at their registries, and so the only way to build a data
pipeline there is to download all the data regularly. This is a very nice feature of IATI Registry.

Further stages of the unified data pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once new data has been downloaded, it goes through several stages.

It is validated using the same `IATI Validator tool that is available to others <https://validator.iatistandard.org/>`_.
Anyone can see the results of this validation for any publisher by going to
`the IATI Validator public data viewer <https://validator.iatistandard.org/organisations>`_. (Here you can also see
details of when the data appeared in the data store)

Next the data is cleaned up. Some documents may have some activities which we can process and some which we can't.
Rather than throw away the whole document, we take out the good activities for further processing. This is judged by the
validator, so you can test files out before publishing to avoid surprises.

We then prepare several different representations of the data. We of course prepare an XML version of every activity.

We also prepare a JSON version. Some API users may find JSON easier to use than XML.

(Example query `https://api.iatistandard.org/datastore/activity/select?q=*:*&rows=1&fl=activity_id,iati_json` - and then
turn the `iati_json` field into a JSON object)

.. code-block:: json

   {
      "iati-activity": [
        {
          "@last-updated-datetime": "2020-01-01T14:00:00Z",
          "@default-currency": "GBP",
          "@humanitarian": "false",
          "iati-identifier": [
            {
              "text()": "EXAMPLE-43734874387"
            }
          ],
          "reporting-org": [
            {
              "@ref": "EXAMPLE-43672390",
              "@type": "1",
              "narrative": [
                {
                  "@xml:lang": "EN",
                  "text()": "Example Funder"
                }
              ]
            }
          ],
          "title": [
            {
              "narrative": [
                {
                  "@xml:lang": "EN",
                  "text()": "Example Project"
                }
              ]
            }
          ], …



We also prepare a flattened version. This flattened version is a simple document with every field that has data, and for
that field every value in the activity. For example an activity may have multiple transactions but in the flattened
version there is only one field for transaction values and that field has a list of all the different transaction values.
Flattened versions are no use if you need to know all the details of the transactions individually, but it is great for
a quick summary and for searching. For example searching for all activities with a transaction that is humanitarian is
now easy.

(Example query `https://api.iatistandard.org/datastore/activity/select?q=transaction_humanitarian:1&rows=1&fl=iati_identifier,transaction_value,transaction_humanitarian` )

.. code-block:: json

    {
        "iati_identifier": "EXAMPLE-32788",
        "title_narrative": [
            "An example humanitarian project"
        ],
        "transaction_value": [
            643.0,
            145.0,
            4582.0,
            756.0,
        ],
        "transaction_humanitarian": [
            true,
            true,
            true,
            true,
        ]
    }


Finally once we have all these versions of the data in a document prepared we insert them into the data store. The old
version of the documents data is only removed from the data store at this point. We do this because we think it is better
that the data store has old data than no data (with the exception of data removal, which we will come back to). In the
past, while documents were being processed there was no data in the data store. As this processing could take a few
hours, this was a problem. (More details on this change `are on IATI Connect <https://www.iaticonnect.org/group/9/topic/proposed-update-iati-datastore>`_)

The data is now available for searching via the `Datastore website <https://datastore.iatistandard.org/>`_
and `API <https://developer.iatistandard.org/>`_.

Data removal
~~~~~~~~~~~~

`It is important that publishers can delete data from all the various IATI reporting systems <https://iatistandard.org/en/data-removal/>`_.
They can do this by logging into the IATI Registry and deleting a document or making it private.

If a publisher wishes to remove data it is important to log into the registry and delete it or make it private. If they
merely delete the data file from their own systems then tools may interpret this as a temporary server error and carry
on displaying the old data for a bit (the IATI Datastore will do this).

When this happens tools should try and remove the data as soon as they can. In the case of the Unified Data Platform the
first stage that checks the registry constantly will notice a file which it previously knew about is now gone. When it
notices this it will delete the data for the file straight away. Thus the unified data platform removes data really
quickly.

For other data pipelines that don't use the data hash and rely on downloading all the data every night, removal is not
so fast. You have to wait for the next set of downloads and processing for that download to happen. It can be a day or
more before data is removed.

Why build a Data pipeline at all?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remember you don't have to build a data pipeline yourself. `The IATI data store has an API <https://developer.iatistandard.org/>`_
and maybe you can get the data you need by querying that regularly.

More
~~~~

You can check out `our code online on GitHub <https://github.com/IATI>`_.

If you have `any further questions do get in touch <https://iatistandard.org/en/guidance/get-support/>`_.  We are happy
to help people write their own software to get the best use out of IATI data.



