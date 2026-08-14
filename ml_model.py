import pandas as pd
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression

# 1. Connect to PostgreSQL and load the cleaned data
engine = create_engine('postgresql+psycopg2://postgres:ARSHITHA@localhost:5432/ZEPTO_PROJECT')
df = pd.read_sql('SELECT * FROM zepto_inventory_cleaned', con=engine)

print("--- 1. STATISTICAL SUMMARY ---")
# Calculate basic descriptive statistics for pricing and discounts
print(df[['mrp', 'discounted_selling_price', 'discount_percent', 'available_quantity']].describe())

print("\n--- 2. MACHINE LEARNING: PREDICTING SELLING PRICE ---")
# Prepare data for a simple Linear Regression model
# Let's predict 'discounted_selling_price' using 'mrp' and 'discount_percent'
X = df[['mrp', 'discount_percent']].fillna(0)
y = df['discounted_selling_price'].fillna(0)

model = LinearRegression()
model.fit(X, y)

print(f"Model Intercept: {model.intercept_:.2f}")
print(f"Model Coefficients (MRP, Discount %): {model.coef_}")
print(f"Model R-squared Score: {model.score(X, y):.4f}")

# Example prediction: Predict selling price for an item with MRP = 5000 and 15% discount
sample_pred = model.predict([[5000, 15]])
print(f"\nPredicted selling price for MRP 5000 at 15% discount: ₹{sample_pred[0]:.2f}")
