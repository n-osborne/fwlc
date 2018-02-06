PROJECT=Fun With Lambda Calculus
AUTHOR=Nicolas Osborne
PYTHONPATH=./src
export PYTHONPATH
SPHINXBUILD=sphinx-build
CONFIGPATH=.
SOURCEDOC=sourcedoc
DOC=docs

.PHONY: clean doc archive author

clean:
	rm -f *~ */*~
	rm -rf __pycache__ src/__pycache__
	rm -rf $(DOC)
	rm -f $(PROJECT).zip
	rm -f conf.py-e
	rm -f */*.pyc
	rm -rf .DS_Store

doc: author
	$(SPHINXBUILD) -c $(CONFIGPATH) -b html $(SOURCEDOC) $(DOC)

archive: clean
	zip -r $(PROJECT).zip . -x "sol/*"


author:
	sed -i -e 's/^project =.*/project = "Module $(PROJECT)"/g' conf.py
	sed -i -e 's/^copyright =.*/copyright = "2015-2018, $(AUTHOR)"/g' conf.py
	sed -i -e 's/^author =.*/author = "$(AUTHOR)"/g' conf.py
