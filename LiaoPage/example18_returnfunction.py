# -*- coding: utf-8 -*-

def createcounter():
    n = 0

    def counter():
        nonlocal n  # nonlocal declares variables are not local or global, but variables within an outer function
        n = n + 1
        return n
    return counter


# 测试:
counterA = createcounter()  # return the counter function
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createcounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')