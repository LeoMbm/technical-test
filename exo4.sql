-- # Ex 4: PSQL
-- #
-- # - Write pseudo-SQL statements to create database tables to store the products of a basic webshop.
-- # Each product has a name, a price, a creation date and may belong to several categories.
-- # Categories have a name and a flag to indicate whether the category is private or public.
-- #
-- # - Write a SQL query to find the list of products that belong to more than 5 public categories


CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    created_at DATETIME NOT NULL,
);

CREATE TABLE IF NOT EXISTS categories(
id INTEGER PRIMARY KEY,
name VARCHAR(255) NOT NULL,
public BOOLEAN NOT NULL,
product_id INTEGER NOT NULL,
FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE
);


SELECT products.name, products.name, categories.name
FROM products
INNER JOIN categories ON products.id=categories.product_id
WHERE categories.public=True;

