import pandas as pd
import pymssql as pdb

# READ DATA FILES THAT WERE GENERATED
employees_df = pd.read_csv("/Users/roberthartman/Desktop/employee_data.csv")
contractors_df = pd.read_csv("/Users/roberthartman/Desktop/contractor_data.csv")

# DATABASE SETUP
sql_server = 'idw683509901.database.windows.net'
sql_username = 'IDW'
sql_password = 'Robbie55!87421'
sql_database = 'IDW'
conn = pdb.connect(server=sql_server, user=sql_username, password=sql_password, database=sql_database)
cursor = conn.cursor()

# INSERT STATEMENTS
employee_insert = "INSERT INTO [IDW].[HR_EMPLOYEE_STG] VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

sql_data = tuple(map(tuple, employees_df.values))
cursor.executemany(employee_insert, sql_data)
conn.commit()
cursor.close()
conn.close()
