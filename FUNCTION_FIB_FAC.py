#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Fibonacci Series
def recur_fibo(n):  
    if n <= 1:  
        return n  
    else:  
        return(recur_fibo(n-1) + recur_fibo(n-2))  
# take input from the user  
nterms = int(input("How many terms? "))  
# check if the number of terms is valid  
if nterms <= 0:  
    print("Plese enter a positive integer")  
else:  
    print("Fibonacci sequence:")  
for i in range(nterms):  
    print(recur_fibo(i))  


# In[2]:


# Factorial
def recur_factorial(n):  
    if n == 1:  
        return n  
    else:  
        return n*recur_factorial(n-1)  
# take input from the user  
num = int(input("Enter a number: "))  
# check is the number is negative  
if num < 0:  
    print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
    print("The factorial of 0 is 1")  
else:  
    print("The factorial of",num,"is",recur_factorial(num))  


# In[ ]:




