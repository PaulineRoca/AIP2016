# recursive make: runs make in all the immediate subdirs
# Time-stamp: <2016-09-01 22:28:11 cp983411>
 
SHELL=/bin/bash

SUBDIRS := $(wildcard */.)

.PHONY: all clean putonweb

all: README.html doclist.html
	@for a in $(SUBDIRS); do \
		if [ -f $$a/Makefile ]; then \
			echo "processing folder $$a"; \
			$(MAKE) -C $$a; \
		fi; \
	done;

README.html: README.md
	pandoc -s -S -c pandoc.css $< -o $@


doclist.html: doclist.md
	pandoc -s -S -c pandoc.css $< -o $@

doclist.md:
	echo "<h1>>HTML files:</h1>" > $@
	for f in `find . -name '*.html' | sort `; do \
		echo "* <a href="$$f">$$f</a>"; \
	done >> $@
	echo "<h1>>PDFs:</h1>" >> $@
	for f in `find . -name '*.pdf' | sort `; do \
		echo "* <a href="$$f">$$f</a>"; \
	done >> $@

putonweb:
	rsync -avz --delete --exclude .git --filter='P books/*' ./ pallier@ftp.pallier.org:www/ressources/AIP2016

