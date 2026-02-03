# Anagrams
# Two strings are anagrams if they contain the same characters with the same frequency, just rearranged. Order doesn’t matter; counts do.
# Examples:
# -----------------------------
# listen ↔ silent ✅
# evil ↔ vile ✅
# rat ↔ car ❌
# ---------------------------- 
# using in bulit method
def is_anagram(s,t):
    return sorted(s)== sorted(t)

print(is_anagram("listen","silent"))
#-----------------------------------------------

def anagram(var1,var2):
    dic1 ={}
    dic2 = {}
    for char in var1:
        if char in dic1:
            dic1[char]=+1
        else:
            dic1[char]=1
    for char in var2:
        if char in dic2:
            dic2[char]=+1
        else:
            dic2[char]=1
    if dic1 == dic2:
        print("it is an anagram") 
    else :
        print("it is not an anagram")       
# print(dic1,dic2)

# anagram("hello","hello")
# ----------------------------------------------------
def anagrams2(ana,ana1):
    dic={}
    for i in ana:
        if i not in dic :
            dic[i]=1
        else:
            dic[i]+=1
    for j in ana1:
        if j not in dic:
            # print("It is not an anagram")
            return False
        else:
            if dic[j]==1:
                del dic[j] 
            elif dic[j]>1:
                dic=-1
        if dic == {}:
            # print("This is anagram")
            return True
        else:
            # print("This is not an anagram")
            return False
    
anagrams2("slient","listen")