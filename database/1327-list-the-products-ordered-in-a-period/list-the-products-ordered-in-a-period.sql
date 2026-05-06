SELECT p.product_name, d.unit
FROM products p JOIN (
    SELECT product_id, SUM(unit) AS unit
    FROM orders
    WHERE order_date >= '2020-02-01' AND order_date < '2020-03-01'
    GROUP BY product_id
    HAVING SUM(unit) >= 100
) d ON p.product_id = d.product_id;
