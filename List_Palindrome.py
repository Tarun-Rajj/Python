#!/usr/bin/env python
# coding: utf-8

# In[22]:


x = ['a',33,'r4','df','fd','df','gf']
print(x)


# In[27]:


x.copy()


# In[18]:


x.extend('0')
x


# In[19]:


x.index('df')


# In[20]:


x


# In[21]:


x


# In[23]:


x


# In[26]:


x.index('df','fd')


# In[68]:


x = '111'
y =''
for i in x:
    y= i+y
    if x==y:
        print("p")
    else:
        print("np")


# In[22]:


a = [34,45,89,56]
b = [43,54,56,89]
for i in a:
    for j in b:
        if i==j:
            print("Similar number are:",i)
else:  
        print("Not Similar")
#print


# In[69]:


X = [1,3,5,7,9]
Y = [1,5,10,15]
Z = [val for val in X if val in Y]
print(Z)


# In[73]:


X = [1,3,5,7,9,15]
Y = [1,5,10,15]
Z = [val for val in X if val in Y]
print(Z)


# In[75]:


a = [1,2,35,56]
b = a[0]
a[0]=a[-1]
a[-1]=b
print(a)


# In[80]:


a = [1,2,35,56]
#for i in a:
a[::-1]


# In[9]:


#a = ['1','2','3','4','5']
a = 'sagar'
b = ''
for i in a:
    b = i + b
print(b)


# In[2]:


string = 'aba'
new_string = string.replace('a','b')
print(new_string)


# In[43]:


#Palindrome:- 
# a = int(input("number"))
# c = a
# rev = 0
# while a > 0:
#       b= a%10
#     rev = (rev*10)+b
#     a= a/10
# if c == rev:
#      print("palindrome")
# else:
#       print("not palindrome")

#2nd way:- 
a=int(input("number"))
b=str(a)
rev=''
for i in b:
     rev=i+rev
c=int(rev)
if a==c:
     print("palindrome")
else:
     print("not palindrome")


# In[ ]:




