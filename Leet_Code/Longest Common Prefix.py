x = ["cir","car"]
result = ''
compTemp = ''
if (x is not None and len(x)!=0):
    result = str(x[0])
    for i in range(1,len(x)):
        temp = x[i]
        for j in range(min(len(result),len(temp))):
            if result[0]!=temp[0]:
                print("空的:",'')
            if result[j] == temp[j] :
                compTemp = compTemp + temp[j]
            else:
                break
        result = compTemp
        compTemp = ''
print('{}為字串最長連續字串'.format(result))
                
            
