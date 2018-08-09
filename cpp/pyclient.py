#!/usr/bin/python3

from ctypes import cdll

lib = cdll.LoadLibrary('./libshared.so')

class Greeter(object):
	def __init__(self):
		self.obj = lib.CGreeter_new()
	
	def sayHello(self):
		lib.CGreeter_Hello(self.obj)

	def sayGoodbye(self):
		lib.CGreeter_Goodbye(self.obj)

greeter = Greeter()
greeter.sayHello()
greeter.sayGoodbye()
