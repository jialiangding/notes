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


L1 = ['Hello', 'World', 18, 'Apple', None]

#[s.lower() for s in L1] 
# 发生异常: AttributeError
# 'int' object has no attribute 'lower'
L2=[s.lower() for s in L1 if  isinstance(s, str)]
print(L2)
L3=2
p = [x for x in range(1,101) if x%3 == 0]
#1-100中，不是3的倍数的数取相反数，其余的数保持不变
q = [x if x%3==0 else -x for x in range(1,101)]
print(q)