DELIMITER $$

CREATE PROCEDURE create_tables_for_cursor()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE tableName CHAR(30);
    DECLARE numColumns INT;
    DECLARE sqlQuery VARCHAR(1000);

    DECLARE cur CURSOR FOR SELECT name FROM customers;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO tableName;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SET numColumns = FLOOR(1 + RAND() * 9);

        SET @sqlQuery = CONCAT('CREATE TABLE ', REPLACE(tableName, ' ', '_'), '_',
                               DATE_FORMAT(NOW(), '%Y%m%d%H%i%s'), ' (');

        SET @i = 1;
        WHILE @i <= numColumns DO
            SET @sqlQuery = CONCAT(@sqlQuery, 'column', @i, ' VARCHAR(100)');
            IF @i < numColumns THEN
                SET @sqlQuery = CONCAT(@sqlQuery, ', ');
            END IF;
            SET @i = @i + 1;
        END WHILE;

        SET @sqlQuery = CONCAT(@sqlQuery, ')');

        PREPARE stmt FROM @sqlQuery;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    CLOSE cur;

END $$

DELIMITER ;

CALL create_tables_for_cursor();
