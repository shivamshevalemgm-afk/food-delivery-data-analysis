import pandas as pd
import random
import os
from faker import Faker

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

TOTAL_RESTAURANTS = 5000
OUTPUT_FILE = "data/restaurants.csv"

os.makedirs("data", exist_ok=True)

cuisines = [
    "North Indian","South Indian","Chinese","Italian",
    "Fast Food","Pizza","Burger","Biryani",
    "Mughlai","Maharashtrian","Gujarati",
    "Punjabi","Cafe","Desserts","Street Food"
]

rows = []

for restaurant_id in range(1, TOTAL_RESTAURANTS + 1):

    rows.append({
        "restaurant_id": restaurant_id,
        "restaurant_name": fake.company() + " Restaurant",
        "owner_name": fake.name(),
        "city_id": random.randint(1,50),
        "cuisine_type": random.choice(cuisines),
        "opening_time": random.choice(["08:00:00","09:00:00","10:00:00"]),
        "closing_time": random.choice(["22:00:00","23:00:00","23:30:00"]),
        "average_rating": round(random.uniform(3.0,5.0),1),
        "total_reviews": random.randint(20,5000),
        "commission_rate": round(random.uniform(15,30),2),
        "is_active": random.choice([0,1])
    })

df = pd.DataFrame(rows)

df.to_csv(OUTPUT_FILE,index=False)

print(df.head())
print(f"\nGenerated {len(df):,} restaurants")