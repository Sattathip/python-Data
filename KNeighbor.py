#!/usr/bin/env python
# coding: utf-8

# In[3]:


import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns; sns.set()
sns.pairplot(iris,hue='species',size=1.5);


# In[6]:


x_iris = iris.drop('species',axis=1)
x_iris.shape


# In[7]:


y_iris = iris['species']
y_iris.shape


# In[8]:


from sklearn.linear_model import LinearRegression


# In[9]:


model =  LinearRegression(fit_intercept = True)
model


# In[10]:


import numpy as np
import matplotlib.pyplot as plt
rng = np.random.RandomState(42)
x = 5* rng.rand(100)
y = 2*rng.rand(100)
x=x[:,np.newaxis]
x.shape


# In[11]:


model.fit(x,y)


# In[12]:


model.coef_


# In[13]:


model.intercept_


# In[14]:


xfit=np.linspace(-1,1)


# In[15]:


xfit=xfit[:,np.newaxis]


# In[16]:


yfit=model.predict(xfit)


# In[17]:


plt.scatter(x,y)
plt.plot(xfit,yfit)


# In[24]:


from sklearn.datasets import load_digits


# In[26]:


digits = load_digits()
digits.data.shape


# In[27]:


plt.gray()
plt.matshow(digits.images[0])
plt.show()


# In[28]:


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
iris = datasets.load_iris()
iris.data.shape,iris.target.shape


# In[29]:


x_train,x_test,ytrain,ytest=train_test_split(iris.data,iris.target,test_size=0.4,random_state=0)


# In[33]:


from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(x_train, ytrain)
y_model = model.predict(x_test)


# In[34]:


from  sklearn.metrics import accuracy_score
accuracy_score(ytest,y_model)


# In[35]:


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
digits = datasets.load_digits() 
digits.data.shape,digits.target.shape


# In[36]:


x_train,x_test,ytrain,ytest=train_test_split(digits.data,digits.target,test_size=0.4,random_state=0)


# In[37]:


from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(x_train, ytrain)
y_model = model.predict(x_test)


# In[38]:


from  sklearn.metrics import accuracy_score
accuracy_score(ytest,y_model)


# In[99]:


##knn
from sklearn.datasets import load_iris


# In[100]:


iris=load_iris()


# In[101]:


type(iris)


# In[102]:


iris.keys()


# In[103]:


iris.data


# In[104]:


iris.data.shape


# In[105]:


from sklearn import neighbors,datasets


# In[106]:


iris = datasets.load_iris()


# In[107]:


x,y = iris.data,iris.target


# In[109]:


knn= neighbors.KNeighborsClassifier(n_neighbors=1)


# In[110]:


knn.fit(x,y)


# In[111]:


print (iris.target_names[knn.predict([[1,1,1,1]])])


# In[112]:


##knn
from sklearn.datasets import load_digits


# In[113]:


digits=load_digits()


# In[114]:


type(digits)


# In[115]:


digits.keys()


# In[116]:


digits.data


# In[117]:


digits.data.shape


# In[118]:


from sklearn import neighbors,datasets


# In[119]:


digits = datasets.load_digits()


# In[120]:


x,y = digits.data,digits.target


# In[121]:


knn= neighbors.KNeighborsClassifier(n_neighbors=1)


# In[122]:


knn.fit(x,y)


# In[124]:


print (digits.target_names[knn.predict([[1,2,3,4,5,6,7,8,9,10,11,12,12,1,23,23,22,12,12,23,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,33,3,3,3,3,3,3,3,3,3,3,]])])


# In[ ]:




