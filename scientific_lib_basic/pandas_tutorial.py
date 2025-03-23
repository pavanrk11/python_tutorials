# Pandas

# Pandas Series
# Pandas DataFrame
# How to create Pandas DataFrame?
# Understanding Pandas DataFrames
# Sorting Pandas DataFrames
# Indexing and Slicing Pandas Dataframes
# Subset DataFrames based on certain conditions
# How to fill/drop the null values?
# Lambda functions to modify dataframe
# Merge, Concatenate dataframes
# Grouping and aggregating

# basic two imports

import numpy as np
import pandas as pd

# Basic data structures in pandas

# Pandas provides two types of classes for handling data:

# Series: a one-dimensional labeled array holding data of any type such as integers,
# strings, Python objects etc. Pandas Series is built on top of NumPy array objects.

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s[0])

# In Pandas Series, we can mention index labels.
# If not provided, by default it will take default indexing(RangeIndex 0 to n-1 )

s1 = pd.Series([1, 3, 5, np.nan, 6, 8], index=['a','b','c','d','e','f'])
print(s1['a'])

# DataFrame: a two-dimensional data structure that holds data like a two-dimension array
# or a table with rows and columns. Each column in Pandas DataFrame is a Pandas Series.

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

dict_2 = {
            "A": 1.0,
            "B": pd.Timestamp("20130102"), # pd.Timestamp('2017-01-01T12') # pd.Timestamp(1513393355.5, unit='s') #pd.Timestamp(year=2017, month=1, day=1, hour=12)
            "C": pd.Series(1, index=list(range(4)), dtype="float32"),
            "D": np.array([3] * 4, dtype="int32"),
            "E": pd.Categorical(["test", "train", "test", "train"]),
            "F": "foo",
        }
df2 = pd.DataFrame(data = dict_2)
df2.dtypes

# NumPy arrays have one dtype for the entire array while pandas DataFrames have one dtype per column.
# Pandas and 3rd party libraries may extend NumPy’s type system to add support for custom arrays (see dtypes).

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
# To get the actual data inside a Index or Series, use the .array property
s.array
s.index.array

ser = pd.Series(pd.date_range("2000", periods=2, tz="CET"))
ser.to_numpy(dtype=object)

#df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])
#df.to_numpy()

long_series = pd.Series(np.random.randn(1000))
long_series.head()
long_series.tail()

index = pd.date_range("1/1/2000", periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])
df.head()
df.tail()
df.index
df.columns
df.to_numpy()
df[:2]
df.describe() # statistic summary
df.T


df3 = pd.DataFrame([1, 2, 3, 4, 5], index=[100, 29, 234, 1, 150], columns=['A'])
df3.sort_index()
df3.sort_index(ascending=False)

data = {
    'C': [1, 2, 3],
    'A': [4, 5, 6],
    'B': [7, 8, 9]
}
df = pd.DataFrame(data)
df.sort_values(by="B")
df.sort_index(axis=1)

# item selections

# Getitem ([])
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])
df["A"] #or  df.A
df[0:3] # slicing
df["20130102":"20130104"] # known index slicing

# by labels

df.loc[index[0]]
df.loc[:, ["A", "B"]] # allrows, specific columns
df.loc["20130102":"20130104", ["A", "B"]] # # specific sliced rows, specific columns

# grab a specific item by loc
df.loc[dates[0], "A"] # or
df.at[dates[0], "A"]  # faster

# by positions
df.iloc[3]
df.iloc[3:5, 0:2]
df.iloc[[1, 2, 4], [0, 2]]

# explicit row and column slicing
df.iloc[1:3, :]
df.iloc[:, 1:3]

# grab a specific item by iloc
df.iloc[:, 1:3]
df.iat[1, 1]

# boolean indexing

df[df["A"] > 0]
df[df > 0]

# add data and filter

#add
df4 = df.copy()
df4["E"] = ["one", "one", "two", "three", "four", "three"]
df4
#filter
df2[df2["E"].isin(["two", "four"])]
df4[df4["E"].isin(["two", "four"])]

dates = pd.date_range("20130101", periods=6)
df5 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
df5["F"] = s1


# setting values
df5.at[dates[0], "A"] = 0
df5.iat[0, 1] = 0
df5.loc[:, "D"] = np.array([5] * len(df5))

# missing data
# For NumPy data types, np.nan represents missing data. It is by default not included in computations.

df6 = df5.reindex(index=dates[0:4], columns=list(df5.columns) + ["E"])
df6.loc[dates[0] : dates[1], "E"] = 1
df6

df6.dropna(how="any") # drops any rows with missing data
df6.fillna(value=5) # fills missing data
pd.isna(df6)

## session 3

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

df.mean()
df.mean(axis=1)


df.agg(lambda x: np.mean(x) * 5.6)
df.agg({'A' : ['sum', 'min'], 'B' : ['min', 'max']})
df.transform(lambda x: x * 101.2)

s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts()

s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
s.str.lower() # one example many other string methods to follow

# merge
df = pd.DataFrame(np.random.randn(10, 4))
df

# break it into pieces
pieces = [df[:3], df[3:7], df[7:]]
pieces

pd.concat(pieces)

# join
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})


df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)
