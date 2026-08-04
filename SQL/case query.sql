-- select customer_id,name AS customer_name,total_orders,
-- case
--       when total_orders >= 100 Then 'Platinum'
--       when total_orders >= 50 Then 'Gold'
--       when total_orders >= 20 Then 'silver'
--       ELSE 'Regular'
--        END AS customer_category
-- from customers;

-- select order_id,customer_id,total_amount,
-- case
-- 	when total_amount >= 1000 Then 'High'
--     when total_amount >= 500 Then 'Medium'
--     ELSE'Low'
--     END AS order_category
--     from orders;

-- with restaurant_value AS
-- (
-- select r.restaurant_id,r.restaurant_name,sum(o.total_amount) AS total_revenue
-- from restaurants r
-- JOIN orders o
-- On r.restaurant_id = o.restaurant_id
-- Group by r.restaurant_id,r.restaurant_name
-- )
-- select restaurant_id,restaurant_name,total_revenue,
-- CASE
--     when total_revenue >=20000 Then 'High'
--     when total_revenue >5000 Then 'Medium'
--     ELSE 'Low'
--     END AS order_category
--     from restaurant_value;

-- with restaurant_value AS
-- (
-- select c.customer_id,c.name AS customer_name,sum(o.total_amount) AS total_revenue
-- from customers c
-- JOIN orders o
-- On c.customer_id = o.customer_id
-- Group by c.customer_id , c.name
-- )
-- select customer_id,customer_name,total_revenue,
-- CASE
--     when total_revenue >=20000 Then 'Vip'
--     when total_revenue >= 10000 Then 'Premium'
--     when total_revenue >= 5000 Then 'Regular'
--     ELSE 'New_customer'
--     END AS order_category
--     from restaurant_value;


-- SELECT
--     COUNT(*) AS total_orders,

--     SUM(CASE
--             WHEN order_status = 'completed' THEN 1
--             ELSE 0
--         END) AS completed_orders,

--     SUM(CASE
--             WHEN order_status = 'cancelled' THEN 1
--             ELSE 0
--         END) AS cancelled_orders,

--     SUM(CASE
--             WHEN order_status = 'pending' THEN 1
--             ELSE 0
--         END) AS pending_orders

-- FROM orders;

-- select r.restaurant_id , r.restaurant_name , count(o.order_status) AS total_orders ,
-- SUM(CASE
--             WHEN order_status = 'Delivered' THEN 1
--             ELSE 0
--         END) AS completed_orders,

--     SUM(CASE
--             WHEN order_status = 'cancelled' THEN 1
--             ELSE 0
--         END) AS cancelled_orders,

--     SUM(CASE
--             WHEN order_status = 'preparing' THEN 1
--             ELSE 0
--         END) AS pending_orders,
--         
--         SUM(CASE 
--                 WHEN order_status = 'On the way' THEN 1
--                 ELSE 0
-- 			END)AS Reaching
-- from restaurants r
-- JOIN orders o
-- ON r.restaurant_id = o.restaurant_id
-- group by r.restaurant_id,r.restaurant_name;


-- select order_id,customer_id, order_datetime,total_amount AS order_amount,
-- sum(total_amount)
-- over
-- (
-- partition by customer_id
-- order by order_datetime) AS running_total
-- from orders;

-- select order_id,customer_id, order_datetime,total_amount AS order_amount,
-- AVG(total_amount)
-- over
-- (
-- partition by customer_id
-- order by order_datetime) AS running_total
-- from orders;

   



