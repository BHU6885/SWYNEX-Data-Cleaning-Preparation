# Data Cleaning & Preparation

## Internship Task

This project was completed as part of my Data Analytics internship at SWYNEX.

**Task 1: Data Cleaning & Preparation**

---

## Project Objective

The objective of this project is to clean and prepare a raw dataset for further data analysis.

The dataset contains information about movies and TV shows, including their titles, directors, cast, countries, release years, ratings, duration, genres, and descriptions.

The main goal was to identify and handle common data-quality issues such as:

- Missing values
- Duplicate records
- Incorrect data types
- Inconsistent text formatting

---

## Dataset

The dataset used for this project is a Netflix Movies and TV Shows dataset.

It contains information about Netflix titles and includes the following columns:

- show_id
- type
- title
- director
- cast
- country
- date_added
- release_year
- rating
- duration
- listed_in
- description

---

## Data Quality Issues Identified

During the initial inspection of the raw dataset, the following issues were identified:

### Missing Values

Missing values were found in:

| Column | Missing Values |
|---|---:|
| director | 1,969 |
| cast | 570 |
| country | 476 |
| date_added | 11 |
| rating | 10 |

Other columns did not contain missing values.

### Duplicate Records

The dataset contained:

**0 duplicate records**

Therefore, no duplicate rows needed to be removed.

### Data Type Issues

The `date_added` column was originally stored as text.

It was converted into a proper datetime format.

The `show_id` column was originally stored as an integer and was converted to a string because it represents an identifier rather than a numerical measurement.

---

## Data Cleaning Process

The following cleaning operations were performed:

### 1. Missing Value Handling

Missing values in the following columns were replaced with `Unknown`:

- director
- cast
- country
- rating

This was done to preserve the records instead of unnecessarily deleting rows.

### 2. Date Conversion

The `date_added` column was converted from text to datetime format using Pandas.

### 3. ID Conversion

The `show_id` column was converted from integer to string because it is an identifier.

### 4. Duplicate Removal

Duplicate records were checked and removed using Pandas.

The original dataset contained no duplicate rows.

### 5. Text Cleaning

Whitespace was removed from relevant text columns to improve consistency.

### 6. Cleaned Dataset Export

After cleaning, the processed dataset was saved as:

`netflix_titles_cleaned.csv`

---

## Tools & Technologies

- Python
- Pandas
- VS Code
- GitHub

---

## Project Structure

```text
SWYNEX-Data-Cleaning-Preparation
│
├── data
│   ├── netflix_titles.csv
│   └── netflix_titles_cleaned.csv
│
├── cleaning
│   └── data_cleaning.py
│
└── README.md