# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:06:41 2019

@author: prash
"""
import math
from math import acos, sin, cos, radians, floor
RADIUS_MILES = 3963

class DestinationCalculator:
    def __init__(self):
        self.cities={}
        pass
    
    def process(self, line: str) -> str:
        line_splits=line.split(":")
        if line_splits[0]=="LOC":
            lat_in_radians=(float(line_splits[2]) * math.pi)/180
            long_in_radians=(float(line_splits[3]) * math.pi)/180
            self.cities[line_splits[1]]=[lat_in_radians ,long_in_radians]
            return line_splits[1]
        elif line_splits[0]=="TRIP":
            city1=self.cities[line_splits[2]]
            city2=self.cities[line_splits[3]]
            
            delta_phi=abs(city1[1]-city2[1])
            delta_sigma=acos(sin(city1[0]) * sin(city2[0]) + cos(city1[0]) * cos(city2[0]) * cos(delta_phi))
            distance=floor(RADIUS_MILES * delta_sigma)
            return line[5:len(line)] + ":" + str(distance)

dc= DestinationCalculator()
dc.process("LOC:CHI:41.836944:-87.684722")
dc.process("LOC:NYC:40.7127:-74.0059")
print(dc.process("TRIP:C0FFEE1C:CHI:NYC"))