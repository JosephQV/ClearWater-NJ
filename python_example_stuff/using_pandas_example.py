import pandas as pd
import os
from pathlib import Path

# Reading an Excel file and storing the data in a DataFrame object
file = f"{Path(os.curdir).parent}/data/water_systems/EPA_Water System Summary_20250507.xlsx"
dataframe = pd.read_excel(file)
# This should automatically read the first row from the Excel table as
# the column names for each column. If you want to use different column
# names or read the data from a different sheet in the Excel file, see the
# other optional arguments you can pass to the read_excel function on the 
# pandas documentation page for it.


# Printing the first 10 columns of the dataframe to the terminal to see
# what the data looks like, as a test.
print(dataframe.head(10))
print("\n") # prints newline character

# Accessing an entire column of the table. Replace with the appropriate
# column name.
column = dataframe["Contact Name"]
print(column)   # printing as a test
print("\n")

# Accessing a specific row
row = dataframe.iloc[5]   # 6th row (starts from 0)
print(row)
# Accessing a specific column/field of that row
print(row["Contact Name"])
print("\n")

# Looping through all rows of the dataframe
for index in range(len(dataframe)):
    row = dataframe.iloc[index]
    # Checking if the row satisfies some condition,
    # i.e. filtering
    town = "Chester"
    if row["City"] == town:
        print(row)
        # This prints rows where the value of the City
        # column is "Chester"
print("\n")

# Making a new, empty dataframe
columns = {
    "my column 1": [],  # Each of these is created with
    "my column 2": [],  # an empty list as the data, so the
    "my column 3": []   # dataframe will be created with just the column
                        # head, no data yet.
}
new_dataframe = pd.DataFrame(columns)
print(new_dataframe.head())
print("\n")


# Adding data to the new, empty dataframe
new_row = pd.DataFrame(
    [
    {
    "my column 1": "value",
    "my column 2": "value 2",
    "my column 3": "etc."
    }
    ]
    )
new_dataframe = pd.concat([new_dataframe, new_row])
# This data in new_row is appended to the end of new_dataframe
print(new_dataframe.head())
print("\n")




