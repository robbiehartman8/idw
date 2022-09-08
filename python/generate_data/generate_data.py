import requests
import pymssql as pdb
import datetime
import pandas as pd
import re
import traceback
import os
import random
from faker import Faker
fake = Faker()
fake.seed_instance(4321)

def getData(number_of_people, iteration):
    employee_id = str(1000000 + iteration + 1)
    first_name = fake.first_name()
    middle_name = fake.first_name()
    last_name = fake.last_name()
    hire_date = str(fake.date_time_between(start_date='-1y', end_date='+5d'))[:10]
    status = "A"
    employee_types = ("FULL_TIME", "PART_TIME")
    employee_type = random.choice(employee_types)
    locations = ("9384", "2838", "2394", "7432")
    locations_dict = {"9384":"NEW YORK CITY - DOWNTOWN", "2838":"NEW YORK CITY - MIDTOWN", "2394":"CHICAGO", "7432":"SEATTLE"}
    location = random.choice(locations)
    location_description = locations_dict[location]
    job_titles = ("SWTENG", "SWTMGR", "TECDIR", "TECHVP")
    job_titles_dict = {"SWTENG":"SOFTWARE ENGINEER", "SWTMGR":"SOFTWARE ENGINEER MANAGER", "TECDIR":"TECHNOLOGY DIRECTOR", "TECHVP":"TECHNOLOGY VP"}
    job_title = random.choice(job_titles)
    job_title_desc = job_titles_dict[job_title]
    email_domains = ("@gmail.com", "@yahoo.com", "@aol.com")
    email_domain = random.choice(email_domains)
    person_email = "{}_{}_{}{}".format(first_name,middle_name,last_name,email_domain)
    phone_number = fake.phone_number()
    print(phone_number)


for i in range(0,100):
    getData(100, i)
