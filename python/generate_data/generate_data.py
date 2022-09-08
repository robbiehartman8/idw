import pandas as pd
import random
from faker import Faker
fake = Faker()
fake.seed_instance(4321)

def getData(number_of_people, iteration):
    # GENERATE ATTIBUTES FOR HR DATA
    employee_id = 1000000 + iteration + 1
    first_name = fake.first_name()
    middle_name = fake.first_name()
    last_name = fake.last_name()
    locations = ("9384", "2838", "2394", "7432")
    locations_dict = {"9384":"NEW YORK CITY - DOWNTOWN", "2838":"NEW YORK CITY - MIDTOWN", "2394":"CHICAGO", "7432":"SEATTLE"}
    location = random.choice(locations)
    location_description = locations_dict[location]
    cost_center_dict = {"9384":"28348577", "2838":"2884001", "2394":"2339490", "7432":"23848019"}
    cost_center = cost_center_dict[location]
    email_domains = ("@gmail.com", "@yahoo.com", "@aol.com")
    email_domain = random.choice(email_domains)

    # JOB TITLE CALC
    job_title = ""
    if employee_id == 1000001:
        job_title = "CEO"
    elif employee_id in range(1000002, 1000007):
        job_title = "EVP"
    elif employee_id in range(1000006, 1000011):
        job_title = "SVP"
    elif employee_id in range(1000010, 1000021):
        job_title = "VP"
    elif employee_id in range(1000020, 1000031):
        job_title = "SDIR"
    elif employee_id in range(1000030, 1000041):
        job_title = "DIR"
    elif employee_id in range(1000040, 1000056):
        job_title = "SM"
    elif employee_id in range(1000055, 1000071):
        job_title = "EM"
    elif employee_id in range(1000070, 1000101):
        job_title = "ENG"
    elif employee_id > 1000100:
        job_title = "ANALYST"

    # JOB TITLE DESC MAPPING
    job_title_dict = {"CEO":"CHIEF EXECUTIVE OFFICER", "EVP":"EXECUTIVE VICE PRESIDENT", "SVP":"SENIOR VICE PRESIDENT", "VP":"VICE PRESIDENT", "SDIR":"SENIOR DIRECTOR", "DIR":"DIRECTOR", "SM":"SENIOR MANAGER", "EM":"ENGINEERING MANAGER", "ENG":"ENGINEER", "ANALYST":"BUSINESS ANALYST"}
    job_title_desc = job_title_dict[job_title]

    # EMPLOYEE TYPE CALC
    employee_types = ("FULL_TIME", "PART_TIME")
    if job_title == "ENG" or job_title == "ANALYST":
        employee_type = random.choice(employee_types)
    else:
        employee_type = "FULL_TIME"

    # START DICTIONARY
    dict = {
        "EMPLOYEE_ID": str(employee_id),
        "FIRST_NAME": first_name,
        "MIDDLE_NAME": middle_name,
        "LAST_NAME": last_name,
        "HIRE_DATE": str(fake.date_time_between(start_date='-1y', end_date='+5d'))[:10],
        "STATUS": "A",
        "EMPLOYEE_TYPE": employee_type,
        "LOCATION_NUMBER": location,
        "LOCATION_DESCRIPTION": location_description,
        "JOB_TITLE": job_title,
        "JOB_TITLE_DESCRIPTION": job_title_desc,
        "COST_CENTER": cost_center,
        "MANAGER_EMPLOYEE_ID": "",
        "PERSONAL_EMAIL": "{}_{}_{}{}".format(first_name,middle_name,last_name,email_domain),
        "PHONE_NUMBER": fake.phone_number()
    }

    # RETURN THE DICT WITH USER DATA
    return dict

#CREATE DATAFRAME WITH HR DATA
df = pd.DataFrame()
for i in range(0,130):
    df = df.append(getData(100, i), ignore_index = True)

df.to_csv('/Users/roberthartman/Desktop/employee_data.csv', index = False)
