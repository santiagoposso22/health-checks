#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:09:34 2020

@author: santiagopossomurillo
"""


import os 
import shutil 
import sys 

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there is not disk space, False otherwhise."""
    
    du=shutil.disk_usage(disk)
    
    #calculate the percentage of the free space""
    
    percent_free= 100* du.free / du.total
    
    #Calculate how many  free gigabytes 
    
    gygabytes_free = du.free / 2**30
    
    if percent_free < min_percent or gygabytes_free < min_gb:
        
        return True 
    return False 

def check_root_full():
    """Returns True if the root partitiion  is full. False otherwise."""
    return check_disk_full(disk="/",min_gb=2, min_percent=10)

def main(): 
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
        
    if check_root_full():   
        print("Root partition full")
        sys.exit(1)
        
    print("Everything ok.")
    sys.exit(0)
        
main()
        
        

