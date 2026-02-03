DSA (Data Structures and Algorithms) is the study of how data is stored, organized, and managed in a computer so it can be accessed, modified, and used efficiently, and how step-by-step procedures (algorithms) are designed to process that data effectively.
-------------------------------------------------------------------------
time complexity
O(1)-constant the program takes the same time no matter how big input is. ex.print("hi").
O(n)-linear-Time grows linearly as input grows.
O(logn)-logoarthmeic-Very efficient, grows slowly (like binary search).
O(nlogn)-lineararthemtic
O(n2)-quardic-worst case- Time grows much faster as input grows (like nested loops).
this the  most of the time complextiy occurs we have O(n3) etc.... 
-----------------------
array is like a container which we can store multiple values and mixed data type values array is stored in contigenous memory array is ordered and indexed based the array index  is start from 0,1,2...we can access the array through index array is mutable and accept duplicates we can update,add,remove,and change the array. in python there is no array they called as list


lst = [1,2,3,4,4,"praveen",10.5,True,(1,2),[10,9] ] creating the list and assiging the value 

print(lst)
print(lst[2]) # accesing through the index value - O(1) very fast
print(lst.append(11)) # appending the value to the last - O(1) very fast
print(lst.pop()) #removing the value at the last -  O (1) very fast
print(lst.pop(4)) # removing the value tyravising through the array it is - O(n) worst case slow must shift the all the items (same for remove()) 
lst.insert(2,55)  # inserting the value throught the index - O(n) slow must shift the all the items
lst.remove(2)  # remove  the value throught the value  - O(n) slow must shift the all the items
lst.index(3) # access the value through the value - O(1) very fast
print (lst) 