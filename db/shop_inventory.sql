DROP TABLE manufacturers;
DROP TABLE products;

CREATE TABLE manufacturers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  category VARCHAR(255),
  name VARCHAR(255)
);
