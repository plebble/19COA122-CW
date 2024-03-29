import database
import bookcheckout # Used for testing purposes
"""
Created by: Jacob Toller (B922435), ‎‎09 ‎December ‎2019, ‏‎10:04:41

bookreturn.py is the module used for mid-level operations which involve
putting books back into the system

for low-level direct operations, see database.py

"""

def deposit(book_id):
    """Sets a books member value to 0, returns false if not found or is already returned

Parameters:
    book_id: string; the book_id used to find the book to be returned

Returns:
    deposit(...): boolean; True if successful, False otherwise
"""
    data = database.read_database()
    current_member_id = "-1"
    for i in data:
        if i[0] == book_id:
            current_member_id = i[4]
            break

    if current_member_id == "-1":
        print("book not found")
        return False
    elif current_member_id == "0":
        print("book is not currently checked out")
        return False
    else:
        database.update_member_id(book_id,"0")
        database.create_log_entry("+",book_id,current_member_id)
        return True

if __name__ == "__main__":
    bookcheckout.checkout("1","4657") # makes sure that book 4657 is out of the library
    print("Success:",deposit("1")) # This should return true
    print("Success:",deposit("1")) # Should return false as book 1 is out
