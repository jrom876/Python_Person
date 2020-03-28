#!/usr/bin/python3
## https://www.geeksforgeeks.org/sql-using-python/
# Python code to demonstrate table creation and
# insertions with SQL

# importing module
import re
import os
import ast
import pdb
import math
import time
import sqlite3
import unittest
from sys import *
from random import *
from ThisGroup import *
from ThisPerson import *

# connecting to the database
connection = sqlite3.connect("myTable.db")

# cursor allows us to traverse and fetch records from the database
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE ThisGroup (
fname VARCHAR(20),
lname VARCHAR(20),
pword VARCHAR(20),
id INTEGER PRIMARY KEY,
gender CHAR(1),
salary INTEGER);"""

# execute the statement
crsr.execute(sql_command)

# SQL command to insert the data in the table
# sql_command = """INSERT INTO ThisGroup VALUES ("Yari", "Koznow", "vodka", 65500, 'M', 61);"""
# crsr.execute(sql_command)
#
# # another SQL command to insert the data in the table
# sql_command = """INSERT INTO ThisGroup VALUES ("Testo", "Scripto", "tequila", 1096, 'M', 49);"""
# crsr.execute(sql_command)

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()

# close the connection
connection.close()
