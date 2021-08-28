DROP PROCEDURE IF EXISTS sUniversityAdd;
CREATE PROCEDURE sUniversityAdd( IN PUniversityID int(11), IN PName varchar(1024), IN PCode varchar(64), IN PAddr1 varchar(255), IN PAddr2 varchar(255), IN PAddr3 varchar(255), IN PCityID int(11), IN PStateID int(11), IN PPincode int(11), IN PPhone varchar(255), IN PEmail varchar(255), IN PLogo varchar(1024), IN PURL varchar(1024) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tUniversity (UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL)
    VALUES (PUniversityID, PName, PCode, PAddr1, PAddr2, PAddr3, PCityID, PStateID, PPincode, PPhone, PEmail, PLogo, PURL);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'University_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sUniversityUpdate;
CREATE PROCEDURE sUniversityUpdate(IN PUniversityID int(11), IN PName varchar(1024), IN PCode varchar(64), IN PAddr1 varchar(255), IN PAddr2 varchar(255), IN PAddr3 varchar(255), IN PCityID int(11), IN PStateID int(11), IN PPincode int(11), IN PPhone varchar(255), IN PEmail varchar(255), IN PLogo varchar(1024), IN PURL varchar(1024))
  BEGIN
    DECLARE _id INT;
    UPDATE tUniversity
    SET
    UniversityID = PUniversityID, Name = PName, Code = PCode, Addr1 = PAddr1, Addr2 = PAddr2, Addr3 = PAddr3, CityID = PCityID, StateID = PStateID, Pincode = PPincode, Phone = PPhone, Email = PEmail, Logo = PLogo, URL = PURL
    WHERE University_ID = PUniversity_ID;

    SET _id = PUniversity_ID;

    CALL sGetTransactionStatus(1,_id, 'University_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sUniversityDelete;
CREATE PROCEDURE sUniversityDelete(IN PID INT)
  BEGIN
    DELETE FROM tUniversity
    WHERE University_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'University_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sUniversityGet;
CREATE PROCEDURE sUniversityGet(IN PID INT)
  BEGIN
    SELECT
      UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL
    FROM tUniversity
    WHERE University_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sUniversityGetList;
CREATE PROCEDURE sUniversityGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL

      FROM tUniversity;

    ELSE
      SELECT
      UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL

      FROM tUniversity
      WHERE find_in_set(University_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sUniversityObjectGet;
CREATE PROCEDURE sUniversityObjectGet(IN PID INT)
  BEGIN
    SELECT
      UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL
    FROM tUniversity
    # WHERE University_ID = PUniversity_ID;
  END;



DROP PROCEDURE IF EXISTS sUniversityObjectGetList;
CREATE PROCEDURE sUniversityObjectGetList(IN PUniversityID int(11), IN PName varchar(1024), IN PCode varchar(64), IN PAddr1 varchar(255), IN PAddr2 varchar(255), IN PAddr3 varchar(255), IN PCityID int(11), IN PStateID int(11), IN PPincode int(11), IN PPhone varchar(255), IN PEmail varchar(255), IN PLogo varchar(1024), IN PURL varchar(1024))
  BEGIN


    SELECT
    UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL

    FROM
      tUniversity
    #       WHERE Status = PStatus
    ORDER BY University_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sUniversityObjectGetListPage;
CREATE PROCEDURE sUniversityObjectGetListPage(IN PUniversityID int(11), IN PName varchar(1024), IN PCode varchar(64), IN PAddr1 varchar(255), IN PAddr2 varchar(255), IN PAddr3 varchar(255), IN PCityID int(11), IN PStateID int(11), IN PPincode int(11), IN PPhone varchar(255), IN PEmail varchar(255), IN PLogo varchar(1024), IN PURL varchar(1024) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tUniversity
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL

      FROM
        tUniversity
      #       WHERE Status = PStatus
      ORDER BY University_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


