#!/usr/bin/python

#imports
import sys
import pymssql as mdb
import cred

# Variables for the program
sql_username = cred.sql_user
sql_password = cred.sql_pass
sql_database = cred.db

#variables for testing ***** Need to switch to an argument or something else
store_org = input('Please input the store#: ')
store_new = input('Please enter the new store#: ')

cursor.execute("update tbldslip set [store #] = %s where [store #] = %s") (store_org, store_new)

#Cleanup after everything is done
#close the sql connection
sql_connection.close()