
n = 5

print( ' '*(n-1) + str(1) )

for i in range(n-2) :
    print( ' '*(n-2-i) + str(i+2) + ' '*(1+2*i) + str(i+2) )

print( str(n)*(2*n-1) )
