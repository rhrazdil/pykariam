from collections.abc import Mapping
import yaml


class Strings(Mapping):
    """
    Class provides dictionary-like access to game strings in desired language. Inherits Mapping abstract
    class which provides handful of abstract methods that this class overrides.
    Advantage of this approach is that instance['key'] and instange.get('key') both call overriden __getitem__ method
    (as opposed to Strings(dict) implementation).
    """
    def __init__(self, language):
        self.language = language
        self._storage = self.strings()

    def strings(self):
        _strings = ''
        with open('languages/' + self.language + '.yaml') as file:
            _strings = file.read()
        return yaml.load(_strings)

    def __getitem__(self, key):
        return self._storage[key]

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)
