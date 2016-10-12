i = 99
while i > 0:
    print """%(b)d bottles of beer on the wall, %(b)d bottles of beer.
              Take one down, pass it around, %(bn)d bottles of beer on the wall.""" % { 'b' : i, 'bn' : i-1 } 
    i = i - 1
    
