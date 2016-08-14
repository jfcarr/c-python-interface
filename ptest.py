#!/usr/bin/python3

import sys
from ctypes import *

try:
	libc = cdll.LoadLibrary("./libshared.so")

except Exception as ex:
	print ("[LoadLibrary Error] " + str(ex))
	sys.exit()

try:
	libc.SayHello()
	libc.SayGoodbye()
	
	returnInt = libc.ReturnInt()
	print ("Returned int is " + str(returnInt))
	
	libc.ReturnFloat.restype = c_float
	returnFloat = libc.ReturnFloat()
	print ("Returned float is " + str(returnFloat))
	
except Exception as ex:
	print ("[libc Calling Error] " + str(ex))
