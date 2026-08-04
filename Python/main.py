import pandas as pd
import mysql.connector

# ==========================
# DATABASE CONFIGURATION
# ==========================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shiva@3012",
    database="flipkart_goat_sale"
)

cursor = conn.cursor()

# ==========================
# READ CSV
# ==========================
df = pd.read_csv(r"C:\Users\SHIVAM\OneDrive\Apps\Python\data\delivery_partners.csv")

print(f"Total Delivery Partners: {len(df):,}")

# Replace NaN with None
df = df.where(pd.notnull(df), None)

# ==========================
# INSERT QUERY
# ==========================
sql = """
INSERT INTO delivery_partners
(
partner_id,
name,
phone,
city_id,
joining_date,
vehicle_type,
average_rating,
total_deliveries,
is_active,
gender,
age
)
VALUES
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

# ==========================
# INSERT IN BATCHES
# ==========================
batch_size = 5000

for start in range(0, len(df), batch_size):

    batch = df.iloc[start:start + batch_size]

    cursor.executemany(sql, batch.values.tolist())

    conn.commit()

    print(f"Inserted {min(start + batch_size, len(df)):,} rows")

cursor.close()
conn.close()

print("\n✅ Delivery Partners imported successfully!")