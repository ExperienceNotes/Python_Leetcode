s = "abcabcbb"
sub_str = ''
max_len = 0
for i in s:
    while i in sub_str:
        sub_str = sub_str[1:]
    else:
        sub_str += i
        max_len = max(len(sub_str),max_len)
print('Logest substr:',max_len)