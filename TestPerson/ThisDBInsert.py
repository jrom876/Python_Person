#!/usr/bin/python3
## https://www.geeksforgeeks.org/sql-using-python/
# Python code to demonstrate insertions with SQL

# https://realpython.com/python-debugging-pdb/
# debugger: python3 -m pdb app.py arg1 arg2

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

table_name = ThisGroup

seedarray = [seedperson,blankMan,dudeMan]

personSQLArray = [ ("Yari","Koznow","vodka",'F',65517,61),
        ("blankman","nunya","nada",'_',7,0),
        ("Charlie","Zulu","whiskey",'M',7777,25),
        ("Steve","Koz","yuno",'M',1942,55),
        ("James","Bond","scotch","U",1027,47) ]
############################################
def convertPersonToString(person):
    strPerson = "(\"%s\", \"%s\", \"%s\", \'%c\', %i, %i)"  % (person.fname,
    person.lname,person.pword, person.gender,person.id,person.salary)
    print("strPerson: {0}".format(strPerson))
    return strPerson

def convertGroupToString(array):
    result = []
    for i in array.perlist:
        result.append(convertPersonToString(i))
        print("result111: {0}".format(result))
    print("result00: {0}".format(result))
    return result

def insertGroupIntoTable(array):
    gp0 = ThisGroup(array)
    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()
    for p in gp0.perlist:
        sql_insert = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
        VALUES ("{0}","{1}","{2}","{3}","{4}","{5}");""".format(p.fname,
        p.lname,p.pword,p.gender,p.id,p.salary)
        crsr.execute(sql_insert)
    connection.commit()
    connection.close()

def deleteAllInDatabase():
    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()
    crsr.execute("""DELETE FROM ThisGroup;""")
    connection.commit()
    connection.close()

def displayAllInDatabase():
    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM ThisGroup;")
    ans = crsr.fetchall()
    for i in ans:
        print(i)
    connection.close()

def transferGroupIntoTable(array):
    gp0 = ThisGroup(array)
    tfile = gp0.readGroupFromFile()
    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()
    for p in tfile:
        sql_insert = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
        VALUES %s;""" % (p)
        crsr.execute(sql_insert)
    connection.commit()
    connection.close()

## Construction Zone ## 
def transferTableIntoGroupList():
    # p0 = ThisPerson()
    # tfile = gp0.readGroupFromFile()
    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()
    crsr.execute("""SELECT * FROM ThisGroup;""")
    ans = crsr.fetchall()
    for i in ans:
        print(i)
        # convertStringToPerson(i)
        # p0 = ThisPerson(i)
        # print(p0.mytuple)
        for j in i:
            print(j)
            # p0.copyPerson(i)
    connection.close()

def convertStringToPerson():
    p0 = ThisPerson(blankMan)
    # res = p0.convertThisPersonToString(p0)
    res = str(p0.myperson)
    # pa = res.split(', ')
    print(res)
    # return pa
## End of Construction Zone ##

        
############################################
### User Interface ###
def getuserInput():
    print("1 = insert dudeMan       11 = delete dudeMan             111 = delete all from table")
    print("2 = insert stevo         22 = delete stevo               222 = fetch all from table")
    print("3 = insert blankMan      33 = delete blankMan")
    print("4 = insert seedperson    44 = delete seedperson\n")
    choice = int(input("Choose from the list:\t"))

    if choice == 1: # insert dudeMan
        strdm = convertPersonToString(dudeMan)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_insert = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
                    VALUES %s;""" % (strdm)
        crsr.execute(sql_insert)
        connection.commit()
        connection.close()
    elif choice == 11:  # delete dudeMan
        # obj = ThisPerson(dudeMan)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_del = """DELETE FROM ThisGroup WHERE id = %i;""" % (dudeMan.id)
        crsr.execute(sql_del)
        connection.commit()
        connection.close()
    elif choice == 111: # delete all
        deleteAllInDatabase()
    elif choice == 2:   # insert stevo
        strobj = convertPersonToString(stevo)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_insert = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
                    VALUES %s;""" % (strobj)
        crsr.execute(sql_insert)
        connection.commit()
        connection.close()
    elif choice == 22:  # delete stevo
        # obj = ThisPerson(dudeMan)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_del = """DELETE FROM ThisGroup WHERE id = %i;""" % (stevo.id)
        crsr.execute(sql_del)
        connection.commit()
        connection.close()
    elif choice == 222: # display all in database
        displayAllInDatabase()
    elif choice == 3:   # insert blankMan
        strobj = convertPersonToString(blankMan)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_insert = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
                    VALUES %s;""" % (strobj)
        crsr.execute(sql_insert)
        connection.commit()
        connection.close()
    elif choice == 33:   # delete blankMan
        # obj = ThisPerson(dudeMan)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_del = """DELETE FROM ThisGroup WHERE id = %i;""" % (blankMan.id)
        crsr.execute(sql_del)
        connection.commit()
        connection.close()
    elif choice == 333: #insert group into myTable.db
        insertGroupIntoTable(seedarray)
    elif choice == 4:
        strobj = convertPersonToString(seedperson)
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_insert = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
                    VALUES %s;""" % (strobj)
        crsr.execute(sql_insert)
        connection.commit()
        connection.close()
    elif choice == 44:
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        sql_del = """DELETE FROM ThisGroup WHERE id = %i;""" % (seedperson.id)
        crsr.execute(sql_del)
        connection.commit()
        connection.close()
    elif choice == 5:   # transfer data from text file to database
        transferGroupIntoTable(personSQLArray)
    elif choice == 55:   # transfer data from database to text file, incomplete
        transferTableIntoGroupList()
    elif choice == 555:   # test
        convertStringToPerson()

# Driver program
if __name__ == "__main__":
    exit_flag = 0
    while exit_flag == 0:
        print("\nWelcome to This Database Control Panel")
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

        # for p in personSQLArray:
        #     format_str = """INSERT INTO ThisGroup (fname, lname, pword, gender, id, salary)
        #     VALUES ("{first}", "{last}", "{pw}", "{gr}", "{idd}", "{sal}");"""
        #     sql_insert = format_str.format(first=p[0], last=p[1], pw=p[2], gr=p[3], idd=p[4], sal=p[5])
        #     crsr.execute(sql_insert)
