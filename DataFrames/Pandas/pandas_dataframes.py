import pandas as pd

"""
    DataFrames
        Datasets in Pandas are multi-dimensional tables, called DataFrames.
        Series is like a column, DataFrames is the whole table
"""

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
my_df = pd.DataFrame(data, index=["Activity 1", "Activity 2", "Activity 3"])
print(my_df)

"""
    Locate Row
        Pandas use the loc attribute to return one or more specified row(s)
"""
print()
print(my_df.loc["Activity 1"])

# Return row 0 and 1
print()
print(my_df.loc[["Activity 1", "Activity 2"]])
