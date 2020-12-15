DROP TABLE products;
DROP TABLE manufacturers;

CREATE TABLE manufacturers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  stock_quantity INT,
  buying_cost INT,
  selling_cost INT,
  manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE
);
