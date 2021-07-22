import sqlite3
conn = sqlite3.connect('identifier.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Users
(TG_ID INTEGER,
First_Name STRING,
PHONE INTEGER,
TABLE_NUMB INTEGER,
Zakaz LIST,
Mark LIST )
''')
first_insert = '''
INSERT INTO Users VALUES ('{}', '{}', '0', 0,'a',0)
'''