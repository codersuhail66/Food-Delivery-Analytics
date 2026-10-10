import pandas as pd
import mysql.connector

# Read cleaned CSV
df = pd.read_csv("data/Food_Delivery_Cleaned.csv")

print(f"Loaded {len(df)} rows from CSV.")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="food_importer",
    password="Sulluaashiq@66",
    database="food_delivery_analytics"
)
cursor = conn.cursor()

# Insert query
sql = """
INSERT INTO food_orders (
    order_id,
    order_date,
    state,
    city,
    restaurant,
    category,
    food_type,
    order_value,
    rating,
    discount,
    payment_mode,
    order_status,
    net_sales,
    month,
    month_number,
    quarter,
    day_name,
    day_number
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""

# Convert dates to MySQL-compatible format
df["order_date"] = pd.to_datetime(df["order_date"]).dt.strftime("%Y-%m-%d")

# Convert dataframe to tuples
data = [tuple(row) for row in df.itertuples(index=False, name=None)]

# Insert records
cursor.executemany(sql, data)

conn.commit()

print(f"Successfully inserted {cursor.rowcount} rows.")

cursor.close()
conn.close()