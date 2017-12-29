#!/usr/bin/python
import re

pattern = re.compile('\d+\.\d+')

src = '3.14, 1232.2121, 323.323, 432, abc, 1213.222'
print(src)

result = pattern.findall(src)

print(result)