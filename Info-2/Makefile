# recursive make: runs make in all the immediate subdirs
# Time-stamp: <2016-09-06 20:23:41 cp983411>
 
SHELL=/bin/bash

SUBDIRS := $(wildcard */.)

.PHONY: all

all: README.html doclist.html
	@for a in $(SUBDIRS); do \
		if [ -f $$a/Makefile ]; then \
			echo "processing folder $$a"; \
			$(MAKE) -C $$a; \
		fi; \
	done;

