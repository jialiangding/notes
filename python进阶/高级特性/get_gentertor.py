L=[]
for i  in range(1,11):
    L.append(i*i)
print(L)

print([x*x for x in range(1,11)])

print([m + n for m in 'ABC' for n in 'XYZ'])
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)


print([k + '=' + v for k, v in d.items()])