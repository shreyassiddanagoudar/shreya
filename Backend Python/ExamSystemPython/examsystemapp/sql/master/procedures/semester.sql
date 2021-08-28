DROP PROCEDURE IF EXISTS sSemesterAdd;
CREATE PROCEDURE sSemesterAdd( IN PSemesterID int(11), IN PName varchar(1024), IN PCode varchar(64) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tSemester (SemesterID, Name, Code)
    VALUES (PSemesterID, PName, PCode);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'Semester_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sSemesterUpdate;
CREATE PROCEDURE sSemesterUpdate(IN PSemesterID int(11), IN PName varchar(1024), IN PCode varchar(64))
  BEGIN
    DECLARE _id INT;
    UPDATE tSemester
    SET
    SemesterID = PSemesterID, Name = PName, Code = PCode
    WHERE Semester_ID = PSemester_ID;

    SET _id = PSemester_ID;

    CALL sGetTransactionStatus(1,_id, 'Semester_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sSemesterDelete;
CREATE PROCEDURE sSemesterDelete(IN PID INT)
  BEGIN
    DELETE FROM tSemester
    WHERE Semester_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'Semester_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sSemesterGet;
CREATE PROCEDURE sSemesterGet(IN PID INT)
  BEGIN
    SELECT
      SemesterID, Name, Code
    FROM tSemester
    WHERE Semester_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sSemesterGetList;
CREATE PROCEDURE sSemesterGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      SemesterID, Name, Code

      FROM tSemester;

    ELSE
      SELECT
      SemesterID, Name, Code

      FROM tSemester
      WHERE find_in_set(Semester_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sSemesterObjectGet;
CREATE PROCEDURE sSemesterObjectGet(IN PID INT)
  BEGIN
    SELECT
      SemesterID, Name, Code
    FROM tSemester
    # WHERE Semester_ID = PSemester_ID;
  END;



DROP PROCEDURE IF EXISTS sSemesterObjectGetList;
CREATE PROCEDURE sSemesterObjectGetList(IN PSemesterID int(11), IN PName varchar(1024), IN PCode varchar(64))
  BEGIN


    SELECT
    SemesterID, Name, Code

    FROM
      tSemester
    #       WHERE Status = PStatus
    ORDER BY Semester_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sSemesterObjectGetListPage;
CREATE PROCEDURE sSemesterObjectGetListPage(IN PSemesterID int(11), IN PName varchar(1024), IN PCode varchar(64) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tSemester
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      SemesterID, Name, Code

      FROM
        tSemester
      #       WHERE Status = PStatus
      ORDER BY Semester_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


