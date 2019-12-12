import database
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
