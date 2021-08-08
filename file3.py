#!/usr/bin/env python
# coding: utf-8

# In[1]:


#creating sets
thisset = {"apple", "banana", "cherry"}
print(thisset)


# In[3]:


#duplicates not allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#lenght
print(len(thisset))


# In[4]:


#acess item
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# In[5]:


#add item
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# In[6]:


#add iterables
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


# In[7]:


#remove
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


# In[8]:


#loop 
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# In[9]:


#union 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# In[10]:


#updates
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# In[11]:


#intreaction
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


# In[12]:


#difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)


# In[13]:


#dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# In[14]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)


# In[15]:


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)


# In[16]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


# In[18]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)


# In[19]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


# In[20]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


# In[22]:


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)


# In[23]:


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)


# In[24]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# In[25]:


#nested dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)


# In[26]:


#if condition
a = 33
b = 200

if b > a:
  print("b is greater than a")


# In[27]:


#elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# In[28]:


#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# In[29]:


i = 1
while i < 6:
  print(i)
  i += 1


# In[30]:


i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1


# In[31]:


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# In[32]:


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# In[33]:


x = lambda a : a + 10
print(x(5))


# In[34]:


x = lambda a, b : a * b
print(x(5, 6))


# In[ ]:




