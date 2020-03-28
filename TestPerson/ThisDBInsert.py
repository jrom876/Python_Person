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
    print("1 = insert dudeMan       11 = delete dudeMan             111 = delete all from table")
    print("2 = insert stevo         22 = delete stevo               222 = fetch all from table")
    print("3 = insert blankMan      33 = delete blankMan")
    print("4 = insert seedperson    44 = delete seedperson\n")
    choice = int(input("Choose from the list:\t"))

    if choice == 1:
        strdm = ThisPerson(dudeMan).convertPersonToString(dudeMan)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_insert = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
                    VALUES %s;""" % (strdm)
        crsr.execute(sql_insert)
        connection.commit()
    elif choice == 11:
        # obj = ThisPerson(dudeMan)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_del = """DELETE FROM ThisGroup WHERE id = %i;""" % (dudeMan.id)
        crsr.execute(sql_del)
        connection.commit()
    elif choice == 111:
        # obj = ThisPerson(dudeMan)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_del_all = """DELETE FROM ThisGroup;"""
        crsr.execute(sql_del_all)
        connection.commit()
    elif choice == 2:
        strobj = ThisPerson(stevo).convertPersonToString(stevo)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_insert = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
                    VALUES %s;""" % (strobj)
        crsr.execute(sql_insert)
        connection.commit()
    elif choice == 22:
        # obj = ThisPerson(dudeMan)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_del = """DELETE FROM ThisGroup WHERE id = %i;""" % (stevo.id)
        crsr.execute(sql_del)
        connection.commit()
    elif choice == 222:
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM ThisGroup")
        ans = crsr.fetchall()
        for i in ans:
            print(i)
    elif choice == 3:
        strobj = ThisPerson(blankMan).convertPersonToString(blankMan)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_insert = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
                    VALUES %s;""" % (strobj)
        crsr.execute(sql_insert)
        connection.commit()
    elif choice == 33:
        # obj = ThisPerson(dudeMan)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_del = """DELETE FROM ThisGroup WHERE id = %i;""" % (blankMan.id)
        crsr.execute(sql_del)
        connection.commit()
    elif choice == 4:
        strobj = ThisPerson(seedperson).convertPersonToString(seedperson)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_insert = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
                    VALUES %s;""" % (strobj)
        crsr.execute(sql_insert)
        connection.commit()
    elif choice == 44:
        # obj = ThisPerson(dudeMan)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_del = """DELETE FROM ThisGroup WHERE id = %i;""" % (seedperson.id)
        crsr.execute(sql_del)
        connection.commit()
# close the connection
    connection.close()


# Driver program
if __name__ == "__main__":
    exit_flag = 0
    while exit_flag == 0:
        print("\nWelcome to This Database ")
        ch = input("To begin, choose (c)ontinue or (q)uit\n")
        if ch == "q":
            print("Now exiting the program\n ")
            exit_flag = 1
        elif ch == "c":
            getuserInput()
            exit_flag = 0
        else:
            print("Incorrect answer. \n Exiting\n ")
            exit_flag = 1

        # for p in personArray:
        #     format_str = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
        #     VALUES ("{first}", "{last}", "{pw}", "{gr}", "{idd}", "{sal}");"""
        #     sql_insert = format_str.format(first=p[0], last=p[1], pw=p[2], gr=p[3], idd=p[4], sal=p[5])
        #     crsr.execute(sql_insert)
