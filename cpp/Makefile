COMPILER = g++
DELETER = -rm -f
FORMATTER = astyle -t --style=stroustrup

default:
	@echo 'Targets:'
	@echo ' all        (build everything)'
	@echo ' cppclient  (application)'
	@echo ' slib       (create shared library - cpp)'
	@echo ' clean'
	@echo ' format'

all: cppclient slib

cppclient: cppclient.o lib.o
	$(COMPILER) -o cppclient cppclient.o lib.o

cppclient.o: cppclient.cpp
	$(COMPILER) -c cppclient.cpp

lib.o: lib.cpp
	$(COMPILER) -c lib.cpp

slib:
	$(COMPILER) -Wall -fPIC -c lib.cpp
	$(COMPILER) -shared -Wl,-soname,libshared.so.1 -o libshared.so lib.o

clean:
	$(DELETER) cppclient.o lib.o
	$(DELETER) cppclient.exe cppclient
	$(DELETER) libshared.so
	$(DELETER) *.stackdump
	$(DELETER) cppclient.cpp.orig lib.cpp.orig lib.h.orig

format:
	$(FORMATTER) cppclient.cpp
	$(FORMATTER) lib.cpp
	$(FORMATTER) lib.h
