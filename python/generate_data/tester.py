import pyodbc as pdb
import pandas as pd
import logging
import traceback

# LOGGING CONFIG
logging.basicConfig(format = '%(asctime)s %(name)s %(funcName)s:%(lineno)d %(levelname)s %(message)s')
logger = logging.getLogger('hrdata.py')
logger.setLevel("INFO")


sql_server = 'idw683509901.database.windows.net'
sql_username = 'IDW'
sql_password = 'Robbie55!87421'
sql_database = 'IDW'

conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};' + "SERVER={};".format(sql_server) + 'DATABASE={};'.format(sql_database) + 'UID=IDW;' + 'PWD=Robbie55!87421;'

# DB CONNECTION FUNCTION
def dbConnetion():
    try:
        # conn = pdb.connect(server=sql_server, user=sql_username, password=sql_password, database=sql_database)
        conn = pdb.connect(conn_str)
        cursor = conn.cursor()
    except:
        logger.critical("CANNOT CONNECT TO SQL SERVER\n")
        logger.critical(traceback.print_exc())
        exit()
    return conn, cursor

conn, cursor = dbConnetion()

random_contractors = "SELECT TOP 5 PERCENT * FROM IDW.HR_CONTRACTOR_FILE_STG ORDER BY NEWID()"

# df = pd.read_sql(random_contractors, conn)

cursor.execute(random_contractors)
data = cursor.fetchall()
pandas = pd.DataFrame(data)

print(pandas)