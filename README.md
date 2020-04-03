# TestPerson
Python code to create person, group, and unittest classes, with an sql database interface

This project started as an interview programming challenge from a potential employer who gave me an hour to create a struct program in C with at least one string, one char, one int, and one short int which would also convert all outputs to bytecode, and then write the python version for extra credit.

This is similar to the classic struct person program that every computer science student has done 
at one time or another. So I wrote the first struct Person program, then later I expanded their requirements to 
include both C and python versions of a robust .txt object to sql converter. That is the genesis of this project.

See: https://github.com/jrom876/Person_check for the latest C version.

Since then (three weeks ago as of this writing) the python version has evolved into this ambitious project 
which creates the framework for a Person-class .txt file to database converter with unit testing, using sqlite3. 

The current python version has:
    
    0.   ThisPerson class which defines the methods and attributes of the fundamental ThisPerson object
    1.   ThisGroup class which creates an expandable, iterable and testable array of ThisPerson text objects
    2.   .txt file to sql interface for creation and manipulation of a database of ThisPerson text objects
    3.   unittest framework with assertions, searchlists, and iterators for testing all classes
    
This project is under continuous development, and may change at any time.

