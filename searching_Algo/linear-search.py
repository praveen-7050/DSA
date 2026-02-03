#linear search 
arr=[1,2,3,4,5,5,6,6,7,8,6]
x =3
for i in range(0,len(arr)): # to check the index and the value of the element x
    if arr[i]==x:
        print(i)
        break
else:

    print("! not found ") 