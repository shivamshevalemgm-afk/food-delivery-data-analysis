-- select customer_id , name AS customer_name
-- from customers c
--  where exists 
-- (select *
-- from orders o
-- where o.customer_id = c.customer_id);

-- select restaurant_id , restaurant_name
-- from restaurants r
-- where not exists 
-- (select 1
-- from reviews s
-- where r.restaurant_id = s.restaurant_id);

-- select c.customer_id , c.name AS customer_name , sum(o.total_amount) AS total_spending
-- from customers c
-- JOIN orders o
-- on c.customer_id = o.customer_id
-- group by c.customer_id , c.name
-- Having sum(o.total_amount) >
-- (select AVG(total_customer)
-- from (select sum(total_amount) AS total_customer
-- from orders 
-- group by customer_id 
-- ) AS customer_spending
-- );


-- WITH customer_spending AS
-- (
--     SELECT
--         c.customer_id,
--         c.name AS customer_name,
--         SUM(o.total_amount) AS total_spending
--     FROM customers c
--     JOIN orders o
--         ON c.customer_id = o.customer_id
--     GROUP BY c.customer_id, c.name
-- )

-- SELECT
--     customer_id,
--     customer_name,
--     total_spending
-- FROM customer_spending
-- ORDER BY total_spending DESC
-- LIMIT 5;


-- with restaurant_revenue AS
-- (
-- select r.restaurant_id , r.restaurant_name  , sum(o.total_amount) AS total_revenue
-- from restaurants r
-- JOIN orders o
-- ON r.restaurant_id = o.restaurant_id
-- group by r.restaurant_id , r.restaurant_name
-- )
-- select restaurant_id , restaurant_name , total_revenue
-- from restaurant_revenue
-- where total_revenue > 500000
-- order by total_revenue DESC;


-- with city_revenue AS
-- (
-- select c.city_id , c.city_name , sum(o.total_amount) AS total_revenue
-- from cities c
-- JOIN orders o 
-- ON c.city_id = o.city_id
-- Group by c.city_id , c.city_name
-- )
-- select city_id , city_name , total_revenue
-- from city_revenue
-- where total_revenue > 1000000
-- order by total_revenue DESC;


-- with customer_spending AS
-- (
-- select c.customer_id , c.name AS customer_name , SUM(o.total_amount) AS total_spending
-- from customers c
-- JOIN orders o
-- ON c.customer_id = o.customer_id
-- group by c.customer_id , c.name
-- )
-- select customer_id , customer_name , total_spending
-- from customer_spending
-- where total_spending > (select avg(total_spending) from customer_spending); 

-- with restaurant_revenue AS 
-- (
-- select r.restaurant_id , r.restaurant_name , sum(o.total_amount) AS total_revenue
-- from restaurants r
-- JOIN orders o
-- ON r.restaurant_id = o.restaurant_id
-- group by r.restaurant_id , r.restaurant_name
-- )
-- select restaurant_id , restaurant_name , total_revenue
-- from restaurant_revenue
-- order by total_revenue
-- limit 3;


