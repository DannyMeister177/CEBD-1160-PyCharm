import pandas as pd

# 2. Load the insurance.csv in a DataFrame using pandas. Explore the dataset using functions like to_string(), columns,
# index, dtypes, shape, info() and describe(). Use this DataFrame for the following exercises.
df = pd.read_csv('winter2020-code/4-python-advanced-notebook/data/insurance.csv', header=0)

print(df.to_string())
print()
print(df.columns)
print()
print(df.index)
print()
print(df.dtypes)
print()
print(df.shape)
print()
print(df.info())
print()
print(df.describe())
print()
