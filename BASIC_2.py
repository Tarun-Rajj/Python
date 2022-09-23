#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PRIME NUMBER
num = int(input("Enter your number to fine the that the number is prime or not"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Not prime number")
            break
    else:
        print("prime number")
else:
    print("Not prime")


# In[2]:


# DISPLAY CALENDAR
import calendar  
# Enter the month and year  
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
  
# display the calendar  
print(calendar.month(yy,mm))  


# In[3]:


# TRANSPOSE THE MATRIX
X = [[1,2,3],  
       [4,5,6],  
       [7,8,9]]    
  
Result = [[0,0,0],  
                [0,0,0],  
                [0,0,0]]  
# iterate through rows  
for i in range(len(X)):  
   # iterate through columns  
   for j in range(len(X[0])):  
        Result[j][i] = X[i][j]
for r in Result:  
    print(r)  


# In[5]:


# ARRANGE THE STRING IN ALPHABETICAL ORDER
myString = input("Enter a string: ")  
# breakdown the string into a list of words  
spe = myString.split()  
# sort the list  
spe.sort()  
# display the sorted words  
for w in spe:  
    print(w)  


# In[6]:


# Prime number in an given interval.
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number) 


# In[9]:


# Find the factorial of a number.
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
    print(" Factorial does not exist for negative numbers")    
elif num == 0:    
    print("The factorial of 0 is 1")    
else:    
    for i in range(1,num + 1):    
        factorial = factorial*i    
    print("The factorial of",num,"is",factorial) 


# In[ ]:




