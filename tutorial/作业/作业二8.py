#第八题
for x in range(10000,10000):
   a = x // 10000    #取万位数
   b = x //1000 % 10  #取千位
   c = x // 100 % 10  #取百位
   d = x // 10 % 10  #取十位
   e = x % 10
   if a == e and b == c:
      s = s + 1
      print(x)
print(s)
