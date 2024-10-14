# 조건문 if 는 조건에 따라 코드 블록을 실행 하거나
# 실행 하지 않도록 제어함.
#  input 함수는 콘솔 입력을 받는 함수
#  int(), str(), float() <-- 타입 변환 함수
#  input은 기본 str으로 리턴됨.
num = int(input("숫자를 입력 하세요:"))
if num > 10:   # 콜론 : 으로 구분
    # 들여쓰기 된 부분이 해당 조건이 True일때 실행되는 부분
    print("입력은 10보다 큼")
elif num == 10:
    print("10 이군")
elif num < 10:
    pass  # 아무 작업도 하지 않을때
print("종료")
# None, [], 0 은 False로 인식
arr = []
if arr:
    print("if 조건 True")
else:
    print("False")

