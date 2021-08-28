DROP PROCEDURE IF EXISTS sBSSubjectDtlAdd;
CREATE PROCEDURE sBSSubjectDtlAdd( IN PBSSubjectDtlID int(11), IN PBSSID int(11), IN PName varchar(1024), IN PSubjectID int(11) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tBSSubjectDtl (BSSubjectDtlID, BSSID, Name, SubjectID)
    VALUES (PBSSubjectDtlID, PBSSID, PName, PSubjectID);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'BSSubjectDtl_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sBSSubjectDtlUpdate;
CREATE PROCEDURE sBSSubjectDtlUpdate(IN PBSSubjectDtlID int(11), IN PBSSID int(11), IN PName varchar(1024), IN PSubjectID int(11))
  BEGIN
    DECLARE _id INT;
    UPDATE tBSSubjectDtl
    SET
    BSSubjectDtlID = PBSSubjectDtlID, BSSID = PBSSID, Name = PName, SubjectID = PSubjectID
    WHERE BSSubjectDtl_ID = PBSSubjectDtl_ID;

    SET _id = PBSSubjectDtl_ID;

    CALL sGetTransactionStatus(1,_id, 'BSSubjectDtl_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sBSSubjectDtlDelete;
CREATE PROCEDURE sBSSubjectDtlDelete(IN PID INT)
  BEGIN
    DELETE FROM tBSSubjectDtl
    WHERE BSSubjectDtl_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'BSSubjectDtl_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sBSSubjectDtlGet;
CREATE PROCEDURE sBSSubjectDtlGet(IN PID INT)
  BEGIN
    SELECT
      BSSubjectDtlID, BSSID, Name, SubjectID
    FROM tBSSubjectDtl
    WHERE BSSubjectDtl_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sBSSubjectDtlGetList;
CREATE PROCEDURE sBSSubjectDtlGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      BSSubjectDtlID, BSSID, Name, SubjectID

      FROM tBSSubjectDtl;

    ELSE
      SELECT
      BSSubjectDtlID, BSSID, Name, SubjectID

      FROM tBSSubjectDtl
      WHERE find_in_set(BSSubjectDtl_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sBSSubjectDtlObjectGet;
CREATE PROCEDURE sBSSubjectDtlObjectGet(IN PID INT)
  BEGIN
    SELECT
      BSSubjectDtlID, BSSID, Name, SubjectID
    FROM tBSSubjectDtl
    # WHERE BSSubjectDtl_ID = PBSSubjectDtl_ID;
  END;



DROP PROCEDURE IF EXISTS sBSSubjectDtlObjectGetList;
CREATE PROCEDURE sBSSubjectDtlObjectGetList(IN PBSSubjectDtlID int(11), IN PBSSID int(11), IN PName varchar(1024), IN PSubjectID int(11))
  BEGIN


    SELECT
    BSSubjectDtlID, BSSID, Name, SubjectID

    FROM
      tBSSubjectDtl
    #       WHERE Status = PStatus
    ORDER BY BSSubjectDtl_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sBSSubjectDtlObjectGetListPage;
CREATE PROCEDURE sBSSubjectDtlObjectGetListPage(IN PBSSubjectDtlID int(11), IN PBSSID int(11), IN PName varchar(1024), IN PSubjectID int(11) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tBSSubjectDtl
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      BSSubjectDtlID, BSSID, Name, SubjectID

      FROM
        tBSSubjectDtl
      #       WHERE Status = PStatus
      ORDER BY BSSubjectDtl_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


