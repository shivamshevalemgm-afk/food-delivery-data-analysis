import pandas as pd
import numpy as np
import os

# -----------------------------
# Configuration
# -----------------------------
CHUNK_SIZE = 100000
OUTPUT_FILE = "data/payments.csv"

np.random.seed(42)

payment_methods = np.array([
    "UPI",
    "Credit Card",
    "Debit Card",
    "Wallet",
    "Net Banking",
    "Cash on Delivery"
])

payment_method_prob = [0.45, 0.20, 0.15, 0.10, 0.05, 0.05]

payment_statuses = np.array([
    "Success",
    "Failed",
    "Refunded"
])

payment_status_prob = [0.97, 0.02, 0.01]

# Delete old file if it exists
if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

payment_id = 1
header = True

for chunk in pd.read_csv("data/orders.csv", chunksize=CHUNK_SIZE):

    n = len(chunk)

    transaction_ids = np.char.zfill(
        np.arange(payment_id, payment_id + n).astype(str),
        10
    )

    payment_df = pd.DataFrame({
        "payment_id": np.arange(payment_id, payment_id + n),

        "order_id": chunk["order_id"].to_numpy(),

        "payment_method": np.random.choice(
            payment_methods,
            size=n,
            p=payment_method_prob
        ),

        "payment_status": np.random.choice(
            payment_statuses,
            size=n,
            p=payment_status_prob
        ),

        "transaction_amount": chunk["total_amount"].to_numpy(),

        "transaction_datetime":
            pd.to_datetime(chunk["order_datetime"]) +
            pd.to_timedelta(
                np.random.randint(0, 6, n),
                unit="m"
            ),

        "transaction_reference":
            np.char.add("TXN", transaction_ids)
    })

    payment_df.to_csv(
        OUTPUT_FILE,
        mode="a",
        index=False,
        header=header
    )

    payment_id += n
    header = False

    print(f"{payment_id - 1:,} payments generated")

print("\npayments.csv generated successfully!")