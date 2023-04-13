#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
obj = pd.Series([4,7,-5,3])
obj


# In[ ]:





# In[2]:


obj.values


# In[3]:


obj.index


# In[5]:


obj2= pd.Series([4,7,-5,3], index=['a','b','c','d'])
obj2


# In[25]:


import pandas as pd
obj = pd.Series(['Ant','Bird','Cat','Bat','Rat','Fish','Rabbit','Cow'])
obj


# In[29]:


obj3= pd.Series(['Ant','Bird','Cat','Bat','Rat','Fish','Rabbit','Cow'], index=['1','2','3','4','5','6','7','8'])
opj3[2,4,6,8,] = 'Hen'
obj3


# In[30]:


s1=pd.Series([7.3,-2.5,3.4,1.5], index =['a','c','d','e'])


# In[31]:


s2=pd.Series([-2.1,3.6,-1.5,4,3.1], index=['a','c','e','f','g'])


# In[32]:


s1


# In[33]:


s2


# In[34]:


s1+s2


# In[35]:


sales=pd.Series([2,5,8,9])
sales


# # การดึงข้อมูลใน Series 

# In[37]:


sales[1]


# In[38]:


sales[2:]


# In[47]:


sales[1:3]


# In[39]:


sales*20


# In[40]:


sales.index


# In[41]:


sales.sum()


# In[42]:


sales.mean()


# In[43]:


sales.max()


# In[45]:


s = pd.Series([2,5,8,9], index=['a','b','c','d'])
s


# In[46]:


s['a']


# In[48]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[49]:


s.plot()


# In[50]:


s.plot(kind='bar')


# # ค่าของ Series กำหนด index เอง

# In[51]:


obj = pd.Series(range(4), index=['d','a','b','c'])
obj


# In[52]:


obj.sort_index()


# ## Series สามารถสร้าง index ซ้ำกันได้

# In[53]:


obj1 = pd.Series(range(5), index=['a','a','b','c','d'])
obj1


# # การสร้าง Data fame

# In[56]:


data ={'state': ['ohio','ohio','ohio','nevada','nevada','nevada'],
      'year':[2017,2018,2019,2020,2021,2022],
      'pop':[1.5,2.5,3.2,3.6,4.3,6.7]}
frame=pd.DataFrame(data)
frame


# ### การดึงข้อมูลที่อยู่ใน data frame มาแสดง

# In[57]:


pd.DataFrame(data,columns=['year','state','pop'])


# In[58]:


import numpy as np
df1 = pd.DataFrame(np.arange(9.).reshape(3,3),columns=list('bcd'),
                index=['Ohio','Texas','Colorado'])
df1


# In[60]:


df2 = pd.DataFrame(np.arange(12.).reshape(4,3),columns=list('bde'),
                index=['Ohio','Texas','Colorado','Oregon'])
df2


# #### ข้อ2

# In[99]:


data1 ={'A': [7,8]}


# In[100]:


frame1=pd.DataFrame(data)
frame1


# In[101]:


data2 ={'B': [9,10]}


# In[102]:


frame2=pd.DataFrame(data)
frame2


# In[104]:


import numpy as np
frame1 = pd.DataFrame(data1,index=['No1','No2'])
frame1


# In[106]:


import numpy as np
frame2 = pd.DataFrame(data2,index=['No3','No4'])
frame2


# In[107]:


df = pd.DataFrame([[1.4,np.nan],[7.1,-4.4],
                  [np.nan,np.nan],[0.75,-1.3]],
                 index=['a','b','c','d'],
                 columns=['one','two'])


# In[108]:


df


# In[109]:


df.sum()


# In[111]:


df = pd.read_csv('data/cars.csv')
df


# In[113]:


df[df.brand.str.contains('Lotus Europa|Toyota Corolla|Honda Civic')]


# ## groupby

# In[114]:


df.groupby('brand').sum().nsmallest(5,'carb')


# ### ข้อ3

# In[120]:


df = pd.read_csv('https://gist.github.com/omarish/5687264/raw/7e5c814ce6ef33e25d5259c1fe79463c190800d9/mpg.csv')


# In[121]:


df


# In[134]:


df.nsmallest(5,'acceleration')


# In[152]:


df ['value'] = df.acceleration*2


# In[154]:


df.head(5)


# In[156]:


df['trans'] = df['name'].str[0]
df.head()


# In[ ]:




