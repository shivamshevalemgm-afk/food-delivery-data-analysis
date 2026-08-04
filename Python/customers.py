import pandas as pd
import numpy as np
from faker import Faker
import random
import os

# -----------------------------
# CONFIGURATION
# -----------------------------
TOTAL_CUSTOMERS = 100000
OUTPUT_FILE = "data/customers.csv"

fake = Faker("en_IN")
Faker.seed(42)
random.seed(42)
np.random.seed(42)

os.makedirs("data", exist_ok=True)

if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

# -----------------------------
# LOAD CITIES
# -----------------------------
cities = pd.read_csv("data/cities.csv")
city_ids = cities["city_id"].to_numpy()

# -----------------------------
# MEMBERSHIP DISTRIBUTION
# -----------------------------
membership_types = np.array([
    "Regular",
    "Silver",
    "Gold",
    "Platinum"
])

membership_prob = [0.60, 0.22, 0.13, 0.05]

# -----------------------------
# GENDER DISTRIBUTION
# -----------------------------
genders = np.array([
    "MALE",
    "FEMALE",
    "OTHER"
])

gender_prob = [0.49, 0.49, 0.02]

rows = []

print("Generating customers...")

for customer_id in range(1, TOTAL_CUSTOMERS + 1):

    gender = np.random.choice(genders, p=gender_prob)

    if gender == "MALE":
        name = fake.name_male()
    elif gender == "FEMALE":
        name = fake.name_female()
    else:
        name = fake.name()

    dob = fake.date_of_birth(
        minimum_age=18,
        maximum_age=65
    )

    reg_date = fake.date_between(
        start_date="-5y",
        end_date="today"
    )

    total_orders = random.randint(0, 150)

    avg_order = random.uniform(250, 700)

    lifetime_value = round(
        total_orders * avg_order,
        2
    )

    rows.append({
        "customer_id": customer_id,
        "name": name,
        "gender": gender,
        "date_of_birth": dob,
        "email": fake.unique.email(),
        "phone": fake.msisdn()[:10],
        "city_id": int(np.random.choice(city_ids)),
        "registration_date": reg_date,
        "membership_type": np.random.choice(
            membership_types,
            p=membership_prob
        ),
        "is_active": np.random.choice(
            [1, 0],
            p=[0.92, 0.08]
        ),
        "total_orders": total_orders,
        "lifetime_value": lifetime_value
    })

    # Write every 10,000 rows
    if customer_id % 10000 == 0:

        df = pd.DataFrame(rows)

        df.to_csv(
            OUTPUT_FILE,
            mode="a",
            index=False,
            header=customer_id == 10000
        )

        rows = []

        print(f"{customer_id:,} customers generated")

# Write remaining rows
if rows:
    pd.DataFrame(rows).to_csv(
        OUTPUT_FILE,
        mode="a",
        index=False,
        header=False
    )

print("\ncustomers.csv generated successfully!")