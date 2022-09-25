#!/usr/bin/env python
# coding: utf-8

# In[1]:


# defining a function to calculate LCM  
def calculate_lcm(x, y):  
    # selecting the greater number  
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm    
  
# taking input from users  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
# printing the result for the users  
print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2))  


# In[2]:


# defining a function to calculate HCF  
def calculate_hcf(x, y):  
    # selecting the smaller number  
    if x > y:  
        smaller = y  
    else:  
        smaller = x  
    for i in range(1,smaller + 1):  
        if((x % i == 0) and (y % i == 0)):  
            hcf = i  
    return hcf  
  
# taking input from users  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
# printing the result for the users  
print("The H.C.F. of", num1,"and", num2,"is", calculate_hcf(num1, num2))  


# In[ ]:




