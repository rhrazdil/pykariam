import yaml


def load_strings(language):
    with open('languages/'+ language + '.yaml') as lang:
        strings = yaml.load(lang)
    return strings
