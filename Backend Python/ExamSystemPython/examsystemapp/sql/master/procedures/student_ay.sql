DROP PROCEDURE IF EXISTS sStudentAYAdd;
CREATE PROCEDURE sStudentAYAdd( IN PStudentAYID int(11), IN PStudentID int(11), IN PAYID int(11), IN PSemesterID int(11), IN PStartDATE date, IN PEndDATE date )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tStudentAY (StudentAYID, StudentID, AYID, SemesterID, StartDATE, EndDATE)
    VALUES (PStudentAYID, PStudentID, PAYID, PSemesterID, PStartDATE, PEndDATE);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'StudentAY_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sStudentAYUpdate;
CREATE PROCEDURE sStudentAYUpdate(IN PStudentAYID int(11), IN PStudentID int(11), IN PAYID int(11), IN PSemesterID int(11), IN PStartDATE date, IN PEndDATE date)
  BEGIN
    DECLARE _id INT;
    UPDATE tStudentAY
    SET
    StudentAYID = PStudentAYID, StudentID = PStudentID, AYID = PAYID, SemesterID = PSemesterID, StartDATE = PStartDATE, EndDATE = PEndDATE
    WHERE StudentAY_ID = PStudentAY_ID;

    SET _id = PStudentAY_ID;

    CALL sGetTransactionStatus(1,_id, 'StudentAY_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sStudentAYDelete;
CREATE PROCEDURE sStudentAYDelete(IN PID INT)
  BEGIN
    DELETE FROM tStudentAY
    WHERE StudentAY_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'StudentAY_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sStudentAYGet;
CREATE PROCEDURE sStudentAYGet(IN PID INT)
  BEGIN
    SELECT
      StudentAYID, StudentID, AYID, SemesterID, StartDATE, EndDATE
    FROM tStudentAY
    WHERE StudentAY_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sStudentAYGetList;
CREATE PROCEDURE sStudentAYGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      StudentAYID, StudentID, AYID, SemesterID, StartDATE, EndDATE

      FROM tStudentAY;

    ELSE
      SELECT
      StudentAYID, StudentID, AYID, SemesterID, StartDATE, EndDATE

      FROM tStudentAY
      WHERE find_in_set(StudentAY_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sStudentAYObjectGet;
CREATE PROCEDURE sStudentAYObjectGet(IN PID INT)
  BEGIN
    SELECT
      StudentAYID, StudentID, AYID, SemesterID, StartDATE, EndDATE
    FROM tStudentAY
    # WHERE StudentAY_ID = PStudentAY_ID;
  END;



DROP PROCEDURE IF EXISTS sStudentAYObjectGetList;
CREATE PROCEDURE sStudentAYObjectGetList(IN PStudentAYID int(11), IN PStudentID int(11), IN PAYID int(11), IN PSemesterID int(11), IN PStartDATE date, IN PEndDATE date)
  BEGIN


    SELECT
    StudentAYID, StudentID, AYID, SemesterID, StartDATE, EndDATE

    FROM
      tStudentAY
    #       WHERE Status = PStatus
    ORDER BY StudentAY_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sStudentAYObjectGetListPage;
CREATE PROCEDURE sStudentAYObjectGetListPage(IN PStudentAYID int(11), IN PStudentID int(11), IN PAYID int(11), IN PSemesterID int(11), IN PStartDATE date, IN PEndDATE date , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tStudentAY
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      StudentAYID, StudentID, AYID, SemesterID, StartDATE, EndDATE

      FROM
        tStudentAY
      #       WHERE Status = PStatus
      ORDER BY StudentAY_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


