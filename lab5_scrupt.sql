DROP DATABASE IF EXISTS laba4;

CREATE DATABASE IF NOT EXISTS laba4;

USE laba4;
-- -----------------------------------------------------
-- Table `laba4`.`city`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `laba4`.`city` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_city_id` (`id` ASC) VISIBLE,
  INDEX `idx_city_name` (`name` ASC) VISIBLE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `laba4`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `laba4`.`customers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `adress` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_customers_name` (`name` ASC) VISIBLE,
  INDEX `idx_customers_adress` (`adress` ASC) VISIBLE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `laba4`.`street`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `laba4`.`street` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `number_street` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_street_name` (`name` ASC) VISIBLE,
  INDEX `idx_street_number_street` (`number_street` ASC) VISIBLE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `laba4`.`location`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `laba4`.`location` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `city_id` INT NOT NULL,
  `street_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_location_city_id` (`city_id` ASC) VISIBLE,
  INDEX `idx_location_street_id` (`street_id` ASC) VISIBLE,
  CONSTRAINT `location_ibfk_1`
    FOREIGN KEY (`city_id`)
    REFERENCES `laba4`.`city` (`id`),
  CONSTRAINT `location_ibfk_2`
    FOREIGN KEY (`street_id`)
    REFERENCES `laba4`.`street` (`id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `laba4`.`delivery`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `laba4`.`delivery` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `term` VARCHAR(45) NULL DEFAULT NULL,
  `location_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_delivery_location_id` (`location_id` ASC) VISIBLE,
  INDEX `idx_delivery_term` (`term` ASC) VISIBLE,
  CONSTRAINT `delivery_ibfk_1`
    FOREIGN KEY (`location_id`)
    REFERENCES `laba4`.`location` (`id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `laba4`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `laba4`.`orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `order_date` DATE NULL DEFAULT NULL,
  `order_status` VARCHAR(255) NULL DEFAULT NULL,
  `customer_id` INT NOT NULL,
  `delivery_cost` INT NULL DEFAULT NULL,
  `delivery_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_orders_customer_id` (`customer_id` ASC) VISIBLE,
  INDEX `fk_orders_delivery1_idx` (`delivery_id` ASC) VISIBLE,
  CONSTRAINT `orders_ibfk_1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `laba4`.`customers` (`id`),
  CONSTRAINT `fk_orders_delivery1`
    FOREIGN KEY (`delivery_id`)
    REFERENCES `laba4`.`delivery` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `laba4`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `laba4`.`products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `product_name` VARCHAR(255) NULL DEFAULT NULL,
  `description` VARCHAR(255) NULL DEFAULT NULL,
  `price` INT NULL DEFAULT NULL,
  `position` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_products_product_name` (`product_name` ASC) VISIBLE,
  INDEX `idx_products_description` (`description` ASC) VISIBLE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `laba4`.`orders_has_products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `laba4`.`orders_has_products` (
  `orders_id` INT NOT NULL,
  `products_id` INT NOT NULL,
  PRIMARY KEY (`orders_id`, `products_id`),
  INDEX `idx_orders__has_products_orders_id` (`orders_id` ASC) VISIBLE,
  INDEX `idx_orders__has_products_products_id` (`products_id` ASC) VISIBLE,
  CONSTRAINT `orders_has_products_ibfk_1`
    FOREIGN KEY (`orders_id`)
    REFERENCES `laba4`.`orders` (`id`),
  CONSTRAINT `orders_has_products_ibfk_2`
    FOREIGN KEY (`products_id`)
    REFERENCES `laba4`.`products` (`id`)
    ON DELETE CASCADE  # Adjust this based on your requirements
    ON UPDATE CASCADE
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `laba4`.`stores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `laba4`.`stores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `address` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_stores_name` (`name` ASC) VISIBLE,
  INDEX `idx_stores_address` (`address` ASC) VISIBLE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `laba4`.`stores_has_products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `laba4`.`stores_has_products` (
  `stores_id` INT NOT NULL,
  `products_id` INT NOT NULL,
  `last_date` DATE NULL DEFAULT NULL,
  `expiration_date` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`stores_id`, `products_id`),
  INDEX `idx_stores_has_products_products_id` (`products_id` ASC) VISIBLE,
  INDEX `idx_stores_has_products_stores_id` (`stores_id` ASC) VISIBLE,
  CONSTRAINT `stores_has_products_ibfk_1`
    FOREIGN KEY (`stores_id`)
    REFERENCES `laba4`.`stores` (`id`),
  CONSTRAINT `stores_has_products_ibfk_2`
    FOREIGN KEY (`products_id`)
    REFERENCES `laba4`.`products` (`id`))
ENGINE = InnoDB;


INSERT INTO city (name) VALUES
('Lviv'),
('Kyiv'),
('Lviv'),
('Lviv'),
('Kyiv'),
('Lviv'),
('Lviv'),
('Lviv'),
('Kyiv'),
('Lviv');

INSERT INTO customers (name, adress, email) VALUES
('Taras Chupa', 'st. I.G 21', 'fghjk@gmail.com'),
('Alla Vaniusiv', 'st. G.K 13', 'akjnb@gmail.com'),
('Marta Hentosh', 'st. N.U 14', 'dfghj@gmail.com'),
('Mariya Kulish', 'st. G.L 18', 'dfghj@gmail.com'),
('Kostia Bulo', 'st. R.U 17', 'dfgh@gmail.com'),
('Ruslan Bytr', 'st. T.K 17', 'dfghj@gmail.com'),
('Nazar Melnuk', 'st. N.T 25', 'dfghjk@gmail.com'),
('Katya Shevchenko', 'st R.k 17', 'fghjkl@gmail.com'),
('Stas Melnuk', 'st. E.K 18', 'dfgh@gmail.com'),
('Nika Sem', 'st.E.L 78', 'dfghjk@gmail.com'),
('Petro', 'st.E.L 78', 'dfghjk@gmail.com');



INSERT INTO street (name, number_street) VALUES
('st. R.T', '1A'),
('st R.L', '28'),
('st. T.K', '34'),
('st K.J', '4D'),
('st R.U', '57'),
('st. E.K', '69'),
('st. N.K', '72'),
('st. E.M', '87'),
('st. V.K', '90'),
('st. Y.L', '120');

INSERT INTO location (city_id, street_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO delivery (term, location_id) VALUES
('fast', 1),
('slow', 2),
('very fast', 3),
('fast', 4),
('slow', 5),
('slow', 6),
('fast', 7),
('fast', 8),
('fast', 9),
('very fast', 10);

INSERT INTO orders (order_date, order_status, customer_id, delivery_cost, delivery_id) VALUES
('2023-10-18', 'Pending', 1, 70, 1),
('2023-10-19', 'Shipped', 2, 40, 2),
('2023-10-20', 'Delivered', 3, 80, 3),
('2023-10-21', 'Pending', 1, 40, 4),
('2023-10-22', 'Shipped', 2, 30, 5),
('2023-10-23', 'Delivered', 3, 30, 6),
('2023-10-24', 'Pending', 1, 40, 7),
('2023-10-25', 'Shipped', 2, 70, 8),
('2023-10-26', 'Delivered', 3, 10, 9),
('2023-10-27', 'Pending', 1, 50, 10);

INSERT INTO products (product_name, description, price, position) VALUES
('vegetables', 'save in fridge', 65, 'y'),
('fruits', 'save in fridge', 80, 'n'),
('milk', 'save in fridge', 45, 'y'),
('seafood', 'save in fridge', 250, 'y'),
('bread', 'none', 30, 'n'),
('ice-cream', 'save in fridge', 35, 'y'),
('flowers', 'save in fridge', 320, 'n'),
('books', 'none', 269, 'n'),
('flour', 'none', 50, 'y'),
('meet', 'save in fridge', 150, 'y');

INSERT INTO orders_has_products (orders_id, products_id) VALUES
(1, 2),
(2, 2),
(3, 5),
(4, 4),
(5, 6),
(6, 7),
(7, 7),
(8, 9),
(9, 9),
(10, 8);

INSERT INTO stores (name, address) VALUES
('Ashan', 'st. I.L 23'),
('Silpo', 'st. I.F 14'),
('ATB', 'st. L.U 17'),
('Bluzenko', 'st. V.L 28'),
('Rykavucka', 'st. V.C 45A'),
('Lidl', 'st. T.S 84'),
('Market', 'st. I.H 12'),
('23/7', 'st. H.S 18'),
('Capers', 'st. R.H 62'),
('Metro', 'st. E.T 12');

INSERT INTO stores_has_products (stores_id, products_id, last_date, expiration_date) VALUES
(1, 1, '2023-10-18', '2023-12-31'),
(2, 7, '2023-10-18', '2023-12-31'),
(3, 3, '2023-10-18', '2023-12-31'),
(4, 4, '2023-10-18', '2023-12-31'),
(5, 5, '2023-10-18', '2023-12-31'),
(6, 6, '2023-10-18', '2023-12-31'),
(7, 1, '2023-10-18', '2023-12-31'),
(8, 8, '2023-10-18', '2023-12-31'),
(9, 9, '2023-10-18', '2023-12-31'),
(10, 10, '2023-10-18', '2023-12-31')