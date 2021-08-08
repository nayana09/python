#!/usr/bin/env python
# coding: utf-8

# In[3]:


fruits = [('banana',30),('orange',40),('grapes',20)]


# In[5]:


for item in fruits:
    print(item)


# In[6]:


for item,price in fruits:
    print(item)


# In[7]:


for item,price in fruits:
    print(price)


# In[15]:


working_hours = [('ram',100),('sham',200), ('bam',300)]


# In[27]:



def employee_max(working_hours):
    current_max_hours = 0
    employee_name = ''
    
    for employee,hours in working_hours:
        if hours >  current_max_hours :
            current_max_hours  = hours
            employee_name = employee
            
    return (employee_name,current_max_hours)


# In[28]:


employee_max(working_hours)


# In[32]:


employee,hours = employee_max(working_hours)


# employee

# In[33]:


employee


# In[34]:


hours


# In[42]:


def sum_num(a,b,c):
    return sum((a,b,c))


# In[43]:


sum_num(10,20,30)


# In[48]:


def kw_example(**kwargs):
    if 'food' in kwargs:
        print(kwargs['food'])
    else:
        print('no food in the list')
        


# In[ ]:





# In[ ]:




