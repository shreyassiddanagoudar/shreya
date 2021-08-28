DROP PROCEDURE IF EXISTS sCityAdd;
CREATE PROCEDURE sCityAdd( IN PCityID int(11), IN PStateID int(11), IN PName varchar(1024), IN PCode varchar(64) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tCity (CityID, StateID, Name, Code)
    VALUES (PCityID, PStateID, PName, PCode);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'City_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sCityUpdate;
CREATE PROCEDURE sCityUpdate(IN PCityID int(11), IN PStateID int(11), IN PName varchar(1024), IN PCode varchar(64))
  BEGIN
    DECLARE _id INT;
    UPDATE tCity
    SET
    CityID = PCityID, StateID = PStateID, Name = PName, Code = PCode
    WHERE City_ID = PCity_ID;

    SET _id = PCity_ID;

    CALL sGetTransactionStatus(1,_id, 'City_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sCityDelete;
CREATE PROCEDURE sCityDelete(IN PID INT)
  BEGIN
    DELETE FROM tCity
    WHERE City_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'City_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sCityGet;
CREATE PROCEDURE sCityGet(IN PID INT)
  BEGIN
    SELECT
      CityID, StateID, Name, Code
    FROM tCity
    WHERE City_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sCityGetList;
CREATE PROCEDURE sCityGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      CityID, StateID, Name, Code

      FROM tCity;

    ELSE
      SELECT
      CityID, StateID, Name, Code

      FROM tCity
      WHERE find_in_set(City_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sCityObjectGet;
CREATE PROCEDURE sCityObjectGet(IN PID INT)
  BEGIN
    SELECT
      CityID, StateID, Name, Code
    FROM tCity
    # WHERE City_ID = PCity_ID;
  END;



DROP PROCEDURE IF EXISTS sCityObjectGetList;
CREATE PROCEDURE sCityObjectGetList(IN PCityID int(11), IN PStateID int(11), IN PName varchar(1024), IN PCode varchar(64))
  BEGIN


    SELECT
    CityID, StateID, Name, Code

    FROM
      tCity
    #       WHERE Status = PStatus
    ORDER BY City_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sCityObjectGetListPage;
CREATE PROCEDURE sCityObjectGetListPage(IN PCityID int(11), IN PStateID int(11), IN PName varchar(1024), IN PCode varchar(64) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tCity
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      CityID, StateID, Name, Code

      FROM
        tCity
      #       WHERE Status = PStatus
      ORDER BY City_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


