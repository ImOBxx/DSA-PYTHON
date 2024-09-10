def sub(st, curr, idx):
    if idx == len(st):
        print(curr, end = " ")
        return
    sub(st, curr, idx + 1)
    sub(st, curr + st[idx], idx + 1)

st = "ABC"

curr = " "

idx = 0

sub(st, curr, idx)