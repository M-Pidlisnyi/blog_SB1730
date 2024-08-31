import sqlite3

db_name = "blog.db"
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()


def getCategories():
    open()
    cursor.execute(" SELECT * FROM category ")
    result = cursor.fetchall()
    close()
    return result

def getPosts():
    open()
    cursor.execute(" SELECT * FROM post ")
    result = cursor.fetchall()
    close()
    return result

def getPostsInCategory(id):
    open()
    cursor.execute( "SELECT * FROM post WHERE category_id == ?", [id] )
    result = cursor.fetchall()
    close()
    return result    

def getCategoryById(id):
    open()
    cursor.execute( "SELECT name FROM category WHERE id == ?", [id] )
    result = cursor.fetchone()
    close()
    return result    



