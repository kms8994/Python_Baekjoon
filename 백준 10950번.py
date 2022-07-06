n = int(input())
arr = []

for i in range(n):

    a, b = map(int, input().split())

    add = a + b

    arr.append(add)

for k in range(n):
    print(arr[k])
