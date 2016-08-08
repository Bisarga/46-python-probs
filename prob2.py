def max_of_three(n1,n2,n3):
    try:
        if(n1 > n2 and n1 > n3):
            return n1
        elif(n2 > n1 and n2 > n3):
            return n2
        else:
            return n3
    except:
        print "Can't enter strings"

num1 = int(input("Enter n1 : "))
num2 = int(input("Enter n2 : "))
num3 = int(input("Enter n3 : "))
print "Max of Three is :  " + str(max_of_three(num1,num2,num3))
