Python Database Helper
======================

A few python database helper functions

This helper currently only supports sqlite3 database, but can be easily adapted to support other databases.

Tested on sqlite3 databases.

####All the functions support concurrency, utilizing sqlite built-in locks. Resolved conflicts in concurrency situations.


##Usage: 

from db_helper import *

##Functions:

###def findinDatabase(db_path, table, field, value, timeout=60)
Will return the row if found in database otherwise return None.

###def fetchData(db_path, table, timeout=60)
Fetch the first row and delete it from the table specified.

Return the row if succeed.

Support multithreading/concurrency: this function can be called from different instances.

NOTE: In order to use this function you need to have a field "TEXT flag" in the table.


###def insertData(db_path, table, data, timeout=60)
Parameter "data" should be a dictionary with keys as column name and values as values
corresponding to each column.

Support multithreading/concurrency: this function can be called from different instances.

Prevented SQL injection.

###def log(content)

###def errlog(content)

