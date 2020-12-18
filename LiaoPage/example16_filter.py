# _*_ coding:utf-8 _*_
# ----------------example------------------
# generate an odd series from 3
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# filter function
def _not_divisible(n):
    return lambda x: x % n > 0


# primes
def primes():
    yield 2
    it = _odd_iter()  # initial series
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)  # new series


# print the primes lower than 1000
for y in primes():
    if y < 1000:
        print(y)
    else:
        break


# ----------------exercise 1------------------
def is_palindrome(n):
    m = str(n)
    m1 = m[::-1]  # reverse the number
    return n == int(m1)


# test
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')