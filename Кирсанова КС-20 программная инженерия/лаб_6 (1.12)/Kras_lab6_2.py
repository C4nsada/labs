n = int(input())
f2 = lambda c: c+c

def f1(f, n):
    return f(n) + n


print(f"{f1(f2, n)}")