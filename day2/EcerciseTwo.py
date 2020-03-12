#练习一：
list1=[11,13,5,7,0,56,23,34,72]
#1、求该列表中的最大值，最小值及列表中一共有几个元素
print('输出最大值：',max(list1))
print('输出最小值：',min(list1))
print('输出列表中元素的数量：',len(list1))

#2、获取56元素在列表的位置
print('获取56元素在列表的位置：',list1.index(56))

#3、追加元素7
list1.append(7)
print('追加元素7，并输出追加后的列表：',list1)

#4、删除元素0
a=list1.index(0)
del list1[a]
print('输出删除元素0，并输出列表：',list1)

#5、排序列表（由大到小）
print('排序列表（由大到小）:',sorted(set(list1)))

#6、将列表[66,67,68]与原列表组合
list2=[66,67,68]
list1.extend(list2)
print('输出组合后的列表：',list1)



#练习二：列出100以内偶数中能整除3的所有数字
example=[ i for i in range(1,101)if i%2==0 and i/3==0]
print('输出10000以内偶数中能整除3的所有数字：',example )



#练习三：分别定义一个集合和一个字典
s={4,9,36,58,90,2}
dict1={'a':34,'b':'happy','c':'so','d':60}
#1、为集合和字典分别插入元素：55（d：55）
s.add(55)#为集合添加元素
print('输出添加元素后集合：',s)
dict1['e']=55#为字典添加元素
print('输出添加元素胡后的字典：',dict1)

#2、分别删除集合和字典内的一个元素
s.remove(9)#删除元素9
print('输出删除元素9的集合：',s)
del dict1['c']#删除元素so
print('输出删除元素so的字典',dict1)

#3、取出字典内的所有值（value）和集合组合一个列表
for i in dict1.values():
    s.add(i)
print('取出字典的值并和集合组合成一个列表：',s)

#4、集合和字典的区别
'''集合和字典的区别
集合没有键只有值，字典是以键值对的形式存在,只能通过键引用或者是整体引用'''

#练习四
#1、if练习--从键盘输入一个数，判断该数是否在列表中，如果在就打印happy
a1=int(input('请输出一个数字：'))
s1=[3,5,50,10,30]
if a1 in s1:
    print('happy')
else:
    print('您输入的数字不在列表中！')

#2、if-else练习—从键盘输入一个数，判断该数是否在列表中，如果在就打印happy，并且让列表中的该值+1，否则打印sad
a2=int(input('请输出一个数字：'))
s2=[3,5,50,10,30]
if a2 in s2:
    ind1=s2.index(a2)
    s2[ind1] += 1
    print('happy,输出值存在列表中数字+1后的列表',s2)
else:
    print('sad！')

#3、输入一个数，判断该数的范围：90-100：等价为A……60以下：等级为E
a3=int(input('请输出一个数字：'))
if a3>100:
    print('输入的数字超出最大值！')
elif a3>=90 and a3<100:
    print('A')
elif a3>=80 and a3<90:
    print('B')
elif a3>=70 and a3 <80:
    print('C')
elif a3>=60 and a3<70:
    print('D')
else:
    print('E')


