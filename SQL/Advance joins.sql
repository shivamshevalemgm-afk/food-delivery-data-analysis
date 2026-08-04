-- SELECT
--     p.partner_id,
--     p.name AS partner_name,
--     COUNT(o.order_id) AS number_delivery_orders
-- FROM delivery_partners p
-- JOIN orders o
--     ON p.partner_id = o.partner_id
-- WHERE o.order_status = 'Delivered'
-- GROUP BY p.partner_id, p.name
-- ORDER BY number_delivery_orders DESC
-- LIMIT 5;

-- select c.customer_id , c.name AS customer_name , o.order_id
-- from customers c
-- LEFT JOIN orders o
-- ON c.customer_id = o.customer_id
-- group by c.customer_id , c.name , o.order_id;

-- select c.customer_id , c.name AS customer_name
-- from customers c
-- LEFT JOIN orders o
-- ON c.customer_id = o.customer_id
-- where o.order_id IS NULL;


-- select r.restaurant_id , r.restaurant_name
-- from restaurants r
-- LEFT JOIN orders o
-- ON r.restaurant_id = o.restaurant_id
-- where o.order_id IS NULL;

-- select d.partner_id , d.name AS partner_name
-- from delivery_partners d
-- LEFT join orders o
-- ON d.partner_id = o.partner_id
-- AND o.order_status NOT IN ('delivered')
-- WHERE o.order_id IS NULL;

--  Find all customers whose lifetime value is greater than the average lifetime value of all customers.
-- SELECT customer_id,name As customer_name ,lifetime_value
-- from customers
-- where lifetime_value > (select AVG(lifetime_value) from customers)

-- Find all restaurants whose average rating is higher than the overall average rating of all restaurants.

-- select restaurant_id , restaurant_name , total_reviews
-- from restaurants
-- where total_reviews > (select avg(total_reviews) from restaurants);

-- Find customers who have placed more orders than the average customer.
-- SELECT c.customer_id , c.name AS customer_name , count(o.order_id) AS number_orders
-- from customers c
-- JOIN orders o
-- ON c.customer_id = o.customer_id
-- group by c.customer_id , c.name
-- having count(o.order_id)> AVG(o.order_id);

