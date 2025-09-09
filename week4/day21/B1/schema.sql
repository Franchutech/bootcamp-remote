-- Bootcamp Remote -SQL Avanzado
-- Scenary: Onlin Bookstore (E-commerce)

DROP TABLE IF EXISTS bs_order_items;
DROP TABLE IF EXISTS bs_orders;
DROP TABLE IF EXISTS bs_books;
DROP TABLE IF EXISTS bs_categories;
DROP TABLE IF EXISTS bs_customers;

--Create Clients table

CREATE TABLE bs_customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    country VARCHAR(100),
    loyalty_program VARCHAR(20) -- Basic, Silver, Gold, Premium
);

-- Create books category

CREATE TABLE bs_categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

-- Books

CREATE TABLE bs_books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150),
    category_id INT REFERENCES bs_categories(id),
    price NUMERIC(10,2)
);

-- Orders

CREATE TABLE bs_orders (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES bs_customers(id),
    order_date DATE, 
    purchase_behavior VARCHAR(20) -- Frequent, Occasional, Promotional
);

-- Orders detail

CREATE TABLE bs_order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES bs_orders(id),
    book_id INT REFERENCES bs_books(id),
    quantity INT
);




