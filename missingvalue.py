#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# #### อ่านไฟล์ .csv ผ่าน url (pd.read_csv)

# In[3]:


df = pd.read_csv('https://gist.github.com/omarish/5687264/raw/7e5c814ce6ef33e25d5259c1fe79463c190800d9/mpg.csv')


# ### แสดง 5 แถวแรกหรือหัวของตารางนี้ (head)

# In[4]:


df.head()


# ### แสดง 5 แถวสุดท้ายหรือหางของตารางนี้ (tail)

# In[5]:


df.tail()


# ### แสดงแถวกับ colump ทั้งหมด

# In[6]:


df.shape


# #### แสดงชื่อรถและจำนวนรถทั้งหมดที่มีว่ายี่ห้อไหนมีกี่คัน name.value_counts()

# In[7]:


df.name.value_counts()


# ### หาค่าความสำพัพธ์ เป็น + หรือ - ได้

# In[8]:


df.corr()


# #### อ่านไฟล์ .csv ผ่าน floder ในเครื่อง (pd.read_csv)

# In[9]:


df = pd.read_csv('data/provinces.csv')
df


# ### แสดง 5 แถวแรกหรือหัวของตารางนี้ (head)

# In[10]:


df.head()


# ### แสดง 5 แถวสุดท้ายหรือหางของตารางนี้ (tail)

# In[11]:


df.tail()


# ### การ่สุ่มเลือก random แต่ละคนจะได้ไม่เหมือนกัน สุ่มตามจำนวนสัดส่วน (sample)

# In[12]:


df.sample()


# ### การ่สุ่มเลือก random ว่าอยากได้กี่แถว ให้กำหนดค่า n = ***  ตัวอย่างนี้เช่น(N=5)ก็จะแสดง5แถว

# In[13]:


df.sample(n=5)


# #### ต้องการแค่ 10% จากจำนวนแถวทั้งหมด (frac=.1) .1=10% .2=20%

# In[14]:


df.sample(frac=.1)


# #### สุ่มเอาเฉพาะ attribute ที่ชื่อ Province   กำหนดค่า n = ***  ตัวอย่างนี้เช่น(N=5)ก็จะแสดง5แถวเฉพาะ attribute ที่ชื่อ Province 

# In[15]:


df.Province.sample(n=5)


# # asm 1 concat คือฟังก์ชั่นที่อยู่ในไลบารี่ pd ใช้รวมหรือต่อฟังก์ชั่น

# In[16]:


## เอาส่วนหัว 5 บรรทัดกับส่วนท้าย 5 บรรทัดมาแสดงต่อกัน
pd.concat([df.head(), df.tail()])


# In[17]:


## หรือแบบนี้ก็ได้มี axis หรือไม่มีก็ได้
pd.concat([df.head(), df.tail()],axis=0)


# #### อ่านไฟล์ .tsv ผ่าน floder ในเครื่อง (pd.read_table)

# In[18]:


df = pd.read_table('https://github.com/prasertcbs/tutorial/raw/master/employee.tsv')


# ### แสดง 5 แถวแรกหรือหัวของตารางนี้ (head)

# In[19]:


df.head()


# In[20]:


df.info()


# ## เปลี่ยนจาก วดป เป็น ปดว เพิ่มคำสั่ง parse_date=['dob']

# In[21]:


df = pd.read_table('https://github.com/prasertcbs/tutorial/raw/master/employee.tsv',parse_dates=['dob'])


# ### แสดง 5 แถวแรกหรือหัวของตารางนี้ (head)

# In[22]:


df.head()


# #### หาค่าเฉลี่ยของ attribute ชือ salary

# In[23]:


df.salary.mean()


# #### หาผลรวมของ attribute ชือ salary

# In[24]:


df.salary.sum()


# ### นับจำนวนข้อมูลของ attribute ชือ occupation.value_counts()

# In[25]:


df.occupation.value_counts()


# ### เปลี่ยนตัวอักษรจาก เล็กเป็น ใหญ่ของ attribute ชือ occupation .str.upper()

# In[26]:


df.occupation.str.upper()


# ### หาวันที่นี้เวลานี้

# In[27]:


pd.to_datetime('today')


# ### หาปีนี้

# In[28]:


pd.to_datetime('today').year


# ### หาเดือนนี้

# In[29]:


pd.to_datetime('today').month


# ### แสดงจำนวนพนักงานที่มีบ้าน

# In[30]:


df.own_house.value_counts()


# ### การหาค่าสถิติทั้งหมด mean-std-min-max เบื้องต้น

# In[31]:


df.describe()


# # asm2

# ### เอาค่า dob มาเ็บไว้ใน Attribute ที่ชื่อ age

# In[32]:


df ['age'] = df.dob
df


# ### กำหนดค่าให้ attribute age = ปีปัจจุบันเก็บไว้ในตัวแปรyear

# In[33]:


df.age = pd.to_datetime('today').year


# ### ตัวแปร year = attribute dob เก็บไว้ใน ปีปัจจุบัน

# In[34]:


year = df ['dob'].dt.year


# ### จะได้ age = ปีนี้-yearที่เป็นattribute dob

# In[35]:


age = pd.to_datetime('today').year-year


# ### เอาค่า age ที่ลบเสร็จมาเก็บไว้ใน attribute age

# In[36]:


df['age']=age


# In[37]:


df


# ### หาค่าเฉลี่ยของอายุ df.age.mean()

# In[38]:


df.age.mean()


# ## วิธีของ อ.

# In[39]:


df['age']=pd.to_datetime('today').year-df.dob.dt.year


# In[40]:


df


# In[41]:


df.age.mean()


# # การจัดการข้อมูล หรือ missing value

# #### ignore the tuple / dopping

# In[42]:


import numpy as np


# ### สร้างdataframeเอง

# In[43]:


user_data = {'first_name':['sammy','jesse',np.nan,'jame'],
            'last_name':['S','O',np.nan,'M'],
            'online':[True,np.nan,False,True],  
            'followers':[500,450,300,np.nan]}


# In[44]:


df = pd.DataFrame(user_data,columns=['first_name','last_name','online','followers'])
df


# In[45]:


df_drop_missing = df.dropna()
df_drop_missing


# In[46]:


df_fill = df.fillna(0)
df_fill


# #### atribute mean

# # asm3

# In[49]:


import pandas as pd
df = pd.read_csv('data/Iris1.csv')


# In[50]:


df


# In[51]:


df['SpeciesName'].fillna(value ='unknown',inplace=True)
df.head(n=10)


# In[52]:


df.PetalWidth.mean()


# In[53]:


df['PetalWidth'].fillna(df.PetalWidth.mean(),inplace=True)
df.head(n=30)


# ## เฉลย ของ อ.

# In[54]:


import pandas as pd
df = pd.read_csv('data/Iris1.csv')


# In[55]:


df


# In[ ]:




