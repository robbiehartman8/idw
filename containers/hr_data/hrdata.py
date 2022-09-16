from pkgutil import get_data
import flask
import pymssql as pdb
import pandas as pd
from flask import request, jsonify
import traceback
import os
import logging

# LOGGING CONFIG
logging.basicConfig(format = '%(asctime)s %(name)s %(funcName)s:%(lineno)d %(levelname)s %(message)s')
logger = logging.getLogger('hrdata.py')
logger.setLevel("INFO")

# CREATE FLASK APP
hrdata = flask.Flask(__name__)

# DATABASE CONNECTION DETAILS
# sql_server = os.getenv("sql_server")
# sql_username = os.getenv("sql_username")
# sql_password = os.getenv("sql_password")
# sql_database = os.getenv("sql_database")
sql_server = 'idw683509901.database.windows.net'
sql_username = 'IDW'
sql_password = 'Robbie55!87421'
sql_database = 'IDW'

# SQL STATEMENTS FOR APIS
select_employees = "SELECT * FROM IDW.HR_EMPLOYEE_API_STG"
select_contractors = "SELECT * FROM IDW.HR_CONTRACTOR_STG"

# DB CONNECTION FUNCTION
def dbConnetion():
    try:
        conn = pdb.connect(server=sql_server, user=sql_username, password=sql_password, database=sql_database)
        cursor = conn.cursor()
    except:
        logger.critical("CANNOT CONNECT TO SQL SERVER\n")
        logger.critical(traceback.print_exc())
        exit()
    return conn, cursor

# GET EMPLOYEE DATA FROM DATABASE
def getEmployeeData():
    conn, cursor = dbConnetion()
    get_data = pd.read_sql(select_employees, conn)
    # get_data = pd.read_csv("/Users/roberthartman/Desktop/employee_data.csv")
    js = get_data.to_json(orient = 'records')
    conn.close()
    return js

# GET CONTRCTOR DATA FROM DATABASE
def getContractorData():
    conn, cursor = dbConnetion()
    get_data = pd.read_sql(select_contractors, conn)
    get_data = pd.read_csv("/Users/roberthartman/Desktop/contractor_data.csv")
    js = get_data.to_json(orient = 'records')
    conn.close()
    return js

# EMPLOYEE ROUTES
@hrdata.route('/api/v1/employees', methods=["GET", "POST", "PUT"])
def processEmployees():
    if request.method == "GET":
        return getEmployeeData()

# CONTRACTOR ROUTES
@hrdata.route('/api/v1/contractors', methods=["GET", "POST", "PUT"])
def processContractors():
    if request.method == "GET":
        return getContractorData()

# START FLASK APP
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    hrdata.run(debug=False, host='0.0.0.0', port=port)
