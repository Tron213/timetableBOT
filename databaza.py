import sqlite3

database=sqlite3.connect('students.sqlite')
cursor=database.cursor()



def add_user(message):
    cursor.execute("""SELECT id FROM users WHERE id=?""",(message.chat.id,))
    user=cursor.fetchone
    if not user:
        cursor.execute("INSERT INTO users VALUES(?,?,?)",(message.chat.id,"name","namb",))
        database.commit
    else:
        pass

def add_user_name(message):
    cursor.execute("UPDATE users SET name=? WHERE id=?",(message.text,message.chat.id,))
    database.commit()

def add_user_namb(message):
    cursor.execute("UPDATE users SET namb=? WHERE id=?",(message.text,message.chat.id,))
    database.commit()
    