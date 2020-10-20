
n = 5

for i in range(n-1,-1,-1) :
    w = ' '*(n-1-i) + str(i+1)*(i+1) + ' '
    print( w * n )