import yaml


def ysl_wrapper(yamlfile):
    with open(yamlfile, "r") as stream:
        try:
            safe_loaded = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return safe_loaded


supplemtary_prefixes_file = "prefixes_suffix.yaml"
deficient_linkml_file = "personinfo.yaml"

prefixes_suffix = ysl_wrapper(supplemtary_prefixes_file)

model_to_supplement = ysl_wrapper(deficient_linkml_file)

prefixes_to_supplement = model_to_supplement["prefixes"]

prefixes_to_supplement.update(prefixes_suffix["prefixes"])
model_to_supplement["prefixes"] = prefixes_to_supplement

with open(deficient_linkml_file, "w") as outfile:
    yaml.safe_dump(model_to_supplement, outfile, default_flow_style=False)

