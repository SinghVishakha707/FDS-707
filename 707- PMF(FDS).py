#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib .pyplot as plt
n = np.random.randint(2,10,40)
print(n)


# In[2]:


df=pd.DataFrame(n) #convert list n to dataframe
df=pd.DataFrame(df[0].value_counts()) # count each variable how many times repeated
df


# In[3]:


length=len(n)
length


# In[4]:


df.columns=['Counts']
df


# In[5]:


df['prob']=df['Counts']/length # find PMF take count value of each no.
df


# In[6]:


plt.bar(df['Counts'],df['prob'])


# In[7]:


#plot PMF using seaborn
import seaborn as sns

sns.barplot(df['Counts'],df['prob'])


# In[8]:


#Another example of PMF

data={'Candy':['blue','orange','yellow','green'],
     'Total':[30000,10000,20000,12000]}
df=pd.DataFrame(data)
df


# In[9]:


df["pmf"]=df["Total"]/df["Total"].sum()
df


# In[10]:


plt.bar(df['Candy'],df['pmf'])


# In[11]:


sns.barplot(df['Candy'],df['pmf'])


# # Probability Density Function(PDF)

# In[12]:


data=np.random.normal(size=100)
data=np.append(data,[1.2,1.2,1.2,1.2,1.2])
sns.distplot(data)


# In[13]:


import scipy.stats as stats

mu=20
sigma=2
h=sorted(np.random.normal(mu,sigma,100))


# In[14]:


import scipy.stats as stats
plt.figure(figsize=(10,5))
fit=stats.norm.pdf(h,np.mean(h),np.std(h))
plt.plot(h,fit,'-o')
plt.hist(h,density=True)


# # Cummulative Distribution Function(CDF)

# In[17]:


import scipy.stats as ss

x=np.linspace(-5,5,5000)
mu=0
sigma=1

y_pdf=ss.norm.pdf(x,mu,sigma)
y_cdf=ss.norm.cdf(x,mu,sigma)

plt.plot(x,y_pdf,label='pdf')
plt.plot(x,y_cdf,label='cdf')


# In[18]:


import scipy.stats as stats
plt.figure(figsize=(10,5))
fit=stats.norm.cdf(h,np.mean(h),np.std(h))
plt.plot(h,fit,'-o')
plt.hist(h,density=True)

