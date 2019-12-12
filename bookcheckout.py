import database

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

    
