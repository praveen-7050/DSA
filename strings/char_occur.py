# count how many times the value is ocuuring 

str1 = "praveen"
occur ='e'
count =0

for i in str1 :
    if i == occur :
        count += 1
    
print(f"the letter '{occur}' is occurred in the string is {count}")

# this is to count a single letter

# ----------------------------------------------------------------------------------------------------------

str2 = "occurancee"

freq ={}


for char in str2:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
        
print(freq)
#  using the dictorany 
# -------------------------------------------------------
from collections import Counter
str3 = "siueenurrdrjwweefoaxffnf"
freq2  =Counter(str3)
print(freq2)
# -----------------------------------------------------------------