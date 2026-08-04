import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Number of records
rows = 1000000

# Generate IDs
review_id = np.arange(1, rows + 1)

order_id = np.random.randint(1, 2000001, rows)        # 2 million orders
customer_id = np.random.randint(1, 500001, rows)      # 5 lakh customers
restaurant_id = np.random.randint(1, 50001, rows)     # 50k restaurants


# Generate ratings (1.0 to 5.0)
restaurant_rating = np.round(
    np.random.uniform(1, 5, rows), 1
)

food_rating = np.round(
    np.random.uniform(1, 5, rows), 1
)

delivery_rating = np.round(
    np.random.uniform(1, 5, rows), 1
)


# Calculate overall rating
overall_rating = np.round(
    (restaurant_rating + food_rating + delivery_rating) / 3,
    1
)


# Review text samples
positive_reviews = [
    "Excellent food and fast delivery",
    "Amazing taste, will order again",
    "Food quality was great",
    "Very satisfied with service",
    "Fresh food and good packaging",
    "Delivery was quick and smooth"
]

negative_reviews = [
    "Food was cold",
    "Late delivery experience",
    "Poor food quality",
    "Not satisfied with service",
    "Taste was not good",
    "Packaging was damaged"
]

neutral_reviews = [
    "Food was okay",
    "Average experience",
    "Service was normal",
    "Could be improved",
    "Decent food quality"
]


review_text = []

for rating in overall_rating:
    if rating >= 4:
        review_text.append(random.choice(positive_reviews))
    elif rating <= 2.5:
        review_text.append(random.choice(negative_reviews))
    else:
        review_text.append(random.choice(neutral_reviews))


# Generate dates
review_date = pd.to_datetime(
    np.random.randint(
        pd.Timestamp('2023-01-01').value // 10**9,
        pd.Timestamp('2026-12-31').value // 10**9,
        rows
    ),
    unit='s'
).date


# Create dataframe
reviews = pd.DataFrame({

    "review_id": review_id,
    "order_id": order_id,
    "customer_id": customer_id,
    "restaurant_id": restaurant_id,
    "restaurant_rating": restaurant_rating,
    "food_rating": food_rating,
    "delivery_rating": delivery_rating,
    "overall_rating": overall_rating,
    "review_text": review_text,
    "review_date": review_date

})


# Save CSV
reviews.to_csv(
    "reviews.csv",
    index=False
)

print("Reviews data generated successfully!")
print(reviews.head())
print(reviews.shape)