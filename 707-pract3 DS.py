#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import os


# In[8]:


os.chdir("C:/Users/MSCIT/Downloads")
cars_data=pd.read_csv("Toyota.csv",index_col=0,na_values=["??","????"])
cars_data.size


# In[30]:


cars_data.dropna(axis=0,inplace=True)
cars_data.size


# In[35]:


cars_data=pd.read_csv('Toyota.csv',index_col=0)
cars_data.head()


# In[10]:


sns.set(style="dark")
sns.regplot(x=cars_data['Age'], y=cars_data['Price'])


# In[50]:


sns.regplot(x=cars_data['Age'], y=cars_data['Price'], marker="*", fit_reg=False)


# In[21]:


sns.lmplot(x='Age', y='Price', data=cars_data, fit_reg=False, hue="FuelType", legend=True, palette="Set1")


# In[16]:


sns.distplot(cars_data['Age'])


# In[17]:


sns.distplot(cars_data['Age'],kde=False)


# In[18]:


sns.distplot(cars_data['Age'],kde=False,bins=5)


# In[22]:


sns.countplot(x="FuelType", data=cars_data)


# In[23]:


sns.countplot(x="FuelType", data=cars_data, hue="Automatic")


# In[24]:


pd.crosstab(index=cars_data['Automatic'], columns=cars_data['FuelType'], dropna=True)


# In[25]:


sns.boxplot(x=cars_data['FuelType'], y=cars_data['Price'])


# In[28]:


sns.boxplot(x=cars_data['FuelType'], y=cars_data['Price'],hue='Automatic',data=cars_data)


# In[34]:


f,(ax_box,ax_hist)=plt.subplots(2,gridspec_kw={"height_ratios":(0.15,0.85)})


# In[36]:


f,(ax_box,ax_hist)=plt.subplots(2,gridspec_kw={"height_ratios":(0.15,0.85)})
sns.boxplot(cars_data['Price'],ax=ax_box)
sns.distplot(cars_data['Price'],ax=ax_hist,kde=False)


# In[39]:


sns.pairplot(cars_data,kind="scatter",hue="FuelType",diag_kws={'bw':0.1})
plt.show()


# In[40]:


data=np.random.randint(1,100,size=(10,10))
print("the data to be plotted:\n")
print(data)


# In[41]:


#heatmap
hm=sns.heatmap(data=data)
plt.show()


# In[43]:


hm=sns.heatmap(data=data,vmin=30,vmax=70)
plt.show()


# In[48]:


#setting the parameter value
cmap="tab20"
center=0
annot=True #setting the parameter values
hm=sns.heatmap(data=data,cmap=cmap,annot=annot) #plotting the heatmap
plt.show()


# In[ ]:




