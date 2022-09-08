FROM tadeorubio/pyodbc-msodbcsql17

ENV sql_server="host.docker.internal"
ENV sql_username="SA"
#TODO: replace to pull password from azure key vault rather than hard coding
ENV sql_password="SpaceXTest12345"
ENV sql_database="SPACEX"

WORKDIR /app
COPY . .

# # install FreeTDS and dependencies
# RUN apt-get update \
#  && apt-get install unixodbc -y \
#  && apt-get install unixodbc-dev -y \
#  && apt-get install freetds-dev -y \
#  && apt-get install freetds-bin -y \
#  && apt-get install tdsodbc -y \
#  && apt-get install --reinstall build-essential -y
# # populate "ocbcinst.ini" as this is where ODBC driver config sits
# RUN echo "[FreeTDS]\n\
# Description = FreeTDS Driver\n\
# Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
# Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini



# RUN apt-get install sudo -y
# RUN apt update && sudo apt upgrade -y
# RUN apt-get install wget build-essential checkinstall -y
# RUN apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev -y
# RUN cd /usr/src
# RUN wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
# RUN tar xzf Python-3.7.9.tgz
# RUN cd Python-3.7.9
# RUN ./configure --enable-optimizations
# RUN make altinstall


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["hrdata.py"]
