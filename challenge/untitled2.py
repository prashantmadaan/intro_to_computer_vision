# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:26:07 2019

@author: prash
"""

import operator
class PathCalculator:
    
    # You may enter code here.
    def __init__(self):
        self.maxdistance=-1
        self.dict={}
        self.maxdistancestring=""
    
    def process(self, line: str) -> str:
        
        # You must enter code here.
        line_split=line.split(":")
        city1=line_split[0]
        city2=line_split[1]
        
        if city1 not in self.dict.keys():
            self.dict[city1]= {}
            self.dict[city1][city2]=int(line_split[2])
        else:
            #self.dict[city1]=self.dict[city1].append({city2:line_split[2]})
            self.dict[city1][city2]=int(line_split[2])
        
        if city2 not in self.dict.keys():
            self.dict[city2]= {}
            self.dict[city2][city1]=int(line_split[2])
            #self.dict[city2]=[{city1:line_split[2]}]
        else:
            self.dict[city2][city1]=int(line_split[2])
            #self.dict[city2]=self.dict[city2].append({city1:line_split[2]})
                
        if self.maxdistance==-1 and len(self.dict)==2:
            return "NONE"        
                
        # calculate max distances with city 1 
        sorted_list = sorted(self.dict[city1].items(), key=operator.itemgetter(1))
        if sorted_list[0][0]==city2:
            max_dist_city1=self.dict[city1][sorted_list[1][0]]
        else:   
            max_dist_city1=self.dict[city1][sorted_list[0][0]]
        
        #calculate max distance with city 2
        sorted_list_2 = sorted(self.dict[city2].items(), key=operator.itemgetter(1))
        if sorted_list_2[0][0]==city2:
            max_dist_city2=self.dict[city2][sorted_list_2[1][0]]
        else:   
            max_dist_city2=self.dict[city2][sorted_list_2[0][0]]
        #max_dist_city2=self.dict[city2][sorted_list_2[0][0]]
        
        via_city=""
        end_city=""
        
        if(max_dist_city1>max_dist_city2):
            via_city=city1
            end_city=sorted_list[0][0]
        else:
            via_city=city2
            end_city=sorted_list_2[0][0]
            
        
        total_max_dist=int(max(max_dist_city1,max_dist_city2)) + int(line_split[2])
        
        
        if(int(total_max_dist)>int(self.maxdistance)):
            self.maxdistance=total_max_dist
            if via_city==city1:
                self.maxdistancestring=str(total_max_dist) +":"+city2+":"+city1+":"+end_city
            else:
                self.maxdistancestring=str(total_max_dist) +":"+city1+":"+city2+":"+end_city
            
        return self.maxdistancestring
             
        
             
        
        
          
pc=PathCalculator()

print(pc.process("CHI:NYC:719"))
print(pc.process("NYC:LA:2414"))
print(pc.process("NYC:SEATTLE:2448"))
print(pc.process("NYC:HAWAII:4924"))



        
        
        
        