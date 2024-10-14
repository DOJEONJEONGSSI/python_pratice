# 주석  ctrl + /
# 주석은 코드 실행에 영향을 주지 않음.
'''
 다중 주석
 코드에 영향을 주지 않음.
'''
print('hi')  # 콘솔 프린트
num = 10 # python은 타입 선언을 하지 않음
print(num, type(num))
# type() <- 내장함수 변수의 타입을 리턴함.
num = 3.14 # 다른 타입을 할당 해도 오류 안남.
print(num, type(num))
# 변수는 예약어 사용이 안되며 스네이크 표기법을 사용함.
mem_nm = "Hello, Nick"
msg = '''
    문자열이 길때 """ 작은 따옴표 or 따옴표 3개로 열고 닫음 
'''
print(msg)
print('Hello' * 100)  # 문자열 곱하기 가능
nm = mem_nm.replace('Hello', 'hi')
print(nm)
arr = nm.split(',') # 구분자로 잘라서 배열로 리턴.(디폴트 공백1)
print(arr)
# 동적배열(Dynamic Array)
#  [] <-- 비어 있는 배열
arr2 = [1, True, "Hi", [2, 3 , ['Nick']]] # type 자유로움.
print(arr2[1])        # index 1번 value 접근
print(arr2[3][2])     # index 3번에 2번째 요소
print(arr2[3][2][0])  # index 3번에 2번째에 0번째 요소
print(arr2[-1])       # 마지막 요소
arr3 = [1, 2, 3, 4, 5] * 10  # 배열 곱하기 가능
print(arr3)
# 슬라이스 가능
print(arr3[1:4]) # 1 인덱스 부터 4인덱스 -1 까지
print(arr3[ :3]) # 처음 부터 3 인덱스 -1 까지
print(arr3[3: ]) # 3인덱스 부터 끝까지 
print(len(arr3))  # len 사이즈를 리턴

# 튜플 배열과 같이 인덱스로 데이터에 접근하며 슬라이싱을 지원 (하지만 수정이 안됨)
t = (1, 3, 5)  # 수정이 안되기 때문에 초기값을 할당해야함.
print(t[-1])
print(t[0])
print(t[1:])
t2 =  (7, 8)
t3 = t + t2 # 병합
print(t3)
# t3[1]= 1   오류남. 튜플은 수정이 안됨.
# dictionary (dict)  key-value 쌍을 요소로 가지는 자료형
# {} 비어있는 딕셔너리
mate = {"팽수": 100, "길동":90 , '동길':80 }
print(mate, type(mate))
print(mate['팽수']) # key로 value접근
mate['팽수'] = 99   # 수정
print(mate.items())
# set 중복을 허용하지 않으며
# set() <-- 비어있는 set 선언
lotto = {1, 2, 2, 4, 5, 6}
print(lotto, type(lotto))
# {}로 표현하지만 {} 선언은 비어있는 딕셔너리
my_set = {}
print(my_set, type(my_set))
my_set = set()
print(my_set, type(my_set))



