# !/usr/bin/python3
from union.union_intersection import *

while(True):
    num = int(input("Select menu: 1)b2h 2)set 3)fibo 4)exit ? "))
    if num == 1:
        bin = input("inpyut bin number: ")

    elif num == 2:
        data1 = list(map(int, input("input the 1st list: ").split()))
        data2 = list(map(int, input("input the 2nd list: ").split()))
        union(data1, data2)
    elif num == 3:
        f = int(input("fibonacci number: "))

    elif num == 4:
        print("exit the program...")
        break

    else:
        print("Invalid num!!")
