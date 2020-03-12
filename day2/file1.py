#练习1：读取以下文件：a-全部内容；b-每一行的内容；c-读取所有行的内容
with open('/Users/qixiaohan/code/vip5/day2/file1.txt', 'r+') as file:
 print(file.readlines())
 file.seek(0)

 list1=[]
 for i in file.readlines():
  l=i.strip('\n')
  list1.append(l)
 print('输出列表：',list1)


