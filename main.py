import sqlite3
conn =sqlite3.connect('identifier.sqlite')
cur = conn.cursor()
cur.execute('''
UPDATE Users
SET TABLE_NUMB = 100
WHERE 
''')