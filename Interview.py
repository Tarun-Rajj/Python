# Reverse the whole String without reverse the word sequence in Python
# Input :- "Tarun is Where"
# Output:- "Where is Tarun"

# string1 = "Tarun is Where"
# list = string1.split()
# list = list[::-1]
# string2 = " ".join(list)
# print(string2)  

# Question 2:- In a list print those elements who occur at once..

list_1 = [1,2,2,3,3,4,5,6,5,6,7]
new_list = []
for num in list_1:
    if list_1.count(num)==1:
        new_list.append(num)
print(new_list)



# Question 3:- count the occurence no of a variable...
# Input = my_str = "a,a,a,b,b,c,c,c"
# Output = a:3, b:2, c:3
my_str = "a,a,a,b,b,c,c,c"
mylist = my_str.split(',')
visited = []
final_list = []
for ch in mylist:
    if ch not in visited:
        final_list.append(f"{ch}:{mylist.count(ch)}")
        visited.append(ch)
print(final_list)
print(",".join(final_list))