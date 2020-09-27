for x in range(1,240):
    for i in range(2,x+1):
        test=x/i
        test_1=x//i
        if(test==test_1 and x!=i):
            break
        elif(i==x):
            print(x,'is a prime number')
            #something
