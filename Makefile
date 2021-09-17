.PHONY: gen_person_artifacts, run_validation

gen_person_artifacts:
	gen-project -d personinfo personinfo.yaml

run_validation:
	python person_validation.py

clean:
	rm -rf personinfo/*
