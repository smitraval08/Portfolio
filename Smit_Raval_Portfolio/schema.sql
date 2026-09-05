CREATE DATABASE IF NOT EXISTS mca_portfolio;

USE mca_portfolio;

CREATE TABLE IF NOT EXISTS contact_messages (

    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(120) NOT NULL,

    email VARCHAR(190) NOT NULL,

    subject VARCHAR(200),

    message TEXT NOT NULL,

    created_at DATETIME NOT NULL

);