from models.TypeOfInstruments import TypeOfInstruments


class ChemistryInstrument():

    def __init__(self, brand = None, model = None, year_of_release = 0,
                 type_of_instruments = None):

        self.brand = brand
        self.model = model
        self.year_of_release = year_of_release
        self.type_of_instruments = type_of_instruments

    def __del__(self):
        print("Destructor is here")

    def __str__(self):
        return str(self.__dict__)
