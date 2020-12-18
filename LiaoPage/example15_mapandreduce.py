# _*_ coding:utf-8 _*_
from functools import reduce


def str2int(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
              '6': 6, '7': 7, '8': 8, '9': 9}

    def char2num(ss):
        return digits[ss]

    def fn(x, y):
        return x * 10 + y

    return reduce(fn, list(map(char2num, s)))


b = str2int('123456')
print(b)

# -----------------exercise 1--------------------


def normalize(name):
    name = name.lower()
    return name[0].upper()+name[1:]


# test
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# -----------------exercise 2--------------------


def prod(m):
    def mul(x, y):
        return x * y
    n = reduce(mul, m)
    return n


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# -----------------exercise 3--------------------


def str2float(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
              '6': 6, '7': 7, '8': 8, '9': 9}
    n = s.index('.')  # find the index of '.'
    s2 = s[n+1:]
    s3 = s2[::-1]  # reverse order
    if len(s3) < 2:  # request at least 2 order decimal
        pass
    else:
        def char2num(ss):
            return digits[ss]

        def ft(x, y):
            return x * 0.1 + y
    return str2int(s[:n]) + 0.1 * reduce(ft, list(map(char2num, s3)))


# test
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
