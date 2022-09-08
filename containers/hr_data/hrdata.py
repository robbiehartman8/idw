from pkgutil import get_data
import flask
import requests
import pymssql as pdb
import datetime
import pandas as pd
import re
from flask import request, jsonify
import traceback
import os
import logging

#logging config
logging.basicConfig(format = '%(asctime)s %(name)s %(funcName)s:%(lineno)d %(levelname)s %(message)s')
logger = logging.getLogger('hrdata.py')
logger.setLevel("INFO")

#create flask app
hrdata = flask.Flask(__name__)

#database connection details
# sql_server = os.getenv("sql_server")
# sql_username = os.getenv("sql_username")
# sql_password = os.getenv("sql_password")
# sql_database = os.getenv("sql_database")
sql_server = 'idw683509901.database.windows.net'
sql_username = 'IDW'
sql_password = 'Robbie55!87421'
sql_database = 'IDW'

select = "SELECT * FROM IDW.HR_DATA_STG"

def dbConnetion():
    #create databse connection
    try:
        conn = pdb.connect(server=sql_server, user=sql_username, password=sql_password, database=sql_database)
        cursor = conn.cursor()
    except:
        logger.critical("CANNOT CONNECT TO SQL SERVER\n")
        logger.critical(traceback.print_exc())
        exit()
    return conn, cursor

def getData():
    conn, cursor = dbConnetion()
    get_data = pd.read_sql(select, conn)
    js = get_data.to_json(orient = 'records')
    conn.close()
    return js

#define api operations and path
@hrdata.route('/api/v1/hrdata', methods=["GET", "POST", "PUT"])
def processRequest():
    if request.method == "GET":
        return getData()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    hrdata.run(debug=False, host='0.0.0.0', port=port)
