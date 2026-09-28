import pandas as pd

DATA_PATH = "data/agriculture_smart_irrigation_sample.csv"

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("DATASET INSPECTION")
print("=" * 60)

print("\n1. Shape:")
print(df.shape)

print("\n2. Columns:")
print(df.columns.tolist())

print("\n3. First 5 rows:")
print(df.head())

print("\n4. Data Types:")
print(df.dtypes)

print("\n5. Missing Values:")
print(df.isnull().sum())

print("\n6. Duplicate Rows:")
print(df.duplicated().sum())

print("\n7. Numerical Statistics:")
print(df.describe())

print("\n8. Categorical Columns:")
for column in df.select_dtypes(include="object").columns:
    print(f"\n{column}:")
    print(df[column].value_counts(dropna=False))

print("\n" + "=" * 60)