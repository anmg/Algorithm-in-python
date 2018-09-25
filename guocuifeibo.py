def febonaqi(num):
    a=0
    b=1
    print a
    print b
    count=2
    while(count<num):
        
        temp=a
        a=b
        b=a+temp
        count=count+1
    print b
febonaqi(5)
        
