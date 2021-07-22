import sqlite3
from func import *

conn = sqlite3.connect('identifier.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Users
(TG_ID INTEGER,
First_Name STRING,
Phone_number INTEGER,
TABLE_NUMB INTEGER,
Zakaz LIST,
Mark INTEGER 
)
''')
first_insert = '''
INSERT INTO Users VALUES ('{}', '{}', 0, 0,'no',0)
'''
id_in_table = '''
SELECT TG_ID
FROM Users
WHERE TG_ID = '{}'
'''
update_phone ='''
UPDATE Users
SET Phone_number = '{}'
WHERE TG_ID = '{}'
'''

add_zakaz = '''
SELECT Zakaz
FROM Users
WHERE TG_ID = '{}'
'''

update_zakaz ='''
UPDATE Users
SET Zakaz = '{}'
WHERE TG_ID = '{}'
'''

update_mark = '''
UPDATE Users
SET Mark = '{}'
WHERE TG_ID = '{}'
'''

update_history = '''
UPDATE Users
SET Zakaz = '{}'
WHERE TG_ID = '{}'
'''


update_table_number = '''
UPDATE Users
SET TABLE_NUMB = '{}'
WHERE TG_ID = '{}'
'''
table_number_in_table = '''
SELECT TABLE_NUMB
FROM Users
WHERE TG_ID = '{}'
'''