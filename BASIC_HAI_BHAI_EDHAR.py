#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Accept the maks of 5 subject and calculate there total and percentage.

print("Enter marks of 5 subjects")
English = int(input())
Hindi = int(input())
Math = int(input())
Science = int(input())
Chemistry = int(input())
Total = English+Hindi+Math +Science +Chemistry
Percentage = Total/5
print(Total)
print(Percentage)


# In[2]:


# si and ci|
p = int(input("enter principal"))
r = int(input("enter rate"))
t = int(input("enter time in years"))
print("Enter Principal amount , rate of interest, time period")
si = (p*r*t)/100
ci = p*pow((1+r/100),t)-p
print(si)
print("%.2f"%ci)


# In[10]:


# circumference of a circle

r = int(input("enter radius of a circle"))
a = 3.14*r*r
p = 2*3.14*r
print(a)
print("%.2f"%p)


# In[15]:


# Swap using 3rd variable

# a = 2
# b = 6
# a,b = b,a
# print(a,b)

a = 3 
b = 8
c = a
a = b
b = c
print(a,b)


# In[18]:


# Tem in Centigrade and convert into Fahrenheit.\
T = int(input("Enter temperature into degree celcius"))
F = 9/5*T+32
print(F)


# In[22]:


# cHeck 2 no r = or !
print("Enter 2 number")
n1= int(input())
n2= int(input())
if (n1==n2):
    print("eql")
else:
    print("not eql")


# In[27]:


# Greatest of 3 number
print("Enter 3 number")
n1= int(input())
n2= int(input())
n3= int(input())
if (n1==n2 and n2==n3):
    print("eql")
else:
    if(n1>n2) and(n1>n3):
        print("n1 bada h")
    elif(n2>n1) and (n2>n3):
        print("n2 bada h bhai yrr")
    else:
        print("n3 sbse bada h yrrr")


# In[29]:


# number is even or odd
n = int(input())
if(n%2==0):
    print("even")
else:
    print("odd")


# In[31]:


# leap yr or not
year = int(input("saal ko daalo bhai"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("leap yr")
else:
    print("nhi hai bhai yr leap year")


# In[35]:


# GRADES DENE H BHAI ENKO
print("Enter marks of 5 subjects")
English = int(input())
Hindi = int(input())
Math = int(input())
Science = int(input())
Chemistry = int(input())
Total = English+Hindi+Math +Science +Chemistry
P = Total/5
print(Total)
print(P)
if(P>=90):
    print("A LEJA BHAi")
elif(P>=80):
    print("b")
elif(P>=70):
    print("c")
else:
    print("d")
            


# In[ ]:




