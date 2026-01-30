x=int(input() )
y=int(input() )
z=int(input() )
n=int(input() )
list_com =[]
for i in range(0,x+1,1):
    for j in range(0,y+1,1):
        for k in range(0,z+1,1):
             if(n==i+j+k):
                 continue
             list_com.append([i,j,k])
print(list_com)

     
      
      
        

 