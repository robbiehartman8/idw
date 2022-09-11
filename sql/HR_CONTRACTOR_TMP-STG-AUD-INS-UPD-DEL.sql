--------------------------------------------------------------------
----- CREATE HR_CONTRACTOR_TMP-STG-AUD-INS-UPD -----
--------------------------------------------------------------------

CREATE TABLE [IDW].[HR_CONTRACTOR_TMP] (
    IDW_GUID VARCHAR(255) NOT NULL PRIMARY KEY,
    IDW_USER_CREATE VARCHAR(255) NOT NULL,
    IDW_USER_MODIFY VARCHAR(255) NOT NULL,
    IDW_CREATE_TIMESTAMP DATETIME NOT NULL,
    IDW_MODIFY_TIMESTAMP DATETIME NOT NULL,
    IDW_PRIMARY_KEY VARCHAR(255) NOT NULL,
    IDW_JOB_ID VARCHAR(255) NOT NULL,
    IDW_STG_HASH_VALUE VARCHAR(255) NOT NULL,
    EMPLOYEE_ID VARCHAR(255) NULL,
    FIRST_NAME VARCHAR(255) NULL,
    MIDDLE_NAME VARCHAR(255) NULL,
    LAST_NAME VARCHAR(255) NULL,
    HIRE_DATE VARCHAR(255) NULL,
    TERMINATION_DATE VARCHAR(255) NULL,
    STATUS VARCHAR(255) NULL,
    EMPLOYEE_TYPE VARCHAR(255) NULL,
    LOCATION_NUMBER VARCHAR(255) NULL,
    LOCACTION_DESCRIPTION VARCHAR(255) NULL,
    JOB_TITLE VARCHAR(255) NULL,
    JOB_TITLE_DESCRIPTION VARCHAR(255) NULL,
    COST_CENTER VARCHAR(255) NULL,
    MANAGER_EMPLOYEE_ID VARCHAR(255) NULL,
    PERSONAL_EMAIL VARCHAR(255) NULL,
    PHONE_NUMBER VARCHAR(255) NULL
)
GO

CREATE TABLE [IDW].[HR_CONTRACTOR_STG] (
    IDW_GUID VARCHAR(255) NOT NULL PRIMARY KEY,
    IDW_USER_CREATE VARCHAR(255) NOT NULL,
    IDW_USER_MODIFY VARCHAR(255) NOT NULL,
    IDW_CREATE_TIMESTAMP DATETIME NOT NULL,
    IDW_MODIFY_TIMESTAMP DATETIME NOT NULL,
    IDW_PRIMARY_KEY VARCHAR(255) NOT NULL,
    IDW_JOB_ID VARCHAR(255) NOT NULL,
    IDW_STG_HASH_VALUE VARCHAR(255) NOT NULL,
    EMPLOYEE_ID VARCHAR(255) NULL,
    FIRST_NAME VARCHAR(255) NULL,
    MIDDLE_NAME VARCHAR(255) NULL,
    LAST_NAME VARCHAR(255) NULL,
    HIRE_DATE VARCHAR(255) NULL,
    TERMINATION_DATE VARCHAR(255) NULL,
    STATUS VARCHAR(255) NULL,
    EMPLOYEE_TYPE VARCHAR(255) NULL,
    LOCATION_NUMBER VARCHAR(255) NULL,
    LOCACTION_DESCRIPTION VARCHAR(255) NULL,
    JOB_TITLE VARCHAR(255) NULL,
    JOB_TITLE_DESCRIPTION VARCHAR(255) NULL,
    COST_CENTER VARCHAR(255) NULL,
    MANAGER_EMPLOYEE_ID VARCHAR(255) NULL,
    PERSONAL_EMAIL VARCHAR(255) NULL,
    PHONE_NUMBER VARCHAR(255) NULL
)
GO

CREATE TABLE [IDW].[HR_CONTRACTOR_AUD] (
    OPERATION VARCHAR(255) NOT NULL,
    IDW_GUID VARCHAR(255) NOT NULL,
    IDW_USER_CREATE VARCHAR(255) NOT NULL,
    IDW_USER_MODIFY VARCHAR(255) NOT NULL,
    IDW_CREATE_TIMESTAMP DATETIME NOT NULL,
    IDW_MODIFY_TIMESTAMP DATETIME NOT NULL,
    IDW_PRIMARY_KEY VARCHAR(255) NOT NULL,
    IDW_JOB_ID VARCHAR(255) NOT NULL,
    IDW_STG_HASH_VALUE VARCHAR(255) NOT NULL,
    EMPLOYEE_ID VARCHAR(255) NULL,
    FIRST_NAME VARCHAR(255) NULL,
    MIDDLE_NAME VARCHAR(255) NULL,
    LAST_NAME VARCHAR(255) NULL,
    HIRE_DATE VARCHAR(255) NULL,
    TERMINATION_DATE VARCHAR(255) NULL,
    STATUS VARCHAR(255) NULL,
    EMPLOYEE_TYPE VARCHAR(255) NULL,
    LOCATION_NUMBER VARCHAR(255) NULL,
    LOCACTION_DESCRIPTION VARCHAR(255) NULL,
    JOB_TITLE VARCHAR(255) NULL,
    JOB_TITLE_DESCRIPTION VARCHAR(255) NULL,
    COST_CENTER VARCHAR(255) NULL,
    MANAGER_EMPLOYEE_ID VARCHAR(255) NULL,
    PERSONAL_EMAIL VARCHAR(255) NULL,
    PHONE_NUMBER VARCHAR(255) NULL
)
GO