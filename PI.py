import time
pi=3
i=1000000
x=2
t= time.time()
for n in range(i):
    if n & 1:
        pi -= 4/(((2*n)+2)*((2*n)+3)*((2*n)+4))
    else:
        pi += 4/(((2*n)+2)*((2*n)+3)*((2*n)+4))
    # x = ((2*n)+2)
    #print(x, " " , n)
    #x +=2
#    print(x, " " , n)
    print(n, " " , pi)
print(time.time()-t)