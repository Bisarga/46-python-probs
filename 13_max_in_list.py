def max_in_list(l1):
    max = 0
    for i in l1:
        if i > max:
            max = i
    return max

u_input = raw_input("Enter numbers: ")
list1 = map(int, u_input.split(','))

print max_in_list(list1)
