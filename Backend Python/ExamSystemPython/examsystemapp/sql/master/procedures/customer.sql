DROP PROCEDURE IF EXISTS sCustomerAdd;
CREATE PROCEDURE sCustomerAdd( IN PCustomerID int(11), IN PEmail varchar(1024), IN PPhone bigint(20), IN PName varchar(1024), IN PPassword varchar(1024) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tCustomer (CustomerID, Email, Phone, Name, Password)
    VALUES (PCustomerID, PEmail, PPhone, PName, PPassword);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'Customer_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sCustomerUpdate;
CREATE PROCEDURE sCustomerUpdate(IN PCustomerID int(11), IN PEmail varchar(1024), IN PPhone bigint(20), IN PName varchar(1024), IN PPassword varchar(1024))
  BEGIN
    DECLARE _id INT;
    UPDATE tCustomer
    SET
    CustomerID = PCustomerID, Email = PEmail, Phone = PPhone, Name = PName, Password = PPassword
    WHERE Customer_ID = PCustomer_ID;

    SET _id = PCustomer_ID;

    CALL sGetTransactionStatus(1,_id, 'Customer_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sCustomerDelete;
CREATE PROCEDURE sCustomerDelete(IN PID INT)
  BEGIN
    DELETE FROM tCustomer
    WHERE Customer_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'Customer_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sCustomerGet;
CREATE PROCEDURE sCustomerGet(IN PID INT)
  BEGIN
    SELECT
      CustomerID, Email, Phone, Name, Password
    FROM tCustomer
    WHERE Customer_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sCustomerGetList;
CREATE PROCEDURE sCustomerGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      CustomerID, Email, Phone, Name, Password

      FROM tCustomer;

    ELSE
      SELECT
      CustomerID, Email, Phone, Name, Password

      FROM tCustomer
      WHERE find_in_set(Customer_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sCustomerObjectGet;
CREATE PROCEDURE sCustomerObjectGet(IN PID INT)
  BEGIN
    SELECT
      CustomerID, Email, Phone, Name, Password
    FROM tCustomer
    # WHERE Customer_ID = PCustomer_ID;
  END;



DROP PROCEDURE IF EXISTS sCustomerObjectGetList;
CREATE PROCEDURE sCustomerObjectGetList(IN PCustomerID int(11), IN PEmail varchar(1024), IN PPhone bigint(20), IN PName varchar(1024), IN PPassword varchar(1024))
  BEGIN


    SELECT
    CustomerID, Email, Phone, Name, Password

    FROM
      tCustomer
    #       WHERE Status = PStatus
    ORDER BY Customer_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sCustomerObjectGetListPage;
CREATE PROCEDURE sCustomerObjectGetListPage(IN PCustomerID int(11), IN PEmail varchar(1024), IN PPhone bigint(20), IN PName varchar(1024), IN PPassword varchar(1024) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tCustomer
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      CustomerID, Email, Phone, Name, Password

      FROM
        tCustomer
      #       WHERE Status = PStatus
      ORDER BY Customer_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


