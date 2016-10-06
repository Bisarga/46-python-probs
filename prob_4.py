def check_vowels(c1):
    for c in c1:
        if c in 'AEIOUaeiou':
            return True
        else:
            return False


chr1 = raw_input("Enter the character : ")
print check_vowels(chr1)
