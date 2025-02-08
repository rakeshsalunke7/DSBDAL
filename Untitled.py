#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
from sklearn import preprocessing


# In[11]:


dt=pd.read_csv('salary.csv')


# In[12]:


dt


# In[13]:


dt.info()


# In[16]:


print(dt.dtypes)


# In[17]:


numeric_columns = dt.select_dtypes(include=['number'])


# In[18]:


print(numeric_columns.head())


# In[ ]:




