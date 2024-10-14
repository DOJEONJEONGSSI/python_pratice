import math
# math모듈 안에 있는 factorial 함수 호출
print(math.factorial(5))
from math import factorial as f
# math모듈 안에 있는 factorial함수를 f 로 별칭을 붙여서 호출
print(f(10))
import luck
print(luck.make_lotto())