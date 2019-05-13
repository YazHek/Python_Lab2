from models.ChemistryInstrument import ChemistryInstrument
from models.TypeOfInstruments import TypeOfInstruments


class Flask(ChemistryInstrument):

    def __init__(self, brand = "sms", model = "", year_of_release = 2001, type_of_instruments = TypeOfInstruments.ACIDS,
                 name = "", height = 1, radius = 2):
        super().__init__(brand, model, year_of_release, type_of_instruments)
        self.name = name
        self.height = height
        self.radius = radius

    def __del__(self):
        print("Destructor is here")

    def __str__(self):
        return "Flask" + str(self.__dict__)
