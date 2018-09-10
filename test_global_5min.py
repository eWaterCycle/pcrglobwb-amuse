#~ import logging
#~ logging.basicConfig(level=logging.DEBUG)
#~ logging.getLogger("code").setLevel(logging.DEBUG)

import numpy
from matplotlib import pyplot

from interface import PCRGlobWB

ini_file="setup_05min_non-natural.ini"

p=PCRGlobWB(redirection="none") # ini_file=ini_file

p.parameters.ini_file=ini_file

# parameters currently only contains ini_file!
print p.parameters

print p.data_store_names()

grid=getattr(p, p.data_store_names()[0])

print grid
print grid.cellsize()

minpos=grid.get_minimum_position()
maxpos=grid.get_maximum_position()
extent=[minpos[1].number,maxpos[1].number,minpos[0].number,maxpos[0].number]

tbegin=p.model_time
dt=p.time_step
tend=tbegin+100*dt

f=pyplot.figure(figsize=(12,6))
pyplot.ion()
pyplot.show()

while p.model_time<tend:
    p.evolve_model(p.model_time+p.time_step)

    ussd=grid.upper_soil_saturation_degree
    pyplot.clf()
    pyplot.imshow(ussd.number, origin="lower",vmin=0, vmax=1, extent=extent)
    pyplot.title(str(p.model_time-tbegin))
    cb=pyplot.colorbar()
    cb.set_label("upper soil saturation")
    pyplot.draw()
    pyplot.pause(0.1)

p.stop()

print "done"
raw_input()
