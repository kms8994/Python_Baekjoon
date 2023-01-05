

Num = [1, 1, 2, 2, 2, 8]

ipNum = list(map(int, input().split()))


# 0으로 이루어진 6칸의 리스트 생성
ansList = [0 for i in range(6)]


for i in range(6):
    ansList[i] = Num[i] - ipNum[i]


# print() 함수의 출력 결과 중 ','를 없애주는 역할
print(' '.join(map(str, ansList)))
