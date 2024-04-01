import pandas as pd
import numpy as np
import matplotlib as mpl
import sklearn as skl

# Reading and cleaning dataset 
url = "C:\\Users\\User\\Desktop\\ML Projects\\Breast Cancer Cluster Analysis\\Breast-Cancer-Cluster-Analysis\\data.csv"
data = pd.read_csv(url)
# print(data)
# print(data.head())

# Removing "id" and "Unnamed: 32" columns
data = data.drop('id', axis = 1)
data = data.drop('Unnamed: 32', axis = 1)
# Changing "M" (Malignant) to 1 and "B" (Benign) to 0
data['diagnosis'] = data['diagnosis'].map({'M': 1,'B': 0}) 
