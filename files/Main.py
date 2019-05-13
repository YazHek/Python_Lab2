from models.ChemistryInstrument import ChemistryInstrument
from models.Flask import Flask
from models.MeasuringCylinder import MeasuringCylinder
from models.Pipette import Pipette
from models.Tripod import Tripod
from models.TypeOfInstruments import TypeOfInstruments
from managers.ChemistryInstrumentManager import ChemistryInstrumentManager

Flask = Flask()
MeasuringCylinder = MeasuringCylinder()
Pipette = Pipette()
Tripod = Tripod()

chemistry_instrument_list = [Tripod, Flask, Pipette, MeasuringCylinder]
manager = ChemistryInstrumentManager(chemistry_instrument_list)

manager.output(manager.find_by_type(TypeOfInstruments.ACIDS))

manager.output(manager.sort_by_type())

manager.output(manager.sort_by_year())
