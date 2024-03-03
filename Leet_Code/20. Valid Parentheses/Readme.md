# 20. Valid Parentheses
## Input
* s: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'(給一個字串包含各種括號)

## Target
* Return determine if the input string is valid return True else False


## Example
* s = "()"
* Output = true

## Explane
* 何謂合法括號?左括號肯定會對應到右括號。
* 因此遇到左括號，先把該左括號append入list中。
* 而遇到右括號，要尋找list中最後的左括號是否配對該括號，如果沒有就回傳否
## Tip
* 如果一開始就為右括號ex. "]" 就要先判定list是否空，如空就回傳False
* 如果一開始就為左括號ex. "[" 就要最終的就要判斷temp是否空如空回傳True
