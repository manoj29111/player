m=input()
n=input()
s=0
while True:
    m=m+1
    if m%2==0:
        d=0
    elif m>=n:
        break
    else:
        s+=1
print(s)
