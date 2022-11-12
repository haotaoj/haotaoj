a = int(input('输入数字：'))
if a > 0:
    print('正数')
elif a < 0:
    print('负数')

b = int(input('输入数字二：'))
if type(b) is int and b > 2:
    print('正确且大于2')
