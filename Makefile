.PHONY: all clean 

all: clean person_validation.txt

clean:
	rm -rf personinfo.yaml
	rm -rf personinfo/*
	rm -rf person_validation.txt

# prefix commons or bioregistry
# defualt curiemap semweb context
# delete emission of skos
personinfo.yaml:
	curl https://raw.githubusercontent.com/linkml/linkml/main/examples/PersonSchema/personinfo.yaml > temp.yaml
	python add_prefixes_from_file.py \
		--model_to_supplement_file temp.yaml \
		--additional_prefixes_file prefixes_suffix.yaml > $@
	
personinfo/personinfo.py: personinfo.yaml
	gen-project -d personinfo personinfo.yaml

person_validation.txt: personinfo.yaml personinfo/personinfo.py
	python person_validation.py > $@
