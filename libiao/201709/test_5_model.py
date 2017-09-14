#!/usr/bin/python
#encoding=utf-8

import random
num=random.randint(1,100000)
print num

f=open("test.yaml","r")
lines=f.readlines()
for line in lines:
	print line
