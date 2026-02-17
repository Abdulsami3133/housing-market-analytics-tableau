# ============================================================
# HOUSING MARKET DATA PREPROCESSING & BUSINESS ANALYSIS
# ============================================================

# ------------------------------------------------------------
# 1. Import Required Libraries
# ------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8')
sns.set_palette("Set2")

# ------------------------------------------------------------
# 2. Load Dataset
# ------------------------------------------------------------
df = pd.read_csv("Transformed_Housing_Data2.csv")

print("Initial Dataset Shape:", df.shape)
print("\nDataset Info:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

# ------------------------------------------------------------
# 3. Data Cleaning
# ------------------------------------------------------------

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Fill basement area missing values with 0 (if exists)
if 'basement_area' in df.columns:
    df['basement_area'] = df['basement_area'].fillna(0)

# Drop rows with missing sale_price (critical column)
if 'sale_price' in df.columns:
    df = df.dropna(subset=['sale_price'])

print("\nDataset Shape After Cleaning:", df.shape)

# ------------------------------------------------------------
# 4. Feature Engineering
# ------------------------------------------------------------

CURRENT_YEAR = 2025

# House Age
if 'year_built' in df.columns:
    df['house_age'] = CURRENT_YEAR - df['year_built']

# Years Since Renovation
if 'year_renovated' in df.columns:
    df['years_since_renovation'] = np.where(
        df['year_renovated'] == 0,
        0,
        CURRENT_YEAR - df['year_renovated']
    )

# Price per Square Foot
if 'sqft_living' in df.columns:
    df['price_per_sqft'] = df['sale_price'] / df['sqft_living']

# Sale Price Bins
df['price_category'] = pd.cut(
    df['sale_price'],
    bins=[0, 300000, 600000, 1000000, 2000000, df['sale_price'].max()],
    labels=['Low', 'Medium', 'High', 'Luxury', 'Ultra-Luxury']
)

# ------------------------------------------------------------
# 5. Outlier Removal using IQR
# ------------------------------------------------------------

Q1 = df['sale_price'].quantile(0.25)
Q3 = df['sale_price'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df['sale_price'] >= lower_bound) & 
        (df['sale_price'] <= upper_bound)]

print("\nDataset Shape After Outlier Removal:", df.shape)

# ------------------------------------------------------------
# 6. Save Cleaned Dataset
# ------------------------------------------------------------

df.to_csv("Cleaned_Dataset.csv", index=False)
print("\nCleaned_Dataset.csv successfully saved!")

# ============================================================
# BUSINESS QUESTIONS & VISUALIZATIONS
# ============================================================

# ------------------------------------------------------------
# Business Question 1:
# Does renovation increase sale price?
# ------------------------------------------------------------

if 'years_since_renovation' in df.columns:
    plt.figure(figsize=(8,5))
    sns.boxplot(x='years_since_renovation', y='sale_price', data=df)
    plt.title("Renovation Impact on Sale Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------
# Business Question 2:
# How does house age influence pricing?
# ------------------------------------------------------------

if 'house_age' in df.columns:
    plt.figure(figsize=(8,5))
    sns.scatterplot(x='house_age', y='sale_price', data=df)
    plt.title("House Age vs Sale Price")
    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------
# Business Question 3:
# Which structural feature has strongest correlation with sale price?
# ------------------------------------------------------------

feature_cols = ['bedrooms', 'bathrooms', 'floors', 'sale_price']
existing_cols = [col for col in feature_cols if col in df.columns]

if len(existing_cols) >= 2:
    plt.figure(figsize=(6,5))
    corr = df[existing_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------
# Business Question 4:
# What is the distribution of houses across price categories?
# ------------------------------------------------------------

plt.figure(figsize=(7,5))
df['price_category'].value_counts().plot(kind='bar')
plt.title("Price Category Distribution")
plt.xlabel("Price Category")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# Business Question 5:
# Does number of bathrooms influence price?
# ------------------------------------------------------------

if 'bathrooms' in df.columns:
    plt.figure(figsize=(8,5))
    sns.boxplot(x='bathrooms', y='sale_price', data=df)
    plt.title("Bathrooms vs Sale Price")
    plt.tight_layout()
    plt.show()

print("\nPreprocessing and Business Analysis Completed Successfully.")
