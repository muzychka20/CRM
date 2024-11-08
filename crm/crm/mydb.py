import pyodbc

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={{WIN-4R9LA9I48B5}};DATABASE={{CRM}};Trusted_Connection=yes;Encrypt=no;' # UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)
cursor = conn.cursor()

SQL_QUERY = """SELECT * FROM test"""

cursor.execute(SQL_QUERY)
for row in cursor.fetchall():
    print (row)