def overlapping(l1,l2):
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False

u_input1 = raw_input("Enter list1 data: ")
list1 = map(int, u_input1.split(','))

u_input2 = raw_input("Enter list2 data: ")
list2 = map(int, u_input2.split(','))

print overlapping(list1,list2)
