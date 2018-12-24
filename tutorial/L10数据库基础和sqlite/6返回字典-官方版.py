import sqlite3

def dict_factory(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

connect = sqlite3.connect("testsqlite.db")
connect.row_factory = dict_factory
cursor = connect.cursor()
cursor.execute("select * from employee;")
print(cursor.fetchall())