import os
root ="C:\\"
# 파일 시스템의 디렉토리 트리를 반복적으로 순회
# 주어진 경로의 하위 디렉토리와 파일을 재귀적으로 탐색
# root:현재 디랙토리 경로, dirs:하위 디랙토리 목록
# files:해당디랙토리 내의 파일 목록
# for root, dirs, files in os.walk(root):
#     print(root, dirs, files)
# 시작 경로, 찾을 파일명을 입력받아
# 찾으면 찾았 습니다. & 파일 전체 경로 출력.
# 함수로 생성->재귀함수 및 중첩 for문을 사용할 경우 return으로 멈춤
# 1.files에 파일이 있으니 해당 배열에서 찾고자하는 파일이 있는지
# 2.있으면 경로 출력.



import os
def fn_search(dir, file_nm):
    # 현재 디렉토리부터 시작하여 모든 하위 디렉토리 탐색
    for root, dirs, files in os.walk(dir):
        print(root)
        for file in files:
            if file_nm in file:
                full_path = os.path.join(root, file_nm)
                print("=" * 100)
                print(file)
                # 사용자에게 삭제 여부를 묻기
                user_input = input("이 파일이 맞나요? (y/n): ").lower()
                if user_input == 'y':
                    print("파일을 찾았습니다.")
                    print(os.path.join(root, file))
                    print("=" * 100)
                    return
    print("파일을 찾을 수 없습니다.")
    print("=" * 100)

if __name__ == '__main__':
    while True:
        msg = input("찾을 시작경로, 파일명을 입력하세요 (종료q):").split()
        if msg[0] == 'q':
            print("종료 합니다.")
            break
        fn_search(msg[0], msg[1])