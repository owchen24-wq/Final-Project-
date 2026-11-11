import sqlite3

con = sqlite3.connect("project.db")
con.execute("CREATE TABLE IF NOT EXISTS test (x INTEGER)")
con.execute("DELETE FROM test")
con.execute("INSERT INTO test VALUES (1)")
con.commit()

for row in con.execute("SELECT * FROM test"):
    print(row)

con.close()