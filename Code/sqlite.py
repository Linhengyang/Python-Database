# author: Linhengyang
import sqlite3

# search in DB
def get_salary_in(low, high):
    try:
        conn = sqlite3.connect(r"../Data/testDB.db")
        cursor = conn.cursor()
        sql = "SELECT NAME FROM COMPANY WHERE SALARY BETWEEN ? AND ? ORDER BY SALARY ASC"
        cursor.execute(sql, (low, high))
        outputs = cursor.fetchall()
    except Exception as err:
        print(err)
        outputs = []
    else:
        print("SQLite works well")
    finally:
        cursor.close()
        conn.close()
    return [tp[0] for tp in outputs]

# try to create table and insert records
conn = sqlite3.connect(r"../Data/testDB.db")
cursor = conn.cursor()
# create one table
sql = "CREATE TABLE USER (ID INT PRIMARY KEY NOT NULL, NAME CHAR(20), SCORE INT)"
cursor.execute(sql)
# insert one record to USER table
sql = "INSERT INTO USER VALUES (?, ?, ?)"
cursor.execute(sql, (1, "Aaron", 99))
cursor.rowcount
# insert another record to USER table
cursor.execute(sql, (2, "Hengyang", 100))
cursor.rowcount
# insert multiple records to USER table by executemany(sql, seq_of_params)
cursor.executemany(sql, ((3, "Lin", 100), (4, "other", 50)))

cursor.close()
conn.commit()
conn.close()