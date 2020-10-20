
n = 5

p = 1
for i in range(1,n+1) :
    p = p * i

for i in range(n,0,-1) :
    print( i , '! = ' , p , sep="" )
    p = p//i

    
