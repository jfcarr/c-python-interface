#!/usr/bin/python

import sys
from ctypes import *

def HeaderMessage(message):
	print ("\n___{0}___".format(message))

def LibCTest():
	HeaderMessage("___ C Test ___")

	try:
		libc = cdll.LoadLibrary("./libshared.so")

	except Exception as ex:
		print ("[C LoadLibrary Error] {0}".format(str(ex)))
		sys.exit()

	try:
		HeaderMessage("Simple Printing")
		libc.SayHello()
		libc.SayGoodbye()
		
		HeaderMessage("Returning Numbers")
		returnInt = libc.ReturnInt()
		print ("Returned int is {0}".format(str(returnInt)))
		
		libc.ReturnFloat.restype = c_float
		returnFloat = libc.ReturnFloat()
		print ("Returned float is {0}".format(str(returnFloat)))
		
		HeaderMessage("Statics")
		libc.SetStatic(10)
		print ("Static value is {0}".format(str(libc.GetStatic())))
		libc.SetStatic(20)
		print ("Static value is {0}".format(str(libc.GetStatic())))
		
		HeaderMessage("Pointer References (NOT working)")
		returnString = "Old Value";
		print ("String is {0}".format(returnString))
		libc.PointerReference(returnString)
		print ("String is now {0}".format(returnString))
		
	except Exception as ex:
		print ("[libc Calling Error] " + str(ex))

if __name__ == '__main__':
	LibCTest()
