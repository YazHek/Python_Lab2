from models.ChemistryInstrument import ChemistryInstrument
from models.Flask import Flask
from models.MeasuringCylinder import MeasuringCylinder
from models.Pipette import Pipette
from models.Tripod import Tripod
from models.TypeOfInstruments import TypeOfInstruments
from managers.ChemistryInstrumentManager import ChemistryInstrumentManager

flask = Flask()
measuring_cylinder = MeasuringCylinder()
pipette = Pipette()
tripod = Tripod()
flask1 = Flask("Brand", "Model", 2004, type_of_instruments=TypeOfInstruments.BASIS)
measuring_cylinder1 = MeasuringCylinder("MeasuringBrand", "MeasuringModel",
                                        2002, type_of_instruments=TypeOfInstruments.ACIDS)

chemistry_instrument_list = [tripod, flask, pipette, measuring_cylinder, flask1, measuring_cylinder1]
manager = ChemistryInstrumentManager(chemistry_instrument_list)

manager.output(manager.find_by_type(TypeOfInstruments.ACIDS))

manager.output(manager.sort_by_type())

manager.output(manager.sort_by_year())

