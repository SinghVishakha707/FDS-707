#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
#create a figure and axis
fig,ax=plt.subplots()

x=[2,4,6,6,9,2,7,2,1,8,9,1,7,8,1]
y=[7,8,4,5,1,0,8,2,6,9,1,2,4,8,6]

ax.scatter(x,y)


# In[6]:


import pandas as pd
iris=pd.read_csv('E:/iris.csv')
iris


# In[10]:


import matplotlib.pyplot as plt
fig,ax=plt.subplots()
ax.scatter(iris['sepal_length'],iris['sepal_width'])
ax.set_title('iris Dataset')
ax.set_xlabel('sepal_lenght')
ax.set_ylabel('sepal_width')


# In[9]:


fig


# In[ ]:




