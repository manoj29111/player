try:
	b=0
	p=str(raw_input())
	a=[]
	m=str()
	for i in range (0,len(p)):
		a.append(p[i])
	if len(p)%2==0:
		j=len(p)
	else:
		j=len(p)-1
	while(b!=j):
		t=a[b]
		a[b]=a[b+1]
		a[b+1]=t
		b=b+2
	for i in range (0,len(a)):
		m=m+a[i]
	print m
except:
	print("Invalid")
