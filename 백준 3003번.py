

Num = [1, 1, 2, 2, 2, 8]

ipNum = list(map(int, input().split()))


# 0���� �̷���� 6ĭ�� ����Ʈ ����
ansList = [0 for i in range(6)]


for i in range(6):
    ansList[i] = Num[i] - ipNum[i]


# print() �Լ��� ��� ��� �� ','�� �����ִ� ����
print(' '.join(map(str, ansList)))
