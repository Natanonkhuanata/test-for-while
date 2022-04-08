# list




g = [0]*10
d = g + g
a = [0]*10
a = a + a

for i in range(20):
   a[i] = i

for index in a:
    if index % 2 == 0:
        print(index)


