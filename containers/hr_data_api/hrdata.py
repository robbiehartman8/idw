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
logger = logging.getLogger('hrdata.py')
logger.setLevel("INFO")

# CREATE FLASK APP
hrdata = flask.Flask(__name__)

# DATABASE CONNECTION DETAILS
sql_server = 'idw683509901.database.windows.net'
sql_username = 'IDW'
sql_password = 'Robbie55!87421'
sql_database = 'IDW'

# SQL STATEMENTS FOR APIS
select_employees = "SELECT EMPLOYEE_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME,HIRE_DATE,TERMINATION_DATE,STATUS,EMPLOYEE_TYPE,LOCATION_NUMBER,LOCATION_DESCRIPTION,JOB_TITLE,JOB_TITLE_DESCRIPTION,COST_CENTER,MANAGER_EMPLOYEE_ID,PERSONAL_EMAIL,PHONE_NUMBER FROM IDW.HR_EMPLOYEE_API_STG WHERE UPDATE_FLAG IS NOT NULL"
select_employee = "SELECT EMPLOYEE_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME,HIRE_DATE,TERMINATION_DATE,STATUS,EMPLOYEE_TYPE,LOCATION_NUMBER,LOCATION_DESCRIPTION,JOB_TITLE,JOB_TITLE_DESCRIPTION,COST_CENTER,MANAGER_EMPLOYEE_ID,PERSONAL_EMAIL,PHONE_NUMBER FROM IDW.HR_EMPLOYEE_API_STG WHERE UPDATE_FLAG IS NOT NULL AND EMPLOYEE_ID = '{}'"

# DB CONNECTION FUNCTION
#TODO: CHANGE TO PYODBC
def dbConnetion():
    try:
        conn = pdb.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+sql_server+';DATABASE='+sql_database+';ENCRYPT=yes;UID='+sql_username+';PWD='+ sql_password)
        cursor = conn.cursor()
    except:
        logger.critical("CANNOT CONNECT TO SQL SERVER\n")
        logger.critical(traceback.print_exc())
        exit()
    return conn, cursor

# GET EMPLOYEE DATA FROM DATABASE
def getEmployeesData():
    conn, cursor = dbConnetion()
    get_data = pd.read_sql(select_employees, conn)
    js = get_data.to_json(orient = 'records')
    conn.close()
    return js 

# GET EMPLOYEE DATA FROM DATABASE
def getEmployeeData(employeeID):
    conn, cursor = dbConnetion()
    get_data = pd.read_sql(select_employee.format(employeeID), conn)
    js = get_data.to_json(orient = 'records')
    conn.close()
    return js


########################################### API 

# EMPLOYEE ROUTES
@hrdata.route('/api/v1/employees', methods=["GET"])
def processEmployees():
    if request.method == "GET":
        return getEmployeesData()

# EMPLOYEE ROUTES
@hrdata.route('/api/v1/employee/<employeeID>', methods=["GET"])
def processEmployee(employeeID):
    if request.method == "GET":
        return getEmployeeData(employeeID)

########################################### API         

# START FLASK APP
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    hrdata.run(debug=False, host='0.0.0.0', port=port)
