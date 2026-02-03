def my_length(item):
    count = 0 
    for _ in item:
        count+=1
    return count

word = "python"
print(my_length(word))
list1 = [1,2,3,4,5,6]
print(my_length(list1)-1)
# -------------------------------------------
def my_length1(item):   
    counting =0 
    for _ in item :
      counting +=1
    return counting
print(my_length1("praveen"))
# ------------------------------------------------------------------
name1="762"
name2="123"
if my_length1(str(name1))==my_length1(str(name2)):
    print("true")
else:
    print("false")
    