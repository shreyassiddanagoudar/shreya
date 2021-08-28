DROP PROCEDURE IF EXISTS sCollegeBranchAdd;
CREATE PROCEDURE sCollegeBranchAdd( IN PCollegeBranchID int(11), IN PBranchID int(11), IN PCollegeID int(11), IN PPhoneNUM varchar(255), IN PEmail varchar(255), IN PURL varchar(1024) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tCollegeBranch (CollegeBranchID, BranchID, CollegeID, PhoneNUM, Email, URL)
    VALUES (PCollegeBranchID, PBranchID, PCollegeID, PPhoneNUM, PEmail, PURL);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'CollegeBranch_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sCollegeBranchUpdate;
CREATE PROCEDURE sCollegeBranchUpdate(IN PCollegeBranchID int(11), IN PBranchID int(11), IN PCollegeID int(11), IN PPhoneNUM varchar(255), IN PEmail varchar(255), IN PURL varchar(1024))
  BEGIN
    DECLARE _id INT;
    UPDATE tCollegeBranch
    SET
    CollegeBranchID = PCollegeBranchID, BranchID = PBranchID, CollegeID = PCollegeID, PhoneNUM = PPhoneNUM, Email = PEmail, URL = PURL
    WHERE CollegeBranch_ID = PCollegeBranch_ID;

    SET _id = PCollegeBranch_ID;

    CALL sGetTransactionStatus(1,_id, 'CollegeBranch_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sCollegeBranchDelete;
CREATE PROCEDURE sCollegeBranchDelete(IN PID INT)
  BEGIN
    DELETE FROM tCollegeBranch
    WHERE CollegeBranch_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'CollegeBranch_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sCollegeBranchGet;
CREATE PROCEDURE sCollegeBranchGet(IN PID INT)
  BEGIN
    SELECT
      CollegeBranchID, BranchID, CollegeID, PhoneNUM, Email, URL
    FROM tCollegeBranch
    WHERE CollegeBranch_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sCollegeBranchGetList;
CREATE PROCEDURE sCollegeBranchGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      CollegeBranchID, BranchID, CollegeID, PhoneNUM, Email, URL

      FROM tCollegeBranch;

    ELSE
      SELECT
      CollegeBranchID, BranchID, CollegeID, PhoneNUM, Email, URL

      FROM tCollegeBranch
      WHERE find_in_set(CollegeBranch_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sCollegeBranchObjectGet;
CREATE PROCEDURE sCollegeBranchObjectGet(IN PID INT)
  BEGIN
    SELECT
      CollegeBranchID, BranchID, CollegeID, PhoneNUM, Email, URL
    FROM tCollegeBranch
    # WHERE CollegeBranch_ID = PCollegeBranch_ID;
  END;



DROP PROCEDURE IF EXISTS sCollegeBranchObjectGetList;
CREATE PROCEDURE sCollegeBranchObjectGetList(IN PCollegeBranchID int(11), IN PBranchID int(11), IN PCollegeID int(11), IN PPhoneNUM varchar(255), IN PEmail varchar(255), IN PURL varchar(1024))
  BEGIN


    SELECT
    CollegeBranchID, BranchID, CollegeID, PhoneNUM, Email, URL

    FROM
      tCollegeBranch
    #       WHERE Status = PStatus
    ORDER BY CollegeBranch_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sCollegeBranchObjectGetListPage;
CREATE PROCEDURE sCollegeBranchObjectGetListPage(IN PCollegeBranchID int(11), IN PBranchID int(11), IN PCollegeID int(11), IN PPhoneNUM varchar(255), IN PEmail varchar(255), IN PURL varchar(1024) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tCollegeBranch
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      CollegeBranchID, BranchID, CollegeID, PhoneNUM, Email, URL

      FROM
        tCollegeBranch
      #       WHERE Status = PStatus
      ORDER BY CollegeBranch_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


