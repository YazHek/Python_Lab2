from models.ChemistryInstrument import ChemistryInstrument
from models.TypeOfInstruments import TypeOfInstruments


class MeasuringCylinder(ChemistryInstrument):

    def __init__(self, brand = "dfs", model = "fds", year_of_release = 2010,
             type_of_instruments = TypeOfInstruments.BASIS, height = 3, volume = 1, radius = 5):
        super().__init__(brand, model, year_of_release, type_of_instruments)
        self.height = height
        self.volume = volume
        self.radius = radius

    def __del__(self):
        print("Destructor is here")

    def __str__(self):
        return "MeasuringCylinder" + str(self.__dict__)
