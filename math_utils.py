def is_prime(a):
    factor=0
    for i in range(1,a+1):
        if a%i==0:
            factor=factor+1
    if factor==2:
            print("PRIME") 
    else:
            print("NOT PRIME")