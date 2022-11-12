alist = []
blist = ['a', 'b', [1, 2, 3]]
print(blist[2][1])
clist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
dlist = []
for i in range(3):
    for j in range(3):
        alist.append(clist[i][j])
        dlist.append(clist[j][i])
print(alist)
print(dlist)

# extend
alist1 = [1, 2, 3]
alist2 = ['a', 'b', 'c']
alist1.extend(alist2)
alist1.extend('abd')
alist1.extend((0, 12, 121, 232))
print(alist1)

# index  pop
blist1 = [1, 2, 3, 4, 5, 6]
print(blist1.index(3))
print(blist1.pop(0))  # 删除索引为0的元素并返回删除的元素
print(blist1)
# insert
blist1.insert(2, 'abd')  # 在索引为2的地方插入元素
print(blist1)

# reverse
blist1.reverse()
print(blist1)

# copy()
a = blist1.copy()
a.append('bbb')
print(a)
