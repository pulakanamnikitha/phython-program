import string
Input = string.upper(raw_input())
I = string.count(Input, "I")
V = string.count(Input, "V")
X = string.count(Input, "X")
L = string.count(Input, "L")
C = string.count(Input, "C")
D = string.count(Input, "D")
M = string.count(Input, "M")
if I > 3 or V > 2 or X > 3 or L > 3 or C > 3 or D > 3 or M > 3:
    print Input[0],"'s."
else:
    if I < 3:
        equation = I * 1 + V * 5 + X * 10 + L * 50 + C * 100 + D * 500 + M * 1000
        print   equation
