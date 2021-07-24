/* Cart */
DROP TABLE IF EXISTS tCart;
CREATE TABLE tCart
(
  CartID        INT             AUTO_INCREMENT PRIMARY KEY,
  SessionID     VARCHAR(1024)   NOT NULL UNIQUE,
  CustomerID    INT             NOT NULL UNIQUE
);
--Add
DROP PROCEDURE IF EXISTS sCartAdd;
CREATE PROCEDURE sCartAdd
  (
    IN pSessionID  VARCHAR(1024),
    IN pCustpmerID INT
  )
  BEGIN
    DECLARE _id INT DEFAULT NULL;
    INSERT INTO tCart (
      SessionID,
      CustomerID
    ) VALUES
      (
        pSessionID,
        pCustomerID
      );
SET _id = (SELECT last_insert_id());
    SELECT
      1    AS IS_SUCCESS,
      _id  AS TRANSACTION_ID,
      ''   AS PRIMARY_COLUMN,
      NULL AS DB_RESPONSE_CODE,
      NULL AS DB_RESPONSE_MESSAGE
    FROM dual;
  END;

-- Update
DROP PROCEDURE IF EXISTS sCartUpdate;
CREATE PROCEDURE sCartUpdate
  (
    IN pCartID        INT,
    IN pSessionID     VARCHAR(1024),
    IN pCustomerID    INT
  )
  BEGIN
    UPDATE tCart
    SET
    SessionID  = pSessionID,
    CustomerID = pCustomerID
    WHERE CartID   = pCartID;

    SELECT
      1         AS IS_SUCCESS,
      pCartID   AS TRANSACTION_ID,
      ''        AS PRIMARY_COLUMN,
      NULL      AS DB_RESPONSE_CODE,
      NULL      AS DB_RESPONSE_MESSAGE
    FROM dual;
  END;

-- Delete
DROP PROCEDURE IF EXISTS sCartDelete;
CREATE PROCEDURE sCartDelete
  (
    IN pCartID INT
  )
  BEGIN
    DELETE FROM tCart
    WHERE CartID = pCartID;

    SELECT
      1         AS IS_SUCCESS,
      pCartID   AS TRANSACTION_ID,
      ''        AS PRIMARY_COLUMN,
      NULL      AS DB_RESPONSE_CODE,
      NULL      AS DB_RESPONSE_MESSAGE
    FROM dual;
  END;

  --  Get By Cart

DROP PROCEDURE IF EXISTS sCartGet;
CREATE PROCEDURE sCartGet
  (
    IN pCartIID INT
  )
  BEGIN
    SELECT
    CartItemID,
    CartID,
    Date,
    ProductID,
    Qty, 
    Price
    FROM tCartItem
    WHERE CartItemID = pCartItemID;
  END;

---------------------------------------------------------------------------

/* Cart Item */
DROP TABLE IF EXISTS tCartItem;
CREATE TABLE tCartItem
(
  CartItemID   INT      AUTO_INCREMENT PRIMARY KEY,
  CartID       INT      NOT NULL,
  Date         Date     NOT NULL,
  ProductID    INT      NOT NULL, UNIQUE,
  Qty          INT      NOT NULL, 
  Price        FLOAT    NOT NULL 
);

--Add
DROP PROCEDURE IF EXISTS sCartItemAdd;
CREATE PROCEDURE sCartItemAdd
  (
    IN pCartID      INT,
    IN pDate        DATE,
    IN pProductID   INT,
    IN pQty         INT,
    IN pPrice       FLOAT
  )
  BEGIN
    DECLARE _id INT DEFAULT NULL;
    INSERT INTO tCartItem (
    CartID,
    Date,
    ProductID,
    Qty, 
    Price
    ) VALUES
      (
    pCartID,
    pDate,
    pProductID,
    pQty,
    pPrice 
      );
SET _id = (SELECT last_insert_id());
    SELECT
      1    AS IS_SUCCESS,
      _id  AS TRANSACTION_ID,
      ''   AS PRIMARY_COLUMN,
      NULL AS DB_RESPONSE_CODE,
      NULL AS DB_RESPONSE_MESSAGE
  END;

-- Update
DROP PROCEDURE IF EXISTS sCartItemUpdate;
CREATE PROCEDURE sCartItemUpdate
  (
    IN pCartItemID  INT,
    IN pCartID      INT,
    IN pDate        DATE,
    IN pProductID   INT,
    IN pQty         INT,
    IN pPrice       FLOAT
  )
  BEGIN
    UPDATE tCartItem
    SET
    CartID    =   pCartID,
    Date      =   pDate,
    ProductID =   pProductID,
    Qty       =   pQty, 
    Price     =   pPrice
    WHERE CartItemID = pCartItemID;

    SELECT
      1             AS IS_SUCCESS,
      pCartItemID   AS TRANSACTION_ID,
      ''            AS PRIMARY_COLUMN,
      NULL          AS DB_RESPONSE_CODE,
      NULL          AS DB_RESPONSE_MESSAGE
    FROM dual;
  END;

-- Delete
DROP PROCEDURE IF EXISTS sCartItemDelete;
CREATE PROCEDURE sCartItemDelete
  (
    IN pCartItemID INT
  )
  BEGIN
    DELETE FROM tCartItem
    WHERE CartItemID = pCartItemID;

    SELECT
      1             AS IS_SUCCESS,
      pCartItemID   AS TRANSACTION_ID,
      ''            AS PRIMARY_COLUMN,
      NULL          AS DB_RESPONSE_CODE,
      NULL          AS DB_RESPONSE_MESSAGE
    FROM dual;
  END;

--  Get By CartItem

DROP PROCEDURE IF EXISTS sCartItemGet;
CREATE PROCEDURE sCartItemGet
  (
    IN pCartItemID INT
  )
  BEGIN
    SELECT
    CartItemID,
    CartID,
    Date,
    ProductID,
    Qty, 
    Price
    FROM tCartItem
    WHERE CartItemID = pCartItemID;
  END;
--------------------------------------------------------------------------

/* Order */
DROP TABLE IF EXISTS tOrder;
CREATE TABLE tOrder
(
  OrderID           INT             AUTO_INCREMENT PRIMARY KEY,
  CustomerID        INT             NOT NULL,UNIQUE,
  OrderItemID       INT             NOT NULL UNIQUE,
  Status            INT             NOT NULL,
  AddressID         FLOAT           NOT NULL, 
  PaymentType       VARCHAR(1024)   NOT NULL, 
  PaymentStatus     VARCHAR(1024)   NOT NULL, 
  TotalPrice        INT             NOT NULL 

);

--Add
DROP PROCEDURE IF EXISTS sOrderAdd;
CREATE PROCEDURE sOrderAdd
  (
    IN pCustomerID       INT,
    IN pOrderItemID      INT,
    IN pStatus           INT,
    IN pAdressID         FLOAT,
    IN pPaymentType      VARCHAR(1024),
    IN pPaymentStatus    VARCHAR(1024),
    IN pTotalPrice       INT
  )
  BEGIN
    DECLARE _id INT DEFAULT NULL;
    INSERT INTO tOrder (
    CustomerID,
    OrderItemID,
    Status,
    AdressID,
    PaymentType, 
    PaymentStatus, 
    TotalPrice 
    ) VALUES
      (
    pCustomerID,
    pOrderItemID,
    pStatus,
    pAdressID,
    pPaymentType, 
    pPaymentStatus, 
    pTotalPrice 
      );
SET _id = (SELECT last_insert_id());
    SELECT
      1    AS IS_SUCCESS,
      _id  AS TRANSACTION_ID,
      ''   AS PRIMARY_COLUMN,
      NULL AS DB_RESPONSE_CODE,
      NULL AS DB_RESPONSE_MESSAGE
  END;

-- Update
DROP PROCEDURE IF EXISTS sOrderUpdate;
CREATE PROCEDURE sOrderUpdate
  (
    In pOrderID         INT,
    IN pCustomerID      INT,
    IN pOrderItemID     INT,
    IN pStatus          INT,
    IN pAdressID        FLOAT,
    IN pPaymentType     VARCHAR(1024),
    IN pPaymentStatus   VARCHAR(1024),
    IN pTotalPrice      INT
  )
  BEGIN
    UPDATE tOrder
    SET
    CustomerID      =   pCustomerID,
    OrderItemID     =   pOrderItemID,
    Status          =   pStatus,
    AdressID        =   pAdressID,
    PaymentType     =   pPaymentType, 
    PaymentStatus   =   pPaymentStatus, 
    TotalPrice      =   pTotalPrice 
    WHERE OrderID = pOrderID;

    SELECT
      1           AS IS_SUCCESS,
      pOrderID    AS TRANSACTION_ID,
      ''          AS PRIMARY_COLUMN,
      NULL        AS DB_RESPONSE_CODE,
      NULL        AS DB_RESPONSE_MESSAGE
    FROM dual;
  END;

-- Delete
DROP PROCEDURE IF EXISTS sOrderDelete;
CREATE PROCEDURE sOrderDelete
  (
    IN pOrderID INT
  )
  BEGIN
    DELETE FROM tOrder
    WHERE OrderID = pOrderID;

    SELECT
      1           AS IS_SUCCESS,
      pOrderID    AS TRANSACTION_ID,
      ''          AS PRIMARY_COLUMN,
      NULL        AS DB_RESPONSE_CODE,
      NULL        AS DB_RESPONSE_MESSAGE
    FROM dual;
  END;

  --  Get By Order

DROP PROCEDURE IF EXISTS sOrderGet;
CREATE PROCEDURE sOrderGet
  (
    IN pOrderID INT
  )
  BEGIN
    SELECT
    OrderID,
    CustomerID,
    OrderItemID,
    Status,
    AdressID,
    PaymentType, 
    PaymentStatus, 
    TotalPrice 
    FROM tOrder
    WHERE OrderID = pOrderID;
  END;

  -- Get Order by Customer
DROP PROCEDURE IF EXISTS sOrderbyCustomer;
CREATE PROCEDURE sOrderbyCustomer
  (
    IN pCustomerID INT
  )
  BEGIN
    SELECT
    OrderID,
    CustomerID,
    OrderItemID,
    Status,
    AdressID,
    PaymentType, 
    PaymentStatus, 
    TotalPrice
    FROM tOrder
    WHERE
      WHERE CustomerId = pCustomerID
      END;
  END;


--------------------------------------------------------------------------



/* Order Item */
DROP TABLE IF EXISTS tOrderItem;
CREATE TABLE tOrderItem
(
  OrderItemID       INT             AUTO_INCREMENT PRIMARY KEY,
  OrderID           INT             NOT NULL,UNIQUE,
  ProductID         INT             NOT NULL UNIQUE,
  Qty               INT             NOT NULL,
  Price             FLOAT           NOT NULL, 
  Status            VARCHAR(1024)   NOT NULL 
);


--Add
DROP PROCEDURE IF EXISTS sOrderItemAdd;
CREATE PROCEDURE sOrderItemAdd
  (
    IN pOrderID     INT,
    IN pProductID   INT,
    IN pQty         INT,
    IN pPrice       FLOAT,
    IN pStatus      VARCHAR(1024)
  )
  BEGIN
    DECLARE _id INT DEFAULT NULL;
    INSERT INTO tOrderItem (
    OrderID,
    ProductID,
    Qty,
    Price,
    Status 
    ) VALUES
    (
    pOrderID,
    pProductID,
    pQty,
    pPrice,
    pStatus 
    );
SET _id = (SELECT last_insert_id());
    SELECT
      1    AS IS_SUCCESS,
      _id  AS TRANSACTION_ID,
      ''   AS PRIMARY_COLUMN,
      NULL AS DB_RESPONSE_CODE,
      NULL AS DB_RESPONSE_MESSAGE
  END;

-- Update
DROP PROCEDURE IF EXISTS sOrderItemUpdate;
CREATE PROCEDURE sOrderItemUpdate
  (
    IN OrderItemID  INT,
    IN pOrderID     INT,
    IN pProductID   INT,
    IN pQty         INT,
    IN pPrice       FLOAT,
    IN pStatus      VARCHAR(1024)
  )
  BEGIN
    UPDATE tOrderItem
    SET
    OrderID     =   pOrderID,
    ProductID   =   pProductID,
    Qty         =   pQty,
    Price       =   pPrice,
    Status      =   pStatus 
    WHERE ID = pID;

    SELECT
      1               AS IS_SUCCESS,
      pOrderItemID    AS TRANSACTION_ID,
      ''              AS PRIMARY_COLUMN,
      NULL            AS DB_RESPONSE_CODE,
      NULL            AS DB_RESPONSE_MESSAGE
    FROM dual;
  END;

-- Delete
DROP PROCEDURE IF EXISTS sOrderItemDelete;
CREATE PROCEDURE sOrderItemDelete
  (
    IN pOrderItemID INT
  )
  BEGIN
    DELETE FROM tOrderItem
    WHERE OrderItemID = pOrderItemID;

    SELECT
      1               AS IS_SUCCESS,
      pOrderItemID    AS TRANSACTION_ID,
      ''              AS PRIMARY_COLUMN,
      NULL            AS DB_RESPONSE_CODE,
      NULL            AS DB_RESPONSE_MESSAGE
    FROM dual;
  END;

  --  Get By OrderItem

DROP PROCEDURE IF EXISTS sCartItemGet;
CREATE PROCEDURE sCartItemGet
  (
    IN pOrderItemID INT
  )
  BEGIN
    SELECT
    OrderItemID,
    OrderID,
    ProductID,
    Qty,
    Price,
    Status
    FROM tCartItem
    WHERE OrderItemID = pOrderItemID;
  END;


-- OrderItemGetListPage

-- DROP PROCEDURE IF EXISTS sOrderItemGetListPage;
-- CREATE PROCEDURE sOrderItemGetListPage
--   (
--     IN pOrderID     INT,
--     IN pProductID   INT,
--     IN pQty         INT,
--     IN pPrice       FLOAT,
--     IN pStatus      VARCHAR(1024)
--   )
--   BEGIN

--     DECLARE _offset INT;
--     DECLARE _total_rec INT;

--     IF pPageNum = 0 OR pPageNum = 1
--     THEN
--       SET _offset = 0;
--     ELSE
--       SET _offset = (pPageNum - 1) * pPageSize;
--     END IF;

--     IF pOrderID = 0
--     THEN
--       SET pProductID = NULL;
--     END IF;

--     IF pOrderID = 0
--     THEN
--       SET pOrderID = NULL;
--     END IF;

--     SET _total_rec = (
--       SELECT count(*)
--       FROM tOrderItem
--       WHERE
--         CASE WHEN pUniversityName = '' OR pUniversityName IS NULL
--           THEN
--             1 = 1
--         ELSE
--           Name LIKE concat(pUniversityName, '%')
--         END AND
--         StateID = ifnull(pStateID, StateID) AND
--         CityID = ifnull(pCityID, CityID)
--     );

--     SELECT _total_rec AS Total;

--     SELECT
--     OrderItemID,
--     OrderID,
--     ProductID,
--     Qty,
--     Price,
--       URL
--     FROM tOrderItem
--     WHERE
--       CASE WHEN pUniversityName = '' OR pUniversityName IS NULL
--         THEN
--           1 = 1
--       ELSE
--         Name LIKE concat(pUniversityName, '%')
--       END AND
--       OrderID = ifnull(pOrderID, OrderID) AND
--       ProductID = ifnull(pProductID, ProductID)
--     LIMIT _offset, pPageSize;
--   END;




----------------------------------------------------------------------------------

/* Payment */
DROP TABLE IF EXISTS tPayment;
CREATE TABLE tPayment
(
  PaymentID           INT             AUTO_INCREMENT PRIMARY KEY,
  OrderID             INT             NOT NULL,UNIQUE,
  TransactionNum      VARCHAR(1024)   NOT NULL, UNIQUE,
  TransactionDate     Date            NOT NULL, UNIQUE
);

--Add
DROP PROCEDURE IF EXISTS sPaymentAdd;
CREATE PROCEDURE sPaymentAdd
  (
    IN pOrderID             INT,
    IN pTransactionNum      VARCHAR(1024),
    IN pTransactionDate     DATE,
    
  )
  BEGIN
    DECLARE _id INT DEFAULT NULL;
    INSERT INTO tPayment (
    OrderID,
    TransactionNum,
    TransactionDate 
    ) VALUES
    (
    pOrderID,
    pTransactionNum,
  pTransactionDate 
    );
SET _id = (SELECT last_insert_id());
    SELECT
      1    AS IS_SUCCESS,
      _id  AS TRANSACTION_ID,
      ''   AS PRIMARY_COLUMN,
      NULL AS DB_RESPONSE_CODE,
      NULL AS DB_RESPONSE_MESSAGE
  END;

-- Update
DROP PROCEDURE IF EXISTS sPaymentUpdate;
CREATE PROCEDURE sPaymentUpdate
  (
    IN PaymentID        INT,
    IN pOrderID         INT,
    IN pTransactionNum  VARCHAR(1024),
    IN pTransactionDate DATE
  )
  BEGIN
    UPDATE tOrderItem
    SET
    OrderID         =   pOrderID,
    TransactionNum  =   pTransactionNum,
    TransactionDate =   pTransactionDate
    WHERE PaymentID =   pPaymentID;

    SELECT
      1             AS IS_SUCCESS,
      pPaymentID    AS TRANSACTION_ID,
      ''            AS PRIMARY_COLUMN,
      NULL          AS DB_RESPONSE_CODE,
      NULL          AS DB_RESPONSE_MESSAGE
    FROM dual;
  END;

-------------------------------------------------------------------------------------

/* Return */
DROP TABLE IF EXISTS tReturn;
CREATE TABLE tReturn
(
  ReturnID          INT             AUTO_INCREMENT PRIMARY KEY,
  OrderItemID       INT             NOT NULL,UNIQUE,
  Date              Date            NOT NULL, 
  Status            VARCHAR(1024)   NOT NULL,
  Qty               INT             NOT NULL 
);


--Add
DROP PROCEDURE IF EXISTS sReturnAdd;
CREATE PROCEDURE sReturnAdd
  (
    IN pOrderItemID     INT,
    IN pDate            DATE,
    IN pQty             INT,
    IN pStatus          INT
  )
  BEGIN
    DECLARE _id INT DEFAULT NULL;
    INSERT INTO tOrderItem (
    OrderItemID,
    Date,
    Qty,
    Status 
    ) VALUES
    (
    pOrderItemID,
    pDate,
    pQty,
    pStatus 
    );
SET _id = (SELECT last_insert_id());
    SELECT
      1    AS IS_SUCCESS,
      _id  AS TRANSACTION_ID,
      ''   AS PRIMARY_COLUMN,
      NULL AS DB_RESPONSE_CODE,
      NULL AS DB_RESPONSE_MESSAGE
  END;

-- Update
DROP PROCEDURE IF EXISTS sReturnUpdate;
CREATE PROCEDURE sReturnUpdate
  (
    IN ReturnID         INT,
    IN pOrderItemID     INT,
    IN pDate            DATE,
    IN pQty             INT,
    IN pStatus          INT
  )
  BEGIN
    UPDATE tOrderItem
    SET
    OrderItemID     =  pOrderItemID,
    Date            =   pDateID,
    Qty             =   pQty,
    Status          =   pStatus 
    WHERE ReturnID  =   pReturnID;

    SELECT
      1           AS IS_SUCCESS,
      pReturnID   AS TRANSACTION_ID,
      ''          AS PRIMARY_COLUMN,
      NULL        AS DB_RESPONSE_CODE,
      NULL        AS DB_RESPONSE_MESSAGE
    FROM dual;
  END;

-- Delete
DROP PROCEDURE IF EXISTS sReturnDelete;
CREATE PROCEDURE sReturnDelete
  (
    IN pReturnID INT
  )
  BEGIN
    DELETE FROM tReturn
    WHERE ReturnID = pReturnID;

    SELECT
      1           AS IS_SUCCESS,
      pReturnID   AS TRANSACTION_ID,
      ''          AS PRIMARY_COLUMN,
      NULL        AS DB_RESPONSE_CODE,
      NULL        AS DB_RESPONSE_MESSAGE
    FROM dual;
  END;
----------------------------------------------------------------------------------
