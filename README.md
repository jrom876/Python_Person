# TestPerson
Python code to create person, group, unittest, and sql database classes

This project started as an interview programming challenge from a potential employer 
who gave me an hour to create a person struct program in C which could also convert all 
class attributes to bytecode, and then write the python version for extra credit. 

See https://github.com/jrom876/arrStructExample/arrStructExample.c for the C version.

Since then it has evolved into a much larger project to create the framework for an expandable 
person class database written in python and sqlite3 with:
    
    0. a ThisPerson class which defines the methods and attributes of the Person data entity
    1. a ThisGroup class which creates an expandable, iterable and testable array of ThisPerson objects
    2. a python to sql database interface for creation and manipulation of a database of Person objects
    3. a unittest framework with assertions, searchlists, and iterators for testing all classes
    
This project is under continual development, and may change at any time.

