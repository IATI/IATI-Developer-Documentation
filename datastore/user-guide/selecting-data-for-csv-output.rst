Selecting Data for CSV output
=============================

Method
------

CSV data can be retrieved directly via the API. The basic form that we have constructed builds a query for you by displaying a paramaterised link to the API. So …

* Build a query by selecting from the check boxes and dropdowns
* Click on ‘Submit’
* Click on the link that appears at the top of the page
* The resulting csv file will be downloaded
* Depending on the settings on your computer the file will be automatically opened in your spreadsheet application.

Format Check Boxes (Mandatory)
------------------------------

- | Dataset
  | Choose whether each row in your spreadsheet will contain a single activity, transaction or budget period. See :doc:`how-is-the-csv-data-displayed` for more information on these three different table outputs.
  
  Tip! If you are looking to analyse activity finances by year you need to select “Transactions” and calculate the year from the transaction date.

- | Dataset Format
  | By default, choose “Summary”. The sector and country boxes are not sort options, but handle multiple values within a single activity or transaction.

  IATI allows for activities to be classified with multiple sectors and for the costs of the activity to be split proportionately across these sectors. If you are specifically looking to do sectoral analysis choose “By Sector”. This will repeat each row of your chosen dataset for each reported sector value. The percentage split for each sector is also displayed in a separate column which allows you to perform arithmetic on the financial values.

  Similarly IATI allows for individual activities to be reported in multiple countries with percentage splits between them. The above sector logic applies if you choose “By Country” .

  Warning! Choosing sector or country will duplicate rows of data. Do not add up financial values without introducing arithmetic to apply the relevant percentage to each row.

- | Sample Size
  | By default choose “Entire selection”

  If you want to check your selection by seeing a preview, choose “50 rows”.

Filters (Optional)
------------------

- | Overview
  | The form contains five dropdown lists for you to filter your query. Any logical combination of filters can be applied.
  
  | Multiple selections can be made in each dropdown using holding down the Ctrl key.
  | AND relations are applied between dropdowns
  | OR relations are applied within dropdowns

  Warning! If you don’t add at least one filter to your query you will download the entire dataset. The Datastore currently holds over 200,000 activities and 1,000,000 transactions. This number increases on a daily basis.

- | Reporting Organisation
  | The reporting organisation is the publisher of the IATI data. You would choose this filter to analyse a particular donor or agency’s data. This might typically be used in conjunction with a country and/or a sector.

  Warning! The Datastore contains activities reported by both primary and secondary sources. A secondary source, such as the UNOCHA Financial Tracking Service, reports data it holds about other agencies’ activities. An agency may well report activities to IATI and FTS, which in turn reports the same activities to IATI.

- | Type of Reporting Organisation
  | This allows you to filter by the type of organisation. To access data on NGOs only you would select International NGO and/or National NGO and/or Regional NGO

- Sector
- | Country
  | Choose the recipient country or countries you are looking for. See Region notes below for potential pitfalls.
- | Region
  | Selecting a region will return activities that publishers have been unable to allocate to specific countries.

  Warning! Choosing a Region AND a Country will not return data as most publishers report either a Country or a Region. There is no way, currently of creating a filter that will return all activities for, say, Southern Africa. You can choose all the countries you would like to include, but you will need to run a separate query for the region.

  Warning! There is no international consensus on the definition of regions. IATI currently uses to OECD DAC rules, but is about to add a second vocabulary that is maintained by the UN. IATI has more work to do to create a cross-mapping between different region codes and map countries to regions.

- | Future Options
  | In future filters will be available on all IATI fields. A number of these are already available via the API. Watch this space…
