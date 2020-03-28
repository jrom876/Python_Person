#!/usr/bin/python3
## https://www.geeksforgeeks.org/sql-using-python/
# Python code to demonstrate insertions with SQL

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

seedperson = ThisPerson("Yari","Koznow","vodka",'F',65500,61)
blankMan = ThisPerson("blankman","nunya","nada",'_',0,0)
dudeMan = ThisPerson("Charlie","Zulu","whiskey",'M',7077,25)
stevo = ThisPerson("Steve","Koz","yuno",'M',1042,59)
jb = ThisPerson("James","Bond","scotch","U",1007,47)

personArray = [ ("Yari","Koznow","vodka",'F',65517,61),
        ("blankman","nunya","nada",'_',7,0),
        ("Charlie","Zulu","whiskey",'M',7777,25),
        ("Steve","Koz","yuno",'M',1942,55),
        ("James","Bond","scotch","U",1027,47) ]

### User Interface ###
def getuserInput():
    print("1 = insert dudeMan       2 = update MCN (DO NOT USE!!)   3 = show Master k:v pairs")
    print("5 = mean (40,0,0)        15 = mean ceil (40,1,0)         25 = th (40,2,0.25)")
    print("35 = ceil th (40,3,0.25) 45 = globalTH (40,4,0.25)       55 = globalTH ceil (40,5,0.25)")
    print("7 = extract MeanAvg      17 = extract th Avg 0.1         27 = extract th Avg 0.25")
    print("9 = read mean and th     19 = update archive             99 = exit")
    print("31 = gen LOC             32 = gen Cash5                  33 = gen anyLotto\n")
    choice = int(input("Choose:\t"))

    if choice == 1:    # Read Master Lists and Dicts

        strjb = ThisPerson(stevo).convertPersonToString(dudeMan)
        # connecting to the database
        connection = sqlite3.connect("myTable.db")
        # cursor allows us to traverse and fetch records from the database
        crsr = connection.cursor()

        # for p in personArray:
        #     format_str = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
        #     VALUES ("{first}", "{last}", "{pw}", "{gr}", "{idd}", "{sal}");"""
        #
        #     sql_insert = format_str.format(first=p[0], last=p[1], pw=p[2], gr=p[3], idd=p[4], sal=p[5])
        #     crsr.execute(sql_insert)

        ### SQL command to insert the data in the table
        sql_insert = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
                    VALUES %s;""" % (strjb)
        crsr.execute(sql_insert)

        # # SQL command to insert the data in the table
        # sql_insert = """INSERT INTO ThisGroup VALUES ("Yertle", "Turtle", "vodka", 65506, 'F', 61);"""
        # crsr.execute(sql_insert)
        #
        # # SQL command to insert the data in the table
        # sql_insert = """INSERT INTO ThisGroup VALUES ("Yert", "Koz", "vodka", 65504, 'M', 61);"""
        # crsr.execute(sql_insert)
        #
        # # another SQL command to insert the data in the table
        # sql_insert = """INSERT INTO ThisGroup VALUES ("Testo", "Scripto", "kahlua", 1101, 'M', 49);"""
        # crsr.execute(sql_insert)

        # To save the changes in the files. Never skip this.
        # If we skip this, nothing will be saved in the database.
        connection.commit()

# close the connection
connection.close()
