# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)

import math
from math import pi
d = len(input("Введите число d c заданной точностью:\n").split(".")[1])
print(f"число π с заданной точностью {d} = {round(pi, d)}")
