def pallindrom(n):
	a=str(n)
	b=a[::-1]
	if(a==b):
		return True
p=0
lp=0
for i in range(100,1000):
	for j in range(100,1000):
		p=i*j
		if(pallindrom(p)):
			if(p>lp):
				lp=p
print(lp)
