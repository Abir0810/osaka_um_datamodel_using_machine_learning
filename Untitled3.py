#!/usr/bin/env python
# coding: utf-8

# In[76]:


import pandas as pd
from sklearn import linear_model
import numpy as np


# In[77]:


df=pd.read_csv(r"D:\New folder\Ume_in_Osaka(ENG)\ume_in_osaka.csv")


# In[78]:


df.head(2)


# In[79]:


from sklearn.linear_model import LinearRegression


# In[80]:


y = df[['day']]
x = df.drop(['serial','year','month','local pressure','sea pressure','total preci','hr1 preci','min10 preci','min temp','avg humid','min humid','sun hours','bloom','day','avg temp'],axis=1)
x=x.dropna()


# In[81]:


from sklearn.model_selection import train_test_split


# In[82]:


x_train, x_test, y_train, y_test = train_test_split(
x, y, test_size=0.2, random_state=10)


# In[83]:


x_train, x_test, y_train, y_test = train_test_split(
x, y, test_size=0.2, random_state=10)


# In[84]:


logmodel=LinearRegression()


# In[85]:


logmodel.fit(x_train, y_train)


# In[87]:


logmodel.predict([[600]])


# In[88]:


df=pd.read_csv(r"D:\New folder\Ume_in_Osaka(ENG)\ume_in_osaka.csv")


# In[89]:


y = df[['max temp']]
x = df.drop(['serial','year','month','local pressure','sea pressure','total preci','hr1 preci','min10 preci','min temp','avg humid','min humid','sun hours','bloom','max temp','avg temp'],axis=1)
x=x.dropna()


# In[90]:


from sklearn.model_selection import train_test_split


# In[91]:


x_train, x_test, y_train, y_test = train_test_split(
x, y, test_size=0.2, random_state=10)


# In[92]:


logmodel=LinearRegression()


# In[93]:


logmodel.fit(x_train, y_train)


# In[96]:


logmodel.predict([[14]])


# In[ ]:




