DROP PROCEDURE IF EXISTS sStateAdd;
CREATE PROCEDURE sStateAdd( IN PStateID int(11), IN PName varchar(1024), IN PCode varchar(64) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tState (StateID, Name, Code)
    VALUES (PStateID, PName, PCode);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'State_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sStateUpdate;
CREATE PROCEDURE sStateUpdate(IN PStateID int(11), IN PName varchar(1024), IN PCode varchar(64))
  BEGIN
    DECLARE _id INT;
    UPDATE tState
    SET
    StateID = PStateID, Name = PName, Code = PCode
    WHERE State_ID = PState_ID;

    SET _id = PState_ID;

    CALL sGetTransactionStatus(1,_id, 'State_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sStateDelete;
CREATE PROCEDURE sStateDelete(IN PID INT)
  BEGIN
    DELETE FROM tState
    WHERE State_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'State_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sStateGet;
CREATE PROCEDURE sStateGet(IN PID INT)
  BEGIN
    SELECT
      StateID, Name, Code
    FROM tState
    WHERE State_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sStateGetList;
CREATE PROCEDURE sStateGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      StateID, Name, Code

      FROM tState;

    ELSE
      SELECT
      StateID, Name, Code

      FROM tState
      WHERE find_in_set(State_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sStateObjectGet;
CREATE PROCEDURE sStateObjectGet(IN PID INT)
  BEGIN
    SELECT
      StateID, Name, Code
    FROM tState
    # WHERE State_ID = PState_ID;
  END;



DROP PROCEDURE IF EXISTS sStateObjectGetList;
CREATE PROCEDURE sStateObjectGetList(IN PStateID int(11), IN PName varchar(1024), IN PCode varchar(64))
  BEGIN


    SELECT
    StateID, Name, Code

    FROM
      tState
    #       WHERE Status = PStatus
    ORDER BY State_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sStateObjectGetListPage;
CREATE PROCEDURE sStateObjectGetListPage(IN PStateID int(11), IN PName varchar(1024), IN PCode varchar(64) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tState
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      StateID, Name, Code

      FROM
        tState
      #       WHERE Status = PStatus
      ORDER BY State_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


