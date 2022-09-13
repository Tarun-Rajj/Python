#!/usr/bin/env python
# coding: utf-8

# # Tuple Questions
# 

# In[7]:


# 5 Write a python program to convert a tuple to a string.

x = [1,2,3,4]
y = list(x)
y =['1','2','3','4']
z = tuple(y)
z


# In[10]:


# 6. Write a program to convert list to a tuple


a = [1,2,3,4,5]
# type(a)
b =tuple(a)
b


# In[7]:


# 7. Write a python program to remove an item from a tuple.


t = (4,5,6,7,8)
s =list(t)
s.pop(3)
u = tuple(s)
u


# In[8]:


# 8. Write a python program to find the index of an item from a tuple.

e = (4,5,6,78,9,0)
e.index(78)


# In[12]:


# 9. Write a python program to reverse a tuple.

e =(34,5,67,5,43,5)
s = list(e)
s.reverse()
t = tuple(s)
t



# In[13]:


# 10. Write a program calculate the product, multiplying all the numbers of a given tuple.


T = (4,3,2,2,-1,18)
s = list(T)
V = s*T[0]
V


# In[20]:


x = [(45,90,75,60)]
k = 5
for i in x:
    for j in i:
print(i)
if j%k==0:
    print("div")
else:
    print("ND")
    


# In[ ]:


a = int(input("enter you salary"))
b = int(input("enter you working years"))
if b>5:
      print("you are eligible for bonus")
      c =(a*(5/100))
      print("your bonus : " , c)
else:
      print("no bonus")


# In[ ]:


a= int(input ("enter length"))
b= int(input ("enter breadth"))
if a==b:
     print("square")
else:
     print("not square")


# In[ ]:


year of service = int(input('year of service'))
salary =int(input('salary'))
if year of service = >5:
    bonus=(salary*5/100)
    print('bonus')
else:
    print('no bonus')


# In[ ]:



a= int(input ("enter marks"))
if a>80:
     print(" grade A")
Elif a<=80 and a>60:
     print("grade B")
elif a<=60 and a>50:
       print("grade C")
elif a<=50 and a>45:
      print("grade D")
elif a<=45 and a>25:
       print("grade E")
elif a<=25:
      print("fail")







# 
# 
# 
# 

# In[10]:


# Question 4

a= int(input ("enter qty"))
T_cost= a*100
if a>10:
      
dis= T_cost * (10/100)
       F_amt= T_cost - dis
print(" final amount after discount" , F_amt)
else:
       print(" Amount without deduction " , T_cost)


# In[5]:


a= int(input ("enter num1"))
b= int(input ("enter num2"))
c= int(input ("enter num3"))
if a>b:
     print("greatest",a)
elif b>c:
     print("greatest",b)
elif c>a:
     print("greatest",c)
else:
            print ("invalid input")


# In[ ]:


a = int(input("enter quantity"))
b = int(input("enter price of one quantity"))
if b>100:
      print("you are eligible for discount")
      c =(a*(10/100))                                                           #wrong answer
      print("your discount : " , c)
else:
      print("no bonus")


# In[4]:


a= int(input ("enter marks"))
if a>80:
     print(" grade A")
elif a<=80 and a>60:
     print("grade B")
elif a<=60 and a>50:
       print("grade C")
elif a<=50 and a>45:
      print("grade D")
elif a<=45 and a>25:
       print("grade E")
elif a<=25:
      print("fail")


# In[2]:


a= int(input ("enter num1"))
b= int(input ("enter num2"))
c= int(input ("enter num3"))
if a>b:
     print("greatest",a)
elif b>c:
     print("greatest",b)
elif c>a:
      print("greatest",c)


# In[6]:


unitPrice = 100
purchase = 11
price = unitPrice*purchase

if price >= 1000:
    dis = (price*10)/100
    print(dis)
    pay = price-dis
    print(pay)


# In[ ]:


class_held = 100
class_attend = 7
per_Class_attend = (class_attend/class_held)*100
if per_Class_attend > 75:  
    print("Allowed")
else:
    med = input("Type Y for YES and N for No for medical condition")
    if med == "Y":
        print("Allowed")
    else:
        print("not allowed")


# In[ ]:


class_held = 100
class_attend = 7
per_Class_attend = (class_attend/class_held)*100
if per_Class_attend >=75:  
    print("Allowed")
else:
    med = input("Type Y for YES and N for No for medical condition")
    if med == "Y":
        print("Allowed")
    else:
        print("not allowed")


# In[ ]:


#def fxn():
     Sum = 0
     print("Enter the 10 numbers")
        for i in range(1,11):
        num = int(input("Number %d=",i))
        Sum = Sum+num
        print("The sum of 10 numbers is",Sum)


# In[7]:


fxn()


# In[3]:


def fxn():       
    Sum = 0
    print("Enter the 10 numbers")
    for i in range(1,11): 
        num = int(input("Number %d ="%i))

        Sum = Sum+num 
        print(Sum)
        


# 

# In[1]:


fxn()


# In[5]:


def fxn():       
        Sum = 0
        print("Enter the 10 numbers")
        for i in range(1,11): 
            num = int(input("Number %d ="%i))
    
            Sum = Sum+num 
            print(Sum)


# In[9]:


#x = 100
for i in range(1,51,2):
        print(" \n",i)


# In[3]:


class student:
    a = 'hello students'
    
s = student()
s.a


# In[ ]:


a = (4)
b = (2)
a//b


# In[ ]:


x = [1,2,3,4]
y = list(x)
for i in y :
    y.append(5)
    print(y)
    


# In[2]:


x = {
    'name':['neha',('priya','priyanka'),'kirti'],
    'age': (2,3,4,5),
    'marks': (6,7,6,8)
}


# In[7]:


y = {
    'name' :'tarun'
}


# In[4]:


type(y)


# In[8]:


x.copy()


# In[12]:


x.get('age')


# In[23]:


x.update({'gaali': 'bsdk'}) 
x


# In[ ]:





# In[ ]:




