###############################
#                             #
#  Author: Daniel Liu (hpec)  #
#  Email: hpec.liu@gmail.com  #
#                             #
###############################

import time
import traceback
import sqlite3

log = print
errlog = print

def findinDatabase(db_path, table, field, value, timeout=60):
    connection = sqlite3.connect(db_path, timeout)
    with connection:
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE {field}=? LIMIT 1".format(table = table, field = field)
        cursor.execute(query, (unicode(str(value), 'utf-8'), ))
        row = cursor.fetchone()
        return row

def fetchData(db_path, table, timeout=60):
    connection = sqlite3.connect(db_path, timeout)
    while True:
        try:
            with connection:
                cursor = connection.cursor()
                flag = int(random.random()*100000000)
                query = "UPDATE {table} SET flag = {flag} WHERE id = (SELECT id FROM {table} WHERE flag IS NULL LIMIT 1)".format(table = table, flag = flag)
                cursor.execute(query)
                query = "SELECT * FROM {table} WHERE flag = {flag}".format(table = table, flag = flag)
                cursor.execute(query)
                row = cursor.fetchone()
                query = "DELETE FROM {table} WHERE flag = {flag}".format(table = table, flag = flag)
                cursor.execute(query)
                return row
        except Exception, detail:
            if 'locked' in str(detail):
                log('Database busy')
                time.sleep(5)
                continue
            if 'Keyboard' in str(detail):
                sys.exit(0)
            errlog(str(traceback.format_exc()))
            errlog(query)
            return

def insertData(db_path, table, data, timeout=60):
    connection = sqlite3.connect(db_path, timeout)
    with connection:
        cursor = connection.cursor()
        cursor.execute("PRAGMA table_info({table})".format(table = table))
        columns = cursor.fetchall()
        col_str = ''
        val_str = ''
        val = []
        for column in columns:
            if column[1] in data:
                col_str = col_str + column[1] + ','
                val.append(unicode(str(data[column[1]]), 'utf8'))
        col_str = col_str[:-1]
        val_str = '?,'*len(val)
        val_str = val_str[:-1]
        while True:
            try:
                query = "INSERT INTO {table}({col}) VALUES({val})".format(table = table, col = col_str, val = val_str)
                cursor.execute(query,val)
                break
            except Exception, detail:
                if 'locked' in str(detail):
                    log('Database busy')
                    time.sleep(5)
                    continue
                errlog(str(traceback.format_exc()))
                errlog(query)
                errlog(val)
                break


