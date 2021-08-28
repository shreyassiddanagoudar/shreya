DROP PROCEDURE IF EXISTS sUniversityAYAdd;
CREATE PROCEDURE sUniversityAYAdd( IN PAYID int(11), IN PUniversityID int(11), IN PStartDate date, IN PEndDate date )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tUniversityAY (AYID, UniversityID, StartDate, EndDate)
    VALUES (PAYID, PUniversityID, PStartDate, PEndDate);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'UniversityAY_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sUniversityAYUpdate;
CREATE PROCEDURE sUniversityAYUpdate(IN PAYID int(11), IN PUniversityID int(11), IN PStartDate date, IN PEndDate date)
  BEGIN
    DECLARE _id INT;
    UPDATE tUniversityAY
    SET
    AYID = PAYID, UniversityID = PUniversityID, StartDate = PStartDate, EndDate = PEndDate
    WHERE UniversityAY_ID = PUniversityAY_ID;

    SET _id = PUniversityAY_ID;

    CALL sGetTransactionStatus(1,_id, 'UniversityAY_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sUniversityAYDelete;
CREATE PROCEDURE sUniversityAYDelete(IN PID INT)
  BEGIN
    DELETE FROM tUniversityAY
    WHERE UniversityAY_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'UniversityAY_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sUniversityAYGet;
CREATE PROCEDURE sUniversityAYGet(IN PID INT)
  BEGIN
    SELECT
      AYID, UniversityID, StartDate, EndDate
    FROM tUniversityAY
    WHERE UniversityAY_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sUniversityAYGetList;
CREATE PROCEDURE sUniversityAYGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      AYID, UniversityID, StartDate, EndDate

      FROM tUniversityAY;

    ELSE
      SELECT
      AYID, UniversityID, StartDate, EndDate

      FROM tUniversityAY
      WHERE find_in_set(UniversityAY_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sUniversityAYObjectGet;
CREATE PROCEDURE sUniversityAYObjectGet(IN PID INT)
  BEGIN
    SELECT
      AYID, UniversityID, StartDate, EndDate
    FROM tUniversityAY
    # WHERE UniversityAY_ID = PUniversityAY_ID;
  END;



DROP PROCEDURE IF EXISTS sUniversityAYObjectGetList;
CREATE PROCEDURE sUniversityAYObjectGetList(IN PAYID int(11), IN PUniversityID int(11), IN PStartDate date, IN PEndDate date)
  BEGIN


    SELECT
    AYID, UniversityID, StartDate, EndDate

    FROM
      tUniversityAY
    #       WHERE Status = PStatus
    ORDER BY UniversityAY_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sUniversityAYObjectGetListPage;
CREATE PROCEDURE sUniversityAYObjectGetListPage(IN PAYID int(11), IN PUniversityID int(11), IN PStartDate date, IN PEndDate date , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tUniversityAY
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      AYID, UniversityID, StartDate, EndDate

      FROM
        tUniversityAY
      #       WHERE Status = PStatus
      ORDER BY UniversityAY_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


