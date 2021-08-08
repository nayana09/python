#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, Welcome to python Introduction")


# In[2]:


#Python Variables
x = 5
y = "Nayana"
print(x)
print(y)


# In[7]:


x = 4
x = "Grapes"
print(x)


# In[4]:


#casting
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)


# In[6]:


#get data type
x = 5
y = "Nayana"
print(type(x))
print(type(y))


# In[8]:


x = "Orange"
print(x)
#double quotes are the same as single quotes:
x = 'Orange'
print(x)


# In[10]:


#case sensetive 
a = 4
A = "Orange"

print(a)
print(A)


# In[11]:


#assign multiple values in one line
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)


# In[12]:


x = y = z = "Orange"

print(x)
print(y)
print(z)


# In[13]:


fruits = ["apple", "banana", "grapes"]
x, y, z = fruits

print(x)
print(y)
print(z)


# In[15]:


#output variable
x = "good morning"
print("Hello " + x)


# In[16]:


x = "I Am "
y = "Groot"
z = x + y
print(z)


# In[17]:


#Global variable
x = "Groot"

def myfunc():
  print("I Am  " + x)

myfunc()


# In[18]:


x = "Groot"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("I AM " + x)


# In[19]:


def myfunc():
  global x
  x = "Groot"

myfunc()

print("I Am " + x)


# In[22]:


x = 5
y = 5.0
z = 'orange'
a = 1j
print(type(x)) 
print(type(y))
print(type(z))
print(type(a))


# In[23]:


#random number
import random

print(random.randrange(1, 10))


# In[25]:


#casting
x = int(1.005)
y = float(2)
z = str(3.0)
print(x)
print(y)
print(z)


# In[26]:


#python string 
a = "hai am very happy to learn python"
print(a)


# In[27]:


#slicing a string
a = "Hello, World!"
print(a[2:5])


# In[31]:


#slicing front, end, negative indexing
b = "Hello, World!"
print(b[:5])
print(b[2:])
print(b[-5:-2])


# In[41]:


#String modifications
a = " I am a groot "

print(a.upper())
print(a.lower())
#remove white space
print(a.strip())
#replace string 
print(a.replace("a", "not"))


# In[47]:


#split string
a = "Hello, World"
b = a.split(",")
print(b)


# In[48]:


#String concatanation
a = "Hello"
b = "World"
c = a + b
print(c)


# In[49]:


a = "Hello"
b = "World"
c = a + " " + b
print(c)


# In[55]:


#string format
age = 23
txt = "My name is Nayana, and I am {}"
print(txt.format(age))


# In[57]:


#string format using index
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} rupees for {0} pieces of Dolls {1}."
print(myorder.format(quantity, itemno, price)) 


# In[59]:


#escape chracter
txt = "I am very \"innocent\" from the heart."
print(txt) 


# In[ ]:




