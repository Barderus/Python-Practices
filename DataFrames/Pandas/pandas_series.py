import pandas as pd

"""
    Pandas Series
        A pandas series is like a column in a table. One-dimensional array holding any data type
"""

a = [1, 7, 2, 10, 83, 99, 65, 0]
my_series = pd.Series(a)
print(my_series)
print()

"""
    Labels
        The default label is the index number of each value. Starting from 0.
        To create your own label you can use the index argument.
"""
my_series = pd.Series(a, index=["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8"])
print(my_series)

# Accessing value by the label
print("\n", my_series["Day 4"])

"""
    Key/Value Objects as Series
        You can create key/value objects, like a dictionary, when creating a series
"""
print()
grades = {"Essay 1": 98, "Response": 91, "Critic": 89, "Research Paper": 100}
grades_series = pd.Series(grades)
print(grades_series)
