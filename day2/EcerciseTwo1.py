#练习五：计算1+2+3+4……+100的和
sum1=0
n=1
for i in range(1,101):
    sum1+=n
    n=n+1
print('计算1+2+3+4……+100的和：',sum1)



#练习六：
# 1、求10阶乘
sum2=1
for i1 in range(1,11):
    sum2*=i1
    i1=+1
print('求10阶乘:',sum2)

#2、求100以内能被3整除的数，并将作为列表输出
list_1=[]
for a in range(1,101):
  if a%3==0:
      list_1.append(a)
print('输出被3整除的数，并输出列表：',list_1)


#3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
j=[]
list_2=[1,2,3,4,3,4,2,5,5,8,9,7]
for k in list_2:
    if not k in j:
     j.append(k)
print('输出去重后的列表',j)

#4、求斐波那契数列 1 1 2 3 5 8 13 ……
a1=int(input('请输入一个数字：'))
a,b=0,1
list4=[]
for i1 in range(0,a1):
    a,b=b,a+b
    list4.append(a)
print('请输出列表：',list4)


#5、求100以内的质数（只能被1和它本身整除）
i=2
list4=[]
for i in range(2,101):
    j=2
    for j in range(2,i):
      if i%j==0:
         break
    else:
     list4.append(i)
print('请输出列表：',list4)
