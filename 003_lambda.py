def calc(a, b):
    return a + b


s = lambda a, b: a + b  # 匿名函数
print(type(s))
print(s(10, 20))  # 调用匿名函数
print('-' * 30)
lst = [10, 20, 30, 40, 50]
for i in range(len(lst)):
    result = lambda x: x[i]  # 隐式return x[i]
    print(result(lst))
