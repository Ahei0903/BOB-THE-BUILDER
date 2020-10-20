
n = int( input("> ") )

for i in range(n-1) :
    s1 = i
    n1 = (1 + i)%10
    s2 = 2*n-3 - 2 * i
    n2 = ((2*n-1)-i)%10
    print( ' '*s1 + str(n1) + ' '*s2 + str(n2) )

print( ' '*(n-1) + str(n%10) )

#i=0 1 2


    
