#!/usr/bin/env python
# coding: utf-8

# 1.ผลลัพธ์a= 25 <class 'int'>
# b= 35.5 <class 'float'>
# c=25+35.50= 60.5 <class 'float'>

# In[2]:


a=25
print('a=25',type(a))
b=35.5
print('b=35.5',type(b))
c=25+35.5
print('c=25+35.5=60.5',type(c))


# ข้อ 2 ผลลัพธ์ แปลง ค่า 175 เป็นค าตอบข้างล่าง
# - แปลงเลขฐานสิบ เป็น ฐานสอง 0b10101111
# - แปลงเลขฐานสิบ เป็น ฐานแปด 0o257
# - แปลงเลขฐานสิบ เป็น ฐานสิบหก 0xaf

# In[8]:


a = 175
bin_a = bin(a)
oct_a = oct(a)
hex_a = hex(a)
print("แปลงเลขฐานสิบ เป็นฐานสอง"+bin_a)
print("แปลงเลขฐานสิบ เป็นฐานแปด"+oct_a)
print("แปลงเลขฐานสิบ เป็นฐานสิบหก"+hex_a)


# -สร้างอาร์เรย์ a (1 ชุด) คือ 24, 26, 23, 20, 38
# -แสดงข้อมูลของอาร์เรย์ในต าแหน่งที่ 3
# -แสดงค่าสูงสุดในอาร์เรย์

# In[24]:


import numpy as np
a = np.array ([24,26,23,20,38])
print ("ตำแหน่งที่ 3 คือ",a[2],"\t","Max =",max(a) )


# In[1]:


name = input("กรุณาใส่ชื่อ:")
lastname = input("กรุณาใส่นามสกุล:")
print("ชื่อนามสกุล"+name+lastname)


# In[2]:


a=int (input("Enter First number"))
b=int (input("Enter Second number"))
print ("a-b = %d" %(a-b))


# In[3]:


a=float(input("Enter  number"))
b=float(input("Enter  number"))
print ("a+b=%d "%(a+b))


# In[4]:


import pandas as pd


# In[5]:


data = {'day':['1/1/2022','2/1/2002','3/1/2002'],
        'temp':[20,21,22],
        'event':['cold','hot','cool'],
}


# In[6]:


print (data)


# In[7]:


df = pd.DataFrame(data)


# In[8]:


print(df)


# In[9]:


print(df.shape)


# In[10]:


print(df['temp'].max())


# In[11]:


import numpy as np


# In[13]:


a = np.array ([1,2,3,4,5])


# In[14]:


print (a)


# In[ ]:




