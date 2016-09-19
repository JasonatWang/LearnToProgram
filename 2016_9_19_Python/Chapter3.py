years_list = list(range(1997,2002))
print("The Year of 3 Years Old:%d\nThe Year of MAX AGE:%d"%(years_list[2],years_list[4]))
#print的传值可以直接在“”后面加 , 之后加变量，也可以像上面用元组来传值
things=['mozzarella','cinderella','salmonella']
for thing in things:
    print(thing.upper())#只有返回值是大写，并没有改变变量本身
things.pop(1)
print(things)
surprise=['Groucho','Chico','Harpo']
surprise[-1]=surprise[-1].lower()[::-1].capitalize()#切片可以用在字符串之后的任意位置
print(surprise)
e2f={'dog':'chien',
     'cat':'chat',
     'walrus':'morse'}
print(e2f['walrus'])
f2e = {}
for english,franch in e2f.items():#items方法获取所有键值对
    f2e[franch]=english
print(f2e['chien'])
englishs = set(e2f.keys())
print(englishs)
life = {
    'animals':
        {
            'cats': ['Henri','Grumpy','Lucy'],
            'octopi': {},
            'emus': {}
        },
    'plants': {},
    'others': {}
}
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])
even=[number for number in range(10) if number % 2 == 0] #range括号后的数字-1为实际范围最大值
print(even)
squares={number**2:number for number in range(10)}
print(squares)
odd={number for number in range(10) if number % 2 == 1}
print(odd)
generaters=("Got%s" % number for number in range(10) if number % 2 == 1)
for gitems in generaters:
    print(gitems)
def good():
    return ['Harry','Ron','Hermione']
def get_odds():
    for number in range(1,10,2):
        yield number
for count,number in enumerate(get_odds(),1):
    #enumerate为枚举，返回:[(0,value),(1,value)]参数:前面的是可迭代类型,后面的是标号起始的数字
    if count == 3:
        print("The third odd number is:",number)
        break
def test(func):
    def new_func(*args,**kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func()
#装饰器需要先定义↑，然后直接在函数之前写出
@test
def greetings():
    print("Hello World!")