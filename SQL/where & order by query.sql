-- select customer_id , name , email , membership_type
-- from customers
-- where membership_type = 'gold'
-- order by name ;

-- select customer_id , name
-- from customers
-- where total_orders >20  AND is_active = 1
-- order by lifetime_value DESC;

-- select customer_id , name , membership_type , lifetime_value
-- from customers
-- where is_active = 1
-- AND lifetime_value > '50000' AND membership_type = 'platinum'
-- order by lifetime_value DESC;

-- select customer_id , name , membership_type
-- from customers
-- where membership_type  IN ('Gold' , 'Platinum')
-- order by membership_type , name;

-- select customer_id , name , membership_type , lifetime_value
-- from customers
-- where lifetime_value BETWEEN 20000 AND 50000
-- AND is_active = 1
-- order by lifetime_value DESC;

-- select customer_id , name ,email
-- from customers
-- where email LIKE  '%@gmail.com'
-- order by name ;

-- select customer_id , name ,city_id
-- from customers
-- where name LIKE 'A%'
-- order by name ;

-- select customer_id , name , phone
-- from customers
-- where phone LIkE '98%'
-- order by customer_id;


 

