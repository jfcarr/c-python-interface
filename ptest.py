#!/usr/bin/python

import sys
from ctypes import *

def HeaderMessage(message):
	print ("\n___" + message + "___")

def LibCTest():
	HeaderMessage("___ C Test ___")

	try:
		libc = cdll.LoadLibrary("./libshared.so")

	except Exception as ex:
		print ("[C LoadLibrary Error] " + str(ex))
		sys.exit()

	try:
		HeaderMessage("Simple Printing")
		libc.SayHello()
		libc.SayGoodbye()
		
		HeaderMessage("Returning Numbers")
		returnInt = libc.ReturnInt()
		print ("Returned int is " + str(returnInt))
		
		libc.ReturnFloat.restype = c_float
		returnFloat = libc.ReturnFloat()
		print ("Returned float is " + str(returnFloat))
		
		HeaderMessage("Statics")
		libc.SetStatic(10)
		print ("Static value is " + str(libc.GetStatic()))
		libc.SetStatic(20)
		print ("Static value is " + str(libc.GetStatic()))
		
		HeaderMessage("Pointer References (NOT working)")
		returnString = "Old Value";
		print ("String is " + returnString)
		libc.PointerReference(returnString)
		print ("String is now " + returnString)
		
	except Exception as ex:
		print ("[libc Calling Error] " + str(ex))

if __name__ == '__main__':
	LibCTest()
