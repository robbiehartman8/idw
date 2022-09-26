--------------------------------------------------------------------
----- CREATE GENERATE_EMAIL -----
--------------------------------------------------------------------

CREATE OR ALTER FUNCTION [IDW].[GENERATE_EMAIL] (@FIRST_NAME VARCHAR(255), @MIDDLE_NAME VARCHAR(255), @LAST_NAME VARCHAR(255))
RETURNS VARCHAR(255)
AS
BEGIN
    DECLARE @EMAIL VARCHAR(255) 
    DECLARE @EXISTS BIT = 0
    DECLARE @NUMBER INT = 1
    SET @EMAIL = TRIM(@FIRST_NAME) + '_' + TRIM(@MIDDLE_NAME) + '_' + TRIM(@LAST_NAME) + '@company.com'
    WHILE (@EXISTS = 0)
    BEGIN
        IF (SELECT COUNT(DISTINCT [WORK_EMAIL]) FROM IDW.IDW_WKR_MAIN WHERE [WORK_EMAIL] = @EMAIL) = 0  
            BEGIN
                SET @EXISTS = 1
            END
        ELSE
            BEGIN
                SET @EMAIL = REPLACE(@EMAIL, '@company.com', '')
                SET @EMAIL = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE (@EMAIL, '0', ''),'1', ''),'2', ''),'3', ''),'4', ''),'5', ''),'6', ''),'7', ''),'8', ''),'9', '')
                SET @EMAIL = @EMAIL + CAST(@NUMBER AS VARCHAR(20)) + '@company.com'
                SET @NUMBER = @NUMBER + 1
                SET @EXISTS = 0
            END
    END
    RETURN @EMAIL
END
GO