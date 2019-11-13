import time
"""
Created by: Jacob Toller (B922435), 14:39, 13/11/19

database.py is the module which handles the low level database interactions,
this means reading and writing data to and from the file and directly
returning the data with minimal processing.

An exception to this is the exchange between ';' and '*sc*', as I'm using
';' as the separator to separate attributes between the same entry

To separate different entries inside the database.txt file, a new line is used
as 

"""

def read_database():
    """Reads and returns data from the database.txt file.

This function has no parameters

Returns a 2D array with the data from database.txt, after performing the
following:
    splits the whole text file into an array, with each line as a separate
    element

    removes any spare instances of new lines at the end of the array

    splits each element from the array into its own array, creating a 2D array,
    changes everything to its correct data type, and replaces '*sc*' with ';'
    in the title of the book

Returns a 2D array

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

def create_log_entry(operation,book_id,member_id):
    """Creates a new entry in the logbook.txt file.

Parameters:
    operation: string; sets what operation will be written to the log
    book_id, member_id: integer; sets the book and member IDs to be written

This function takes 3 parameters, as well as taking the system time
automatically, and adds them to the end of logfile.txt. For example:
create_log_entry("+","5","4657") would be called if member 4657 was to
return the book with ID 5, and would create the following line in the log:
+;5;4657;1573663746
The operation + signifies a book coming back into the library, as a return,
while - is used for checking out books.

This function does not return a value
"""
    data = ";".join([operation,str(book_id),str(member_id),str(round(time.time()))]) + "\n"
    
    with open("logfile.txt","a+") as file:
        file.write(data)

#print(read_database())
#create_log_entry("-","34","2309")
     
