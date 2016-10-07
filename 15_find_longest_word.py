def find_longest_word(l1):
    longest = ""
    for word in l1:
        if len(word) > len(longest):
            longest = word
    return longest


user_input = raw_input("Make A String List:  ")
list1 = map(str, user_input.split(','))

print find_longest_word(list1)
