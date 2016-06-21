def soinsu(_n):
    _o=2
    for m in range(_n):
        x=_n%_o
        if x==0:
            return _o
            _n/=_o
        else:
            _o+=1
