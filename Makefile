.PHONY: all clean gen_person_artifacts run_validation

all:
	clean
	gen_person_artifacts
	run_validation

clean:
	rm -rf personinfo/*
	
gen_person_artifacts:
	gen-project -d personinfo personinfo.yaml

run_validation:
	python person_validation.py


