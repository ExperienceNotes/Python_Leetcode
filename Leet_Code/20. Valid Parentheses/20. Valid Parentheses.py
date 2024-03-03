class Solution:
    def left_item(self, item) -> str:
        if item == ')':
            return '('
        elif item == ']':
            return '['
        return '{'
    def isValid(self, s: str) -> bool:
        temp = []
        for item in s:
            if item in ['(', '[', '{']:
                temp.append(item)
            elif temp!= []:
                if temp[-1] == self.left_item(item):
                    temp.pop()
                else:
                    return False
            else:
                return False
        return temp == []
