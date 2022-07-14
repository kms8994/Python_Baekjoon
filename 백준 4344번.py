c = int(input())

list_a = []

for i in range(c):
    list_b = list(map(int, input().split()))
    stack = 0
    avg = sum(list_b[1:]) / list_b[0]
    
    for score in list_b[1 : ]:
        if score > avg:
            stack += 1

    ans = stack / list_b[0] * 100
    print(f'{ans:.3f}%')

'''n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')'''
