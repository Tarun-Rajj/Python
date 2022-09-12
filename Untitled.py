#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = [1,2,34,4,5,6]
x[::-1]


# In[2]:


x = [1,2,34,4,5,6]
x[0],x[-1]= x[-1],x[0]
print(x)


# In[6]:


x = [1,2,4,434,4,44,54,4,6]
y= 0
for i in x:
    if i>y:
        y=i
    
print(y)
    


# In[8]:


x = [1,2,34,4,5]
y = 0
for i in x:
    y= i+y
print(y)


# In[10]:


x = [1,2,4,434,4,44,54,4,6,3]
even = 0
odd = 0
for i in x:
    if i%2==0:
        print("even",i)
        even = even+1
    else:
        print("odd",i)
        odd = odd+1
print(" even number count is",even)
print(" odd number count is",odd)


# In[ ]:





# In[ ]:


x = [1,2,3,4]
# y = list(x)
for i in x:
    y = i.append(5,6)
    print(y)


# In[1]:


x = [1,2,3,4,5]
for i in x:
    y = x + [5,6]
print(y)
    


# In[42]:


n = int(input("Enter the number"))
if n>=1:
    for i in range(2,n):
        if n%i == 0:
            print("not prime number")
            break
    else:
        print("prime number")
else: 
    print("not prime")


# In[39]:


n = int(input("Enter the number"))
if n>1:
    for i in range(2,n):
        if n%i == 0:
            print("not prime number",n)
            break
    else: 
        print("prime number",n)
else: 
    print("not prime",n)


# In[9]:


n = int(input())
if n%2 == 1:
    print("Weird")
elif (n>=2) and (n<=5):
    print("Not Weird")
elif (n>=6) and (n<=20):
    print("Weird")
else:
    print("Not Weird")
            


# In[14]:


def is_leap(year):
    #leap = False
    if(year%4==0 and year%100!=0 or year%400==0):
        print("True")
    else:
        print("False")
    
    
    
    return leap

year = int(input())
print(is_leap(year))


# In[23]:


def is_leap(year):
    n = int(input())
    if(n%4==0 and n%100!=0 or n%400==0):
        print("True")
    else:
        print("False")

year()        
        
            


# In[32]:


n = int(input())
if(n%4==0 and n%100!=0 or n%400==0):
    print("leap year")
else:
    print("Not Leap year")


# In[3]:


def is_leap(n):
    leap = False
    n = int(input())
    if(n%4==0 and n%100!=0 or n%400==0):
        print("True")
    else:
        print("False")
is_leap(n)    
    
    


# In[11]:


def is_leap(year):
    leap = False
    year = int(input())
    if(year%4==0 and year%100!=0 or year%400==0):
        print("True")
    else:
        print("False")
is_leap(1990)    


# In[5]:


is_leap()


# In[ ]:




