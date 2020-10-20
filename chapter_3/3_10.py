
n = int( input("> ") )

for i in range(2*n-1) :

    s1 = abs(i-(n-1))
    s2 = 2*(n-1) - 2 * abs(i-(n-1))

    print( ' '*s1 + '*'*n + ' '*s2 + '*'*n )

