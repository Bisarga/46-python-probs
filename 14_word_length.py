def word_length(l1):
    lenlist = [len(word)for word in l1]
    return lenlist

u_input1 = raw_input("MAKE A WORD LIST: ")
list1 = map(str, u_input1.split(','))

print word_length(list1)      
