# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:30:27 2019

@author: prash
"""

def process(line: str) -> str:
    # Return 'VALID' or 'INVALID'
    checksum=line[0:2]
    try:
        acc_num=int(line[2:len(line)],16)
    except (ValueError):
        return "INVALID"
    sum=0
    while(acc_num>0):
        dig=acc_num%10
        sum=sum+dig
        acc_num=acc_num//10
    
    generated_checksum=hex(sum).split('x')[-1]
    
    if checksum.lower()==generated_checksum.lower():
        return "VALID"
    else:
        return "INVALID"
    
    
    
    
print(process("1C00000"))
    

def process(line: str) -> str:
    # Return 'VALID' or 'INVALID'
    if len(line)!=8:
        return "INVALID"
    checksum=line[0:2]
    try:
        acc_num=int(line[2:8],16)
    except (ValueError):
        return "INVALID"
    
    sum=0
    while(acc_num>0):
        dig=acc_num%10
        sum=sum+dig
        acc_num=acc_num//10
    
    generated_checksum=hex(sum).split('x')[-1]
    
    if checksum.lower()==generated_checksum.lower():
        return "VALID"
    else:
        return "INVALID"
    
    
    