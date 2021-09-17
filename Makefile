.PHONY: all clean 

all: clean person_validation.txt

clean:
	rm -rf personinfo.yaml
	rm -rf personinfo/*
	rm -rf person_validation.txt

personinfo.yaml:
	curl https://raw.githubusercontent.com/linkml/linkml/main/examples/PersonSchema/personinfo.yaml > $@
	# python add_prefixes_from_file.py
	
personinfo/personinfo.py: personinfo.yaml
	gen-project -d personinfo personinfo.yaml

person_validation.txt: personinfo.yaml personinfo/personinfo.py
	python person_validation.py > $@
