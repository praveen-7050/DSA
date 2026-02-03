#  A palindrome is a string or numbers that reads the same backward and farward
# If you reverse it and it doesn’t change, it’s a palindrome.

# String Palindrome
# "madam" ✅
# "racecar" ✅
# "level" ✅
# "hello" ❌
# Number Palindrome
# 121 ✅
# 1331 ✅
# 123 ❌

# ------------------------------------
# inbulit function
# palindromeword = input('Enter the word to check the word is an palindrome = ')
# if palindromeword==palindromeword[::-1] :
#     print('its is  a palindrome')
# else:
#     print('it is not an palindrome')
# ----------------------------------------------
# using two pointer 
def palindrome(x):
    str2 = str(x)
    left = 0
    right = len(str2) - 1
    while left < right:
        if str2[left] == str2[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
pali = input('Enter the number to check the palindrome = ')
result = palindrome(pali)
if result:
    print("It is a palindrome")
else:
    print("It is not a palindrome")