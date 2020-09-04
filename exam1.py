s = str(input())
_list = list(s.split(" "))
n = int(_list[0])
m = int(_list[1])
final = []
for i in range (0, n):
    _temp = []
    for j in range (0, m):
        _temp.append(i*j)
    final.append(_temp)
print(final)