DROP PROCEDURE IF EXISTS sBranchAdd;
CREATE PROCEDURE sBranchAdd( IN PBranchID int(11), IN PName varchar(1024), IN PCode varchar(64) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tBranch (BranchID, Name, Code)
    VALUES (PBranchID, PName, PCode);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'Branch_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sBranchUpdate;
CREATE PROCEDURE sBranchUpdate(IN PBranchID int(11), IN PName varchar(1024), IN PCode varchar(64))
  BEGIN
    DECLARE _id INT;
    UPDATE tBranch
    SET
    BranchID = PBranchID, Name = PName, Code = PCode
    WHERE Branch_ID = PBranch_ID;

    SET _id = PBranch_ID;

    CALL sGetTransactionStatus(1,_id, 'Branch_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sBranchDelete;
CREATE PROCEDURE sBranchDelete(IN PID INT)
  BEGIN
    DELETE FROM tBranch
    WHERE Branch_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'Branch_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sBranchGet;
CREATE PROCEDURE sBranchGet(IN PID INT)
  BEGIN
    SELECT
      BranchID, Name, Code
    FROM tBranch
    WHERE Branch_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sBranchGetList;
CREATE PROCEDURE sBranchGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      BranchID, Name, Code

      FROM tBranch;

    ELSE
      SELECT
      BranchID, Name, Code

      FROM tBranch
      WHERE find_in_set(Branch_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sBranchObjectGet;
CREATE PROCEDURE sBranchObjectGet(IN PID INT)
  BEGIN
    SELECT
      BranchID, Name, Code
    FROM tBranch
    # WHERE Branch_ID = PBranch_ID;
  END;



DROP PROCEDURE IF EXISTS sBranchObjectGetList;
CREATE PROCEDURE sBranchObjectGetList(IN PBranchID int(11), IN PName varchar(1024), IN PCode varchar(64))
  BEGIN


    SELECT
    BranchID, Name, Code

    FROM
      tBranch
    #       WHERE Status = PStatus
    ORDER BY Branch_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sBranchObjectGetListPage;
CREATE PROCEDURE sBranchObjectGetListPage(IN PBranchID int(11), IN PName varchar(1024), IN PCode varchar(64) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tBranch
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      BranchID, Name, Code

      FROM
        tBranch
      #       WHERE Status = PStatus
      ORDER BY Branch_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


