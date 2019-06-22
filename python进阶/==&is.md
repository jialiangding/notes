## is和== 的区别
```
a=[1,2,3]
b=a
b==a
print(b==a)  #输出：true

c=[1,2,3]
print(a is c) #输出 false
print(a  == c) #输出 true
print(id(a))
print(id(c))
#输出  4506233160
      4521432840
 ```
is 是判断是否是引用的同一个内存地址
== 是判断值是否相同




