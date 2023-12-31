# -*- coding: utf-8 -*-
"""Internship Task 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pbxN5ouF4L5eYds_Z6ZQwCWBOVGlGSNV

# 1. Write a Python code to Create a figure with 2x2 subplots.

---


#2. In the first subplot (top-left), plot a bar chart using the following data:
Categories: ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
Values: [23, 56, 41, 62, 19]

---


#3. In the second subplot (top-right), plot a histogram using the following data:
Data: [12, 17, 21, 18, 14, 13, 16, 9, 12, 15, 19, 11, 14, 16, 20, 18, 15, 13, 16, 11, 10]

---


#4. In the third subplot (bottom-left), plot a pie chart using the following data:
Labels: ['Apple', 'Banana', 'Orange', 'Mango']
Sizes: [30, 25, 15, 30]

---


#5. In the fourth subplot (bottom-right), plot a scatter plot using the following data:
X values: [1, 2, 3, 4, 5]
Y values: [2, 5, 3, 6, 4]

---


#6. Add appropriate titles and labels to each subplot.

---


#7. Adjust the spacing between subplots to avoid overlapping.

---
"""

import matplotlib.pyplot as plt

# Create a figure with 2x2 subplots
fig, axs = plt.subplots(2, 2)

import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Cat A', 'Cat B', 'Cat C', 'Cat D', 'Cat E']
values = [23, 56, 41, 62, 19]

# Data for histogram
data = [12, 17, 21, 18, 14, 13, 16, 9, 12, 15, 19, 11, 14, 16, 20, 18, 15, 13, 16, 11, 10]

# Data for pie chart
labels = ['Apple', 'Banana', 'Orange', 'Mango']
sizes = [30, 25, 15, 30]

# Data for scatter plot
x_values = [1, 2, 3, 4, 5]
y_values = [2, 5, 3, 6, 4]

# Create a figure with 2x2 subplots
fig, axs = plt.subplots(2, 2)

# Plot bar chart in the first subplot
axs[0, 0].bar(categories, values)
axs[0, 0].set_title('Bar Chart')
axs[0, 0].set_xlabel('Categories')
axs[0, 0].set_ylabel('Values')

# Plot histogram in the second subplot
axs[0, 1].hist(data, bins=5)
axs[0, 1].set_title('Histogram')
axs[0, 1].set_xlabel('Data')
axs[0, 1].set_ylabel('Frequency')

# Plot pie chart in the third subplot
axs[1, 0].pie(sizes, labels=labels, autopct='%1.1f%%')
axs[1, 0].set_title('Pie Chart')

# Plot scatter plot in the fourth subplot
axs[1, 1].scatter(x_values, y_values)
axs[1, 1].set_title('Scatter Plot')
axs[1, 1].set_xlabel('X values')
axs[1, 1].set_ylabel('Y values')

# Adjust spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()

"""Akula Zaheer Sha

---
a.zaheersha@gmail.com

---
9494333702

---
"""