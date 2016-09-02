COMPILER = gcc
OCOMPILER = g++
DELETER = -rm -f
FORMATTER = astyle -t --style=kr

default:
	@echo 'Targets:'
	@echo ' all      (build everything)'
	@echo ' test     (application)'
	@echo ' slib     (create shared library - C)'
	@echo ' solib    (create shared library - C++)'
	@echo ' clean'
	@echo ' format'

all: test slib

test: test.o lib.o
	$(COMPILER) -o test test.o lib.o

test.o: test.c lib.h
	$(COMPILER) -c test.c

lib.o: lib.c lib.h
	$(COMPILER) -c lib.c

olib.o: olib.cpp olib.h
	$(OCOMPILER) -c olib.cpp
	
slib:
	$(COMPILER) -Wall -fPIC -c lib.c
	$(COMPILER) -shared -Wl,-soname,libshared.so.1 -o libshared.so lib.o

solib:
	$(OCOMPILER) -Wall -fPIC -c olib.cpp
	$(OCOMPILER) -shared -Wl,-soname,olibshared.so.1 -o olibshared.so olib.o

clean:
	$(DELETER) test.o lib.o
	$(DELETER) olib.o
	$(DELETER) test.exe test
	$(DELETER) libshared.so
	$(DELETER) olibshared.so
	$(DELETER) *.stackdump

format:
	$(FORMATTER) test.c
	$(FORMATTER) lib.c
	$(FORMATTER) lib.h
	$(FORMATTER) olib.cpp
	$(FORMATTER) olib.h
	$(DELETER) test.c.orig lib.c.orig lib.h.orig olib.cpp.orig olib.h.orig
