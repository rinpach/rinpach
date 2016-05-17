_high=input('身長(cm)＝')
_weight=input('体重(kg)＝')
_high=int(_high)
_weight=int(_weight)
_high/=100
_bmi = _weight/(_high**2)
print (_bmi)
