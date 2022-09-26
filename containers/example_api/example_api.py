import flask
from flask import request, jsonify
import traceback
import os
import logging

# LOGGING CONFIG
logging.basicConfig(format = '%(asctime)s %(name)s %(funcName)s:%(lineno)d %(levelname)s %(message)s')
logger = logging.getLogger('example_api.py')
logger.setLevel("INFO")

# CREATE FLASK APP
example = flask.Flask(__name__)

########################################### API 

# EXAMPLE ROUTES
@example.route('/api/v1/example', methods=["GET"])
def processRequest():
    if request.method == "GET":
        return "Hello World!"

########################################### API         

# START FLASK APP
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    example.run(debug=False, host='0.0.0.0', port=port)
