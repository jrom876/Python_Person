# TestPerson
Python code to create person, group, and unittest classes, with an sql database interface

This project started as an interview programming challenge from a potential employer 
who gave me an hour to create a person struct program in C which could also convert all 
class attributes to bytecode, and then write the python version for extra credit. 

See https://github.com/jrom876/arrStructExample/arrStructExample.c for the early C version.

See: https://github.com/jrom876/Person_check for the latest C version.

Since then (three weeks ago as of this writing) it has evolved into this ambitious project 
to create the frameworks for two person type text-file-to-database converters 
written in both C and python using sqlite3. 

This is the current python version and it has:
    
    0.   ThisPerson class which defines the methods and attributes of the fundamental Person data entity
    1.   ThisGroup class which creates an expandable, iterable and testable array of ThisPerson text objects
    2.   python .txt to sql database interface for creation and manipulation of a database of ThisPerson objects
    3.   unittest framework with assertions, searchlists, and iterators for testing all classes
    
This project is under continual development, and may change at any time.

