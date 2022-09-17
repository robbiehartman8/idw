--------------------------------------------------------------------
----- TRUNCATE TABLES -----
--------------------------------------------------------------------

TRUNCATE TABLE [IDW].[HR_EMPLOYEE_API_STG]
TRUNCATE TABLE [IDW].[HR_CONTRACTOR_FILE_STG]

TRUNCATE TABLE [IDW].[IDW_WKR_WRKING]
TRUNCATE TABLE [IDW].[IDW_WKR_MAIN]
TRUNCATE TABLE [IDW].[IDW_WKR_AUD]

TRUNCATE TABLE [IDW].[HR_EMPLOYEE_TMP]
TRUNCATE TABLE [IDW].[HR_EMPLOYEE_STG]
TRUNCATE TABLE [IDW].[HR_EMPLOYEE_AUD]

TRUNCATE TABLE [IDW].[HR_CONTRACTOR_TMP]
TRUNCATE TABLE [IDW].[HR_CONTRACTOR_STG]
TRUNCATE TABLE [IDW].[HR_CONTRACTOR_AUD]

--------------------------------------------------------------------
----- DROP TABLES -----
--------------------------------------------------------------------

DROP TABLE [IDW].[HR_EMPLOYEE_API_STG]
DROP TABLE [IDW].[HR_CONTRACTOR_FILE_STG]

DROP TABLE [IDW].[HR_EMPLOYEE_TMP]
DROP TABLE [IDW].[HR_EMPLOYEE_STG]
DROP TABLE [IDW].[HR_EMPLOYEE_AUD]

DROP TABLE [IDW].[HR_CONTRACTOR_TMP]
DROP TABLE [IDW].[HR_CONTRACTOR_STG]
DROP TABLE [IDW].[HR_CONTRACTOR_AUD]

DROP TABLE [IDW].[IDW_WKR_WRKING]
DROP TABLE [IDW].[IDW_WKR_MAIN]
DROP TABLE [IDW].[IDW_WKR_AUD]

--------------------------------------------------------------------
----- DROP PROCEDURES -----
--------------------------------------------------------------------

DROP PROCEDURE [IDW].[HR_EMPLOYEE_SP]
DROP PROCEDURE [IDW].[HR_CONTRACTOR_SP]
DROP PROCEDURE [IDW].[IDW_WKR_SP]

--------------------------------------------------------------------
----- DROP VIEWS -----
--------------------------------------------------------------------

DROP VIEW [IDW].[IDW_STAGED_USERS_VIEW]