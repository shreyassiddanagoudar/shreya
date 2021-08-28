DROP PROCEDURE IF EXISTS sSubjectAdd;
CREATE PROCEDURE sSubjectAdd( IN PSubjectID int(11), IN PName varchar(1024), IN PCode varchar(64) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tSubject (SubjectID, Name, Code)
    VALUES (PSubjectID, PName, PCode);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'Subject_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sSubjectUpdate;
CREATE PROCEDURE sSubjectUpdate(IN PSubjectID int(11), IN PName varchar(1024), IN PCode varchar(64))
  BEGIN
    DECLARE _id INT;
    UPDATE tSubject
    SET
    SubjectID = PSubjectID, Name = PName, Code = PCode
    WHERE Subject_ID = PSubject_ID;

    SET _id = PSubject_ID;

    CALL sGetTransactionStatus(1,_id, 'Subject_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sSubjectDelete;
CREATE PROCEDURE sSubjectDelete(IN PID INT)
  BEGIN
    DELETE FROM tSubject
    WHERE Subject_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'Subject_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sSubjectGet;
CREATE PROCEDURE sSubjectGet(IN PID INT)
  BEGIN
    SELECT
      SubjectID, Name, Code
    FROM tSubject
    WHERE Subject_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sSubjectGetList;
CREATE PROCEDURE sSubjectGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      SubjectID, Name, Code

      FROM tSubject;

    ELSE
      SELECT
      SubjectID, Name, Code

      FROM tSubject
      WHERE find_in_set(Subject_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sSubjectObjectGet;
CREATE PROCEDURE sSubjectObjectGet(IN PID INT)
  BEGIN
    SELECT
      SubjectID, Name, Code
    FROM tSubject
    # WHERE Subject_ID = PSubject_ID;
  END;



DROP PROCEDURE IF EXISTS sSubjectObjectGetList;
CREATE PROCEDURE sSubjectObjectGetList(IN PSubjectID int(11), IN PName varchar(1024), IN PCode varchar(64))
  BEGIN


    SELECT
    SubjectID, Name, Code

    FROM
      tSubject
    #       WHERE Status = PStatus
    ORDER BY Subject_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sSubjectObjectGetListPage;
CREATE PROCEDURE sSubjectObjectGetListPage(IN PSubjectID int(11), IN PName varchar(1024), IN PCode varchar(64) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tSubject
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      SubjectID, Name, Code

      FROM
        tSubject
      #       WHERE Status = PStatus
      ORDER BY Subject_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


