import pandas as pd
import numpy as np
import random
from faker import Faker
fake = Faker()
fake.seed_instance(4321)

# GET THE EMPLOYEE DATA
def getEmployeeData(number_of_people, iteration, manager_dict):
    # GENERATE ATTIBUTES FOR HR DATA
    employee_id = 1000000 + iteration + 1
    first_name = fake.first_name()
    middle_name = fake.first_name()
    last_name = fake.last_name()
    locations = ("9384", "2838", "2394", "7432", "3905", "9902")
    locations_dict = {"9384":"NEW YORK CITY - DOWNTOWN", "2838":"NEW YORK CITY - MIDTOWN", "2394":"CHICAGO", "7432":"SEATTLE", "3905": "SALT LAKE CITY", "9902": "SAN DIEGO"}
    location = random.choice(locations)
    location_description = locations_dict[location]
    cost_center_dict = {"9384":"28348577", "2838":"2884001", "2394":"2339490", "7432":"23848019", "3905": "7377488", "9902": "12909949"}
    cost_center = cost_center_dict[location]
    email_domains = ("@gmail.com", "@yahoo.com", "@aol.com")
    email_domain = random.choice(email_domains)

    # NUMBER OF USERS IN JOB TITLE
    number_of_people_in_title_dict = {
        "EVP": 8,
        "SVP": 8,
        "VP": 50,
        "SDIR": 200,
        "DIR": 250,
        "SM": 2500,
        "EM": 4000
    }

    # NUMBER OF PEOPLE RATIOS
    ratio_evp = 1000001 + number_of_people_in_title_dict["EVP"]
    ratio_svp = ratio_evp + number_of_people_in_title_dict["SVP"]
    ratio_vp = ratio_svp + number_of_people_in_title_dict["VP"]
    ratio_sdir = ratio_vp + number_of_people_in_title_dict["SDIR"]
    ratio_dir = ratio_sdir + number_of_people_in_title_dict["DIR"]
    ratio_sm = ratio_dir + number_of_people_in_title_dict["SM"]
    ratio_em = ratio_sm + number_of_people_in_title_dict["EM"]
    ratio_eng = ratio_em + int((number_of_people - (ratio_em - 1000001)) / 2)

    # JOB TITLE CALC AND MANAGERS DICT
    job_title = ""
    if employee_id == 1000001:
        job_title = "CEO"
    elif employee_id in range(1000001, ratio_evp + 1):
        job_title = "EVP"
        manager_dict["report_to_ceo"].append(employee_id)
    elif employee_id in range(ratio_evp, ratio_svp + 1):
        job_title = "SVP"
        manager_dict["report_to_ceo"].append(employee_id)
    elif employee_id in range(ratio_svp, ratio_vp + 1):
        job_title = "VP"
        manager_dict["report_to_evp_svp"].append(employee_id)
    elif employee_id in range(ratio_vp, ratio_sdir + 1):
        job_title = "SDIR"
        manager_dict["report_to_vp"].append(employee_id)
    elif employee_id in range(ratio_sdir, ratio_dir + 1):
        job_title = "DIR"
        manager_dict["report_to_vp"].append(employee_id)
    elif employee_id in range(ratio_dir, ratio_sm + 1):
        job_title = "SM"
        manager_dict["report_to_sdir_dir"].append(employee_id)
    elif employee_id in range(ratio_sm, ratio_em + 1):
        job_title = "EM"
        manager_dict["report_to_sm"].append(employee_id)
    elif employee_id in range(ratio_em, ratio_eng + 1):
        job_title = "ENG"
        manager_dict["report_to_em"].append(employee_id)
    elif employee_id > ratio_eng:
        job_title = "ANALYST"
        manager_dict["report_to_em"].append(employee_id)

    # JOB TITLE DESC MAPPING
    job_title_dict = {"CEO":"CHIEF EXECUTIVE OFFICER", "EVP":"EXECUTIVE VICE PRESIDENT", "SVP":"SENIOR VICE PRESIDENT", "VP":"VICE PRESIDENT", "SDIR":"SENIOR DIRECTOR", "DIR":"DIRECTOR", "SM":"SENIOR MANAGER", "EM":"ENGINEERING MANAGER", "ENG":"ENGINEER", "ANALYST":"BUSINESS ANALYST"}
    job_title_desc = job_title_dict[job_title]

    # EMPLOYEE TYPE CALC
    employee_types = ("FULL_TIME", "PART_TIME")
    if job_title == "ENG" or job_title == "ANALYST":
        employee_type = random.choice(employee_types)
    else:
        employee_type = "FULL_TIME"

    # DATA DICTIONARY
    dict = {
        "EMPLOYEE_ID": str(employee_id),
        "FIRST_NAME": first_name,
        "MIDDLE_NAME": middle_name,
        "LAST_NAME": last_name,
        "HIRE_DATE": str(fake.date_time_between(start_date='-1y', end_date='+5d'))[:10],
        "TERMINATION_DATE": "",
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

# SET THE MANAGER ON THE EMPLOYEE RECORDS
def getManager(df, manager_dict):
    # SET ALL OF THE DICTIONARIES AND LISTS
    employees_title_dict = pd.Series(df.JOB_TITLE.values,index=df.EMPLOYEE_ID).to_dict()
    employee_split_dict = {}
    manager_employee_dict = {}
    employee_manager_dict = {}
    evp_svp_list = []
    vp_list = []
    sdir_dir_list = []
    sm_list = []
    em_list = []

    # CREATE REPORTING SPLITS
    for key, value in manager_dict.items():
        if key == "report_to_evp_svp":
            data = np.array_split(value, len(manager_dict["report_to_ceo"]))
            employee_split_dict[key] = [x.tolist() for x in [*data]]
        elif key == "report_to_vp":
            data = np.array_split(value, len(manager_dict["report_to_evp_svp"]))
            employee_split_dict[key] = [x.tolist() for x in [*data]]
        elif key == "report_to_sdir_dir":
            data = np.array_split(value, len(manager_dict["report_to_vp"]))
            employee_split_dict[key] = [x.tolist() for x in [*data]]
        elif key == "report_to_sm":
            data = np.array_split(value, len(manager_dict["report_to_sdir_dir"]))
            employee_split_dict[key] = [x.tolist() for x in [*data]]
        elif key == "report_to_em":
            data = np.array_split(value, len(manager_dict["report_to_sm"]))
            employee_split_dict[key] = [x.tolist() for x in [*data]]    

    # SEPERATE EMPLOYEES BY TITLES INTO LISTS
    for key, value in employees_title_dict.items():
        if value == "EVP" or value == "SVP":
            evp_svp_list.append(key)
        elif value == "VP":
            vp_list.append(key)
        elif value == "SDIR" or value == "DIR":
            sdir_dir_list.append(key)
        elif value == "SM":
            sm_list.append(key)
        elif value == "EM":
            em_list.append(key)

    # APPLY REPORTING EMPLOYEES TO MANAGERS
    for i in range(len(evp_svp_list)):
        manager_employee_dict[evp_svp_list[i]] = employee_split_dict["report_to_evp_svp"][i]
    for i in range(len(vp_list)):
        manager_employee_dict[vp_list[i]] = employee_split_dict["report_to_vp"][i]
    for i in range(len(sdir_dir_list)):
        manager_employee_dict[sdir_dir_list[i]] = employee_split_dict["report_to_sdir_dir"][i]
    for i in range(len(sm_list)):
        manager_employee_dict[sm_list[i]] = employee_split_dict["report_to_sm"][i]
    for i in range(len(em_list)):
        manager_employee_dict[em_list[i]] = employee_split_dict["report_to_em"][i]

    # SPLIT EMPLOYEES FROM REPORTING STRUCTURES AND MAP THEM TO MANAGERS
    for key, value in manager_employee_dict.items():
        for i in range(len(value)):
            employee_manager_dict[str(value[i])] = str(key)
    
    # PEOPLE THAT REPORT THE CEO
    for i in range(len(manager_dict["report_to_ceo"])):
        employee_manager_dict[str(manager_dict["report_to_ceo"][i])] = '1000001'

    # CEO REPORTS TO THEMSELVES
    employee_manager_dict['1000001'] = '1000001'
    
    # RETURN THE EMPLOYEE TO MANAGER MAPPING
    return employee_manager_dict

def applyManagers(df, employee_manager_dict):
    df["MANAGER_EMPLOYEE_ID"] = df["EMPLOYEE_ID"].map(employee_manager_dict)
    return df


def getContractorData(number_of_people, iteration, managers):
    # GENERATE ATTIBUTES FOR HR DATA
    contractor_id = 9000000 + iteration + 1
    first_name = fake.first_name()
    middle_name = fake.first_name()
    last_name = fake.last_name()
    locations = ("9384", "2838", "2394", "7432", "3905", "9902")
    locations_dict = {"9384":"NEW YORK CITY - DOWNTOWN", "2838":"NEW YORK CITY - MIDTOWN", "2394":"CHICAGO", "7432":"SEATTLE", "3905": "SALT LAKE CITY", "9902": "SAN DIEGO"}
    location = random.choice(locations)
    location_description = locations_dict[location]
    cost_center_dict = {"9384":"28348577", "2838":"2884001", "2394":"2339490", "7432":"23848019", "3905": "7377488", "9902": "12909949"}
    cost_center = cost_center_dict[location]
    email_domains = ("@ey.com", "@pwc.com", "@kpmg.com")
    email_domain = random.choice(email_domains)
    manager = random.choice(managers)

    # DATA DICTIONARY
    dict = {
        "CONTRACTOR_ID": "CW" + str(contractor_id),
        "FIRST_NAME": first_name,
        "MIDDLE_NAME": middle_name,
        "LAST_NAME": last_name,
        "HIRE_DATE": str(fake.date_time_between(start_date='-1y', end_date='+5d'))[:10],
        "TERMINATION_DATE": "",
        "STATUS": "A",
        "LOCATION_NUMBER": location,
        "LOCATION_DESCRIPTION": location_description,
        "JOB_TITLE": "CNTR",
        "JOB_TITLE_DESCRIPTION": "CONTRACTOR",
        "COST_CENTER": cost_center,
        "MANAGER_EMPLOYEE_ID": manager,
        "PERSONAL_EMAIL": "{}_{}_{}{}".format(first_name,middle_name,last_name,email_domain),
        "PHONE_NUMBER": fake.phone_number()
    }

    # RETURN THE DICT WITH USER DATA
    return dict



# CREATE DATAFRAME WITH HR DATA
employee_df = pd.DataFrame()
contractor_df = pd.DataFrame()
number_of_employees = 15000
number_of_contractors = 2500

# MANAGER HIERARCHY SETS
manager_dict = {
    "report_to_ceo": [],
    "report_to_evp_svp": [],
    "report_to_vp": [],
    "report_to_sdir_dir": [],
    "report_to_sm": [],
    "report_to_em": []
}

# GENERATE EMPLOYEE DATA
for i in range(0, number_of_employees):
    employee_df = employee_df.append(getEmployeeData(number_of_employees, i, manager_dict), ignore_index = True)
# GET MANAGER MAPPINGS
employee_manager_dict = getManager(employee_df, manager_dict)
# APPLY MANAGER MAPPINGS TO EMPLOYEE DATA
employee_df = applyManagers(employee_df, employee_manager_dict)
# EXPORT EMPLOYEE DATA
employee_df.to_csv('/Users/roberthartman/Desktop/employee_data.csv', index = False, header=True)

# GET MANAGERS LIST FOR CONTRACTORS
employee_df_managers = employee_df
employee_df_managers.query("JOB_TITLE == 'SM' or JOB_TITLE == 'EM'", inplace = True)
managers = employee_df_managers["EMPLOYEE_ID"].tolist()
# GENERATE CONTRACTOR DATA
for i in range(0, number_of_contractors):
    contractor_df = contractor_df.append(getContractorData(number_of_contractors, i, managers), ignore_index = True)
# EXPORT CONTRACTOR DATA
contractor_df.to_csv('/Users/roberthartman/Desktop/contractor_data.csv', index = False, header=True)