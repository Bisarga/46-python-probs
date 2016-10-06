def is_member(v1,l1):
    for v in l1:
        if v1 == v:
            return True
    return False


val1 = raw_input("Enter the string u want to search : ")
user_input = raw_input("Prepare the list : ")
list1 = map(str, user_input.split(','))
print(is_member(val1,list1))
