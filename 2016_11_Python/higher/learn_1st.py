# 必须要用 **kwargs.items() 来迭代字典中的值
# 用 kwargs 做参数的时候需要把字典的值设成和函数参数一致
def greet_me(x, *thelist, **thedict):
    print(x)
    for l in thelist:
        print(l)
    for key, value in thedict.items():
        print("{0} == {1}".format(key, value))

greet_me(1, '1', '3', '2', name="11", name2="22", name3="33")


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

arg = [x for x in range(5) if x % 2 == 0]
kwargs = {'arg1': 'one', 'arg2': 'two', 'arg3': 'three'}
test_args_kwargs(*arg)
test_args_kwargs(**kwargs)


# 生成器
def test_generation(x):
    prev, aft = 1, 1
    for i in range(x):
        yield prev
        prev, aft = aft, prev + aft
# 第一种使用迭代器的 yield 的方法
for item in test_generation(5):
    print(item)
# 第二种使用 yield 的方法(此处情况貌似只适用于第一种)
print(next(test_generation(3)))
print(next(test_generation(3)))
print(next(test_generation(3)))
# 把字符变成可迭代对象
s = "Watson"
# next(s)会报错, 此处使用 iter() 方法
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

# map
lists_1 = [x for x in range(10)]
lists_2 = [x for x in range(-5, 6)]
after_map = list(map(lambda x: x**3, lists_1))
after_filter = list(filter(lambda x: x > 0, lists_2))
print(after_map)
print(after_filter)
from functools import reduce
lists_3 = [x for x in range(10)]
# 相当于 1~9 的等差数列
after_reduce = reduce((lambda x, y: x + y), lists_3)
print(after_reduce)