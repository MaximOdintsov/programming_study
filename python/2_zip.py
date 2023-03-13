# zip - итератор
# zip(iter1, iter2, iter3, ...) --> zip object

a = [2, 4, 6]
b = [3, 0,  1, 43, 40]
c = 'abcde'

# for i in range(len(a)):
#     print(a[i], b[i])

# принимает минимальную длину итерируемых объектов
zip_lst = list(zip(a, b, c))
print(zip_lst)

for t1, t2, t3 in zip(a, b, c):
    print(t1, t2, t3)

# получаем наши списки обратно
lst1, lst2, lst3 = zip(*zip_lst)
print(lst1, lst2, lst3)


n = int(input())
lst = [int(input()) for _ in range(n)]
index_lst = [i for i in range(len(lst))]
zip_lst = list(zip(lst, index_lst))

for i in zip_lst:
    if i[1] % 2 != 0:
        lst.remove(i[0])
print(lst)