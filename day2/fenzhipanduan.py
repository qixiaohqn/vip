'''例子：
1-	if练习--从键盘输入一个数，判断该数是否在列表中，如果在就打印happy
2-	if-else练习—从键盘输入一个数，判断该数是否在列表中，如果在就打印happy，并且让列表中的该值+1，否则打印sad
3-	输入一个数，判断该数的范围：90-100：等价为A……60以下：等级为E'''

'''a=int(input('输入数字:'))
list1=[3,5,6,7,8,9,20,50]
if a in list1:
    print('happy')
else:
    print('not happy')'''



a=int(input('输入数字:'))
list1=[3,5,6,7,8,9,20,50]
if a in list1:
    ind=list1.index(a)
    list1[ind]+=1
    print('输出列表：',list1)
else:
    print('sad')


a=int(input('输入数字:'))
if a>100:
   print("输入数字超出范围")
elif 90<=a<=100:
    print('A')
elif 80<a<90:
    print('B')
elif 80<a<70:
    print('C')
elif 70<a<60:
    print('D')
else:
    print('E')
