FROM tadeorubio/pyodbc-msodbcsql17

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["hrdata.py"]
