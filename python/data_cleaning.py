
import pandas as pd
import numpy as np



# 1. IMPORT DATA


df = pd.read_excel(
    "data/Food_Delivery_PowerBI_Practice.xlsx"
)
print("Original Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())



# 2. CLEAN COLUMN NAMES


df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nColumn Names:")
print(df.columns.tolist())



# 3. CHECK DATA TYPES


print("\nData Types:")
print(df.dtypes)



# 4. CHECK DUPLICATE ROWS


print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove completely duplicate rows
df = df.drop_duplicates()



# 5. CHECK MISSING VALUES


print("\nMissing Values:")
print(df.isnull().sum())



# 6. CLEAN TEXT COLUMNS


text_columns = [
    "order_id",
    "state",
    "city",
    "restaurant",
    "category",
    "food_type",
    "payment_mode",
    "order_status",
    "month",
    "quarter",
    "day_name"
]

for col in text_columns:
    df[col] = df[col].astype("string").str.strip()



# 7. STANDARDIZE TEXT VALUES


df["state"] = df["state"].str.title()
df["city"] = df["city"].str.title()
df["restaurant"] = df["restaurant"].str.title()
df["category"] = df["category"].str.title()
df["food_type"] = df["food_type"].str.title()
df["payment_mode"] = df["payment_mode"].str.title()
df["order_status"] = df["order_status"].str.title()



# 8. CLEAN ORDER DATE


df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce",
    dayfirst=True
)

print("\nInvalid Order Dates:")
print(df["order_date"].isna().sum())



# 9. CONVERT NUMERIC COLUMNS


numeric_columns = [
    "order_value",
    "rating",
    "discount",
    "net_sales",
    "month_number",
    "day_number"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )



# 10. CHECK INVALID RATINGS


invalid_ratings = (
    (df["rating"] < 1) |
    (df["rating"] > 5)
)

print("\nInvalid Ratings:")
print(invalid_ratings.sum())

# Replace invalid ratings with missing values
df.loc[invalid_ratings, "rating"] = np.nan



# 11. CHECK NEGATIVE VALUES


print("\nNegative Order Values:")
print((df["order_value"] < 0).sum())

print("\nNegative Discounts:")
print((df["discount"] < 0).sum())

print("\nNegative Net Sales:")
print((df["net_sales"] < 0).sum())



# 12. REPLACE INVALID NEGATIVE VALUES


df.loc[df["order_value"] < 0, "order_value"] = np.nan

df.loc[df["discount"] < 0, "discount"] = np.nan

df.loc[df["net_sales"] < 0, "net_sales"] = np.nan



# 13. CHECK DUPLICATE ORDER IDs


print("\nDuplicate Order IDs:")
print(df["order_id"].duplicated().sum())



# 14. REMOVE DUPLICATE ORDER IDs


df = df.drop_duplicates(
    subset=["order_id"],
    keep="first"
)



# 15. RECREATE DATE-RELATED COLUMNS


# These columns are recreated directly from Order_Date
# so they cannot contain incorrect month/day information.

df["month"] = df["order_date"].dt.strftime("%b")

df["month_number"] = df["order_date"].dt.month

df["quarter"] = (
    "Q" + df["order_date"].dt.quarter.astype(str)
)

df["day_name"] = df["order_date"].dt.strftime("%a")

df["day_number"] = df["order_date"].dt.day



# 16. CHECK ORDER STATUS


print("\nOrder Status:")
print(df["order_status"].value_counts())



# 17. CHECK PAYMENT MODE


print("\nPayment Mode:")
print(df["payment_mode"].value_counts())



# 18. CHECK CATEGORY


print("\nCategory:")
print(df["category"].value_counts())



# 19. CHECK FOOD TYPE


print("\nFood Type:")
print(df["food_type"].value_counts())



# 20. CHECK NET SALES


print("\nNet Sales Summary:")
print(df["net_sales"].describe())



# 21. CHECK ORDER VALUE


print("\nOrder Value Summary:")
print(df["order_value"].describe())



# 22. FINAL MISSING VALUE CHECK


print("\nFinal Missing Values:")
print(df.isnull().sum())



# 23. FINAL DATASET INFORMATION


print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Data Types:")
print(df.dtypes)



# 24. VIEW CLEANED DATA


print("\nCleaned Dataset:")
print(df.head())



# 25. SAVE CLEANED DATASET


# Save cleaned dataset
output_path = "data/Food_Delivery_Cleaned.xlsx"

df.to_excel(
    output_path,
    index=False
)

print("====================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("====================================")
print(f"Cleaned file saved to: {output_path}")