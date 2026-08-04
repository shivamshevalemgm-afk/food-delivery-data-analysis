-- Select count(*) AS total_customers , membership_type
-- from customers
-- Group by membership_type
-- order by total_customers DESC;

-- select membership_type , sum(lifetime_value) AS total_lifetime_value
-- from customers
-- group by membership_type
-- order by total_lifetime_value Desc;

-- select membership_type , AVG(lifetime_value) AS avg_lifetime_value
-- from customers
-- group by membership_type
-- order by avg_lifetime_value;

-- select membership_type , MAX(lifetime_value) AS max_lifetime_value 
-- from customers
-- group by membership_type	
-- order by max_lifetime_value DESC;