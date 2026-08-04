WITH RestaurantRevenue AS
(
    SELECT
        r.city_id,
        c.city_name,
        r.restaurant_id,
        r.restaurant_name,
        ROUND(SUM(o.total_amount), 2) AS total_revenue,

        ROW_NUMBER() OVER
        (
            PARTITION BY r.city_id
            ORDER BY SUM(o.total_amount) DESC
        ) AS rn

    FROM restaurants r

    JOIN orders o
        ON r.restaurant_id = o.restaurant_id

    JOIN cities c
        ON r.city_id = c.city_id

    GROUP BY
        r.city_id,
        c.city_name,
        r.restaurant_id,
        r.restaurant_name
)

SELECT
    city_name,
    restaurant_id,
    restaurant_name,
    total_revenue
FROM RestaurantRevenue
WHERE rn <= 3
ORDER BY city_name, total_revenue DESC;