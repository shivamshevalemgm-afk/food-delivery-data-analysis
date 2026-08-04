-- Select membership_type , count(customer_id) AS total_customers
-- from customers 
-- group by membership_type	
-- HAVING count(*) > 20000;

-- select o.order_id , c.customer_id , c.name  , o.total_amount
-- from customers c
-- INNER JOIN orders o 
-- ON c.customer_id = o.customer_id;

-- select c.customer_id , c.name AS customer_name , SUM(o.total_amount) AS total_spent
-- from customers c
-- JOIN orders o
-- ON c.customer_id = o.customer_id
-- group by c.customer_id , customer_name
-- order by total_spent DESC
-- LIMIT 5;

-- select r.restaurant_id , r.restaurant_name , sum(o.total_amount) AS total_revenue
-- from restaurants r
-- JOIN orders o
-- ON r.restaurant_id = o.restaurant_id
-- group by r.restaurant_id , r.restaurant_name
-- order by total_revenue DESC
-- LimIT 5;

-- select max(total_orders) AS number_order , customer_id , name AS customer_name
-- from customers
-- group by customer_id , name
-- order by number_order DESC
-- LIMIT 10;

-- select c.city_id , c.city_name ,  sum(o.total_amount) AS total_revenue
-- from cities c
-- InnER JOIN orders o 
-- on c.city_id = o.city_id
-- group by c.city_id , c.city_name
-- order by total_revenue
-- limit 5;