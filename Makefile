COMPILER = gcc
DELETER = -rm -f
FORMATTER = astyle -t --style=kr

default:
	@echo 'Targets:'
	@echo ' all      (build everything)'
	@echo ' cclient  (application)'
	@echo ' slib     (create shared library - C)'
	@echo ' clean'
	@echo ' format'

all: cclient slib

cclient: cclient.o lib.o
	$(COMPILER) -o cclient cclient.o lib.o

cclient.o: cclient.c lib.h
	$(COMPILER) -c cclient.c

lib.o: lib.c lib.h
	$(COMPILER) -c lib.c

slib:
	$(COMPILER) -Wall -fPIC -c lib.c
	$(COMPILER) -shared -Wl,-soname,libshared.so.1 -o libshared.so lib.o

clean:
	$(DELETER) cclient.o lib.o
	$(DELETER) cclient.exe cclient
	$(DELETER) libshared.so
	$(DELETER) *.stackdump
	$(DELETER) cclient.c.orig lib.c.orig lib.h.orig

format:
	$(FORMATTER) cclient.c
	$(FORMATTER) lib.c
	$(FORMATTER) lib.h
