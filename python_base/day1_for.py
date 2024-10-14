# 반복문 for
arr = ['팽수','길동','동길']
# 방법1. 값만 필요 할때
for v in arr:
    print(v)
# 방법2. 값,인덱스 둘다 필요 할때
for idx, val in enumerate(arr):
    print(idx, val)
# 방법3. 단순 횟수 반복
for i in range(3):
    print(i)
for i in range(len(arr)):
    print(arr[i])

for i in range(1, 4):
    print(i) # 1 부터 ~ 4-1까지
for i in range(2, 11, 2):
    print(i) # 2 부터 11-1 까지 2씩 증가

# 딕셔너리 for문
# 키-값 으로 순서를 보장 하지 않지만, 3.6 이후 부터 보장함.
dic = {"수학":100, "영어":60, "국어":90}
for k in dic:
    print(k, dic[k])