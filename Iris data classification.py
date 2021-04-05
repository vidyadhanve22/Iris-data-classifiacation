#!/usr/bin/env python
# coding: utf-8

# In[12]:


import scipy as sp
import numpy as np
import pandas as pd
import matplotlib as mp
import sklearn as sk


# In[13]:


print('Numpy Version is: ' + np.__version__)
print('SciPy Version is: ' + sp.__version__)
print('Pandas Version is: ' + pd.__version__)
print('Matplotlib Version is: ' + mp.__version__)
print('SkLearn Version is: ' + sk.__version__)


# In[2]:


import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
label = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names = label)
#print(dataset)
dataset.head(10)


# In[4]:


iris = pd.DataFrame(data = dataset, columns = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'])
#iris.head()
#iris.tail()
iris.head(3)
#iris.tail(7)


# In[5]:


import matplotlib.pyplot as plt     #pyplot is the library that contains code to plot the graps or diagrams
import csv    #library to read the csv file directly
import sys
from pandas.plotting import scatter_matrix
import warnings
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

#the following are some basic summarization operations on the iris data set
print(dataset['class'].unique())
#type(dataset['petal-length'])
#type(dataset)

#to print the total number of objects belonging to each class
#print(dataset.groupby('class').size())

#now create data frame for each species or class and try to display them
setosa = dataset[dataset['class'] == 'Iris-setosa']
versicolor = dataset[dataset['class'] == 'Iris-versicolor']
virginica = dataset[dataset['class'] == 'Iris-virginica']
#setosa.head()


# In[6]:


from matplotlib import pyplot as plt

for n in range(0, 150):
    if dataset['class'][n] == 'Iris-setosa':
        plt.scatter(dataset['sepal-length'][n], dataset['sepal-width'][n], c = 'green')
        
    elif dataset['class'][n] == 'Iris-versicolor':
        plt.scatter(dataset['sepal-length'][n], dataset['sepal-width'][n], c = 'red')
        
    elif dataset['class'][n] == 'Iris-virginica':
        plt.scatter(dataset['sepal-length'][n], dataset['sepal-width'][n], c = 'blue')
    
plt.xlabel("sepal length (in cms)")
plt.ylabel("sepal width (in cms)")
plt.title("Sepal Comparision")
plt.show()


# In[ ]:




