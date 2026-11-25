#strong or not
def strongornot(num):
    a=num
    total=0

    while num>0:
        number=num%10
        factorial=1
        for i in range(1,number+1):
            factorial=factorial*i

        total=total+factorial
        num=num//10

    if total==a:
        print("IT IS A STRONG NUMBER....")
    else:
        print("ITS NOT A STRONG NUMBER...")

n=int(input("ENTER A NUMBER :"))
strongornot(n)
print("--------------------------------------------------------------------------------------------------------------")

#find prime number btw numbers

a=int(input("ENTER THE NUMBER 1 :"))
b=int(input("ENTER THE NUMBER 2 :"))
primelist=list()
for i in range(a,b+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1

    if count==2:
        primelist.append(i)
        print("PRIME NUMBERS ARE :",primelist)
