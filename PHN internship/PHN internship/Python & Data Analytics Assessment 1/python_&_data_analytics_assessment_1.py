# -*- coding: utf-8 -*-
"""Python & Data Analytics Assessment 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sOD_OxebHPTJahztI3brp5A-BQdzuk--

> Python & Data Analytics Assessment 1

1.   Prepare the sample csv file for car model and their specification, the column names would be
a. Company Name
b. Model Name
c. Fuel Type (For e.g. Petrol, Gas, Diesel, EV)
d. Body Style (for e.g. Hatchback, Sedan, SUV)
e. Car Length.

---

2. Prepare the sample excel file for the car prizing and loan amount, the column names would be
a. Company Name
b. Model Name
c. On road pricing
d. Loan amount
e. Monthly EMI
f. Interest Rate
g. Monthly Principal
h. Monthly Interest

---


3. Write the code to read the csv file and the excel file and convert them into the Data frame.

---


4. Merge the two Data frame on the basis of primary key

---


5. Fill the “NA” values in the merged data frame

---


6. Iterate over the merged Data frame and add the GST value in the “On road pricing” column

---

Importing Libraries
"""

import pandas as pd

""" Uploading CSV data into online notebook"""

from google.colab import files        #uploading data into online notebook
uploaded = files.upload()

"""Read the CSV file"""

# Read the CSV file
df_car_model  = pd.read_csv("car_model_sample.csv")

"""Uploading excel data into online notebook"""

from google.colab import files        #uploading data into online notebook
uploaded = files.upload()

"""**Write the code to read the csv file and the excel file and convert them into the Data frame.**

---

Read the excel file
"""

# Read the excel file
df_car_pricing  = pd.read_excel("carprizing_loneamount.xlsx")

"""Print the first 5 and last 5 rows of the CSV DataFrame"""

# Print the first 5 and last 5 rows of the CSV DataFrame
print("CSV DataFrame:")
print(df_car_model.head())
print(" ")
print(df_car_model.tail())

"""Print the first 5 and last 5 rows of the Excel DataFrame"""

# Print the first 5 and last 5 rows of the Excel DataFrame
print("Excel DataFrame:")
print(df_car_pricing .head())
print(" ")
print(df_car_pricing .tail())

"""**Merge the two Data frame on the basis of primary key** 
---


"""

# Merge the two DataFrames based on the "Model Name" column
merged_df = pd.merge(df_car_model, df_car_pricing, on="Model Name")

# Print the merged DataFrame
print(merged_df.head())

"""**Fill the “NA” values in the merged data frame**

 ---
"""

# Fill the "NA" values in the merged DataFrame with zeros
merged_df.fillna(0, inplace=True)

# Print the merged DataFrame with "NA" values filled
print(merged_df.head())

"""**Iterate over the merged Data frame and add the GST value in the “On road pricing” column**

---


"""

# Convert the "On Road Pricing (in INR)" column to a numeric data type
merged_df["On Road Pricing (in INR)"] = pd.to_numeric(merged_df["On Road Pricing (in INR)"], errors="coerce")

# Iterate over the merged DataFrame and add the GST value to the "On road pricing" column
for index, row in merged_df.iterrows():
    merged_df.at[index, "On Road Pricing (in INR)"] += merged_df.at[index, "On Road Pricing (in INR)"] * 0.12

print(merged_df.head())

"""**By Akulk Zaheer Sha**


**a.zaheersha@gmail.com**

**9494333702**
"""