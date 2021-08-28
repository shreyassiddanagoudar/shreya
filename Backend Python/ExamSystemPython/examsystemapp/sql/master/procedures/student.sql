DROP PROCEDURE IF EXISTS sStudentAdd;
CREATE PROCEDURE sStudentAdd( IN PStudentID int(11), IN PCollegeID varchar(1024), IN PBranchID varchar(64), IN PCurrentSemester varchar(255), IN PName varchar(255), IN PRollNo int(11), IN PAdd1 varchar(1024), IN PAdd2 varchar(1024), IN PAdd3 varchar(1024), IN PCityID int(11), IN PStateID int(11), IN PPin int(11), IN PPhonenum int(11), IN PEmail varchar(1024), IN PProfilePic varchar(1024), IN PLoginID varchar(1024), IN PPasswd varchar(1024) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tStudent (StudentID, CollegeID, BranchID, CurrentSemester, Name, RollNo, Add1, Add2, Add3, CityID, StateID, Pin, Phonenum, Email, ProfilePic, LoginID, Passwd)
    VALUES (PStudentID, PCollegeID, PBranchID, PCurrentSemester, PName, PRollNo, PAdd1, PAdd2, PAdd3, PCityID, PStateID, PPin, PPhonenum, PEmail, PProfilePic, PLoginID, PPasswd);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'Student_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sStudentUpdate;
CREATE PROCEDURE sStudentUpdate(IN PStudentID int(11), IN PCollegeID varchar(1024), IN PBranchID varchar(64), IN PCurrentSemester varchar(255), IN PName varchar(255), IN PRollNo int(11), IN PAdd1 varchar(1024), IN PAdd2 varchar(1024), IN PAdd3 varchar(1024), IN PCityID int(11), IN PStateID int(11), IN PPin int(11), IN PPhonenum int(11), IN PEmail varchar(1024), IN PProfilePic varchar(1024), IN PLoginID varchar(1024), IN PPasswd varchar(1024))
  BEGIN
    DECLARE _id INT;
    UPDATE tStudent
    SET
    StudentID = PStudentID, CollegeID = PCollegeID, BranchID = PBranchID, CurrentSemester = PCurrentSemester, Name = PName, RollNo = PRollNo, Add1 = PAdd1, Add2 = PAdd2, Add3 = PAdd3, CityID = PCityID, StateID = PStateID, Pin = PPin, Phonenum = PPhonenum, Email = PEmail, ProfilePic = PProfilePic, LoginID = PLoginID, Passwd = PPasswd
    WHERE Student_ID = PStudent_ID;

    SET _id = PStudent_ID;

    CALL sGetTransactionStatus(1,_id, 'Student_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sStudentDelete;
CREATE PROCEDURE sStudentDelete(IN PID INT)
  BEGIN
    DELETE FROM tStudent
    WHERE Student_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'Student_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sStudentGet;
CREATE PROCEDURE sStudentGet(IN PID INT)
  BEGIN
    SELECT
      StudentID, CollegeID, BranchID, CurrentSemester, Name, RollNo, Add1, Add2, Add3, CityID, StateID, Pin, Phonenum, Email, ProfilePic, LoginID, Passwd
    FROM tStudent
    WHERE Student_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sStudentGetList;
CREATE PROCEDURE sStudentGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      StudentID, CollegeID, BranchID, CurrentSemester, Name, RollNo, Add1, Add2, Add3, CityID, StateID, Pin, Phonenum, Email, ProfilePic, LoginID, Passwd

      FROM tStudent;

    ELSE
      SELECT
      StudentID, CollegeID, BranchID, CurrentSemester, Name, RollNo, Add1, Add2, Add3, CityID, StateID, Pin, Phonenum, Email, ProfilePic, LoginID, Passwd

      FROM tStudent
      WHERE find_in_set(Student_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sStudentObjectGet;
CREATE PROCEDURE sStudentObjectGet(IN PID INT)
  BEGIN
    SELECT
      StudentID, CollegeID, BranchID, CurrentSemester, Name, RollNo, Add1, Add2, Add3, CityID, StateID, Pin, Phonenum, Email, ProfilePic, LoginID, Passwd
    FROM tStudent
    # WHERE Student_ID = PStudent_ID;
  END;



DROP PROCEDURE IF EXISTS sStudentObjectGetList;
CREATE PROCEDURE sStudentObjectGetList(IN PStudentID int(11), IN PCollegeID varchar(1024), IN PBranchID varchar(64), IN PCurrentSemester varchar(255), IN PName varchar(255), IN PRollNo int(11), IN PAdd1 varchar(1024), IN PAdd2 varchar(1024), IN PAdd3 varchar(1024), IN PCityID int(11), IN PStateID int(11), IN PPin int(11), IN PPhonenum int(11), IN PEmail varchar(1024), IN PProfilePic varchar(1024), IN PLoginID varchar(1024), IN PPasswd varchar(1024))
  BEGIN


    SELECT
    StudentID, CollegeID, BranchID, CurrentSemester, Name, RollNo, Add1, Add2, Add3, CityID, StateID, Pin, Phonenum, Email, ProfilePic, LoginID, Passwd

    FROM
      tStudent
    #       WHERE Status = PStatus
    ORDER BY Student_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sStudentObjectGetListPage;
CREATE PROCEDURE sStudentObjectGetListPage(IN PStudentID int(11), IN PCollegeID varchar(1024), IN PBranchID varchar(64), IN PCurrentSemester varchar(255), IN PName varchar(255), IN PRollNo int(11), IN PAdd1 varchar(1024), IN PAdd2 varchar(1024), IN PAdd3 varchar(1024), IN PCityID int(11), IN PStateID int(11), IN PPin int(11), IN PPhonenum int(11), IN PEmail varchar(1024), IN PProfilePic varchar(1024), IN PLoginID varchar(1024), IN PPasswd varchar(1024) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tStudent
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      StudentID, CollegeID, BranchID, CurrentSemester, Name, RollNo, Add1, Add2, Add3, CityID, StateID, Pin, Phonenum, Email, ProfilePic, LoginID, Passwd

      FROM
        tStudent
      #       WHERE Status = PStatus
      ORDER BY Student_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


