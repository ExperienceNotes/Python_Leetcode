s = "A man, a plan, a canal: Panama"
s_1 = ''
flag = 0
for i in s:
    if i.isalnum():
        s_1 += i.lower()
if s_1 == '':
    print('T')

for i in range(len(s_1)):
    if s_1[i] == s_1[(len(s_1)-1)-i]:
        pass
    else:
        print('F')
        flag = 1
        break
if flag == 0:
    print('T')