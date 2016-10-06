def sum(l1):
    result = 0
    for i in l1:
        result += i
    return result

def multiply(l1):
    result = 1
    for i in l1:
        result *= i
    return result

user_input = raw_input("Create a  number List ::  ")
l = map(int,user_input.split(','))
print sum(l)
print multiply(l)
