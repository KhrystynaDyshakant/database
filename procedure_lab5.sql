USE laba4;

-- параметизована вставка нових значень
DELIMITER //
CREATE PROCEDURE insert_stores (
IN name varchar(45),
address varchar(45)
)
BEGIN
INSERT INTO stores(name, address) VALUES (name, address);
END;
//

DROP PROCEDURE IF NOT EXISTS insert_stores_and_products_dependency;   

-- вставка в стикувальну таблицю
DELIMITER //
CREATE PROCEDURE insert_stores_and_products_dependency (
IN name_ varchar(255),
IN product_name_ varchar(255)
)
BEGIN
	DECLARE stores INT; 
    DECLARE products INT;
    SELECT id INTO stores FROM stores WHERE name = name_;
	SELECT id INTO products FROM products WHERE product_name = product_name_;
    INSERT INTO stores_has_products (stores_id, products_id) VALUES (stores, products);
END;
//

DROP PROCEDURE IF NOT EXISTS insert_products;

-- пакет, який вставляє 10 стрічок
DELIMITER //
CREATE PROCEDURE insert_products (
)
BEGIN
	Insert INTO products (product_name) VALUES 
		('Noname1'), ('Noname2'), 
		('Noname3'), ('Noname4'), 
		('Noname5'), ('Noname6'), 
		('Noname7'), ('Noname8'), 
		('Noname9'), ('Noname10');
        
END;
//

DROP PROCEDURE IF NOT EXISTS make_operation;

-- користувацька функція для max, min, avg, sum
DELIMITER //
CREATE FUNCTION make_operation(
    operation VARCHAR(45)
)
RETURNS INT
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE result DECIMAL(10,2) DEFAULT 0.0;

    IF operation = 'min' THEN
        SELECT MIN(price) INTO result FROM products;
    ELSEIF operation = 'max' THEN
        SELECT MAX(price) INTO result FROM products;
    ELSEIF operation = 'avg'  THEN
        SELECT AVG(price) INTO result FROM products;
	ELSEIF operation = 'sum'  THEN
        SELECT SUM(price) INTO result FROM products;
    END IF;
    RETURN result;
END;
//

DROP PROCEDURE IF NOT EXISTS make_operation_products;

DELIMITER //
CREATE 
PROCEDURE make_operation_products(
	operation VARCHAR(45)
)
BEGIN
	DECLARE result DECIMAL(10,2);
    SET result = make_operation(operation);
    SELECT result AS operation_result;
END;
//
