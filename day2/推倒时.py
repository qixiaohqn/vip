example4 = [[1,2,3],[4,5,6],[7,8,9],[10]]
exmaple5 = [j**2 for i in example4 if len(i)>1 for j in i if j%2 == 0]
print(exmaple5)

example4 = [[1,2,3],[4,5,6],[7,8,9],[10]]
list1=[]
for i in example4:
    if len(i) > 1:
     for j in i:
         if j % 2 == 0:
            list1.append(j**2)
print(list1)

