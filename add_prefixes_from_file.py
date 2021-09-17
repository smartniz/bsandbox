import yaml
import click


def ysl_wrapper(yamlfile):
    with open(yamlfile, "r") as stream:
        try:
            safe_loaded = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return safe_loaded


supplemtary_prefixes_file = "prefixes_suffix.yaml"
deficient_linkml_file = "personinfo.yaml"



@click.command()
# like personinfo.yaml
@click.option('-m', '--model_to_supplement_file', type=click.Path(exists=True), required=True)
# like 
@click.option('-p', '--additional_prefixes_file', type=click.Path(exists=True), required=True)
def main(model_to_supplement_file, additional_prefixes_file):
	# print(model_to_supplement_file)
	# print(additional_prefixes_file)
	prefixes_suffix = ysl_wrapper(additional_prefixes_file)
	# print(prefixes_suffix['prefixes'])

	model_to_supplement = ysl_wrapper(model_to_supplement_file)

	prefixes_to_supplement = model_to_supplement["prefixes"]
	# print(model_to_supplement)


	prefixes_to_supplement.update(prefixes_suffix["prefixes"])
	model_to_supplement["prefixes"] = prefixes_to_supplement

	# with open(additional_prefixes_file, "w") as outfile:
	#     yaml.safe_dump(model_to_supplement, outfile, default_flow_style=False)

	dumped = yaml.dump(model_to_supplement, default_flow_style=False, sort_keys=False)
	print(dumped)


if __name__=="__main__": 
    main() 