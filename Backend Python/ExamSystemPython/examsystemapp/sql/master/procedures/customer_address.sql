DROP PROCEDURE IF EXISTS sCustomerAddressAdd;
CREATE PROCEDURE sCustomerAddressAdd( IN PCustomerAddressID int(11), IN PCustomerID int(11), IN PAdd1 varchar(1024), IN PAdd2 varchar(1024), IN PAdd3 varchar(1024), IN PCityID int(11), IN PStateID int(11), IN PPinCode int(11) )
  BEGIN

    DECLARE _id INT;

    INSERT INTO tCustomerAddress (CustomerAddressID, CustomerID, Add1, Add2, Add3, CityID, StateID, PinCode)
    VALUES (PCustomerAddressID, PCustomerID, PAdd1, PAdd2, PAdd3, PCityID, PStateID, PPinCode);
    SET _id = (SELECT last_insert_id());

    CALL sGetTransactionStatus(1, _id, 'CustomerAddress_ID', NULL, NULL);
  END;

DROP PROCEDURE IF EXISTS sCustomerAddressUpdate;
CREATE PROCEDURE sCustomerAddressUpdate(IN PCustomerAddressID int(11), IN PCustomerID int(11), IN PAdd1 varchar(1024), IN PAdd2 varchar(1024), IN PAdd3 varchar(1024), IN PCityID int(11), IN PStateID int(11), IN PPinCode int(11))
  BEGIN
    DECLARE _id INT;
    UPDATE tCustomerAddress
    SET
    CustomerAddressID = PCustomerAddressID, CustomerID = PCustomerID, Add1 = PAdd1, Add2 = PAdd2, Add3 = PAdd3, CityID = PCityID, StateID = PStateID, PinCode = PPinCode
    WHERE CustomerAddress_ID = PCustomerAddress_ID;

    SET _id = PCustomerAddress_ID;

    CALL sGetTransactionStatus(1,_id, 'CustomerAddress_ID', NULL, NULL);


  END;



DROP PROCEDURE IF EXISTS sCustomerAddressDelete;
CREATE PROCEDURE sCustomerAddressDelete(IN PID INT)
  BEGIN
    DELETE FROM tCustomerAddress
    WHERE CustomerAddress_ID = PID;
    CALL sGetTransactionStatus(1, PID, 'CustomerAddress_ID', NULL, NULL);

  END;


DROP PROCEDURE IF EXISTS sCustomerAddressGet;
CREATE PROCEDURE sCustomerAddressGet(IN PID INT)
  BEGIN
    SELECT
      CustomerAddressID, CustomerID, Add1, Add2, Add3, CityID, StateID, PinCode
    FROM tCustomerAddress
    WHERE CustomerAddress_ID = PID;
  END;

DROP PROCEDURE IF EXISTS sCustomerAddressGetList;
CREATE PROCEDURE sCustomerAddressGetList(IN PIDs TEXT)
  BEGIN
    IF PIDs = '' OR PIDs IS NULL
    THEN
      SELECT
      CustomerAddressID, CustomerID, Add1, Add2, Add3, CityID, StateID, PinCode

      FROM tCustomerAddress;

    ELSE
      SELECT
      CustomerAddressID, CustomerID, Add1, Add2, Add3, CityID, StateID, PinCode

      FROM tCustomerAddress
      WHERE find_in_set(CustomerAddress_ID, PIDs);
    END IF;

  END;

DROP PROCEDURE IF EXISTS sCustomerAddressObjectGet;
CREATE PROCEDURE sCustomerAddressObjectGet(IN PID INT)
  BEGIN
    SELECT
      CustomerAddressID, CustomerID, Add1, Add2, Add3, CityID, StateID, PinCode
    FROM tCustomerAddress
    # WHERE CustomerAddress_ID = PCustomerAddress_ID;
  END;



DROP PROCEDURE IF EXISTS sCustomerAddressObjectGetList;
CREATE PROCEDURE sCustomerAddressObjectGetList(IN PCustomerAddressID int(11), IN PCustomerID int(11), IN PAdd1 varchar(1024), IN PAdd2 varchar(1024), IN PAdd3 varchar(1024), IN PCityID int(11), IN PStateID int(11), IN PPinCode int(11))
  BEGIN


    SELECT
    CustomerAddressID, CustomerID, Add1, Add2, Add3, CityID, StateID, PinCode

    FROM
      tCustomerAddress
    #       WHERE Status = PStatus
    ORDER BY CustomerAddress_ID DESC;

  END;


DROP PROCEDURE IF EXISTS sCustomerAddressObjectGetListPage;
CREATE PROCEDURE sCustomerAddressObjectGetListPage(IN PCustomerAddressID int(11), IN PCustomerID int(11), IN PAdd1 varchar(1024), IN PAdd2 varchar(1024), IN PAdd3 varchar(1024), IN PCityID int(11), IN PStateID int(11), IN PPinCode int(11) , IN PPage_Num  INT, IN PPage_Size INT)
  BEGIN

    DECLARE _offset INT DEFAULT 0;
    DECLARE _total_rec INT DEFAULT 0;
    DECLARE _total_pages INT DEFAULT 1;
    SET _offset = fGetOffset(PPage_Num, PPage_Size);
    SET _total_rec = (SELECT count(*)
                      FROM tCustomerAddress
      #       WHERE Status = PStatus

    );
    SET _total_pages = fGetTotalPages(_total_rec, PPage_Size);
    IF _total_rec > 0
    THEN

      SELECT
        _total_rec   AS total_records,
        _total_pages AS total_pages;

      SELECT
      CustomerAddressID, CustomerID, Add1, Add2, Add3, CityID, StateID, PinCode

      FROM
        tCustomerAddress
      #       WHERE Status = PStatus
      ORDER BY CustomerAddress_ID DESC
      LIMIT _offset, PPage_Size;

    END IF;
  END;


