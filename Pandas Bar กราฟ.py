#!/usr/bin/env python
# coding: utf-8

# # Pandas

# In[5]:


import pandas as pd
obj = pd.Series([4,7,-5,3])
obj


# In[6]:


obj.values


# In[7]:


obj.index


# In[8]:


obj2= pd.Series([4,7,-5,3], index=['a','b','c','d'])
obj2


# In[9]:


import pandas as pd
obj = pd.Series(['Ant','Bird','Cat','Bat','Rat','Fish','Rabbit','Cow'])
obj


# ## ข้อ 1

# In[10]:


opj3= pd.Series(['ant','bird','cat','bat','rat','fish','robbit','cow'],index=[1,2,3,4,5,6,7,8])
opj3[2,4,6,8,] = "Hen"


# In[11]:


opj3


# In[12]:


s1=pd.Series([7.3,-2.5,3.4,1.5], index =['a','c','d','e'])


# In[13]:


s2=pd.Series([-2.1,3.6,-1.5,4,3.1], index=['a','c','e','f','g'])


# In[14]:


s1


# In[15]:


s2


# In[16]:


s1+s2


# In[17]:


sales=pd.Series([2,5,8,9])
sales


# # การดึงข้อมูลใน Series 

# ##   เริ่มต้นที่ index ตำแหน่งที่ 1 ตัวเดียว

# In[18]:


sales[1]


# ##  เริ่มต้นที่ index ตำแหน่งที่ 2 และมี (:) แปลว่าต่อไปถึงตัวสุดท้าย

# In[19]:


sales[2:]


# ##  เริ่มต้นที่ index ตำแหน่งที่ 1 และมี (:) แปลว่าต่อไปถึง index ตำแหน่งที่ 3

# In[20]:


sales[1:3]


# ### sales ทุกตัวที่มีใน series * 20

# In[21]:


sales*20


# In[22]:


sales.index


# In[23]:


sales.sum()


# In[24]:


sales.mean()


# In[25]:


sales.max()


# นำข้อมูล sales มาplot กราฟ โดยสร้างตัวแปลใหม่แต่ใช้ข้อมูลเดิม

# In[26]:


s = pd.Series([2,5,8,9], index=['a','b','c','d'])
s


# In[27]:


s['a']


# กราฟเส้น

# In[28]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[29]:


s.plot()


# # Bar กราฟ

# In[30]:


s.plot(kind='bar')


# # ค่าของ Series กำหนด index เอง

# In[31]:


obj = pd.Series(range(4), index=['d','a','b','c'])
obj


# In[32]:


obj.sort_index()


# ## Series สามารถสร้าง index ซ้ำกันได้

# In[33]:


obj1 = pd.Series(range(5), index=['a','a','b','c','d'])
obj1


# # การสร้าง Data fame

# In[34]:


data ={'state': ['ohio','ohio','ohio','nevada','nevada','nevada'],
      'year':[2017,2018,2019,2020,2021,2022],
      'pop':[1.5,2.5,3.2,3.6,4.3,6.7]}
frame=pd.DataFrame(data)
frame


# ### การดึงข้อมูลที่อยู่ใน data frame มาแสดง

# In[35]:


pd.DataFrame(data,columns=['year','state','pop'])


# In[36]:


import numpy as np
df1 = pd.DataFrame(np.arange(9.).reshape(3,3),columns=list('bcd'),
                index=['Ohio','Texas','Colorado'])
df1


# In[37]:


df2 = pd.DataFrame(np.arange(12.).reshape(4,3),columns=list('bde'),
                index=['Ohio','Texas','Colorado','Oregon'])
df2


# ## ข้อ2

# In[38]:


data1 ={'A': [7,8]}


# In[39]:


frame1=pd.DataFrame(data)
frame1


# In[40]:


data2 ={'B': [9,10]}


# In[41]:


frame2=pd.DataFrame(data)
frame2


# In[42]:


import numpy as np
frame1 = pd.DataFrame(data1,index=['No1','No2'])
frame1


# In[43]:


import numpy as np
frame2 = pd.DataFrame(data2,index=['No3','No4'])
frame2


# In[44]:


df = pd.DataFrame([[1.4,np.nan],[7.1,-4.4],
                  [np.nan,np.nan],[0.75,-1.3]],
                 index=['a','b','c','d'],
                 columns=['one','two'])


# In[45]:


df


# In[46]:


df.sum()


# In[47]:


df.mean()


# In[48]:


df = pd.read_csv('data/cars.csv')
df


# In[49]:


df[df.brand.str.contains('Lotus Europa|Toyota Corolla|Honda Civic')]


# In[50]:


df.groupby('brand').sum().nsmallest(5,'carb')


# ### ข้อ3

# In[51]:


df = pd.read_csv('https://gist.github.com/omarish/5687264/raw/7e5c814ce6ef33e25d5259c1fe79463c190800d9/mpg.csv')


# In[52]:


df


# In[53]:


df.nsmallest(5,'acceleration')


# #### นำค่า acceleration*2  แลำกำหนดค่านี้เป็น value

# In[54]:


df ['value'] = df.acceleration*2


# In[55]:


df.head(5)


# In[56]:


df['trans'] = df['name'].str[0]
df.head()


# In[57]:


df['value']=df['value'].round(1)
df


# In[ ]:




