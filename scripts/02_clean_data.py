import pandas as pd

INPUT_PATH = "data/agriculture_smart_irrigation_sample.csv"
OUTPUT_PATH = "data/agriculture_smart_irrigation_clean.csv"

# --------------------------------------------------
# 1. Load data
# --------------------------------------------------

df = pd.read_csv(INPUT_PATH)

print("Original shape:", df.shape)

# --------------------------------------------------
# 2. Convert Timestamp
# --------------------------------------------------

df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

# --------------------------------------------------
# 3. Remove duplicate rows
# --------------------------------------------------

duplicates_before = df.duplicated().sum()

df = df.drop_duplicates().reset_index(drop=True)

print("Duplicates removed:", duplicates_before)

# --------------------------------------------------
# 4. Handle missing values
# --------------------------------------------------

# Numeric columns -> median
numeric_columns = [
    "Temperature",
    "Humidity",
    "Rainfall",
    "Soil_Moisture"
]

for column in numeric_columns:
    missing = df[column].isna().sum()

    if missing > 0:
        df[column] = df[column].fillna(df[column].median())

        print(
            f"Filled {missing} missing values in {column} "
            f"using median"
        )

# Categorical column -> mode
categorical_columns = [
    "Crop_Stage"
]

for column in categorical_columns:
    missing = df[column].isna().sum()

    if missing > 0:
        df[column] = df[column].fillna(df[column].mode()[0])

        print(
            f"Filled {missing} missing values in {column} "
            f"using mode"
        )

# --------------------------------------------------
# 5. Validate ranges
# --------------------------------------------------

print("\nRange validation:")

print(
    "Temperature:",
    df["Temperature"].min(),
    "to",
    df["Temperature"].max()
)

print(
    "Humidity:",
    df["Humidity"].min(),
    "to",
    df["Humidity"].max()
)

print(
    "Rainfall:",
    df["Rainfall"].min(),
    "to",
    df["Rainfall"].max()
)

print(
    "Soil Moisture:",
    df["Soil_Moisture"].min(),
    "to",
    df["Soil_Moisture"].max()
)

# --------------------------------------------------
# 6. Check categorical values
# --------------------------------------------------

print("\nCrop stages:")
print(df["Crop_Stage"].unique())

print("\nIrrigation statuses:")
print(df["Irrigation_Status"].unique())

print("\nCrop outcomes:")
print(df["Crop_Outcome"].unique())

# --------------------------------------------------
# 7. Final validation
# --------------------------------------------------

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicates after cleaning:")
print(df.duplicated().sum())

print("\nFinal shape:")
print(df.shape)

# --------------------------------------------------
# 8. Save cleaned dataset
# --------------------------------------------------

df.to_csv(OUTPUT_PATH, index=False)

print("\nCleaned dataset saved to:")
print(OUTPUT_PATH)