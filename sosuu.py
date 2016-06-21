import soinsu_bunkai
a=1
for n in range(10000):
	b=soinsu_bunkai.soinsu(a)
	if b==a:
		print(a)
	if a==1453:
		c=input('OK?')
	a+=1
