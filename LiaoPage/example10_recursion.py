# -*- coding: utf-8 -*-
# Hanoi Tower problem
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)   # move the 1~n-1 from A to B
        print(a, '-->', c)   # move the n from A to C
        move(n-1, b, a, c)   # move the 1~n-1 from B to C
    return


# input
n0 = int(input('please input the number of objects on pillar A:'))
move(n0, 'A', 'B', 'C')