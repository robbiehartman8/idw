--------------------------------------------------------------------
----- CREATE GENERATE_UID -----
--------------------------------------------------------------------

CREATE OR ALTER FUNCTION [IDW].[GENERATE_UID] ()
RETURNS VARCHAR(255)
AS
BEGIN
    DECLARE @UID VARCHAR(255) 
    DECLARE @EXISTS BIT = 0
    WHILE (@EXISTS = 0)
    BEGIN
        SET @UID = CONVERT(VARCHAR(10),LEFT(REPLACE((SELECT NEW_ID FROM [IDW].[GET_NEW_ID]),'-',''),6))
        IF (SELECT COUNT(DISTINCT [UID]) FROM IDW.IDW_WKR_MAIN WHERE [UID] = @UID) = 0  
            BEGIN
                SET @EXISTS = 1
            END
        ELSE
            BEGIN
                SET @EXISTS = 0
            END
    END
    RETURN @UID
END
GO