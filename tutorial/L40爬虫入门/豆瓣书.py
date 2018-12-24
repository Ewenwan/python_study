# encoding:utf-8
import re


pattern =re.compile(r'"501"(.*?)Ark.channels =',re.S)
result = re.findall(pattern,)
print(result)


