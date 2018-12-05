#!/usr/bin/python3

import time
from Vector import Vector as v2
from SerialIO import SerialIO

target = v2
position = v2
course = v2

gps_ready = 0
interface = SerialIO()

print("Starting, waiting for GPS...")

while gps_ready == 0:
    if interface.getGpsSpeed() != 0:
        gps_ready = 1
    else:
        print("Gps Not ready...")
        time.sleep(3)

print("GPS ready...")
print("Running init")

for _ in range(3):
    print("Latitiude:" + interface.getLatitude())
    print("Longitude:" + interface.getLongitude())
    print("Heading:" + interface.getGpsHeading())
    print("Speed:" + interface.getGpsSpeed())
    print("===")
    time.sleep(1)

time.sleep(10)

print("Autonomous mode...")
print("Seeking coordinates: " + target)

interface.setMotorPower(0.5)

while position.distance_to(target) > .001:
    # until within very approximately 10m of desination

    position.set_coords((interface.getLatitude(), interface.getLongitude()))
    course.set_from_polar((interface.getGpsSpeed(),
                           interface.getGpsHeading()))

    print("Position: " + position)
    print("Course: " + course)

    interface.setRudderAngle(course.angle_to(target-position)/5)

interface.setMotorPower(0)
