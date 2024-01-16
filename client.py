
class Client:
    def __init__(self, name, surename, id) -> None:
        self._name = name
        self._surename = surename
        self._id = id
        self._registration_date = None
        self._flat_list  = []

    @property
    def name(self):
        return self._name
    @property
    def surename(self):
        return self._surename
    @property
    def id(self):
        return self._id
    @property
    def flat_list(self):
        return self._flat_list