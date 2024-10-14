# 로또번호 생성
# 사용자 입력 수량 만큼
# 1 ~ 45 의 6자리 로또 번호를 생성 하여 출력 하시오.
# 6개의 1 ~ 45 는 중복이 있으면 안됨 {1, 2, 2, 3, 4, 5} X안됨
import random
# 비어 있는 set()
ex = set()
# 요소 추가
ex.add(5)
print(ex)
# set 길이
print(len(ex))



# 사용자에게 입력받은 수 만큼 로또번호 생성
cnt = int(input("몇개 생성할까요?:"))
# 입력 수 만큼 반복
for i in range(cnt):
    user_lotto = set()
    while len(user_lotto) < 6:
        number = random.randint(1, 45)
        user_lotto.add(number)
    print(f"행운의 로또 번호:{user_lotto}")