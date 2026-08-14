import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# 1. Connect to your local PostgreSQL database (replace 'your_password' with your actual postgres password)
engine = create_engine('postgresql+psycopg2://postgres:ARSHITHA@localhost:5432/ZEPTO_PROJECT')

# 2. EXTRACT: Read data from PostgreSQL table into a Pandas DataFrame
df = pd.read_sql('SELECT * FROM zepto_inventory', con=engine)

print(f"--- 1. EXTRACTED ---")
print(f"Total rows extracted: {len(df)}")

# 3. TRANSFORM: Data Quality & Cleaning
# Check for missing values & handle them
print("\n--- 2. DATA QUALITY & CLEANING ---")
print("Missing values per column before cleaning:")
print(df.isnull().sum())

# Drop duplicates if any
initial_count = len(df)
df = df.drop_duplicates()
print(f"Removed {initial_count - len(df)} duplicate rows.")

# Ensure numeric columns are clean and correct types
df['mrp'] = pd.to_numeric(df['mrp'], errors='coerce')
df['discounted_selling_price'] = pd.to_numeric(df['discounted_selling_price'], errors='coerce')
df['discount_percent'] = pd.to_numeric(df['discount_percent'], errors='coerce')

# Handle any missing/NaN values by filling with appropriate defaults or median
df['discount_percent'] = df['discount_percent'].fillna(0)

# Create a calculated column for absolute discount amount
df['absolute_discount'] = df['mrp'] - df['discounted_selling_price']

print("\nSample cleaned data:")
print(df[['category', 'product_name', 'mrp', 'discounted_selling_price', 'absolute_discount']].head(3))

# 4. LOAD: Write the cleaned data back into PostgreSQL as a new clean table
df.to_sql('zepto_inventory_cleaned', con=engine, if_exists='replace', index=False)
print("\n--- 3. LOADED ---")
print("Cleaned data successfully loaded back into PostgreSQL table: 'zepto_inventory_cleaned'")