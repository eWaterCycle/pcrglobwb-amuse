from amuse.units import units

from pcrglobwb import BmiPCRGlobWB as _BMI

from bmi import bmi
bmi.udunit_to_amuse={ "1" : units.none, "none":units.none, "s":units.s, "K":units.K, "-":units.none,
                  "m.day-1" : units.m/units.day, "m3": units.m**3, "m3.day-1" : units.m**3/units.day,
                  "m." : units.m, "m":units.m, "m3.s-1": units.m**3/units.s, "degrees Celcius": units.K,
                  "undefined" : units.none, 'days since 1901-01-01' : units.day}

# bmi to land at hymuse.community.interface.bmi eventually? 
from bmi.bmi import BMIImplementation, BMIPythonInterface, BMI

class PCRGlobWBImplementation(BMIImplementation):
    def __init__(self):
        self._BMI=_BMI()

class PCRGlobWBInterface(BMIPythonInterface):
    def __init__(self, **options):
        BMIPythonInterface.__init__(self, PCRGlobWBImplementation,  **options)

class PCRGlobWB(BMI):
    _axes_names=["lon","lat"]
    _axes_unit=[units.deg, units.deg, units.none]

    def __init__(self, **options):
        self._ini_file=options.get("ini_file","")
        BMI.__init__(self,PCRGlobWBInterface(**options))
  
