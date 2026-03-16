import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM employees;")


cursor.execute("DELETE FROM sqlite_sequence WHERE name='employees';")

conn.commit()
conn.close()

print("✅ Employees table cleared and IDs reset to start from 1.")