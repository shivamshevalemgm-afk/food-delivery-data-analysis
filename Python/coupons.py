import pandas as pd
import random
import os
from faker import Faker

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

OUTPUT_FILE = "data/coupons.csv"

os.makedirs("data", exist_ok=True)

coupon_names = [
    "WELCOME",
    "SAVEBIG",
    "SUPER",
    "FOODIE",
    "HUNGRY",
    "MEAL",
    "DINNER",
    "LUNCH",
    "BREAKFAST",
    "FAST",
    "TREAT",
    "SPECIAL",
    "FESTIVE",
    "WEEKEND",
    "SUMMER",
    "WINTER",
    "RAINY",
    "HAPPY",
    "FLASH",
    "GOAT"
]

rows = []

for coupon_id in range(1, 501):

    prefix = random.choice(coupon_names)

    code = f"{prefix}{random.randint(100,999)}"

    discount_type = random.choice(["Percentage", "Flat"])

    if discount_type == "Percentage":
        discount_value = random.choice([10,15,20,25,30,40,50])
        max_discount = random.choice([100,150,200,250,300,400,500])
    else:
        discount_value = random.choice([50,75,100,125,150,200,250])
        max_discount = discount_value

    start_date = fake.date_between(
        start_date="-2y",
        end_date="-30d"
    )

    end_date = fake.date_between(
        start_date="today",
        end_date="+1y"
    )

    rows.append({
        "coupon_id": coupon_id,
        "coupon_code": code,
        "coupon_name": prefix,
        "discount_type": discount_type,
        "discount_value": discount_value,
        "min_order_value": random.choice([199,299,399,499,599,799]),
        "max_discount": max_discount,
        "start_date": start_date,
        "end_date": end_date,
        "usage_limit": random.randint(500,50000),
        "is_active": random.choice(["Yes","Yes","Yes","No"])
    })

df = pd.DataFrame(rows)

df.to_csv(OUTPUT_FILE,index=False)

print("✅ coupons.csv generated successfully!")
print("Rows:",len(df))