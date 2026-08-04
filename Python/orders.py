import pandas as pd
import random
import os
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

# ============================
# CONFIGURATION
# ============================

TOTAL_ORDERS = 2_000_000
CHUNK_SIZE = 100_000
OUTPUT_FILE = "data/orders.csv"

# ============================
# LOAD DATASETS
# ============================

customers = pd.read_csv(
    "data/customers.csv",
    usecols=["customer_id", "city_id"]
)

restaurants = pd.read_csv(
    "data/restaurants.csv",
    usecols=["restaurant_id", "city_id"]
)

partners = pd.read_csv(
    "data/delivery_partners.csv",
    usecols=["partner_id", "city_id"]
)

coupons = pd.read_csv(
    "data/coupons.csv",
    usecols=[
        "coupon_code",
        "discount_type",
        "discount_value",
        "max_discount",
        "is_active"
    ]
)

# ============================
# DELETE OLD FILE
# ============================

os.makedirs("data", exist_ok=True)

if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

header_written = False

# ============================
# LOOKUP LISTS
# ============================

customer_ids = customers["customer_id"].tolist()

restaurant_ids = restaurants["restaurant_id"].tolist()

partner_ids = partners["partner_id"].tolist()

coupon_list = coupons.to_dict("records")

# ============================
# ORDER STATUS
# ============================

order_statuses = [
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Cancelled",
    "Preparing",
    "On the Way"
]

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Wallet",
    "Net Banking"
]

# ============================
# HELPER FUNCTIONS
# ============================

def random_order_datetime():

    start = datetime(2022, 1, 1)

    end = datetime(2026, 12, 31)

    seconds = random.randint(
        0,
        int((end - start).total_seconds())
    )

    return start + timedelta(seconds=seconds)



def calculate_delivery_fee(subtotal):

    if subtotal >= 499:
        return 0

    return random.choice([29, 39, 49, 59])


def calculate_tax(subtotal):

    return round(subtotal * 0.05, 2)


def apply_coupon(subtotal):

    # 70% of orders don't use coupons
    if random.random() > 0.30:
        return None, 0

    coupon = random.choice(coupon_list)

    if coupon["is_active"] == "No":
        return None, 0

    if coupon["discount_type"] == "Flat":

        discount = coupon["discount_value"]

    else:

        discount = subtotal * coupon["discount_value"] / 100

        discount = min(
            discount,
            coupon["max_discount"]
        )

    return coupon["coupon_code"], round(discount, 2)

print("All datasets loaded successfully.")
print("Ready to generate orders...")

# ============================
# GENERATE ORDERS
# ============================

order_id = 1

for start in range(1, TOTAL_ORDERS + 1, CHUNK_SIZE):

    rows = []

    end = min(start + CHUNK_SIZE - 1, TOTAL_ORDERS)

    for _ in range(start, end + 1):

        customer = customers.sample(1).iloc[0]
        restaurant = restaurants.sample(1).iloc[0]
        partner = partners.sample(1).iloc[0]

        order_time = random_order_datetime()

        status = random.choice(order_statuses)

        if status == "Delivered":
            delivery_time = order_time + timedelta(
                minutes=random.randint(20, 90)
            )

            payment_status = "Paid"

            customer_rating = random.randint(1, 5)

        elif status == "Cancelled":

            delivery_time = None

            payment_status = random.choice(
                ["Refunded", "Failed"]
            )

            customer_rating = None

        else:

            delivery_time = None

            payment_status = "Paid"

            customer_rating = None

        subtotal = random.randint(150, 1800)

        coupon_code, discount = apply_coupon(subtotal)

        delivery_fee = calculate_delivery_fee(subtotal)

        tax = calculate_tax(subtotal)

        total = subtotal - discount + delivery_fee + tax

        rows.append({

            "order_id": order_id,

            "customer_id": int(customer["customer_id"]),

            "restaurant_id": int(restaurant["restaurant_id"]),

            "partner_id": int(partner["partner_id"]),

            "city_id": int(customer["city_id"]),

            "order_datetime": order_time,

            "delivery_datetime": delivery_time,

            "order_status": status,

            "payment_method": random.choice(payment_methods),

            "payment_status": payment_status,

            "coupon_code": coupon_code,

            "subtotal": subtotal,

            "discount_amount": round(discount, 2),

            "delivery_fee": delivery_fee,

            "tax_amount": round(tax, 2),

            "total_amount": round(total, 2),

            "customer_rating": customer_rating

        })

        order_id += 1

    df = pd.DataFrame(rows)

    df.to_csv(

        OUTPUT_FILE,

        mode="a",

        index=False,

        header=not header_written

    )

    header_written = True

    print(f"Generated {end:,} orders...")

print("\n===================================")
print("orders.csv generated successfully!")
print(f"Total Orders : {TOTAL_ORDERS:,}")
print("===================================")