#!/usr/bin/env python
# coding: utf-8

# In[1]:


#probability of getting 3 when a die is rolled
ns=6 #n(S) = {1,2,3,4,5,6}
na=1 #n(A) ={3}
pa= na/ns #P(A)
print("probability of getting 3 is:",pa)


# In[2]:


#Probability of atleast getting one head when a coin is tossed thrice
ns=8 #n(s) = {HHH,HTH,HHT,THH,TTT,THH,TTH,THT}
na=7 #n(A) ={HHH,HTH,HHT,THH,TTH,THT,THH}
pa=na/ns #P(A)
print("prob. of getting head is:",pa)


# In[3]:


# A glass jar contain 5 red , 3 blue and 2 green jelly beans.
#if a jelly bean is chosen at random from the jar,
# what is the prob. that it is not blue?

ns=10 #n(s) = {R,R,R,R,R,B,B,B,G,G}
na= 7 #n(A) = {R,R,R,R,R,G,G}
pa=na/ns #p(A)
print("prob. of not getting blue:",pa)


# In[4]:


# If the probability that person A  will be alive in 20 years
# is 0.7 and the probability that person B will be alive in 
# 20 years is 0.5, what is the probability that they will 
# both be alive in 20 years?
# These are independent event so, 
P=0.7*0.5
print("probabilty that they will be alive after 20 years is:", P)


# In[5]:


def event_probability(n,s):
    return n/s


# In[6]:


#A fair die is tossed twice, Find the probability of getting
#a 4 or 5 on the first tosse and a 1,2, or 3 in the second toss.
pa = event_probability(2,6)
pb = event_probability(3,6)
p = pa*pb
print("probability of getting a 4 or 5 on the first toss and a 1,2 or 3 in second toss is :",p)


# In[7]:


# A bag contains 5 white marbles, 3 black marbles and 2 green marbles,
# in each draw, a marble is drawn from the bag
# and not replaced. In three draws, find the prob. of obtaining white,
# black and green in that order
pa = event_probability(5,10)
pb = event_probability(3,9)
pc = event_probability(2,8)
print("prob. of obtaining white,black and green in the order:",pa ,pb, pc)


# In[8]:


# sample space
cards = 52
# calculate the prob.  of drawing a heart or a 
hearts = 13 
clubs = 13
heart_or_club = event_probability(hearts,cards) + event_probability(clubs,cards)
print(heart_or_club)


# In[9]:


# calculate the prob. of drawing an ace , king, or a queen
cards=52
ace = 4
king = 4
queen = 4
ace_king_or_queen = event_probability(ace,cards)+event_probability(king,cards)+event_probability(queen,cards)
print(round(ace_king_or_queen,2))


# In[10]:


cards = 52
heart = 13
ace = 4
ace_of_heart = 1
heart_or_ace = event_probability(heart,cards)+event_probability(ace,cards)-event_probability(ace_of_heart,cards)
print(round(heart_or_ace,1))


# In[11]:


#calculate the prob. of drawing red cards or face cards
red = 26
facecards = 12
red_facecards = 6
red_or_facecards = event_probability(red,cards)+event_probability(facecards,cards)-event_probability(red_facecards,cards)
print(round(red_or_facecards,2))


# In[12]:


# prob. of not getting 5 when a fair die is rolled
ns=6 #n(s) = {1,2,3,4,5,6}
na=1 #n(a) ={5}
pa=1-na/ns
print("prob. of not getting 5 is:",pa)


# In[13]:


#suppose you draw 2 cards from deck.
# you win if you get ace given that you draw a jack in first draw
# we used conditional prob.
cards = 52
j = 4
ace = 4
pj = event_probability(j,52)
pa = event_probability(ace,51)
pa_given_pj=(pa*pj)/pj
print(pa_given_pj)


# In[14]:


# conditional probability P(A/B)=P(A & B)/P(B)

import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/MSCIT/Downloads/student-mat - student-mat.csv")
df.head(3)


# In[15]:


len(df)


# In[16]:


df['grade_A'] = np.where(df['G3']*5 >= 80 , 1, 0)
df


# In[22]:


df['high_absences'] = np.where(df['absences']>= 10 , 1, 0)
df


# In[18]:


df['count']=1
df


# In[25]:


df=df[['grade_A','high_absences','count']]
df.head()


# In[26]:


final=pd.pivot_table(
       df,
       values='count',
       index=['grade_A'],
       columns=['high_absences'],
       aggfunc=np.size,
       fill_value=0
)


# In[27]:


print(final)


# In[28]:


total=final.iloc[0,0]+final.iloc[0,1]+final.iloc[1,0]+final.iloc[1,1]
p_a=(final.iloc[1,0]+final.iloc[1,1])/total
p_a


# In[29]:


p_b=(final.iloc[0,1]+final.iloc[1,1])/total
p_b


# In[30]:


p_c=(final.iloc[1,1])/total
p_c


# In[31]:


P_d=p_c/p_b
P_d


# In[ ]:




