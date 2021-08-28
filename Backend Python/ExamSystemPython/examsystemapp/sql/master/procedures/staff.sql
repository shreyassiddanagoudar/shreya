DROP PROCEDURE IF EXISTS sStaffAdd;
CREATE PROCEDURE sStaffAdd( IN PStaffId int(11), IN POwnerId int(50), IN PRole enum('UniversityStaff', IN PName 'CollegeStaff'), IN PStaffNum varchar(255), IN PAddr1 int(50), IN PAddr2 varchar(255), IN PCityId varchar(255), IN PStateId int(11), IN PPin int(11), IN PPhoneNum varchar(255), IN PEmail int(20), IN PProfilePic varchar(255), IN PLoginId varchar(50), IN PPassword int(50) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tStaff (StaffId, OwnerId, Role, Name, StaffNum, Addr1, Addr2, CityId, StateId, Pin, PhoneNum, Email, ProfilePic, LoginId, Password)
    VALUES (PStaffId, POwnerId, PRole, PName, PStaffNum, PAddr1, PAddr2, PCityId, PStateId, PPin, PPhoneNum, PEmail, PProfilePic, PLoginId, PPassword);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'Staff_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sStaffUpdate;
CREATE PROCEDURE sStaffUpdate(IN PStaffId int(11), IN POwnerId int(50), IN PRole enum('UniversityStaff', IN PName 'CollegeStaff'), IN PStaffNum varchar(255), IN PAddr1 int(50), IN PAddr2 varchar(255), IN PCityId varchar(255), IN PStateId int(11), IN PPin int(11), IN PPhoneNum varchar(255), IN PEmail int(20), IN PProfilePic varchar(255), IN PLoginId varchar(50), IN PPassword int(50))
  BEGIN
    DECLARE _id INT;
    UPDATE tStaff
    SET
    StaffId = PStaffId, OwnerId = POwnerId, Role = PRole, Name = PName, StaffNum = PStaffNum, Addr1 = PAddr1, Addr2 = PAddr2, CityId = PCityId, StateId = PStateId, Pin = PPin, PhoneNum = PPhoneNum, Email = PEmail, ProfilePic = PProfilePic, LoginId = PLoginId, Password = PPassword
    WHERE Staff_ID = PStaff_ID;

    SET _id = PStaff_ID;

    CALL sGetTransactionStatus(1,_id, 'Staff_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sStaffDelete;
CREATE PROCEDURE sStaffDelete(IN PID INT)
  BEGIN
    DELETE FROM tStaff
    WHERE Staff_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'Staff_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sStaffGet;
CREATE PROCEDURE sStaffGet(IN PID INT)
  BEGIN
    SELECT
      StaffId, OwnerId, Role, Name, StaffNum, Addr1, Addr2, CityId, StateId, Pin, PhoneNum, Email, ProfilePic, LoginId, Password
    FROM tStaff
    WHERE Staff_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sStaffGetList;
CREATE PROCEDURE sStaffGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      StaffId, OwnerId, Role, Name, StaffNum, Addr1, Addr2, CityId, StateId, Pin, PhoneNum, Email, ProfilePic, LoginId, Password

      FROM tStaff;

    ELSE
      SELECT
      StaffId, OwnerId, Role, Name, StaffNum, Addr1, Addr2, CityId, StateId, Pin, PhoneNum, Email, ProfilePic, LoginId, Password

      FROM tStaff
      WHERE find_in_set(Staff_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sStaffObjectGet;
CREATE PROCEDURE sStaffObjectGet(IN PID INT)
  BEGIN
    SELECT
      StaffId, OwnerId, Role, Name, StaffNum, Addr1, Addr2, CityId, StateId, Pin, PhoneNum, Email, ProfilePic, LoginId, Password
    FROM tStaff
    # WHERE Staff_ID = PStaff_ID;
  END;



DROP PROCEDURE IF EXISTS sStaffObjectGetList;
CREATE PROCEDURE sStaffObjectGetList(IN PStaffId int(11), IN POwnerId int(50), IN PRole enum('UniversityStaff', IN PName 'CollegeStaff'), IN PStaffNum varchar(255), IN PAddr1 int(50), IN PAddr2 varchar(255), IN PCityId varchar(255), IN PStateId int(11), IN PPin int(11), IN PPhoneNum varchar(255), IN PEmail int(20), IN PProfilePic varchar(255), IN PLoginId varchar(50), IN PPassword int(50))
  BEGIN


    SELECT
    StaffId, OwnerId, Role, Name, StaffNum, Addr1, Addr2, CityId, StateId, Pin, PhoneNum, Email, ProfilePic, LoginId, Password

    FROM
      tStaff
    #       WHERE Status = PStatus
    ORDER BY Staff_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sStaffObjectGetListPage;
CREATE PROCEDURE sStaffObjectGetListPage(IN PStaffId int(11), IN POwnerId int(50), IN PRole enum('UniversityStaff', IN PName 'CollegeStaff'), IN PStaffNum varchar(255), IN PAddr1 int(50), IN PAddr2 varchar(255), IN PCityId varchar(255), IN PStateId int(11), IN PPin int(11), IN PPhoneNum varchar(255), IN PEmail int(20), IN PProfilePic varchar(255), IN PLoginId varchar(50), IN PPassword int(50) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tStaff
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      StaffId, OwnerId, Role, Name, StaffNum, Addr1, Addr2, CityId, StateId, Pin, PhoneNum, Email, ProfilePic, LoginId, Password

      FROM
        tStaff
      #       WHERE Status = PStatus
      ORDER BY Staff_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


