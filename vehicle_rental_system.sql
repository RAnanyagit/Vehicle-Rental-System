CREATE DATABASE systems;

-- Use the new database
USE systems;

-- Create the customer table (cust)
CREATE TABLE cust (
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NULL,
    age INT NOT NULL,
    gender ENUM('male', 'female', 'other') NOT NULL,
    license_no VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,  -- Consider hashing this in your application
    phone VARCHAR(15) NOT NULL
);


-- Create the rental table (rent)
CREATE TABLE rent (
    vehicle_type ENUM('car', 'suv', 'van', 'bike') NOT NULL,
    with_driver ENUM('yes', 'no') NOT NULL,
    hours INT NOT NULL,
    total_price DECIMAL(10, 2) DEFAULT 0.00,
    FOREIGN KEY (customer_id) REFERENCES cust(id) ON DELETE CASCADE
);
CREATE TABLE account (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);