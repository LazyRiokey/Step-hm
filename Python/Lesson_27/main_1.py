import pyodbc
from prettytable import from_db_cursor, PrettyTable
from sqlalchemy import create_engine
from sqlalchemy.orm import Session as SQLSession
from sqlalchemy.orm import sessionmaker


""" Способ 1 """


connection_db = pyodbc.connect("Driver={SQL Server};Server=DESKTOP-5M46QKS\\SQLEXPRESS;Database=University;Trusted_connection=yes;")
cursor = connection_db.cursor()
cursor.execute("SELECT * FROM Subjects")

my_table = from_db_cursor(cursor)
print(my_table)

connection_db.close()


""" Способ 2 """


# engine = create_engine("mssql://DESKTOP-5M46QKS\\SQLEXPRESS/University?driver=ODBC Driver 17 for SQL Server")
# connection = engine.connect()

# session = sessionmaker(bind=engine)
# session: SQLSession = session()

# my_table = PrettyTable()
# my_table.field_names = ["Subject_id" ,"Subject"]

# subjects = session.execute("SELECT * FROM Subjects;")

# for i in subjects:
#     my_table.add_row(i)

# my_table.align = "l"
# print(my_table)

# session.close()
