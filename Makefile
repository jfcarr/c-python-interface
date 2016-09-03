COMPILER = gcc
DELETER = -rm -f
FORMATTER = astyle -t --style=kr

default:
	@echo 'Targets:'
	@echo ' all      (build everything)'
	@echo ' test     (application)'
	@echo ' slib     (create shared library - C)'
	@echo ' clean'
	@echo ' format'

all: test slib

test: test.o lib.o
	$(COMPILER) -o test test.o lib.o

test.o: test.c lib.h
	$(COMPILER) -c test.c

lib.o: lib.c lib.h
	$(COMPILER) -c lib.c

slib:
	$(COMPILER) -Wall -fPIC -c lib.c
	$(COMPILER) -shared -Wl,-soname,libshared.so.1 -o libshared.so lib.o

clean:
	$(DELETER) test.o lib.o
	$(DELETER) test.exe test
	$(DELETER) libshared.so
	$(DELETER) *.stackdump

format:
	$(FORMATTER) test.c
	$(FORMATTER) lib.c
	$(FORMATTER) lib.h
	$(DELETER) test.c.orig lib.c.orig lib.h.orig
