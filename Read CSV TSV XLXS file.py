#!/usr/bin/env python
# coding: utf-8

# ### Read CSV file

# In[1]:


import pandas as pd
url = "https://github.com/prasertcbs/tutorial/raw/master/score.csv"
df = pd.read_csv(url)
df


# ### Read TSV file

# In[2]:


url = "https://github.com/prasertcbs/basic-dataset/raw/master/BaskinRobbins.tsv"
df = pd.read_table(url)
df


# ### Read Excel file เพิ่ม ?raw=true ท้ายลิงค์

# In[4]:


url = 'https://github.com/prasertcbs/tutorial/blob/master/BornInGeneration.xlsx?raw=true'
df = pd.read_excel(url)
df


# ### Read CSV file

# In[5]:


df = pd.read_csv('https://github.com/prasertcbs/tutorial/raw/master/score.csv')
df


# #### เอาแค่3colunm ใช้ df[['','','']] ใน '' ใส่ชื่อ colunm ที่ต้องการ

# In[6]:


df[['eng1','eng2','eng3']]


# ### ลดจำนวนข้อมูลduplicateที่ซ้ำreduce

# ## สร้าง data frame

# In[7]:


data = pd.DataFrame({'food':['Bacon','Pork','Bacon','Pastrami','Beef','Bacon','Pastrami','Ham','Lox'],
                    'onces':[4,3,12,6,7.5,8,3,5,6]})


# In[8]:


meat_to_animal = {'bacon':'pig','pork':'pig','pastrami':'cow','beef':'cow','ham':'pig','lox':'salmon'}


# In[9]:


lowercased = data['food'].str.lower()
lowercased


# In[11]:


data['animal']=lowercased.map(meat_to_animal)


# In[12]:


data


# In[13]:


df = pd.read_csv('https://github.com/prasertcbs/tutorial/raw/master/score.csv')
df


# In[17]:


df[['eng1','eng2','eng3']]


# ### การเลือกคอลัมน์ eng1, eng2, eng3 ข้ึนมาแสดง สามารถใช้“loc” มาใช้ในการระบุคอลัมน์ ที่ต้องการ [:,'eng1':'eng3']

# In[15]:


df.loc[:,'eng1':'eng3']


# In[16]:


df.loc[:,'math2':'eng3']


# ### การอ่านและรวมไฟล์CSV หลาย ๆ ไฟล์ก่อนการนำไปประมวลผล

# In[18]:


stocks=['bbl','ktb','scb']
dfs=[]
local_prefix='https://github.com/prasertcbs/tutorial/raw/master/eod/'
dfs=[pd.read_csv(f'{local_prefix}{s}.csv',parse_dates=True,index_col='Date')for s in stocks]


# In[19]:


type(dfs)


# In[20]:


type(local_prefix)


# In[21]:


type(stocks)


# In[22]:


dfs[2]


# In[23]:


dfs[1]


# In[25]:


dfs[0]


# In[26]:


df = pd.concat(dfs)
df


# In[27]:


df = pd.concat(dfs,keys=stocks)
df


# In[28]:


url = "https://github.com/prasertcbs/tutorial/raw/master/mtcars.csv"
df = pd.read_csv(url)
df


# In[29]:


df.index


# In[30]:


df.columns


# In[31]:


###drop แถวแบบชั่วคราว
df.drop(2)


# In[32]:


df


# In[33]:


## drop แถวถาวร
df.drop(2,inplace=True,axis=0)
df


# In[34]:


df


# In[35]:


###drop คอลัมน์แบบชั่วคราว
df.drop(['mpg'],axis=1)


# In[36]:


df


# In[37]:


## drop คอลัมน์ถาวร
df.drop(['mpg'],axis=1,inplace=True)


# In[38]:


df


# In[39]:


df


# In[40]:


from datetime import datetime
datetime(year=2023,month=2,day=1)


# In[41]:


from dateutil import parser
date= parser.parse("2nd of Feb, 2023")
date


# In[42]:


from datetime import datetime
dt1 = datetime(year=2020,month=8,day=22)
dt2 = datetime(year=2020,month=8,day=20)
diff = dt1-dt2


# In[43]:


print("Difference day:",diff.days,"วัน")
print("Difference hours:",diff.total_seconds()/3600,"ชั่วโมง")


# In[44]:


import numpy as np
date = np.array('2023-02-01',dtype=np.datetime64)
date


# In[45]:


date+np.arange(12)


# In[46]:


from datetime import date


# In[47]:


daynow = date.today()
print(daynow)


# In[48]:


current_dateTime = datetime.today().strftime('%Y-%m-%d')

print(current_dateTime)


# In[49]:


now = np.array(current_dateTime,dtype=np.datetime64)
now


# In[50]:


now+np.arange(12)


# ## เฉลย asm

# ##### จงสร้าง data frame ของข้อมูล 2 ชุด ดังรูป แล้วพิจารณาว่า row ไหนบ้างที่ซ้ำซ้อนกัน

# In[51]:


data = pd.DataFrame({'k1':['one','two']*3+['two'],
                    'k2':[1,1,2,3,3,4,4]})
data


# In[52]:


data.duplicated()


# ##### จงหาว่าวันที่ 20 ส.ค. 62 ถึงวันที่ 22 ส.ค.62 มีจำนวนห่างกันกี่วัน/กี่ชั่วโมง

# In[71]:


from datetime import date
d1 = date(2019,8,20)
d2 = date(2019,8,22)
d_ago = d2-d1
print("มีจำนวนห่างกัน",d_ago.days,"วัน")
print(d_ago.days*24,"ชั่วโมง")


# ##### จงแสดงข้อมูลของวันที่ปัจจุบัน และ วันถัดมาอีก 10 วัน นับจากวันปัจจุบัน

# In[74]:


import numpy as np
from datetime import date


# In[75]:


date = np.array(datetime.datetime.now(),dtype = np.datetime64)
date + np.arange(10)


# In[ ]:




