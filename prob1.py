#Define a function max() that takes two numbers as arguments and returns the largest of them.
#Use the if-then-else construct available in Python. 
#(It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)

def max(n1,n2):
    if(n1 > n2):
        return n1
    else:
        return n2
num1 = input("Enter n1 : ")
num2 = input("enter n2 : ")
print "Max number is :" + str(max(num1,num2))
