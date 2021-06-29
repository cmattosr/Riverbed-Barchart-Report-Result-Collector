# Riverbed Barchart Report Result Collector

This **web automation tool** goal is to capture the performance KPIs in **Riverbed**  after a performance testing execution is completed.

## Features

- Access Riverbed page
- Insert the query needed
    - The standard process will capture in the Barchart, Processing Time and Summary reports
- Create an XML file with the information captured in the Barchart report, in the same folder of this file
- Create a subfolder and save screenshots of Barchart, Processing Time and Summary reports in it

## Quick start

Change the date and time in line `epoch = datetime.datetime(<year>, <month>, <day>, <hour>, <minute>).timestamp()` for the initial timestamp of the period you want to capture information from
Change the `duration = <duration>` for the total period of time you want to capture information from the intial timestamp defined above.

### 1. Setup

You must have the browser driver installed on your system to run this application, the information about it is available at https://selenium-python.readthedocs.io/installation.html

#### 1.1. Clone the repository with:

``` bash
git clone https://github.com/cmattosr/Riverbed-Barchart-Report-Result-Collector.git
```

#### 1.2. Install the dependencies

Selenium: pip install selenium

#### 1.3. Update the desired configurations on files at config folder

Not applicable

#### 1.4. Execute the project

python RiverbedResults.py

### Docs

This **web automation tool** goal is to capture the performance KPIs in **Riverbed**  after a performance testing execution is completed. This application will start Riverbed in the timerange defined in `epoch = datetime.datetime(<year>, <month>, <day>, <hour>, <minute>).timestamp()` , with year, month, day, hour and minute sequence as input, this is the starting time, the time period that needs to be collected can be defined in `driver.get(f"https://riverbednp.us.dell.com/#search:time={start_time}+<minutes>)`, inserting the minutes you want to define as the period range.

After accessing Riverbed with the time range defined, the query that generates a Barchart will be inserted in the Search box (i.e. `urlpath = '/sabrix/xmlinvoice' AND http.method = 'POST' AND received.http.request.header = '<request_header>' | barchart -calc transactioncount(),avg(responsetime),percentile(responsetime, 50,95,99),min(responsetime),max(responsetime)`). The application works with a list of request_headers, so the query will be changed in every loop.

Application will create an Excel file in the same directory with the results with the name `ResultRiverbed_{}_{}_{}_{}_{}.xlsx` with the sequence year, month, day, hour, minute, and will generate files with the Barchart, Summary and Processing Time images with the name of each request headers that will be placed in a subfolder.

The application takes some time to complete depending on the list size and the amount of time to load the pages, the `sleep` can be changed to better fit the current environment and network speed.

The list of tuples includes the request_header and two values that will be used as filters in the analysis process: number of certificates and number of lines. The list can be changed according to the user needs.

### Application Status

_If any application status place, put it here for reference_

## Scripts

Not applicable

## Tech

- [Python](https://www.python.org/)

## Contributing

This boilerplate is open to suggestions and contributions, documentation contributions are also important! :)

