import database

def checkout(book_id,member_id):
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

    
