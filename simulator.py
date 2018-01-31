import graphic_simulator
import map_builder
from optparse import OptionParser
import random
import time
import vehicle_classes

random.seed(49307)


def putCarsOnMap(roads,num_cars,car_speeds=None,car_lanes=None):
    """Constructs the car objects and assigns them coordinates that puts them on either
       specified lanes or else randomly chooses lanes to put them on."""
    cars = []
    lane = None

    #car_lanes is the parameter that specifies what lanes the cars should be put in
    # If car_lanes is None then no lanes have been specified so they will be assigned
    # at random.
    if car_lanes is None:
        car_lanes = []
        for _ in range(num_cars):
            car_lanes.append((random.randint(0,num_roads-1),random.randint(0,1)))
            car_speeds.append(5.5)

    #Each entry in car_lanes is the address of a road, and a lane on that road where
    # the car should be placed. Once initialised with this information the Car object
    # will give itself a random location on the specified lane with the same heading as
    # the lane.
    for i,entry in enumerate(car_lanes):
        cars.append(vehicle_classes.Car(roads[car_lanes[i][0]],car_lanes[i][1],\
                    car_speeds[i],i))
    return cars


#Figure of eight
#num_junctions = 6
#num_roads = 7
#num_cars = 1

#road_angles = [90,90,180,180,180,90,90]
#road_lengths = [30,30,30,30,30,30,30]

#junc_pairs = [(0,1),(1,2),(3,2),(4,1),(5,0),(4,3),(5,4)]


#3-road intersection
num_junctions = 4
num_roads = 3
num_cars = 2

run_graphics = True

road_angles = [180,0,50]
road_lengths = [30,30,30]

junc_pairs = [(0,3),(3,1),(2,3)]


clock = 0
runtime = 2.5

junctions,roads = map_builder.buildMap(num_junctions,num_roads,road_angles,road_lengths,\
                                        junc_pairs)

car_speeds = [5.5,0]
car_lanes = [(0,1),(1,1)]
cars = putCarsOnMap(roads,num_cars,car_speeds,car_lanes)

if run_graphics:
    g_sim = graphic_simulator.GraphicSimulator(junctions,roads,cars)

map_builder.printContents(junctions[0])
print("\n")
t0 = time.time()
while(clock<runtime):
    print("TIME: {}".format(clock))
    for entry in cars:
        entry.move(0,0)
        entry.sense()
        print("\nEnd Of Round Status Update:")
        entry.printStatus()
        print("\n")
    g_sim.update()
    
    clock += .1
t1 = time.time()
print("Runtime is {}".format(t1-t0))
