#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree


# In[16]:


balance_data=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer.data')


# In[17]:


balance_data


# In[18]:


print ("dataset lenght:",len(balance_data))


# In[19]:


print ("dataset shape:",balance_data.shape)


# In[20]:


print ("dataset shape:",balance_data.head())


# In[24]:


X=balance_data.values[:,1:10]
Y=balance_data.values[:,0]


# In[25]:


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=5,random_state=100)


# In[26]:


clf_gini = DecisionTreeClassifier(criterion = "gini",random_state=100,max_depth = 3, min_samples_leaf=5)
clf_gini.fit(X_train,Y_train)


# In[ ]:




