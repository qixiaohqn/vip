def count(a,b,c):
 if c=='-':
     print(a-b)
 elif c=='+':
     print(a+b)
 elif c=='*':
   try:
     print(a*b)
   except BaseException as ms1:
       print(ms1)

 elif c=='/':
   try:
       print(a /b)
   except ZeroDivisionError as msg:
       print("除数不能为0",msg)
 else:
     print("不支持运算")


for i in range(1,6):
    a = int(input("请输入第一个数字："))
    c = input("请输入运算符号：")
    b = int(input("请输入第二数字："))
    count(a,b,c)