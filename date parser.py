#!/usr/bin/env python
# coding: utf-8

# ### asm1 วันที่ 2 กันยายน ตรงกับวันอะไร ในปฏิทิน

# In[7]:


from dateutil import parser
date = parser.parse("2nd of September,2019")
date
date.strftime('%A')


# In[8]:


from datetime import datetime
stamp = datetime(2019,7,2)
str(stamp)


# ##### method ในการกำหนด format Date (strf)

# In[9]:


stamp.strftime('%Y-%m-%d')


# ### asm2 

# In[10]:


datestrs=['9/9/2019','9/16/2019']


# In[11]:


[datetime.strptime(x,"%m/%d/%Y")for x in datestrs]


# In[12]:


import pandas as pd
import numpy  as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[13]:


df = pd.read_csv('https://github.com/prasertcbs/tutorial/raw/master/staff.csv',
                 index_col='empID',
                 thousands=',',parse_dates=['dob','join_date'])


# In[14]:


df


# In[15]:


df.info()


# ### หาค่า min max ในคอลัมน์ salary

# In[16]:


min_value=df['salary'].min()
max_value=df['salary'].max()
print(min_value)
print(max_value)


# In[20]:


bins = [0,15000,30000,50000,80000,np.inf]
bins


# In[21]:


labels=['0-15000','15001-30000','30001-50000','50001-80000','80000+']


# In[22]:


df['bins']=pd.cut(df['salary'],bins=bins,labels=labels,include_lowest=True)
df.sort_values(by='bins')


# #### การหาความถี่ของข้อมูล

# In[23]:


df.bins.hist(grid=False)


# In[24]:


df.bins.hist(grid=True)


# In[28]:


import matplotlib.pyplot as plt
plt.hist(df['bins'], bins=5)


# ###### datatranformation

# In[30]:


url = 'https://github.com/prasertcbs/tutorial/raw/master/mpg.csv'
df = pd.read_csv(url)
df


# In[31]:


df [:10]


# In[32]:


x_bar=df.cty.mean()
sd=df.cty.std()
print(f'mean={x_bar},SD={sd}')


# In[33]:


(18-x_bar)/sd


# In[34]:


(df.cty-x_bar)/sd


# In[35]:


df['z_cty']=(df.cty-x_bar)/sd


# In[36]:


df.head()


# In[37]:


df.z_cty.mean()


# In[38]:


df.z_cty.std()


# In[39]:


url='https://github.com/prasertcbs/tutorial/raw/master/mtcars.csv'
df = pd.read_csv(url)
df


# In[40]:


df.shape


# In[41]:


train_ratio=.7
df_train=df[:int(df.shape[0]*train_ratio)]
df_train


# In[42]:


df_train.shape


# In[43]:


df_test= df[int(df.shape[0]*train_ratio):]
df_test


# In[44]:


df_test.shape


# In[45]:


url='https://github.com/prasertcbs/tutorial/raw/master/mpg.csv'
df = pd.read_csv(url)
df


# In[46]:


df.shape


# In[47]:


train_ratio=.6
df_train=df[:int(df.shape[0]*train_ratio)]
df_train


# In[48]:


df_train.shape


# In[49]:


df_test= df[int(df.shape[0]*train_ratio):]
df_test


# In[50]:


df_test.shape


# In[51]:


url='https://github.com/prasertcbs/tutorial/raw/master/msleep.csv'
df = pd.read_csv(url,nrows=10)
df


# #### การสุ่มตามสัดส่วน

# In[52]:


df_train=df.sample(frac=train_ratio)
df_train


# In[53]:


df_train.index


# In[54]:


df.index.isin(df_train.index)


# In[55]:


~df.index.isin(df_train.index)


# In[56]:


~df.index.isin(df_train.index)


# In[57]:


df_test=df[~df.index.isin(df_train.index)]
df_test


# In[58]:


url='https://github.com/prasertcbs/tutorial/raw/master/mpg.csv'
df = pd.read_csv(url,nrows=20)
df


# In[59]:


train_ratio=.6


# In[60]:


df_train=df.sample(frac=train_ratio)
df_train


# In[61]:


df_test=df[~df.index.isin(df_train.index)]
df_test


# In[ ]:




