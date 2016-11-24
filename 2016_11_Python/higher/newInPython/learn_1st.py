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

# map, reduce, filter
lists_1 = [x for x in range(10)]
lists_2 = [x for x in range(-5, 6)]
after_map = list(map(lambda x: x**3, lists_1))
after_filter = list(filter(lambda x: x > 0, lists_2))
print(after_map)
print(after_filter)
from functools import reduce
lists_3 = [x for x in range(10)]
# 相当于1~9的等差数列
after_reduce = reduce((lambda x, y: x + y), lists_3)
print(after_reduce)


# set 数据结构 判断是否有重复元素
some_list = ['a', 'b', 'c', 'd', 'b', 'c', 'c']
repeat_words = set([x for x in some_list if some_list.count(x) > 1])
print(repeat_words)
# 定义方法_1
s1 = {'yellow', 'red', 'blue', 'green', 'black'}
# 定义方法_2
s2 = set(['red', 'brown'])
# 交集表示 表示方法_2：s1.intersection(s2)
# 差集表示 表示方法_2：s1.difference(s2)
print(s1 & s2)
print(s1 - s2)


# 两种三元运算符 推荐 x if expression else y (expression为真时y不执行)
its = True
print("it's true" if its else "it's false")
x = 1 if its else 0
# x = (0, 1)[its]
print(x)


# 函数可以赋值给一个变量
def hi():
    return "Hello Watson!"
greet = hi
print(greet())
del hi
print(greet())
# 函数中可以嵌套定义函数, 也可以返回函数
def say():
    def hello():
        return "Hello!"
    def watson():
        return "Watson!"
    print(hello())
    print(watson())
    return hello
say_hello = say()
print(say_hello())
# 函数可以作为参数传给函数
def hi_2():
    return "Hello Watson Again!"
def use_function(func):
    print(func())
use_function(hi_2)
# 装饰器原理
from functools import wraps
def a_new_decorator(a_func):
    # 这使得调用 a_func 了以后调用的函数名显示为 a_func
    @wraps(a_func)
    def warp_the_function():
        print("\nA dialog added by the decorator: ")
        a_func()
        print("Decorator has been executed")
    return warp_the_function
def a_function_requiring_decoration():
    print("this is a function requiring decoration")
a_function_requiring_decoration()
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()
# 下面写法与上面作用一样
@a_new_decorator
def the_other_function():
    print("this is the other function requiring decoration")
the_other_function()
# 一个装饰器用于日志的例子
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging
@logit
def addition_func(x):
    """Do some math."""
    return x + x
result = addition_func(4)
print(result)


# 不推荐用 global 关键字, 函数可以返回多个值
# __slots__作用:限定可用的属性, 降低内存消耗
class TestClass(object):
    __slots__ = ('name', 'test')

    def __init__(self, name, test):
        self.name = name
        self.test = test


class TestClass2(object):
    __slots__ = ['name2', 'test2']

    def __init__(self, name2, test2):
        self.name2 = name2
        self.test2 = test2

s = TestClass2('watson', 'tests')
print(s.test2)


# 使用 collections 库
import collections,json
colors = (
    ('name1', 'ws'),
    ('name1', 'js'),
    ('name2', 'ms'),
    ('name3', 'ks'),
    ('name3', 'ls')
)
color_list = collections.defaultdict(list)
for name, color in colors:
    color_list[name].append(color)
print(color_list)
tree = lambda: collections.defaultdict(tree) # dict也行
some_dict = tree()
some_dict['name']['color'] = 'yellow'
print(json.dumps(some_dict))


# 枚举
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1)) # 后面的数字是从第几开始计数
print(counter_list)
# 对象的自省
print(dir(my_list), type(my_list), id(my_list))
import inspect
# 查看对象的成员
print(inspect.getmembers(TestClass))


# 推导式
multiples = [i**2 for i in range(11) if i % 2 == 0]
print(multiples)
# 例子: 字典推导式
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
for k in mcase.keys()
}
# 调换键值
mcase_reverse = {v: k for k, v in mcase_frequency.items()}
print(mcase_frequency)
print(mcase_reverse)
squared = {x**2 for x in [1, 1, 2]}
print(squared)

# 列表碾平
import itertools
a_list = [[1, 2], [3, 4], [4, 5], [5, 6]]
print(list(itertools.chain.from_iterable(a_list)))
print('or', list(itertools.chain(*a_list)))

# for-else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    else:
        # 只要每次循环正常完成(没遇到 break )就执行
        print(n, 'is a prime number')


# CPython
from ctypes import *
adder = CDLL('../Cython/adder.dll')
result_int = adder.add_int(3, 4)
print('the result of 3 + 4 is:',result_int)
a_c = c_float(5.5)
b_c = c_float(4.1)
res_f_func = adder.add_float
res_f_func.restype = c_float
print('the result of a + b is:', res_f_func(a_c, b_c))


# IO with 上下文管理器 保证句柄正确释放
with open('../Cython/test.txt', 'rb') as test_file:
    print(test_file.read())

# 用 zip() 迭代多个列表, 列表长度不同时以最小的为准
days = ['Mon', 'Tue', 'Web']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ': drink', drink, '-eat', fruit, '-enjoy', dessert)

# print(dict(zip([num for num in range(4)], 'abcdefghijklmnopqrstuvwxyz'[:4])))