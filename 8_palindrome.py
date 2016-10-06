def is_palindrome(s1):
    return s1 == s1[::-1]

str1 = raw_input("Enter the string to check for palindrome : ")
print is_palindrome(str1)
