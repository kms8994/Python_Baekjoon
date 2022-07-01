h, m = map(int, input().split())
t = int(input())

m += t

if m >= 60:
    
    h += m // 60
    m %= 60
    
    if h > 23:
        h -= 24

print(h, m)
