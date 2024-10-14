'''
    try 블록에서 오류가 발생하면
    except 블록에서 잡아서 처리할 수 있음.
    finally:오류,정상 모두 마지막에 실행
    else:정상만 실행
'''
print("프로그램 시작")
try:
    print("1")
    # result = 10 / 0
    a = "팽수"
    print(a[2])
    print("2")
except ZeroDivisionError as e:
    print(f"영을 왜 나눠.. {e}")
except Exception as e:
    print(f"예외가 발생 {e}")
else:
    print("난 정상 일때만 일해")
finally:
    print("오류가 나도, 정상 처리가 되도 나는 일함..")
print("프로그램 종료")
