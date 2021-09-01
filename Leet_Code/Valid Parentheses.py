s = '(('
list_s = []

top = -1
if len(s) == 1:
    print('F')
else:
    for i in s:
        if i == '(' or i == '[' or i == '{':
            list_s.append(i)
            top+=1
        else:
            if list_s[top] == '(' and i == ')':
                top-=1
                list_s.pop()
            elif list_s[top] == '[' and i == ']':
                top-=1
                list_s.pop()
            elif list_s[top] == '{' and i == '}':
                top-=1
                list_s.pop()
            else:
                print('F')
    if len(list_s) == 0:
        print('T')
    else:
        print('F')