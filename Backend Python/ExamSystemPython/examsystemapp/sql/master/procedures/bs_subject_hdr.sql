DROP PROCEDURE IF EXISTS sBSSubjectHdrAdd;
CREATE PROCEDURE sBSSubjectHdrAdd( IN PBranchSubjectID int(11), IN PBranchID int(11), IN PSemesterID int(11) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tBSSubjectHdr (BranchSubjectID, BranchID, SemesterID)
    VALUES (PBranchSubjectID, PBranchID, PSemesterID);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'BSSubjectHdr_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sBSSubjectHdrUpdate;
CREATE PROCEDURE sBSSubjectHdrUpdate(IN PBranchSubjectID int(11), IN PBranchID int(11), IN PSemesterID int(11))
  BEGIN
    DECLARE _id INT;
    UPDATE tBSSubjectHdr
    SET
    BranchSubjectID = PBranchSubjectID, BranchID = PBranchID, SemesterID = PSemesterID
    WHERE BSSubjectHdr_ID = PBSSubjectHdr_ID;

    SET _id = PBSSubjectHdr_ID;

    CALL sGetTransactionStatus(1,_id, 'BSSubjectHdr_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sBSSubjectHdrDelete;
CREATE PROCEDURE sBSSubjectHdrDelete(IN PID INT)
  BEGIN
    DELETE FROM tBSSubjectHdr
    WHERE BSSubjectHdr_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'BSSubjectHdr_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sBSSubjectHdrGet;
CREATE PROCEDURE sBSSubjectHdrGet(IN PID INT)
  BEGIN
    SELECT
      BranchSubjectID, BranchID, SemesterID
    FROM tBSSubjectHdr
    WHERE BSSubjectHdr_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sBSSubjectHdrGetList;
CREATE PROCEDURE sBSSubjectHdrGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      BranchSubjectID, BranchID, SemesterID

      FROM tBSSubjectHdr;

    ELSE
      SELECT
      BranchSubjectID, BranchID, SemesterID

      FROM tBSSubjectHdr
      WHERE find_in_set(BSSubjectHdr_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sBSSubjectHdrObjectGet;
CREATE PROCEDURE sBSSubjectHdrObjectGet(IN PID INT)
  BEGIN
    SELECT
      BranchSubjectID, BranchID, SemesterID
    FROM tBSSubjectHdr
    # WHERE BSSubjectHdr_ID = PBSSubjectHdr_ID;
  END;



DROP PROCEDURE IF EXISTS sBSSubjectHdrObjectGetList;
CREATE PROCEDURE sBSSubjectHdrObjectGetList(IN PBranchSubjectID int(11), IN PBranchID int(11), IN PSemesterID int(11))
  BEGIN


    SELECT
    BranchSubjectID, BranchID, SemesterID

    FROM
      tBSSubjectHdr
    #       WHERE Status = PStatus
    ORDER BY BSSubjectHdr_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sBSSubjectHdrObjectGetListPage;
CREATE PROCEDURE sBSSubjectHdrObjectGetListPage(IN PBranchSubjectID int(11), IN PBranchID int(11), IN PSemesterID int(11) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tBSSubjectHdr
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      BranchSubjectID, BranchID, SemesterID

      FROM
        tBSSubjectHdr
      #       WHERE Status = PStatus
      ORDER BY BSSubjectHdr_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


