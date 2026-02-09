# --coding utf-8--
import os

os.system("cls")
print("Input coefficients of lineal equation")
a = float(input())
b = float(input())
print(f"try to solve equation:{a}*x+{b}=0")
if ((a == 0) and (b == 0)):
    print("The answer is any number")
elif ((a == 0) and (b != 0)):
    print("The equation has no solution")
else:
    print(f"The equation has the following solution:{-b / a}")