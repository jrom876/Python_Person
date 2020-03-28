#!/usr/bin/python3
## https://www.geeksforgeeks.org/sql-using-python/
# Python code to demonstrate SQL to fetch data.

# importing the module
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

# connect withe the myTable database
connection = sqlite3.connect("myTable.db")

# cursor object
crsr = connection.cursor()

# execute the command to fetch all the data from the table ThisGroup
crsr.execute("SELECT * FROM ThisGroup")

# store all the fetched data in the ans variable
ans= crsr.fetchall()

# loop to print all the data
for i in ans:
    print(i)
