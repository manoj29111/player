count=0
j=0
m=raw_input().lower()
n=raw_input().lower()
if m==n:
    print("NO")
else:
    for i in m:
        if i==n[j]:
            j+=1
        else:
            j+=1
            count+=1
            if count>1:
                break
    if count==1:
        print("YES")
    else:
        print("NO")
