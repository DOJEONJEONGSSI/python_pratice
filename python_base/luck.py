import random
# 함수명  : make_lotto
# input  : 없음
# output : 로또 번호
def make_lotto():
    user_lotto = set()
    while len(user_lotto) < 6:
        number = random.randint(1, 45)
        user_lotto.add(number)
    return sorted(list(user_lotto))
# list.sort()  <-- 리스트 자체를 정렬
# sorted(list) <-- 정렬된 새로운 리스트를 리턴
arr = make_lotto()
arr.sort()  # 기본 오름 차순 정렬
# arr.sort(reverse=True) # 내림차순 정렬
# print(arr)

# 함수명  : user_lotto
# input  : 0 ~ n
# output : 로또번호, 'x x 번호가 적용된 로또 번호' <-- message리턴
# 사용자가 입력한 번호를 포함시켜서 로또번호 생성
# 단 6개 이상이 들어오면 5개까지 포함시키고 1개 랜덤값

def user_lotto(*args):
    user_num = list(args)[:5]
    print(user_num)
    m = ','.join(map(str, user_num)) + " 번호가 적용된 로또"
    lotto = set(user_num)
    while len(lotto) < 6:
        number = random.randint(1, 45)
        lotto.add(number)
    return m, sorted(list(lotto))

if __name__ == '__main__': #모듈내 실행일 경우 True
    arr = [1, 2, 3]
    message = ','.join(map(str, arr))  # map(function, iterable)
    print(message)
    arr2 = ['1','2','3']
    message2 = ','.join(arr2)
    print(message2)
    print(user_lotto(1,2,3))
else: # 다른 모듈에서 실행 했을 경우
    print("임포트 했군...")








