#!/usr/bin/python3

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
from TestPerson import *
from printName import *

class ThisPerson:
    def __init__(self, fname="", lname="", pword="", gender='', id=0, salary=0):
        if id < 0:
            id = 0
        if salary < 0:
            salary = 0
        self.fname = fname
        self.lname = lname
        self.pword = pword
        self.gender = gender
        self.id = id
        self.salary = salary
        self.mytuple = (fname,lname,pword,gender,id,salary)
        self.myperson = [fname,lname,pword,gender,id,salary]
        self.mykvpair = {id: [fname,lname,pword,gender,id,salary]}

    def copyPerson(self, person):
        self.fname = person.fname
        self.lname = person.lname
        self.pword = person.pword
        self.gender = person.gender
        self.id = person.id
        self.salary = person.salary
        self.mytuple = (self.fname,self.lname,self.pword,self.gender,self.id,self.salary)
        self.myperson = [self.fname,self.lname,self.pword,self.gender,self.id,self.salary]
        self.mykvpair = {self.id: [self.fname,self.lname,self.pword,self.gender,self.id,self.salary]}

    def setThisPersonData(self,fn,ln,pw,gr,id,sal):
        self.fname = fn
        self.lname = ln
        self.pword = pw
        self.gender = gr
        self.id = id
        self.salary = sal
        self.mytuple = (fn,ln,pw,gr,id,sal)
        self.myperson = [fn,ln,pw,gr,id,sal]
        self.mykvpair = {id: [fn,ln,pw,gr,id,sal]}

    def getThisPersonData(self):
        print("{0}".format(self.mytuple))
        # print("{0}".format(self.myperson))
        # print("fname:\t {0}".format(self.fname))
        # print("lname:\t {0}".format(self.lname))
        # print("pword:\t {0}".format(self.pword))
        # print("gender:\t {0}".format(self.gender))
        # print("id:\t {0}".format(self.id))
        # print("salary:\t {0}\n".format(self.salary))

    def createPerson(self,fn,ln,pw,gr,id,sal):
        p1 = ThisPerson(fn, ln, pw, gr, id, sal)
        print("{0}".format(p1.mytuple)) ## DBPRINT
        return p1

    def writePersonToFile(self,person):
        localtime = time.asctime( time.localtime(time.time()) )
        file0 = open("personlist.txt","a")
        print("{0}".format(localtime))
        file0.write("{0}\n".format(person.mytuple))
        file0.close()

    def convertPersonToString(self,person):
        strPerson = "(\"%s\", \"%s\", \"%s\", \'%c\', %i, %i)"  % (person.fname,
        person.lname,person.pword, person.gender,person.id,person.salary)
        print("strPerson: {0}".format(strPerson))
        return strPerson

# Driver program
if __name__ == "__main__":
    p0 = ThisPerson("Human","George","yar",'M',2001,40)
    p1 = ThisPerson("H","G","y",'F',10101,140)
    # p0.copyPerson(p1)
    p1.convertPersonToString(p1)
    p0.getThisPersonData()
    # p0.writePersonToFile(ThisPerson("H","G","y",'A',2001,40))
    # p0.writePersonToFile(p0)
    p0.setThisPersonData("TestHuman","Gorgon","meepzor",'U',2041,80)
    p0.getThisPersonData()# printPersonName(p0.fname)
    #
    # ptest2 = p0.createPerson("Hun","Guizang","wong",'M',p0.id,p0.salary)
    # printgender(p0.gender)
    # convID2bytearr(p0.id)
    # convSal2bytearr(p0.salary)
    print("\n")
    # printPerson()
#
