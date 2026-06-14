# Pandas
# Pandas is an open source, high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Pandas adds data structures and tools designed to work with table-like data which is Series and Data Frames. Pandas provides tools for data manipulation:

# reshaping
# merging
# sorting
# slicing
# aggregation
# imputation. If you are using anaconda, you do not have install pandas.

import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np

import pandas as pd

# 1. DataFrame

# DataFrame = tabel.
# Ada baris dan kolom.
data = {
    'nama': ['Andi', 'Budi', 'Citra', 'Dewi'],
    'umur': [20, 21, 19, 22],
    'nilai': [80, 75, 90, 85]
}

df = pd.DataFrame(data)

print("="*20)
print(df)


# Creating Pandas Series with custom index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)
print("="*20)
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

print("="*20)
# Creating Pandas Series from a Dictionary
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
print(s)

print("="*20)
s = pd.Series(10, index = [1, 2, 3])
print(s)

# Creating DataFrames from List of Lists

data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

# Creating DataFrame Using Dictionary
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

# Creating DataFrames from a List of Dictionaries
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)

# Reading CSV File Using Pandas
# To download the CSV file, what is needed in this example, console/command line is enough:
# curl -O https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv


import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)
print("="*20)
print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method
print("="*20)
print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method
print("="*20)
print(df.shape) # as you can see 10000 rows and three columns
print(df.columns)
print("="*20)
heights = df['Height'] # this is now a series
print(heights)

print("="*20)

weights = df['Weight'] # this is now a series
print(len(heights) == len(weights))
print("="*20)
print(heights.describe()) # give statistical information about height data
print("="*20)
import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)
print("="*20)
weights = [74, 78, 69]
df['Weight'] = weights
print(df)

print("="*20)

heights = [173, 175, 169]
df['Height'] = heights
print(df)

# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi

bmi = calculate_bmi()
df['BMI'] = bmi
print(df)

# Formatting DataFrame columns
# The BMI column values of the DataFrame are float with many significant digits after decimal. Let's change it to one significant digit after point.
df['BMI'] = round(df['BMI'], 1)
print(df)

birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2020, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
