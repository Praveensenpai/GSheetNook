* * *

GSheetNook - Google Sheets Simplified
=====================================

The `GSheetNook` module provides a simple and efficient way to interact with Google Sheets using the `gspread` library and convert retrieved data into Pandas DataFrames. This utility is designed to streamline accessing and manipulating Google Sheets data within your Python projects.

Installation
------------

To start using the `GSheetNook` module, follow these installation steps:

1.  Install the required libraries using pip:
    
    bashCopy code
    
    `pip install gspread pandas`
    
2.  Download your Google service account credentials (JSON) file, which will be needed to access your Google Sheets. Ensure that this file is named `service_account.json`.
    

Usage
-----

Here's how you can utilize the `GSheetNook` module within your Python script:

1.  Import the module and create an instance of the `GoogleSheet` class:
    
    pythonCopy code
    
    `from gsheetnook import GoogleSheet  google_sheet = GoogleSheet()`
    
2.  Set a specific Google Sheets spreadsheet (optional) using the `set_spread_worksheet` method:
    
    pythonCopy code
    
    `google_sheet.set_spread_worksheet("YourSpreadsheetName")`
    
3.  Retrieve data from a specific worksheet using the `get_sheet` method:
    
    pythonCopy code
    
    `sheet_name = "Sheet1" data_frame = google_sheet.get_sheet(sheet_name)`
    
4.  Start working with the retrieved data as a Pandas DataFrame:
    
    pythonCopy code
    
    `print(data_frame)`
    

Please ensure you have the necessary permissions to access the specified Google Sheets and provide accurate worksheet names when using the `get_sheet` method.

Example
-------

Below is an example showcasing the usage of the `GSheetNook` module:

pythonCopy code

`from gsheetnook import GoogleSheet  # Create an instance of GoogleSheet google_sheet = GoogleSheet()  # Set a specific Google Sheets spreadsheet (optional) google_sheet.set_spread_worksheet("YourSpreadsheetName")  # Retrieve data from a worksheet sheet_name = "Sheet1" data_frame = google_sheet.get_sheet(sheet_name)  # Display the retrieved data print(data_frame)`

Disclaimer
----------

Please ensure you are familiar with the basics of working with Google Sheets and have the necessary permissions to access the data.

* * *

Feel free to modify and customize this README to align with your project's specifics and objectives.