def prime(n,i):
    if i==1:
        return 1
    else:
        if n%i==0:
            return 0
        else:
            return prime(n, i-1)
n=int(input())
check = prime(n, n//2)
if check == 1:
    print("Prime Number")
else:
    print("Not a Prime Number")
        
        
