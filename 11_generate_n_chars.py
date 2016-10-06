def generate_n_chars(n,c):
    result = ""
    for i in xrange(n):
        result += c
    return result

num = input("Enter how many time U want to repeat the chaharcter :: ")
char = raw_input("Enter the character U want to repeat::  ")
print(generate_n_chars(num,char))
