DROP PROCEDURE IF EXISTS sCollegeAdd;
CREATE PROCEDURE sCollegeAdd( IN PCollegeID int(11), IN PUniversityID int(11), IN PName varchar(1024), IN PCode varchar(64), IN PAddr1 varchar(255), IN PAddr2 varchar(255), IN PAddr3 varchar(255), IN PCityID int(11), IN PStateID int(11), IN PPincode int(11), IN PPhone varchar(255), IN PEmail varchar(255), IN PLogo varchar(1024), IN PURL varchar(1024) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tCollege (CollegeID, UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL)
    VALUES (PCollegeID, PUniversityID, PName, PCode, PAddr1, PAddr2, PAddr3, PCityID, PStateID, PPincode, PPhone, PEmail, PLogo, PURL);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'College_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sCollegeUpdate;
CREATE PROCEDURE sCollegeUpdate(IN PCollegeID int(11), IN PUniversityID int(11), IN PName varchar(1024), IN PCode varchar(64), IN PAddr1 varchar(255), IN PAddr2 varchar(255), IN PAddr3 varchar(255), IN PCityID int(11), IN PStateID int(11), IN PPincode int(11), IN PPhone varchar(255), IN PEmail varchar(255), IN PLogo varchar(1024), IN PURL varchar(1024))
  BEGIN
    DECLARE _id INT;
    UPDATE tCollege
    SET
    CollegeID = PCollegeID, UniversityID = PUniversityID, Name = PName, Code = PCode, Addr1 = PAddr1, Addr2 = PAddr2, Addr3 = PAddr3, CityID = PCityID, StateID = PStateID, Pincode = PPincode, Phone = PPhone, Email = PEmail, Logo = PLogo, URL = PURL
    WHERE College_ID = PCollege_ID;

    SET _id = PCollege_ID;

    CALL sGetTransactionStatus(1,_id, 'College_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sCollegeDelete;
CREATE PROCEDURE sCollegeDelete(IN PID INT)
  BEGIN
    DELETE FROM tCollege
    WHERE College_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'College_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sCollegeGet;
CREATE PROCEDURE sCollegeGet(IN PID INT)
  BEGIN
    SELECT
      CollegeID, UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL
    FROM tCollege
    WHERE College_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sCollegeGetList;
CREATE PROCEDURE sCollegeGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      CollegeID, UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL

      FROM tCollege;

    ELSE
      SELECT
      CollegeID, UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL

      FROM tCollege
      WHERE find_in_set(College_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sCollegeObjectGet;
CREATE PROCEDURE sCollegeObjectGet(IN PID INT)
  BEGIN
    SELECT
      CollegeID, UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL
    FROM tCollege
    # WHERE College_ID = PCollege_ID;
  END;



DROP PROCEDURE IF EXISTS sCollegeObjectGetList;
CREATE PROCEDURE sCollegeObjectGetList(IN PCollegeID int(11), IN PUniversityID int(11), IN PName varchar(1024), IN PCode varchar(64), IN PAddr1 varchar(255), IN PAddr2 varchar(255), IN PAddr3 varchar(255), IN PCityID int(11), IN PStateID int(11), IN PPincode int(11), IN PPhone varchar(255), IN PEmail varchar(255), IN PLogo varchar(1024), IN PURL varchar(1024))
  BEGIN


    SELECT
    CollegeID, UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL

    FROM
      tCollege
    #       WHERE Status = PStatus
    ORDER BY College_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sCollegeObjectGetListPage;
CREATE PROCEDURE sCollegeObjectGetListPage(IN PCollegeID int(11), IN PUniversityID int(11), IN PName varchar(1024), IN PCode varchar(64), IN PAddr1 varchar(255), IN PAddr2 varchar(255), IN PAddr3 varchar(255), IN PCityID int(11), IN PStateID int(11), IN PPincode int(11), IN PPhone varchar(255), IN PEmail varchar(255), IN PLogo varchar(1024), IN PURL varchar(1024) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tCollege
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      CollegeID, UniversityID, Name, Code, Addr1, Addr2, Addr3, CityID, StateID, Pincode, Phone, Email, Logo, URL

      FROM
        tCollege
      #       WHERE Status = PStatus
      ORDER BY College_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


