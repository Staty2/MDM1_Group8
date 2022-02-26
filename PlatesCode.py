#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:42:02 2022

@author: felix
"""
def timetocrossconstant(meters,cars):
    meters = float(meters)
    speed = float(10/2.237)
    cars = float(cars)
    return 3*cars + speed/(2*2.591) + (meters + 5.4)/(speed) - 1.5

def timetocrossacceleration(meters, cars):
    meters = float(meters)
    acceleration = 2*meters + 10.8
    return 3*cars + (acceleration/2.591)**(1/2) - 1.5

def conjestion(x,y):
    rounds = 3
    distances = [5,20,60]
    difference = []
    for i in distances:
                difference.append(timetocrossconstant(i, y))
                difference.append(timetocrossacceleration(i, y))
    difference = [round(i,rounds) for i in difference]
    return round(sum(difference)/6,rounds)
    
print('Low conjestion: \n1-1:')            
print(conjestion(1,1))
print('\n1-5:')
print(conjestion(1,5))
print('\n5-1:')
print(conjestion(5,1))
print('\n5-5:')
print(conjestion(5, 5))
print('\nHigh conjestion: \n1-10:')
print(conjestion(1,10))
print('\n10-1:')
print(conjestion(10,1))
print('\n5-10:')
print(conjestion(5,10))
print('\n10-5:')
print(conjestion(10,5))
print('\n10-10:')
print(conjestion(10, 10))


