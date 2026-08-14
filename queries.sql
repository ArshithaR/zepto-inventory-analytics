DROP TABLE IF EXISTS zepto_inventory;

CREATE TABLE zepto_inventory (
    category VARCHAR(100),
    product_name VARCHAR(255),
    mrp NUMERIC(10, 2),
    discount_percent NUMERIC(5, 2),
    available_quantity INT,
    discounted_selling_price NUMERIC(10, 2),
    weight_in_gms INT,
    out_of_stock BOOLEAN,
    quantity INT
);

COPY zepto_inventory 
FROM 'C:\zepto\zepto_v2.csv' 
WITH (FORMAT csv, HEADER true, ENCODING 'LATIN1');
