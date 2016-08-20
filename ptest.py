#!/usr/bin/python

import sys
from ctypes import *

def HeaderMessage(message):
	print ("\n___" + message + "___")

try:
	libc = cdll.LoadLibrary("./libshared.so")

except Exception as ex:
	print ("[LoadLibrary Error] " + str(ex))
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
	
	HeaderMessage("Pointer References")
	myString = c_char_p("Original Value")
	print ("String is " + myString.value)
	libc.PointerReference(myString)
	print ("String is now " + myString.value)
	
except Exception as ex:
	print ("[libc Calling Error] " + str(ex))
