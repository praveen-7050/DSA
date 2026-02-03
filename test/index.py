# count
def counting (x):
    count=0
    for i in x:
        count+=1
    return count
x={1,2,3,2,3,4,5}
print(counting(x))
# -------------------------------------
# reverse a string
def revstr(y):
    rev=""
    for i in y:
        rev=i+rev
    return rev
y = "praveen"
print(revstr(y))
# ----------------------------------
# count of odd numbers 
def oddnumbers():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    count = []
    for i in numbers:
        if i%2!=0:
            count.append(i)
    return count

print(oddnumbers())
# ----------------------------------------------
# reverse a number
def revnum(z):
    rev = 0
    while z > 0 :
        digit = z%10
        rev = rev*10 +digit
        z //=10
    return rev
z = 12345
print(revnum(z))       
# ------------------------------------------------
# occurance
def occurance(occur,char):
    count = 0
    for i in occur:
        if i==char:
            count+=1
    return count
        
occur = "praveen"
char ="e"
print(occurance(occur,char))
# ------------------------------------------
# occurance 2
def occurance2(occur):
    dic={}
    for i in occur :
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic
occur = "ocuuranceee"
print(occurance2(occur))
# ---------------------------------------------------
# factorial
def fact(n):
    if n ==1:
        return 1
    else:
       return n*(fact(n-1))
print(fact(5))
# --------------------------------------------
# palindrome
def palindrome(x):
    s=str(x)
    l=0
    r=len(s)-1
    while l<=r:
        if s[l]==s[r]:
            l+=1
            r-=1
        else:
            return False
    return True    

print(palindrome("level"))
print(palindrome("lvel"))
# ---------------------------------------
# fabinocii series
def fabi():
    a,b =0,1
    result =[]
    for i in range(10):
        result.append(a)
        a,b = b,a+b
    return result
print(fabi())
# -----------------------------------
# anagram
def anagram(char1,char2):
    dic={}
    if len(char1)!=len(char2):
        return False
    for i in char1:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for j in char2:
        if j not in dic:
            return False
        else:
            if dic[j]==1:
                del dic[j]
            elif dic[j]>1:
                dic[j]-=1
    if dic == {}:
        return True
    else:
        return False
            
        
print(anagram("listen","slient")) 
print(anagram("listen","lient")) 
print(anagram("listen","liennt")) 
# -------------------------------------------
# linear search algo
def linearsearch(x):
    arr=[1,2,3,4,5,6,7,8,10,5,6]
    for i in range(0,len(arr)):
        if arr[i] == x:
            return i
    else:
        return f"not found"
print(linearsearch(5))
# ------------------------------------------


        