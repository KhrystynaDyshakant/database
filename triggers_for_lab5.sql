USE laba4;

DROP TABLE IF EXISTS laba4.orders_base;

-- створення довільної таблиці
CREATE TABLE IF NOT EXISTS laba4.orders_base (
    id INT NOT NULL AUTO_INCREMENT,
    orders_id INT NULL DEFAULT NULL,
    amount INT,
    PRIMARY KEY (id)
)  ENGINE=INNODB;

DROP TRIGGER IF EXISTS update_amount;

-- тригер  для автоматичного встановленння значення amount(для таблиці orders_base)
DELIMITER //
CREATE TRIGGER update_amount
BEFORE INSERT ON laba4.orders_base
FOR EACH ROW
BEGIN 
	SET NEW.amount = (
		SELECT COUNT(*)
        FROM lab4.orders_has_products
        WHERE orders_has_products.orders_id = NEW.orders_id
    );
END;
//
DELIMITER ;

-- перевірка тригера для автоматичного встановленння значення amount 
-- INSERT INTO laba4.orders_base (orders_id) VALUES (1);


DROP TRIGGER IF EXISTS before_update_orders;

-- тригер для оновлення запису (для таблиці orders_base)
DELIMITER //
CREATE TRIGGER before_update_orders
BEFORE UPDATE ON laba4.orders
FOR EACH ROW
BEGIN
    DECLARE orders_base_exists INT;

    -- Check if the referenced id exists in the orders_base table
    SELECT COUNT(*) INTO orders_base_exists
    FROM laba4.orders_base
    WHERE orders_id = NEW.id;

    -- If the id does not exist, prevent the update
    IF orders_base_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Referenced id does not exist in the orders_base table';
    END IF;
END //

DELIMITER ;

-- перевірка на оновлення запису
-- UPDATE laba4.orders_base
-- SET amount = 42
-- WHERE id = 1;


DROP TRIGGER IF EXISTS before_delete_orders_base;

-- тригер для видалення запису довільної таблиці(для таблиці orders_base)
DELIMITER //
CREATE TRIGGER before_delete_orders_base
BEFORE DELETE ON laba4.orders_base
FOR EACH ROW
BEGIN
    DELETE FROM laba4.orders
    WHERE id = OLD.orders_id;
END //

DELIMITER ;

-- перевірка на видалення запису 
-- DELETE FROM laba4.orders_has_products WHERE orders_id = 1;
-- DELETE FROM laba4.orders_base WHERE id = 1;


DROP TRIGGER IF EXISTS before_insert_on_customers;

-- тригер для певного стовпця допускається ввід лише таких імен
DELIMITER //
CREATE TRIGGER before_insert_on_customers
BEFORE INSERT ON customers
FOR EACH ROW 
BEGIN
	IF NOT (NEW.name REGEXP '^(Olya|Petro|Taras|Anna)$')
    THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Only names Olya, Petro, Taras, or Anna are allowed';
	END IF;
END //
DELIMITER ;

-- Перевірка на ввід імен
-- INSERT INTO customers (name, adress, email) VALUES
-- ('Taras', 'st. I.G 21', 'fghjk@gmail.com');

-- тригер "Заборонити видалення стрічок з таблиці"
DROP TRIGGER IF EXISTS before_delete_on_street;
DELIMITER //
CREATE TRIGGER before_delete_on_street
BEFORE DELETE ON street
FOR EACH ROW 
BEGIN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'This sreet cannot be deleted';
END //
DELIMITER ;

-- Спроба видалити запис
-- DELETE FROM street WHERE id = 1;


-- тригер "Значення певного стовпця не може закінчувати двома нулями"
DROP TRIGGER IF EXISTS before_insert_on_orders;
DELIMITER //
CREATE TRIGGER before_insert_on_orders
BEFORE INSERT ON orders
FOR EACH ROW 
BEGIN
	IF NEW.delivery_cost % 100 = 0
    THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid delivery cost. Cost cannot end with two zeros.';
	END IF;
END //
DELIMITER ;

-- перевірка на додвання двох нулів
-- INSERT INTO orders (order_date, order_status, customer_id, delivery_cost, delivery_id) VALUES
-- ('2023-10-18', 'Pending', 1, 70, 1);



