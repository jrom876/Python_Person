#!/usr/bin/python3

# https://realpython.com/python-testing/#automated-vs-manual-testing
# To run test in shell:
# python -m unittest test
# python -m unittest -v test
# python -m unittest discover
# python -m unittest discover -s tests
# python -m unittest discover -s tests -t src
# python -m unittest discover -s tests/integration

#############################################
# unittest Method           Equivalent to
# .assertEqual(a, b) 	    a == b
# .assertTrue(x) 	        bool(x) is True
# .assertFalse(x) 	        bool(x) is False
# .assertIs(a, b) 	        a is b
# .assertIsNone(x) 	        x is None
# .assertIn(a, b) 	        a in b
# .assertIsInstance(a, b) 	isinstance(a, b)
#############################################
# Unwanted Matches between any users are defined as:
# 1) Same passwords
# 2) Same user ID
# 3) Same first and last names
#############################################

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

## globals for testing
parr = []
seedperson = ThisPerson("Yari","Koznow","vodka",'F',65500,61)
blankMan = ThisPerson("blankman","nunya","nada",'_',0,0)
dudeMan = ThisPerson("Charlie","Zulu","whiskey",'M',7007,25)
stevo = ThisPerson("Steve","Koz","yuno",'M',1042,59)
jb = ThisPerson("James","Bond","scotch","U",1007,47)

## Master lists for screening
fnlist = ["James","Homer","Homer1","Steve","Yari","Yert"]
lnlist = ["Bond","Koz","Koznow","Simpson","Simpson1","Stanis"]
pwlist = ["beer","gin","kahlua","mmmbeer","nada","rum","scotch","tequila","vodka","yuno"]
grlist = ['M','F','_','U']
idlist = [0,3,1007,1008,1009,1010,1042,1091,1096,1097,1098,64000,65500]

class TestPerson(unittest.TestCase):

    def testPerAttr(self):

        ###############################################################################
        ############## Instantiate test modules and put them in a list ################
        
        p0 = ThisPerson("Yari","Koznow","vodka",'F',65500,61)
        p1 = ThisPerson("Homer1","Simpson1","mmmbeer",'M',1009,47)
        p2 = ThisPerson("Yert","Stanis","rum",'F',64000,43)
        p3 = ThisPerson("Testo","Scripto","tequila",'M',1096,49)
        p4 = self.cloneHuman(jb)
        p5 = self.cloneHuman(stevo)
        p6 = self.cloneHuman(dudeMan)
        p7 = ThisPerson("James","Bond","gin","U",1007,47)
        p8 = self.cloneHuman(blankMan)
        p9 = ThisPerson()
        p10 = ThisPerson("Testo","Scripto","kahlua",'M',1098,49)
        # p4 = self.cloneHumanFromKeybd()
        # p5 = self.cloneHumanFromKeybd()
        # p0.copyPerson(p4)
        # p0.copyPerson(blankMan)
        # print("""This and """ + """That %s """ % (p10.convertPersonToString(p10)))
        parr = [p0,p1,p2,p3,p10]

        ########################################################################
        ################### Start the Test Battery #############################

        ### Create, clone and modify test arrays
        self.printGroup(parr)
        # ptest = self.cloneGroup(parr)
        tg1 = ThisGroup(parr)
        # tg1 = self.cloneGroup(parr)
        # tg1.addPersonToGroup(p7)
        # tg1.addPersonToGroup(p8)
        # tg1.addPersonToGroup(p10)
        tg1.loopGroup()
        # tg1.removePersonFromGroup(p10)
        # cg1 = self.cloneGroup(tg1.perlist)

        ###########################################
        ### Iteration Tests
        # self.iterateOverPersonArray()
        # self.iterateOverPersonList()
        # self.iterateOverMainItems()
        # self.compareGroup(tg1.perlist,dudeMan)
        self.comparePersonsLoop(tg1.perlist)
        tg1.writeGroupToFile(tg1)
        tg1.readGroupFromFile()

        ###########################################
        ### Print out Person attributes
        # print("\nPerson p0 initialized to: \t{0}\n".format(parr[0].myperson))
        # print("Person p1 initialized to: \t{0}\n".format(parr[1].myperson))
        # print("Person p2 initialized to: \t{0}\n".format(parr[2].myperson))
        # print("Person p3 initialized to: \t{0}\n".format(parr[3].myperson))
        # print("Person p4 initialized to: \t{0}\n".format(parr[4].myperson))
        # print("Person p5 initialized to: \t{0}\n".format(parr[5].myperson))

        ### Alter Person p0 (Yari) so he can pass the assertions below
        # p0.setThisPersonData("Homer","Simpson","beer",p0.gender,p0.id+256,p0.salary)
        # p0.setThisPersonData("Homer","Simpson")
        # print("\nPerson p0 altered to: \t{0}\n".format(p0.myperson))

        ### Alter Person p2 (Yert) so he can pass the assertions below
        # p2.copyPerson(stevo)
        # p2.setThisPersonData("Steve","Koz","yuno",p2.gender,p2.id,p2.salary)
        # print("Person p2 altered to: \t{0}\n".format(p2.myperson))

        ##########################################################
        ########## Watch List Screen ##########

        ###  Assertions to screen for simulated watch list persons

        # print("\nfname for p0: {0}\tlname for p0: {1}\tpword: {2}\n".format(p0.fname,
        # p0.lname,p0.pword))
        # self.assertFalse(((p0.fname == "Yari")&(p0.lname == "Koznow")),"Thats Yari Koznow!!")
        # self.assertFalse((((p0.fname == "Yari")&(p0.lname == "Koznow"))|(p0.id == 65500)),"Thats Yari Koznow!!")

        # print("fname for p1: {0}\tlname for p1: {1}\tpword: {2}\n".format(p1.fname,
        # p1.lname,p1.pword))
        # self.assertEqual(p1.fname, "Homer1", "That's not Homer1")

        # print("fname for p2: {0}\tlname for p2: {1}\tpword: {2}\n".format(p2.fname,
        # p2.lname,p2.pword))

        # self.assertNotIn(p2.id, idlist, "That ID is on the list")
        # self.assertNotIn(p2.pword, pwlist, "That password is being used")

        # print("\nfname for p2: {0}\tlname for p2: {1}\tpword: {2}\n".format(p2.fname,p2.lname,p2.pword))
        # self.assertNotEqual(p2.fname, "Yert", "That's Yert")

        # print("fname for p3: {0}\tlname for p3: {1}\tpword: {2}\n".format(p3.fname,
        # p3.lname,p3.pword))
        # print("fname for p4: {0}\tlname for p4: {1}\tpword: {2}\n".format(p4.fname,
        # p4.lname,p4.pword))
        # print("fname for p5: {0}\tlname for p5: {1}\tpword: {2}\n".format(p5.fname,
        # p5.lname,p5.pword))

        ########## End of Watch List Screen ##########
        ##############################################

        ################ Check Lists #################
        ### These loops and checks verify that the IDs and PWs
        ### of each group are included in the master lists
        self.loopGroupIDList(tg1)
        self.loopGroupPWList(tg1)
        self.checkIDList(p2)
        self.checkPWList(p2)

        ##############################################
        ########## comparePersons ##########
        ## Run comparePersons Method for specific interpersonal screening
        # self.comparePersons(p0,p1)
        # self.comparePersonsLoop(parr)
        # self.compareGroup(parr,dudeMan)

        ####### Assertions #######
        # self.assertNotEqual(p0.pword, p1.pword, "Error: same passwords")
        # self.assertFalse(((p0.fname == p1.fname)&(p0.lname == p1.lname)), "Errror: same first and last names")
        # self.assertFalse((p0.id == p1.id),"Error: same IDs")

        ####### Write to File #######
        ## If they pass all the compares and assertions, write them to file
        # self.wtf(p0,p1,p2,p3,p4,p5)

############################## End of Test Battery #############################
################################################################################

############################## Test Class Methods ##############################

    ## Unwanted Matches between any users are defined as:
    ## 1) Same passwords
    ## 2) Same user ID
    ## 3) Same first and last names

    ## comparePersons Method: using assertions and conditional statements to
    ## screen for unwanted matches between users

    def comparePersons(self,per0,per1):
        p0 = per0
        p1 = per1
        # print("\nCompare " + p0.fname + " and " + p1.fname)
        if(p0.pword == p1.pword):
            print("Passwords match for {0} and {1}: {2}".format(p0.fname,p1.fname,p0.pword))
            # self.assertNotEqual(p0.pword, p1.pword, "Error, same passwords")
        # else:
        #     print("Passwords acceptable")

        if(p0.id == p1.id):
            print("IDs match for {0} and {1}: {2}".format(p0.fname,p1.fname,p0.id))
            self.assertFalse((p0.id == p1.id),"Error, same IDs")
        # else:
        #         print("IDs acceptable")

        if((p0.fname == p1.fname)&(p0.lname == p1.lname)):
            print("First and Last names match for {0} and {1}".format(p0.fname,p1.fname))
            # self.assertFalse(((p0.fname == p1.fname)&(p0.lname == p1.lname)),
            #  "Errror, same first and last names")
        # else:
        #         print("Name acceptable")

    def comparePersonsLoop(self,personarray):
        for i in personarray:
            for j in personarray:
                # if (i.id == j.id)|(i.pword == j.pword):
                #     self.comparePersons(i,j)
                # if (i.mytuple == j.mytuple):
                #     continue
                if (i.id == j.id)&((i.fname == j.fname)&(i.lname == j.lname)):
                    continue
                self.comparePersons(i,j)

    def compareGroup(self,personarray,person):
        for i in personarray:
            if (i.id == person.id)|(i.pword == person.pword):
                self.comparePersons(i,person)
            if ((i.fname == person.fname)&(i.lname == person.lname)&(i.pword != person.pword)):
                continue
            self.comparePersons(i,person)

##############################################################
#################### checkList Methods #######################
### These loops and checks verify that the IDs and PWs of each group
### are included in the master lists

    def checkIDList(self,per1):
        # print("\nfname for per1: {0}\tlname for per1: {1}\tpword: {2}\n".format(per1.fname,per1.lname,per1.pword))
        self.assertIn(per1.id, idlist, "That ID is not on the list")

    def checkPWList(self,per1):
        # print("\nfname for per1: {0}\tlname for per1: {1}\tpword: {2}\n".format(per1.fname,per1.lname,per1.pword))
        self.assertIn(per1.pword, pwlist, "That password is not on the list")

    def loopGroupIDList(self,group):
        for i in group.perlist:
            self.checkIDList(i)

    def loopGroupPWList(self,group):
        for i in group.perlist:
            self.checkPWList(i)

##############################################
####### Clone Human Methods #######

    def cloneHuman(self,person):
        p1 = ThisPerson(person.fname, person.lname,
        person.pword, person.gender, person.id, person.salary)
        print("cloning person:\t {0}".format(p1.mytuple)) ## DBPRINT
        return p1

    def cloneHumanFromDefinition(self,fn,ln,pw,gr,id,sal):
        p1 = ThisPerson(fn, ln, pw, gr, id, sal)
        print("Defined NewPerson: {0}".format(p1.mytuple)) ## DBPRINT
        return p1

    def cloneHumanFromKeybd(self):
        fn = input("Enter first name: ")
        ln = input("Enter last name: ")
        pw = input("Enter pw: ")
        gr = input("Enter gender: ")
        id = input("Enter id: ")
        sal = input("Enter salary: ")
        p1 = ThisPerson(fn, ln, pw, gr, int(id), int(sal))
        print("person:\t {0}".format(p1.mytuple)) ## DBPRINT
        return p1

    def wtf(self,p0,p1,p2,p3,p4,p5):
        ## If they pass the compares and assertions, write them to file
        p0.writePersonToFile(p0)
        p1.writePersonToFile(p1)
        p2.writePersonToFile(p2)
        p3.writePersonToFile(p3)
        p4.writePersonToFile(p4)
        p5.writePersonToFile(p5)

#############################################
####### Group Test Methods #######

    def cloneGroup(self,array):
        g1 = ThisGroup(array)
        print("Clone Group: ")
        self.printGroup(array)
        return g1

    def printGroup(self,array):
        for i in array:
            print("printGroup: \t{0}".format(i.mytuple))

#############################################
####### Iterators #######

    def iterateOverMainItems(self):
        for f in fnlist:
            for l in lnlist:
                for p in pwlist:
                    for i in idlist:
                        tp = ThisPerson(f,l,p,'X',i,100)
                        print("{0}".format(tp.mytuple))
                        # self.assertFalse(((tp.id == 64000)&(tp.pword == "rum")&((tp.fname == "Yert")&(tp.lname == "Stanis"))),"That's Yert")
                        # self.assertFalse(((tp.id == 1007)&(tp.pword == "scotch")&((tp.fname == "James")&(tp.lname == "Bond"))),"Bond. James Bond.")

    def iterateOverPersonList(self):
        for f in fnlist:
            for l in lnlist:
                for p in pwlist:
                    for g in grlist:
                        for i in idlist:
                            tp = ThisPerson(f,l,p,g,i,47)
                            print("{0}".format(tp.mytuple))
                            self.assertFalse(((tp.id == 64000)&(tp.pword == "rum")&((tp.fname == "Yert")&(tp.lname == "Stanis"))),"That's Yert")
                            self.assertFalse(((tp.gender == 'U')&(tp.id == 1007)&(tp.pword == "scotch")&((tp.fname == "James")&(tp.lname == "Bond"))),"Bond. James Bond.")

    def iterateOverPersonArray(self):
        # personArray = [[i] for i in parr]
        for j in parr:
            # self.comparePersons(parr[j],parr[j+1])
            print("{0}".format(parr[j].fname))
        # return parr

##########################################################
## Main ##
if __name__ == '__main__':
    unittest.main()

############ Construction Zone ############
######## End of Construction Zone #########

    # x = str(34)
    # print("""This and """ + """That %s """ % (x))
