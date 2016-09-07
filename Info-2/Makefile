# recursive make: runs make in all the immediate subdirs
# Time-stamp: <2016-09-07 06:43:39 cp983411>
 
SHELL=/bin/bash

SUBDIRS := $(wildcard */.)

.PHONY: all

all: 
	@for a in $(SUBDIRS); do \
		if [ -f $$a/Makefile ]; then \
			echo "processing folder $$a"; \
			$(MAKE) -C $$a; \
		fi; \
	done;

