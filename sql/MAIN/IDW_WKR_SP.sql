--------------------------------------------------------------------
----- CREATE IDW_WKR_SP -----
--------------------------------------------------------------------

CREATE OR ALTER PROCEDURE [IDW].[IDW_WKR_SP] --@IDW_JOB_ID, @USER_ID
AS
    UPDATE STG
    SET
    IDW_USER_MODIFY = TMP.IDW_USER_MODIFY,
    IDW_MODIFY_TIMESTAMP = TMP.IDW_MODIFY_TIMESTAMP,
    IDW_JOB_ID = TMP.IDW_JOB_ID,
    IDW_WKR_HASH_VALUE = TMP.IDW_WKR_HASH_VALUE,
    FIRST_NAME = TMP.FIRST_NAME,
    MIDDLE_NAME = TMP.MIDDLE_NAME,
    LAST_NAME = TMP.LAST_NAME,
    HIRE_DATE = TMP.HIRE_DATE,
    TERMINATION_DATE = TMP.TERMINATION_DATE,
    STATUS = TMP.STATUS,
    EMPLOYEE_TYPE = TMP.EMPLOYEE_TYPE,
    LOCATION_NUMBER = TMP.LOCATION_NUMBER,
    LOCATION_DESCRIPTION = TMP.LOCATION_DESCRIPTION,
    JOB_TITLE = TMP.JOB_TITLE,
    JOB_TITLE_DESCRIPTION = TMP.JOB_TITLE_DESCRIPTION,
    COST_CENTER = TMP.COST_CENTER,
    PERSONAL_EMAIL = TMP.PERSONAL_EMAIL,
    PHONE_NUMBER = TMP.PHONE_NUMBER,
    WORK_EMAIL = TMP.WORK_EMAIL
    FROM IDW.IDW_WKR_MAIN AS STG
    INNER JOIN IDW.IDW_WKR_WRKING AS TMP ON TMP.IDW_GUID = STG.IDW_GUID
    WHERE TMP.IDW_WKR_HASH_VALUE != STG.IDW_WKR_HASH_VALUE

    INSERT INTO IDW.IDW_WKR_MAIN
    SELECT *
    FROM IDW.IDW_WKR_WRKING AS TMP
    WHERE NOT EXISTS (
        SELECT 1 FROM IDW.IDW_WKR_MAIN AS STG WHERE STG.IDW_GUID = TMP.IDW_GUID
    )
GO