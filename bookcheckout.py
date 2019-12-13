import database
import bookreturn # Used for testing purposes
"""
Created by: Jacob Toller (B922435), ‎05 ‎December ‎2019, ‏‎10:33:35

bookcheckout.py is the module used for mid-level operations which involve
taking books out of the system

for low-level direct operations, see database.py

"""

def checkout(book_id,member_id):
    """Sets a books member value to the provided member_id, returns false if not found or is already out

Parameters:
    book_id: string; the book_id used to find the book to be returned
    member_id: string; the member_id of the member borrowing the book

Returns:
    checkout(...): boolean; True if successful, False otherwise
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
    elif current_member_id != "0":
        print("book already checked out")
        return False
    else:
        database.update_member_id(book_id,member_id)
        database.create_log_entry("-",book_id,member_id)
        return True

if __name__ == "__main__":
    bookreturn.deposit("4657") # makes sure that book 4657 is in storage
    print("Success:",checkout("1","4657")) # This should return true
    print("Success:",checkout("1","1456")) # Shoild return false as book 1 is out

    
