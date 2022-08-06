#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


import pandas as pd


# In[6]:


import matplotlib.pyplot as plt


# In[7]:


import operator


# In[18]:


basesalaire=pd.read_csv('ds_salaries.csv',delimiter=',')
basesalaire


# In[22]:


print(basesalaire.columns)


# In[23]:


basesalaire.count()


# In[24]:


basesalaire.head()


# In[25]:


basesalaire.tail()


# In[26]:


basesalaire.describe()


# In[27]:


basesalaire.info()


# In[29]:


x=basesalaire["work_year"].value_counts()
y=["payer en 2020","payer en 2021","payer en 2022"]
plt.bar (y[0],x[2020],label="Payer en 2020",align="center")
plt.bar (y[1],x[2021],label="Payer en 2020",align="center")
plt.bar (y[2],x[2022],label="Payer en 2020",align="center")
plt.legend()
plt.ylabel("Nb. de personnes")
plt.xlabel("Anneé/Payer")
plt.show()


# In[ ]:




