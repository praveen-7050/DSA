#  to import an array
# import array
# synatx => array(type_code,[])
# arr = array.array("i",[1,2,3,5,6])
# import array as ar # using alsis
# arr = ar.array("i",[1,2,3,4,5])
# from array import  *
# arr = array("i",[1,2,3,4,5,6])
from array import array
# arr = array("f",[1,2,3.4,4.4,5.6,-1])
# arr = array("u",['a','b','c'])
# print(arr)1
arr = array("i",[1,2,3,4,5,6])
print(arr[5])  #o(1)
# for i in arr :
#     if i ==5:
#         break
#     print(i)
for i in range(0,len(arr)):
    if arr[i]== 4:
        print(f"index == {i}")
        break
arr.insert(6,7) #o(1) because we manually also insert the value at the last 
# arr.insert(3,4) #0(n)
# arr.pop() #o(1)
arr.pop(4)  #0(n)
arr.append(8) #0(1)
print(arr)