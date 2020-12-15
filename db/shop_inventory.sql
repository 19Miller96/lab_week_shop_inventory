DROP TABLE visits;
DROP TABLE manufacturers;
DROP TABLE products;

CREATE TABLE manufacturers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  product_id INT REFERENCES products(id) ON DELETE CASCADE
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

CREATE TABLE visits (
  id SERIAL PRIMARY KEY,
  product_id INT REFERENCES products(id) ON DELETE CASCADE,
  manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE,
  review TEXT
);
