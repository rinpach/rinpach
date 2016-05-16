x = 0
while x < 1:
    n=input('整数を入れて下さい＞')
    if n%15==0:
        print("Fizz Buzz")
    elif n%3==0:
        print("Fizz")
    elif n%5==0:
        print("BUZZ")
    else:
        print(n)
    a=input('終了：1 続行：0＞')
    if a==1:
        break
