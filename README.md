# Python_Person
Python code to create person, group, and unittest classes, with an sql database interface

This project started as an interview programming challenge from a potential employer who gave me an hour to write and test a program in C that creates a struct with at least one string, one char, one int, and one short int which would also convert all outputs to bytecode, and then write the python version for extra credit.

This is similar to the classic struct person program that every computer science student has done at one time or another.

So I wrote and tested the first part of this program right then in 48 minutes, and it worked so well that I later expanded the requirements to include both C and python versions of a text object to sql converter.

That is the genesis of this project.

See: https://github.com/jrom876/Person_struct for the latest C version.

Since then the python version has evolved into the framework for a Person-class text file to database converter with unit testing, using sqlite3. 

The current python version has:
    
    0.   A ThisPerson class which defines the methods and attributes of the fundamental ThisPerson object
    1.   A ThisGroup class which creates an expandable, iterable and testable array of ThisPerson text objects
    2.   A text file to sql interface for creation and manipulation of a database of ThisPerson text objects
    3.   A unittest framework with assertions, searchlists, and iterators for testing all classes
    
This project is under continuous development, and may change at any time.

