#!/usr/bin/env python
# coding: utf-8

# In[2]:


#if conditions
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# In[3]:


#evaluating variable
print(bool("Hello"))
print(bool(15))


# In[4]:


bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


# In[5]:


def myFunction() :
  return True

print(myFunction())


# In[7]:


print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 % 5)
print(10**2)


# In[8]:


#python list
this_list = ["apple", "banana", "cherry"]
print(this_list)


# In[11]:


#duplicates
this_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(this_list)
print(len(this_list))


# In[21]:


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list1)
print(list2)
print(list3)
print(list4)
print(type(list1))
print(type(list2))
#accessing item 
print(list1[1])
#negative index
print(list1[-1])
#range
print(list1[2:5])



# In[22]:


#change item value
this_list = ["apple", "banana", "cherry"]
this_list[1] = "blackcurrant"
print(this_list)


# In[23]:


#change range 
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
this_list[1:3] = ["blackcurrant", "watermelon"]
print(this_list)


# In[24]:


this_list = ["apple", "banana", "cherry"]
this_list[1:2] = ["blackcurrant", "watermelon"]
print(this_list)


# In[25]:


this_list = ["apple", "banana", "cherry"]
this_list.insert(2, "watermelon")
print(this_list)


# In[26]:


#append item insert item to the last list of the item 
this_list = ["apple", "banana", "cherry"]
this_list.append("orange")
print(this_list)


# In[27]:


this_list = ["apple", "banana", "cherry"]
this_list.insert(1, "orange")
print(this_list)


# In[28]:


this_list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
this_list.extend(tropical)
print(this_list)


# In[29]:


#add any iterables
this_list = ["apple", "banana", "cherry"]
this_tuple = ("kiwi", "orange")
this_list.extend(this_tuple)
print(this_list)


# In[30]:


#remove item 
this_list = ["apple", "banana", "cherry"]
this_list.remove("banana")
print(this_list)


# In[31]:


this_list = ["apple", "banana", "cherry"]
this_list.pop(1)
print(this_list)


# In[32]:


this_list = ["apple", "banana", "cherry"]
this_list.pop()
print(this_list)


# In[33]:


#remove first item
this_list = ["apple", "banana", "cherry"]
del this_list[0]
print(this_list)


# In[37]:


#delete entire list
this_list = ["apple", "banana", "cherry"]
del this_list


# In[38]:


#loop list
this_list = ["apple", "banana", "cherry"]
for x in this_list:
  print(x)


# In[39]:


this_list = ["apple", "banana", "cherry"]
i = 0
while i < len(this_list):
  print(this_list[i])
  i = i + 1


# In[40]:


this_list = ["apple", "banana", "cherry"]
[print(x) for x in this_list]


# In[41]:


#list comprenshion
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# In[42]:


#sort ascending
this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort()
print(this_list)


# In[43]:


#sort descending
this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort(reverse = True)
print(this_list)


# In[44]:


#copylist
this_list = ["apple", "banana", "cherry"]
my_list = this_list.copy()
print(my_list)


# In[45]:


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# In[46]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# In[48]:


#python tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))


# In[49]:


#acces tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


# In[50]:


#range of indexing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


# In[51]:


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


# In[52]:


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# In[54]:


#unpacking tuplefruits = ("apple", "banana", "cherry")

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# In[55]:


#using astrike
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


# In[ ]:




