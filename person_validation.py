import linkml
from linkml_runtime.loaders import yaml_loader
import os
import sys

path_to_append = "personinfo"
person_data_file = "person_glance_data.json"

sys.path.append(os.path.abspath(path_to_append))

from personinfo import *

people = yaml_loader.load(person_data_file, Person)

print(people)
