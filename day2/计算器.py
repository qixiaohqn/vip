#设计一个计算器，输入两个数，自动实现加减乘除（进阶：根据用户输入的计算符号计算结果）

"""def count(a,b):
    print('两数相加：',a+b)
    print('两数相减：', a - b)
    print('两数相乘：', a * b)
    print('两数相除：', a / b)

a=int(input("请输入数字："))
b=int(input("请输入数字："))
count(a,b)
"""

def count(a,b,c):
 if c=='-':
     print(a-b)
 elif c=='+':
     print(a+b)
 elif c=='*':
     print(a*b)
 elif c=='/':
    print(a /b)
 else:
     print("不支持运算")


for i in range(1,6):
    a = int(input("请输入第一个数字："))
    c = input("请输入运算符号：")
    b = int(input("请输入第二数字："))
    count(a,b,c)
