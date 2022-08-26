import flask
import requests
from bs4 import BeautifulSoup
import pymssql as pdb
import datetime
import pandas as pd
import re
from flask import request, jsonify
import traceback
import os

#create flask app
torIPAddresses = flask.Flask(__name__)

#database connection details
sql_server = os.getenv("sql_server")
sql_username = os.getenv("sql_username")
sql_password = os.getenv("sql_password")
sql_database = os.getenv("sql_database")

#define api operations and path
@torIPAddresses.route('/api/v1/hrdata', methods=["GET", "POST"])
def processRequest():
    if request.method == "GET":
        return ['hello']

if __name__ == '__main__':
    torIPAddresses.run(debug=False, host='0.0.0.0')
