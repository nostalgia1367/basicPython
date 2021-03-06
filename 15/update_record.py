import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("""
UPDATE PHONEBOOK SET PHONE=?, EMAIL=? WHERE NAME=?
""", ('123-1234-4567', '123@shinhye.com', '박신혜'))

conn.commit()

cursor.execute("""
SELECT NAME, PHONE, EMAIL FROM PHONEBOOK
WHERE NAME=?
""", ('김범수',))

rows = cursor.fetchall()
for row in rows:
   print ("NAME: {0}, PHONE: {1}, EMAIL: {2} ".
        format(row[0], row[1], row[2]))

cursor.close()
conn.close()