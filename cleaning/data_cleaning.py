from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "netflix_titles.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "netflix_titles_cleaned.csv"

# -----------------------------------------
# 1. Load raw dataset
# -----------------------------------------

df = pd.read_csv(INPUT_FILE)

print("Original dataset shape:", df.shape)


# -----------------------------------------
# 2. Convert data types
# -----------------------------------------

# show_id is an identifier, not a numerical measurement
df["show_id"] = df["show_id"].astype(str)

# Convert date_added from text to datetime
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)


# -----------------------------------------
# 3. Handle missing values
# -----------------------------------------

df["director"] = df["director"].fillna("Unknown")

df["cast"] = df["cast"].fillna("Unknown")

df["country"] = df["country"].fillna("Unknown")

df["rating"] = df["rating"].fillna("Unknown")


# -----------------------------------------
# 4. Remove duplicate records
# -----------------------------------------

df = df.drop_duplicates()


# -----------------------------------------
# 5. Clean text columns
# -----------------------------------------

text_columns = [
    "type",
    "title",
    "director",
    "cast",
    "country",
    "rating",
    "duration",
    "listed_in",
    "description"
]

for column in text_columns:
    df[column] = df[column].str.strip()


# -----------------------------------------
# 6. Save cleaned dataset
# -----------------------------------------

df.to_csv(OUTPUT_FILE, index=False)


# -----------------------------------------
# 7. Validation
# -----------------------------------------

print("\n===== CLEANING RESULTS =====")

print("\nDataset shape after cleaning:")
print(df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

print("\nData types after cleaning:")
print(df.dtypes)

print("\nCleaned dataset saved successfully!")