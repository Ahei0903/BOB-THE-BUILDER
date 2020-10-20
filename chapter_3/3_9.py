
n = int( input("> ") )

for i in range(2*n-1) :

    s = abs(i-(n-1))
    m = (n - abs(i-(n-1)))%10
    p = 2*n-1 - 2 * abs( i-(n-1) )

    print( ' '*s + str(m)*p )
