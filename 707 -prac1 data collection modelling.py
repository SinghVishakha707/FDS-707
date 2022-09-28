#!/usr/bin/env python
# coding: utf-8

# # Data Collection,Modeling And Compilation

# In[1]:


my_dict={'name':["a","b","c","d","e","f","g"],'age':[20,27,35,45,55,43,35],'designation':['VP',"CEO","CFO","VP","VP","CEO","MD"]}
import pandas as pd
import numpy as np
df=pd.DataFrame(my_dict)
df


# In[2]:


df.to_csv("example")
df


# In[3]:


df_csv=pd.read_csv("example")
df_csv


# In[4]:


df.to_csv('ex',index=False)
df_csv=pd.read_csv("ex")
df_csv


# In[5]:


import pandas as pd
df=pd.read_csv("student-mat - student-mat.csv",header=None)
df.head()


# In[6]:


import pandas as pd
location = "student-mat - student-mat.csv"
df=pd.read_csv(location,names=['Rollno','Name','Grades'])
df.columns=['Rollno','Name','Grades']
df.head()


# In[7]:


import pandas as pd
names=['bob','jessica','mary','john','mel']
grades=[76,95,77,78,99]
bsdegrees=[1,1,0,0,1]
msdegrees=[2,1,0,0,0]
phddgrees=[0,1,0,0,0]
degrees=zip(names,grades,bsdegrees,msdegrees,phddgrees)
columns=['Names','Grades','BS','MS','Phd']
df=pd.DataFrame(data=degrees,columns=columns)
df


# In[8]:


import pandas as pd
location='gradedata.xlsx'
df=pd.read_excel("gradedata.xlsx")
df.columns=['first','last','sex','age','exer','hrs','grd','addr']
df.head()


# In[9]:


import pandas as pd
names=['bob','jessica','mary','john','mel']
grades=[76,95,77,78,99]
gradelist=zip(names,grades)
df=pd.DataFrame(data=gradelist,columns=['names','grades'])
writer=pd.ExcelWriter('dataframe.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='sheet1')
writer.save()
                      


# In[10]:


import sqlite3
con = sqlite3.connect("C:/Users/MSCIT/Downloads/portal_mammals.sqlite")
cur = con.cursor()

for row in cur.execute('Select * from species;'):
    print(row)
con.close()


# In[11]:


import sqlite3
#create a SQL connection to our SQlite database
con=sqlite3.connect("C:/Users/MSCIT/Downloads/portal_mammals.sqlite")
cur=con.cursor()
#Return all result of query
cur.execute('Select plot_id From plots Where plot_type="Control"')
print(cur.fetchall())
#Return First Result of query
cur.execute('Select species From species Where taxa="Bird"')
print(cur.fetchone())
#Be sure to close the connection
con.close()


# In[12]:


import pandas as pd
import sqlite3

#read sqlite query results into a pandas dataframe 
con=sqlite3.connect("C:/Users/MSCIT/Downloads/portal_mammals.sqlite")
df=pd.read_sql_query("Select*From surveys",con)

#verify that result of Sql query is the dataframe
print(df.head())
con.close()


# In[13]:


from pandas import DataFrame
Cars={'Brand':['Honda Civic','Toyota Corolla','ford Focus','audi A4'],'Price':[22000,25000,27000,35000]
     }
df=DataFrame(Cars,columns=['Brand','Price'])
print(df)


# In[19]:


import sqlite3
conn=sqlite3.connect('TestDB12.db')
c=conn.cursor()
c.execute('create table Carss(Brand text,Price number)')
conn.commit()


# In[20]:


df.to_sql('cars21',conn,if_exists='replace',index=False)
df


# In[21]:


c.execute('''
SELECT Brand,max(Price) from cars21
''')


# In[22]:


df=DataFrame(c.fetchall(),columns=['Brand','Price'])
df


# In[23]:


import pandas as pd
import os 
import sqlite3 as lite
from sqlalchemy import create_engine


# In[24]:


studentId=["rj101","rj150","rj134","rj07"]
SName=["Shubham","Vaishu","Bittu","Vishal","Suraj"]
LName=["Singh","Yadav","Pawar","Shukla","Mishra"]
Department=["Bsc","Bcom","BMM","Msc","BBI"]
Email=["shum102@gmail.com","Vaishu12@gmail.com","bittu0908@gmail.com","vishal123@gmail.com","surajy12@gmail.com"]


# In[25]:


studata=zip(studentId,SName,LName,Department,Email)


# In[26]:


df=pd.DataFrame(data=studata,columns = ['studentId','SName','LName','Department','Email'])
df


# In[27]:


df.to_csv('Csv ex')
df


# In[31]:


writer=pd.ExcelWriter('dataframe1.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='sheet1')
writer.save()
                


# In[29]:


df.to_sql('studata',conn,if_exists='replace',index=False)
df


# # DATA PREPERATION

# In[3]:


import numpy as np
import pandas as pd


# In[5]:


state=pd.read_csv("C:/Users/MSCIT/Downloads/US_violent_crime - US_violent_crime.csv")
state.head()


# In[6]:


def some_func(y):
    return y*2
state.apply(some_func) # update each entry of data without any loop


# In[7]:


state.apply(lambda n:n*2) #lambda also works the same


# In[11]:


state.transform(func=lambda x:x*10)


# In[14]:


#usinggroupby
mean_purchase=state.groupby('State')['Murder'].mean().rename("user_mean").reset_index()
print(mean_purchase)


# In[15]:


mer=state.merge(mean_purchase)
mer


# In[17]:


#checking for missing value
print(state.isnull().sum())


# In[25]:


import pandas as pd
import numpy as np
cols=['col0','col1','col2','col3','col4']
rows=['row0','row1','row2','row3','row4']
data=np.random.randint(0,100,size=(5,5))
df= pd.DataFrame(data , columns=cols , index=rows)
df.head()


# In[26]:


df.iloc[4,2]


# In[27]:


df.iloc[3,3]=0
df.iloc[1,2]=np.nan
df.iloc[4,0]=np.nan
df['col5']=0
df['col6']=np.nan
df.head()


# In[28]:


df.loc[:,df.all()]# this function is used to remove all zero values 


# In[29]:


df.loc[:,df.any()]# if any values is integer then print all columns


# In[30]:


df.loc[:,df.isnull().any()]


# In[32]:


df.loc[:,df.isnull().all()]


# In[33]:


df.loc[:,df.notnull().any()]


# In[38]:


df.dropna(how="all",axis=0)


# In[37]:


df.dropna(how="all",axis=1)


# In[39]:


df.fillna(df.sum())


# In[43]:


#Demonstrate transfomr function using pandas in python
import pandas as pd 
import numpy as np
import random
data=pd.DataFrame({
    'C':[random.choice(('b','a','d'))for i in range(1000000)],
    'A':[random.randint(1,10)for i in range(1000000)],
    'B':[random.randint(1,10)for i in range(1000000)]
})
data


# In[47]:


v=data.groupby('C')["A"].mean().rename("D").reset_index()
v


# In[49]:


df_1=data.merge(v)
df_1


# In[ ]:




