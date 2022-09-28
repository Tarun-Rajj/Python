#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Copy element of one array into another array
#Initialize array     
arr1 = [1, 2, 3, 4, 5];     
     
#Create another array arr2 with size of arr1    
arr2 = [None] * len(arr1);    
     
#Copying all elements of one array into another    
for i in range(0, len(arr1)):    
    arr2[i] = arr1[i];     
     
#Displaying elements of array arr1     
print("Elements of original array: ");    
for i in range(0, len(arr1)):    
    print(arr1[i]),    
     
print();    
     
#Displaying elements of array arr2     
print("Elements of new array: ");    
for i in range(0, len(arr2)):    
    print(arr2[i]),  


# In[4]:


#Initialize array     
arr = [1, 2, 8, 3, 2, 2, 2, 5, 1];     
#Array fr will store frequencies of element    
fr = [None] * len(arr);    
visited = -1;    
     
for i in range(0, len(arr)):    
    count = 1;    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            count = count + 1;    
            #To avoid counting same element again    
            fr[j] = visited;    
                
    if(fr[i] != visited):    
        fr[i] = count;    
     
#Displays the frequency of each element present in array    
print("---------------------");    
print(" Element | Frequency");    
print("---------------------");    
for i in range(0, len(fr)):    
    if(fr[i] != visited):    
        print("    " + str(arr[i]) + "    |    " + str(fr[i]));    
print("---------------------");    


# In[ ]:




