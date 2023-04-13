#!/usr/bin/env python
# coding: utf-8

# In[144]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree


# In[152]:


zoo_data=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/zoo/zoo.data')


# In[153]:


zoo_data


# In[154]:


X=zoo_data.values[:,1:18]
Y=zoo_data.values[:,0]


# In[155]:


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=100)


# In[156]:


clf_gini = DecisionTreeClassifier(criterion = "gini",random_state=100,max_depth = 3, min_samples_leaf=10)
clf_gini.fit(X_train,Y_train)


# In[157]:


clf_gini.predict([[1,0,0,1,0,0,0,1,1,1,0,0,4,1,0,1,1]])


# In[158]:


y_predict=clf_gini.predict(X_test)


# In[159]:


y_predict


# In[160]:


print("accuract",accuracy_score(Y_test,y_predict)*100)


# In[ ]:





# In[ ]:




