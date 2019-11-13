"""
Created by: Jacob Toller, 14:39, 13/11/19

database.py is the module which handles the low level database interactions,
this means reading and writing data to and from the file and directly
returning the data with minimal processing.

An exception to this is the exchange between ';' and '*sc*', as I'm using
';' as the separator to separate attributes between the same entry

To separate different entries inside the database.txt file, a new line is used
as 

"""

def read_database():
    """Reads and returns data from the database.txt file

returns a 2D array with the data from database.txt, after performing the
following:
    splits the whole text file into an array, with each line as a separate
    element

    removes any spare instances of new lines at the end of the array

    splits each element from the array into its own array, creating a 2D array,
    changes everything to its correct data type, and replaces '*sc*' with ';'
    in the title of the book

"""
    with open("database.txt","r") as file:
        data = file.read().split("\n")

    while data[len(data)-1] == "":
        del data[-1]

    for i in range(0,len(data)):
        data[i] = data[i].split(";")
        data[i][0] = int(data[i][0])
        data[i][4] = int(data[i][4])
        data[i][1] = data[i][1].replace("*sc*",";")
    return data

print(read_database())
     
