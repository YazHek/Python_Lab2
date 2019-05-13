class ChemistryInstrumentManager:

    def __init__(self, chemistry_instrument_list=None):
        self.chemistry_instrument_list = chemistry_instrument_list

    def sort_by_year(self, reverse=True):
        return sorted(self.chemistry_instrument_list,
         key=lambda chemistry_instrument:
          chemistry_instrument.year_of_release, reverse=reverse)

    def sort_by_type(self, reverse=False):
        return sorted(self.chemistry_instrument_list,
         key=lambda chemistry_instrument:
          chemistry_instrument.type_of_instruments.value, reverse=reverse)

    def find_by_type(self, type_of_instruments):
        return list(filter
        (lambda chemistry_instrument:chemistry_instrument.type_of_instruments==type_of_instruments,
         self.chemistry_instrument_list))

    def output(self, list):
        for chemistry_instrument in list:
            print(chemistry_instrument)
        print('\n')
