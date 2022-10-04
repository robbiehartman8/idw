# Step 1: Specify the parent image for the new image 
FROM tadeorubio/pyodbc-msodbcsql17

# STEP 2: Configure work directory 
WORKDIR /app

# STEP 3: Copy API code to container 
COPY . .

# STEP 4: Upgrade PIP and install the python requirements and env variables
ENV sql_server='usedadvcrdsql07.database.windows.net'
ENV sql_username='dbWSS'
ENV sql_password='cZVhQ6A4gW9xpIot*imKkuH9mWJ*IIfi'
ENV sql_database='IDW'

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# STEP 5: Define the entry point of the process that runs in the container
ENTRYPOINT ["python"]
CMD ["worker_api.py"]
