import database
data = database.read_database()
for i in data:
    database.update_member_id(i[0],"0")
