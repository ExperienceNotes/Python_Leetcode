s = input('請輸入羅馬數字:')
map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
result = 0
for i in range(len(s)):
    temp = map[s[i]]
    if i!=0 and map[s[i-1]]<map[s[i]]:
        temp = temp-map[s[i-1]]*2
    result = result + temp
print(result)