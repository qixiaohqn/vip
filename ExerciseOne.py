
#1、求10阶乘
n=1
total=0
for i in range(1,11):
 n=n*i
 total=total+n
print('输出10阶乘结果：',total)


#2、求100以内能被3整除的数，并将作为列表输出
for i in range(1,101):
    if i%3==0 :
        print("输出被3整除的数字：",i)


#3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
 #方法1
list_1=[1,2,3,4,3,4,2,5,5,8,9,7]
list_2=list(set(list_1))
print('输出去重的列表list_2',list_2)
#方法2
list_3={}.fromkeys(list_1).keys()
print('输出去重的列表list_3',list_3)
#方法3
j=[]
for k in list_1:
    if not k  in j:
        j.append(k)
print('输出去重的列表list_4', j)



#4、求斐波那契数列 1 2 3 5 8 13 ⋯⋯
x=int(input('请输入一个数字：'))
a,b=0,1
for i in range(0,x):
    print('输出数列',a)
    a,b=b,a+b



#5、求10000以内的质数

from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
count = 0
for i in range(1, 10000):
    if is_prime(i):
        count = count + 1
        print('{}:{}'.format(count, i))

