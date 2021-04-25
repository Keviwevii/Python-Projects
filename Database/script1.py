import sqlite3

# 5 Steps for a database
# Connect to database
# Create a cursor object to write to database
# Write SQL query
# Commit changes
# Close connection with database

#Creating table
def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

#Inserting data
def insert(item, quantity, price):
    conn=sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()
    

#Viewing database
def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

#Deleting 
def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item=?", (item,))
    conn.commit()
    conn.close()

#Updating
def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()
    



update(11,6, "Water Glass")
# delete("Wine Glass")
print(view())
# insert("Coffee Cup", 10, 5)