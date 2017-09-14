#!/usr/bin/python
#Encoding:utf-8
import os
#cwd 为当前目录的绝对路径
cwd=os.getcwd()
print cwd


def remove(filename=""):
	"Remove file,ignoring errors"
	try:
		os.remove(filename)
	except:
		pass

remove("../aa.tmp")



	
