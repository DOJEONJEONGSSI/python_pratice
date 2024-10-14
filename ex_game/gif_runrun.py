import tkinter as tk
import random
from PIL import Image, ImageTk, ImageSequence  # ImageSequence로 GIF 프레임을 처리 (안그러면 스틸이미지로 나옴)


class HorseRace:
    def __init__(self, root):
        self.root = root
        self.root.title("경마 게임")
        self.canvas = tk.Canvas(self.root, width=1000, height=400)
        self.canvas.pack()

        self.horses = []  # 말의 이미지 객체 리스트 (애니메이션 포함)
        self.positions = []  # 말의 현재 위치
        self.num_horses = 5  # 말의 수
        self.running = False  # 경주가 진행 중인지 확인하는 플래그
        self.winner_declared = False  # 승리자가 이미 선언되었는지 확인하는 플래그

        # 애니메이션 프레임 리스트를 위한 변수
        self.frames = []  # 각 말의 애니메이션 프레임을 저장

        # 결승선 추가 (칠할 위치는 700px)
        self.draw_finish_line()

        # 말 이미지를 로드하고 초기 위치를 설정
        self.create_horses()

        # 시작 버튼 생성
        self.start_button = tk.Button(self.root, text="경주 시작", command=self.start_race)
        self.start_button.pack()

    def draw_finish_line(self):
        """결승선을 캔버스에 그립니다."""
        finish_x = 900  # 결승선의 X 좌표
        self.canvas.create_rectangle(finish_x, 0, finish_x + 10, 400, fill="red")  # 결승선 색상을 빨간색으로 설정

    def create_horses(self):
        """경주에 참가하는 말들을 생성하고 초기 위치를 설정합니다."""
        for i in range(self.num_horses):
            # 애니메이션 GIF 파일 로드
            gif_image = Image.open("horserun.gif")

            # GIF의 모든 프레임 로드, RGBA로 변환하여 투명 배경 유지
            frames = [ImageTk.PhotoImage(frame.convert("RGBA")) for frame in ImageSequence.Iterator(gif_image)]

            # 첫 번째 프레임을 캔버스에 그리기
            horse = self.canvas.create_image(50, 50 * (i + 1), image=frames[0], anchor=tk.NW)
            self.horses.append((horse, frames))  # 말과 프레임 리스트 저장
            self.positions.append(50)  # 초기 위치를 50으로 설정
        self.canvas.update()

    def animate_horses(self):
        """말 애니메이션을 주기적으로 업데이트합니다."""
        for i, (horse, frames) in enumerate(self.horses):
            current_frame = self.positions[i] // 5 % len(frames)  # 현재 말의 프레임 인덱스를 계산
            self.canvas.itemconfig(horse, image=frames[current_frame])  # 프레임 업데이트
        self.canvas.update()

    def move_horses(self):
        """말을 한 번씩 움직이고, 계속해서 경주가 진행되도록 합니다."""
        if self.running and not self.winner_declared:
            for i in range(self.num_horses):
                move_distance = random.randint(5, 30)  # 말이 움직이는 랜덤한 거리
                self.positions[i] += move_distance

                # 말의 위치를 업데이트 (마지막 850까지 이동) 결승선은 900이지만 말 width때문
                if self.positions[i] < 850:
                    self.canvas.coords(self.horses[i][0], self.positions[i], 50 * (i + 1))
                else:
                    self.positions[i] = 850  # 결승선에서 멈춤

                    # 말이 결승선에 도착하면 승리 메시지 표시
                    if not self.winner_declared:
                        self.winner_declared = True  # 승리자가 선언됨
                        self.canvas.create_text(400, 50 * (i + 1) + 15, text=f"말 {i + 1} 승리!", fill="green",
                                                font=("Arial", 16))
                        break  # 승자가 나오면 나머지 말의 경주를 멈춤

            # 애니메이션 프레임 업데이트
            self.animate_horses()

            # 100ms마다 move_horses 함수가 다시 호출되도록 설정
            self.root.after(100, self.move_horses)

    def start_race(self):
        """경주를 시작하고, 말이 움직이도록 합니다."""
        self.running = True
        self.winner_declared = False  # 경주 시작 시 승리자 상태 초기화
        self.start_button.config(state=tk.DISABLED)  # 버튼 비활성화
        self.move_horses()


# Tkinter 애플리케이션 실행
if __name__ == "__main__":
    root = tk.Tk()

    # Pillow 사용을 위해서 'Pillow' 패키지가 설치되어 있어야 합니다.
    # 설치 명령: pip install pillow
    game = HorseRace(root)
    root.mainloop()
