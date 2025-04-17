# add_user.py
import sqlite3

rfid = input("Enter the RFID code: ")
name = input("Enter the user name: ")

conn = sqlite3.connect('rfid_system.db')
c = conn.cursor()
c.execute("INSERT OR REPLACE INTO users (rfid, name) VALUES (?, ?)", (rfid, name))
conn.commit()
conn.close()

print(f"User {name} added.")