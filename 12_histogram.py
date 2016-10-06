def histogram(l1):
    for i in l1:
        print i * '*'


u_input = raw_input("Enter numbers in the list: ")
list1 = map(int, u_input.split(','))

print histogram(list1)
