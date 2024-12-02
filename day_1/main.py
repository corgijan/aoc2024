with open("in.txt") as infile:
    content = infile.read()

list_a = []
list_b = []
list_all = content.split("\n")
sum = 0
for i in list_all:
    vals = i.split("   ")
    a = vals[0]
    b = vals[1]
    list_a.append(a)
    list_b.append(b)
list_a.sort()
list_b.sort()
print(list_a[0:10])
zip_list = zip(list_a, list_b)
for i in zip_list:

    sum += int(i[0]) * int(len([x for x in list_b if x == i[0]]))
print(sum)


