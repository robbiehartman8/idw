from pkgutil import get_data
import flask
import pyodbc as pdb
import pandas as pd
from flask import request, jsonify
import traceback
import os
import logging

# LOGGING CONFIG
logging.basicConfig(format = '%(asctime)s %(name)s %(funcName)s:%(lineno)d %(levelname)s %(message)s')
logger = logging.getLogger('worker_api.py')
logger.setLevel("INFO")

# CREATE FLASK APP
worker = flask.Flask(__name__)

# DATABASE CONNECTION DETAILS
sql_server = os.getenv('sql_server')
sql_username = os.getenv('sql_username')
sql_password = os.getenv('sql_password')
sql_database = os.getenv('sql_database')

# SQL STATEMENTS FOR APIS
select_workers = "SELECT UID,PERSON_TYPE,EMPLOYEE_ID,CONTRACTOR_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME,HIRE_DATE,TERMINATION_DATE,STATUS,EMPLOYEE_TYPE,LOCATION_NUMBER,LOCATION_DESCRIPTION,JOB_TITLE,JOB_TITLE_DESCRIPTION,COST_CENTER,MANAGER_EMPLOYEE_ID,PERSONAL_EMAIL,PHONE_NUMBER,WORK_EMAIL FROM IDW.IDW_WKR_MAIN"
select_worker = "SELECT UID,PERSON_TYPE,EMPLOYEE_ID,CONTRACTOR_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME,HIRE_DATE,TERMINATION_DATE,STATUS,EMPLOYEE_TYPE,LOCATION_NUMBER,LOCATION_DESCRIPTION,JOB_TITLE,JOB_TITLE_DESCRIPTION,COST_CENTER,MANAGER_EMPLOYEE_ID,PERSONAL_EMAIL,PHONE_NUMBER,WORK_EMAIL FROM IDW.IDW_WKR_MAIN WHERE UID = '{}'"

# DB CONNECTION FUNCTION
def dbConnetion():
    try:
        conn = pdb.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+sql_server+';DATABASE='+sql_database+';ENCRYPT=yes;UID='+sql_username+';PWD='+ sql_password)
        cursor = conn.cursor()
    except:
        logger.critical("CANNOT CONNECT TO SQL SERVER\n")
        logger.critical(traceback.print_exc())
        exit()
    return conn, cursor

# GET WORKERS DATA FROM DATABASE
def getWorkersData():
    conn, cursor = dbConnetion()
    get_data = pd.read_sql(select_workers, conn)
    js = get_data.to_json(orient = 'records')
    conn.close()
    return js 

# GET WORKER DATA FROM DATABASE
def getWorkerData(uid):
    conn, cursor = dbConnetion()
    get_data = pd.read_sql(select_worker.format(uid), conn)
    js = get_data.to_json(orient = 'records')
    conn.close()
    return js


########################################### API 

# WORKERS ROUTES
@worker.route('/api/v1/workers', methods=["GET"])
def processWorkers():
    if request.method == "GET":
        return getWorkersData()

# WORKER ROUTES
@worker.route('/api/v1/worker/<uid>', methods=["GET"])
def processWorker(uid):
    if request.method == "GET":
        return getWorkerData(uid)

########################################### API         

# START FLASK APP
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    worker.run(debug=False, host='0.0.0.0', port=port)
