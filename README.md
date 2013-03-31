Python Database Helper
======================

A few python database helper functions

This database helper currently only supports sqlite3 database.

Usage: from db_helper import *

Functions:

##def findinDatabase(db_path, table, field, value, timeout=60)
Will return the row if found in database otherwise return None

##def fetchData(db_path, table, timeout=60)
Fetch the first column and delete it from the table specified \n
Support multithreading/concurrency. You can call this function from different instances \n
NOTE: In order to use this function you need to have a field "TEXT flag" in the table \n

##def insertData(db_path, table, data, timeout=60)
Parameter "data" should be a dictionary with keys as column name and values as values
corresponding to each column

def log(content)

def errlog(content)

