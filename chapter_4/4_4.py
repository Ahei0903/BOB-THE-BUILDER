
n = int(input('> '))

print( ( ' '*(n-1) + str(1) + ' '*(n-1) )*n )

for i in range(n-2) :
    print( ( ' '*(n-2-i) + str(i+2) + ' '*(1+2*i) + str(i+2) + ' '*(n-2-i) ) * n )

print( ( str(n)*(2*n-1) )* n )
