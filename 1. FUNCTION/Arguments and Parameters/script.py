def get_sum (start, end):
    s = 0
    for i in range(start, end +1):
        s += i
    return s
x = get_sum(1, 10)
print(x)