from models.ChemistryInstrument import ChemistryInstrument
from models.TypeOfInstruments import TypeOfInstruments


class Tripod(ChemistryInstrument):
    def __init__(self, brand = "ls", model = "xc", year_of_release = 2020,
             type_of_instruments = TypeOfInstruments.ACIDS, height = 4, diametr = 1, lenght = 2):
        super().__init__(brand, model, year_of_release, type_of_instruments)
        self.height = height
        self.diametr = diametr
        self.lenght = lenght

    def __del__(self):
        print("Destructor is here")

    def __str__(self):
        return "Tripod" + str(self.__dict__)
