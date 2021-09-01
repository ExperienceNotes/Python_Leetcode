number = input('請輸入一個隨機整數:')
reverse = ''
if eval(number) < 0:
    for i in range(len(number)-1,-1,-1):
        if (number[i] == '0'and reverse == '')or number[i] == '-':
            pass
        else:
            reverse +=number[i]
    reverse = eval(reverse)
    reverse = reverse-2*reverse
elif eval(number) == 0:
    print(0)
else:
    for i in range(len(number)-1,-1,-1):
        if (number[i] == '0'and reverse == ''):
            pass
        else:
            reverse +=number[i]
    reverse = eval(reverse)
if 2**31-1<reverse or -2**31>reverse:
    reverse = 0
print(reverse)