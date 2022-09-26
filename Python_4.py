#!/usr/bin/env python
# coding: utf-8

# In[5]:


def decimal_into_binary(decimal_1):  
    decimal = int(decimal_1)  
    print ("The given decimal number", decimal, "in Binary number is: ", bin(decimal))  
decimal_into_binary(12)  


# In[4]:


def decimal_into_binary(decimal_1):  
    decimal = int(decimal_1)  
    
    # then, print the equivalent decimal  
    print ("The given decimal number", decimal, "in Binary number is: ", bin(decimal))  
# we will define the function to convert decimal to octal  
def decimal_into_octal(decimal_1):  
    decimal = int(decimal_1)  
    
    # Then, print the equivalent decimal  
    print ("The given decimal number", decimal, "in Octal number is: ", oct(decimal))  
# we will define the function to convert decimal to hexadecimal  
def decimal_into_hexadecimal(decimal_1):  
    decimal = int(decimal_1)  
    
    # Then, print the equivalent decimal  
    print ("The given decimal number", decimal, " in Hexadecimal number is: ", hex(decimal))  
    
# Driver program  
decimal_1 = int (input (" Enter the Decimal Number: "))  
decimal_into_binary(decimal_1)  
decimal_into_octal(decimal_1)  
decimal_into_hexadecimal(decimal_1)  


# In[7]:


K = input("Please enter a character: ")    
    
print ("The ASCII value of '" + K + "' is ", ord(K)) 


# In[11]:


print ("Please enter the String: ", end = "")  # end is used for print the value in front of character
string = input()  
string_length = len(string)  
for K in string:  
    ASCII = ord(K)  
    print (K, "\t", ASCII)


# In[ ]:




