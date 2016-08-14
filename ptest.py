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
	
except Exception as ex:
	print ("[libc Calling Error] " + str(ex))
