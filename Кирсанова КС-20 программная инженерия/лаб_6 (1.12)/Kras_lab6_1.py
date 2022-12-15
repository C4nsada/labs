n = int(input())
c = int(input())

f1 = lambda c: c+n
f2 = lambda n: f1(c)

print (f"{f2(n)}")
