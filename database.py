import time
"""
Created by: Jacob Toller (B922435), 13 ‎November ‎2019, ‏‎14:39:10

database.py is the module which handles the low level database interactions,
this means reading and writing data to and from the file and directly
returning the data with minimal processing.

An exception to this is the exchange between ';' and '*sc*', as I'm using
';' as the separator to separate attributes between the same entry.

To separate different entries inside the database.txt file, a new line is used
as a separator.

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
        data[i][1] = data[i][1].replace("*sc*",";")
    return data

def find_by_bookID(book_id):
    """Returns the book with the appropriate book ID.

Parameters:
    book_id; string: book id of the book to be returned.

Returns:
    find_by_bookID(...); list/boolean: returns the book as a list if it is found
        or returns False if it is not found.

"""
    for i in read_database():
        if i[0] == book_id:
            return i
    return False

def update_member_id(book_id,new_member_id):
    """Finds the database entry with the appropriate book ID and replaces
the old member ID with the new member ID.

Parameters:
    book_id: string; the book_id used to find the entry to be changed.
    new_member_id: string; the value which the member ID of the entry will
        be set to.

This function does not return a value
"""
    data = read_database()
    for i in data:
        if i[0] == book_id:
            i[4] = new_member_id
            break
    
    for i in range(0,len(data)):
        data[i][1] = data[i][1].replace(";","*sc*")
        data[i] = ";".join(data[i])

    data = "\n".join(data)
    with open("database.txt","w") as file:
        file.write(data)

def create_log_entry(operation,book_id,member_id):
    """Creates a new entry in the logbook.txt file.

Parameters:
    operation: string; sets what operation will be written to the log.
    book_id, member_id: string; sets the book and member IDs to be written.

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

def read_logfile():
    """Reads and returns the logfile data

Returns:
    read_logfile(...); 2D list: List containing each log entry as a sub list,
        with each attribute of the entry as a different element. For more
        information, read the documentation of create_log_entry(...)
"""
    with open("logfile.txt","r") as file:
        data = file.read().split("\n")

    while data[len(data)-1] == "":
        del data[-1]

    for i in range(0,len(data)):
        data[i] = data[i].split(";")
    return data

def reset():
    """FOR TESTING PURPOSES ONLY, resets all member IDs to 0, does not log
"""
    for i in data:
        database.update_member_id(i[0],"0")

if __name__ == "__main__": # Testing and Examples/Demonstration
    print(read_logfile())
    print(read_database())
    create_log_entry("-","34","2309")
    print(read_logfile())
    update_member_id("1","1556")
    if input("press ENTER to continue, enter anything else to reset database") != "":
        reset()

    
     
