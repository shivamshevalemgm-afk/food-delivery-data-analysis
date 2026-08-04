import pandas as pd
import random
import os
from faker import Faker

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

# Load cities
cities = pd.read_csv("data/cities.csv")

OUTPUT_FILE = "data/delivery_partners.csv"
TOTAL_PARTNERS = 20000
CHUNK_SIZE = 5000

os.makedirs("data", exist_ok=True)

# Delete old file if it exists
if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

header_written = False

vehicle_types = [
    "Bike",
    "Scooter",
    "Bicycle"
]

availability = [
    "Available",
    "Busy",
    "Offline"
]

for start in range(1, TOTAL_PARTNERS + 1, CHUNK_SIZE):

    rows = []

    end = min(start + CHUNK_SIZE - 1, TOTAL_PARTNERS)

    for partner_id in range(start, end + 1):

        city = cities.sample(1).iloc[0]

        rows.append({
            "partner_id": partner_id,
            "partner_name": fake.name(),
            "gender": random.choice(["Male", "Female"]),
            "age": random.randint(18, 55),
            "phone": fake.msisdn()[-10:],
            "city_id": int(city["city_id"]),
            "vehicle_type": random.choice(vehicle_types),
            "joining_date": fake.date_between(
                start_date="-6y",
                end_date="today"
            ),
            "rating": round(random.uniform(3.5, 5.0), 1),
            "total_deliveries": random.randint(50, 12000),
            "availability_status": random.choice(
                ["Available", "Available", "Busy", "Offline"]
            )
        })

    df = pd.DataFrame(rows)

    df.to_csv(
        OUTPUT_FILE,
        mode="a",
        index=False,
        header=not header_written
    )

    header_written = True

    print(f"Generated {end:,} delivery partners...")

print("\n✅ delivery_partners.csv generated successfully!")
print(f"Total Delivery Partners: {TOTAL_PARTNERS:,}")