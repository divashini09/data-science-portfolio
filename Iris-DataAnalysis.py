#!/usr/bin/env python
# coding: utf-8

# ### Exploratory Data Analysis of the Iris Dataset
# This notebook performs an exploratory data analysis on the Iris dataset, which includes measurements for three species of iris flowers: Setosa, Versicolor, and Virginica.
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# #### Purpose:
# - Pandas is used for data manipulation and analysis.
# - NumPy is useful for numerical operations.
# - Matplotlib is a plotting library for creating static, animated, and interactive visualizations.
# - Seaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive statistical graphics.
# 
# #### Result: 
# You can now use these libraries to work with your dataset and create visualizations.

# In[2]:


# Load the dataset
iris = sns.load_dataset('iris')


# #### Purpose: 
# Loading the Iris dataset from Seaborn. This dataset contains measurements for three species of iris flowers: Setosa, Versicolor, and Virginica.
# 
# #### Result: 
# The variable iris now holds a DataFrame containing the dataset, which you can manipulate and analyze.

# In[3]:


# Display the first few rows to understand its structure
iris.head()


# #### Purpose: 
# Displays the first five rows of the dataset, providing a quick overview of its structure.
# 
# #### Result: 
# You will see columns for sepal length, sepal width, petal length, petal width, and species. This helps you understand what data you’re working with.

# In[4]:


# Get basic information
iris.info()


# #### Purpose: 
# Provides information about the DataFrame, including the number of non-null entries, data types, and memory usage.
# 
# #### Result: 
# You can check if there are any missing values (non-null counts), which is crucial for data quality.

# In[5]:


# Get descriptive statistics
iris.describe()


# #### Purpose: 
# Generates descriptive statistics for numeric columns, including count, mean, standard deviation, min, max, and quartiles.
# 
# #### Result: 
# This gives you an understanding of the central tendency and dispersion of the features in the dataset. For example, it shows that Setosa tends to have smaller petal lengths than the other species.

# In[6]:


# Pairplot of the Iris dataset
sns.pairplot(iris, hue='species')
plt.title('Pairplot of Iris Dataset')
plt.show()


# #### Purpose: 
# Creates a matrix of scatterplots for each pair of features, colored by species.
# 
# #### Result: 
# Visualizes relationships between all pairs of features, revealing that different species have distinct clusters in the feature space. For instance, Setosa is easily separable from Versicolor and Virginica.

# In[7]:


# Boxplot for sepal length
plt.figure(figsize=(10, 6))
sns.boxplot(x='species', y='sepal_length', data=iris)
plt.title('Boxplot of Sepal Length by Species')
plt.show()


# #### Purpose: 
# Shows the distribution of sepal lengths for each species using box plots.
# 
# #### Result: 
# Provides insights into the central tendency and variability of sepal lengths for each species. You can see which species has the longest or shortest sepal lengths.

# In[8]:


# Violin plot for petal width
plt.figure(figsize=(10, 6))
sns.violinplot(x='species', y='petal_width', data=iris)
plt.title('Violin Plot of Petal Width by Species')
plt.show()


# #### Purpose:
# Combines a box plot with a density plot, showing the distribution of petal widths across species.
# 
# #### Result: 
# This plot highlights the distribution shape and density, making it clear how petal widths vary among the species.

# In[9]:


# Correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(iris.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Iris Dataset')
plt.show()


# #### Purpose: 
# Computes the correlation between features and visualizes it using a heatmap.
# 
# #### Result: 
# You’ll see a matrix showing correlation coefficients (values between -1 and 1). A strong positive correlation (close to 1) between petal length and petal width indicates that as one increases, the other tends to increase as well.

# ### Conclusions
# - The Iris dataset consists of three species with distinct measurements.
# - There are clear differences in sepal and petal measurements between species.
# - Sepal length and petal length have a strong positive correlation.
# 

# In[ ]:




