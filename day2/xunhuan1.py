'''求10阶乘
求100以内能被3整除的数，并将作为列表输出
列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表'''

#求10阶乘

n=1
sum_n=0
for i in range(1,11):
    n=n*i
    sum_n=sum_n+n
print('10的阶乘：',sum_n)

#求100以内能被3整除的数，并将作为列表输出
list_2=[]
for a in range(1,101):
    if a%3==0:
        list_2.append(a)
print("输出被3整除的数字：",list_2)


#列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表'''
list_1=[1,2,3,4,3,4,2,5,5,8,9,7]
j=[]
for k in list_1:
    if not k  in j:
        j.append(k)
print('输出去重的列表list_4', j)
