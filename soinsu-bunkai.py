_n=input('>')
_n=int (_n)
_o=2
for m in range(_n):
    x=_n%_o
    if x==0:
        print(_o)
        _n/=_o
    else:
        _o+=1
