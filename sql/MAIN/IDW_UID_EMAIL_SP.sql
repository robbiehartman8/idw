--------------------------------------------------------------------
----- CREATE IDW_UID_EMAIL_SP -----
--------------------------------------------------------------------

CREATE OR ALTER PROCEDURE [IDW].[IDW_UID_EMAIL_SP] @TABLE VARCHAR(255), @VALUE VARCHAR(255)
AS
    IF @TABLE = 'EMAIL'
    BEGIN 
        INSERT INTO [IDW].[IDW_EMAIL_STG] VALUES (@VALUE)
    END
    ELSE 
    BEGIN
        INSERT INTO [IDW].[IDW_UID_STG] VALUES (@VALUE)
    END
GO