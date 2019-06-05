arr = []

def parens(left,right,string):
    if left == 0 and right == 0:
        arr.append(string)

    if left > 0:
        parens(left-1,right+1,string + "(")

    if right > 0:
        parens(left, right-1, string + ")")

parens(2,0,"")
print(arr)
