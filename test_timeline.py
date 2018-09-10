#~ import logging
#~ logging.basicConfig(level=logging.DEBUG)
#~ logging.getLogger("code").setLevel(logging.DEBUG)

import numpy
from matplotlib import pyplot

from omuse.units import units

from interface import PCRGlobWB

ini_file="setup_natural_test.ini"

p=PCRGlobWB() # ini_file=ini_file

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

grid2=grid.empty_copy()
channel=grid.new_channel_to(grid2)

while p.model_time<tend:
    p.evolve_model(p.model_time+dt)
    print "evolved to:", p.model_time
    
    channel.copy_attributes(["upper_soil_saturation_degree","discharge"])
    grid2.savepoint(timestamp=p.model_time)

p.stop()

t,dis=grid2[-1,1].get_timeline_of_attribute_as_vector("discharge")

f=pyplot.figure()

pyplot.plot((t-tbegin).value_in(units.day), dis.value_in(units.m**3/units.s))
pyplot.xlabel("time (day)")
pyplot.ylabel("discharge (m**3/s)")

pyplot.show()

print "done"
