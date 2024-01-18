import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# Ask for the data file
file_name = input("Enter the name of the data file: ")

# Read the file into a Pandas DataFrame
df = pd.read_csv(file_name)

# Ask for the columns to delete
columns_to_delete = input("Enter the names of the columns to delete, separated by commas: ").split(',')

# Delete the specified columns
for col in columns_to_delete:
    df = df.drop(col, axis=1)

# Remove unnecessary whitespace
df = df.applymap(lambda x: x.strip() if type(x) == str else x)

# Check for duplicate rows
duplicates = df[df.duplicated()]
if not duplicates.empty:
    print("Duplicate rows found:")
    print(duplicates)
    df = df.drop_duplicates()

# Ask if a column contains dates
column_with_dates = input("Enter the name of the column containing dates (or 'none' if there are no date columns): ")
if column_with_dates != "none":
    # Convert the specified column to a date format
    date_formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y"]
    for date_format in date_formats:
        try:
            df[column_with_dates] = pd.to_datetime(df[column_with_dates], format=date_format)
            print(f"Column '{column_with_dates}' converted to date format '{date_format}'.")
            break
        except ValueError:
            continue
    else:
        print(f"Could not convert column '{column_with_dates}' to a date format. Please specify a valid format.")

# Provide the info, description, shape, and head of the data
print("\nDataFrame info:")
print(df.info())
print("\nDataFrame description:")
print(df.describe())
print("\nDataFrame shape:")
print(df.shape)
print("\nDataFrame head:")
print(df.head())
