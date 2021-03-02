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
from printName import *
from TestPerson import *
from ThisPerson import *

seedperson = ThisPerson("Yari","Koznow","victor",'Z',65500,61)
blankMan = ThisPerson("blankman","nunya","nada",'_',0,0)
dudeMan = ThisPerson("Charlie","Zulu","Whiskey",'U',7007,25)
seedarray = [seedperson,blankMan,dudeMan]

class ThisGroup:
    def __init__(self,array=[]):
        self.len = len(array)
        self.perlist = array
        # print("\nCreating ThisGroup: ")
        # self.loopGroup()

    def addPersonToGroup(self,person):
        fn = person.fname
        self.perlist.append(person)
        print("\nadding {0}".format(fn))

    def removePersonFromGroup(self,person):
        self.perlist.remove(person)
        # self.loopGroup()

    def loopGroup(self):
        # print("loopGroup:")
        for i in self.perlist:
            print("{0}".format(i.mytuple))
        # print("\n")

    def getGroup(self):
        for k in self.perlist:
            print("{0}".format(k.id))

    def writeGroupToFile(self,array):
        # localtime = time.asctime( time.localtime(time.time()) )
        file0 = open("grouplist.txt","a")
        # file0.write("{0}\n".format(localtime))
        for i in array.perlist:
            file0.write("{0}\n".format(i.mytuple))
        print("\n")
        file0.close()

    def readGroupFromFile(self):
        file0 = open("grouplist.txt","r")
        print("\n")
        op = file0.readlines()
        print(file0.read())
        file0.close()
        return op

    def convertThisGroupToString(self,array):
        result = []
        for i in array.perlist:
            result.append(i.convertThisPersonToString(i))
            print("result1: {0}".format(result))
        # print("result000: {0}".format(result))
        return result

    def convertG2S(self,array):
        result = [i for i in array.perlist]
        # result = [(k) for k in array]
        # self.insertGroupIntoTable(result)
        for i in array.perlist:
            result.append = i.convertThisPersonToString(i)
            print("strArray: {0}".format(i))
        return result

# Driver program
if __name__ == "__main__":
    g0 = ThisGroup(seedarray)
    print("")
    g0.convertThisGroupToString(g0)
    g0.readGroupFromFile()
    # g0.convertG2S(g0)
    # g0.addPersonToGroup(seedperson)
    # g0.addPersonToGroup(seedperson)
    # g0.getGroup()
    # print("\n")
    # g0.removePersonFromGroup(seedperson)
    # print("\n")
    # g0.loopGroup()
    g0.addPersonToGroup(jb)
    g0.loopGroup()

    print("\n")
