
n = int( input("> ") )

for i in range(n) :

    print( str(i+1)*(i+1) +
           str(n-i)*(2*n-1-2*i) +
           str(i+1)*(i+1) )
    
