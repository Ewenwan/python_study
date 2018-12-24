# change ={'a','b','c','d'}

word =input('输入单词')
output=[]
for c in word:
    # output.append(change[c])
    output.append(chr(ord(c)+4))
    print(output)

print(sum(b for b in range(10)))
# sum 是把里面所有数加起来 第一个B是一个列表 第二个b把for循环1到9值添加到列表当中去 sum 函数吧1到9加起来