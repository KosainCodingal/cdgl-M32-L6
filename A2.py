keypad = [
    '',
    '',
    'abc',
    'def',
    'ghi',
    'jkl',
    'mno',
    'pqrs',
    'tuv',
    'wxyz'
]

def keypadCombs(comb, cur, out, n):
    if cur == n:
        print(*out,sep=", ")
        return
    
    for i in range(len(keypad[comb[cur]])):
        out.append(keypad[comb[cur]][i])
        keypadCombs(comb, cur+1, out, n)
        out.pop()
        if comb[cur] in (0, 1): return


combination = [4, 3, 4]
n = len(combination)
keypadCombs(combination, 0, [], n)