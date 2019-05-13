from models.ChemistryInstrument import ChemistryInstrument
from models.TypeOfInstruments import TypeOfInstruments


class Pipette(ChemistryInstrument):
    def __init__(self, brand = "xb", model = "qx", year_of_release = 2011,
             type_of_instruments = TypeOfInstruments.OXIDS, lenght = 10, volume = 2):
        super().__init__(brand, model, year_of_release, type_of_instruments)
        self.lenght = lenght
        self.volume = volume

    def __del__(self):
        print("Destructor is here")

    def __str__(self):
        return "Pipette" + str(self.__dict__)
