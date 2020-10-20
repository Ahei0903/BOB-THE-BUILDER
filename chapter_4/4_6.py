
n = int(input('> '))

print( str(1)*n , str(2)*n , str(3)*n , sep=' | ' )

for i in range(1,n-1) :
    print( str(i+1)+' '*(n-2)+str(i+1) ,
           str(i+2)+' '*(n-2)+str(i+2) ,
           str(i+3)+' '*(n-2)+str(i+3) , sep=' | ' )

print( str(n)*n , str(n+1)*n , str(n+2)*n , sep=' | ' )
    
