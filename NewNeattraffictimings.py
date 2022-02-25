#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:26:17 2022

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

 
def conjestion(x,y,car):
    x = float(x) #x = the cars on the left
    y = float(y) #y = the cars on the right
    rounds = 3
    leftiterationsneeded = round(x/car,rounds)
    rightiterationsneeded = round(y/car,rounds)
    distances = [5,20,60]
    leftcar = []
    rightcar = []
    difference = []
    
    if leftiterationsneeded < 1:
        if rightiterationsneeded < 1:
            for i in distances:
                difference.append(timetocrossconstant(i, y))
                difference.append(timetocrossacceleration(i, y))
            difference = [round(i,rounds) for i in difference]
            return round(sum(difference)/6,rounds)
        elif rightiterationsneeded > 1:
            for i in distances:
                leftcar.append(timetocrossconstant(i, car))
                leftcar.append(timetocrossacceleration(i, car))
                rightcar.append(3*timetocrossconstant(i, car) + timetocrossconstant(i, (y-car)))
                rightcar.append(3*timetocrossacceleration(i, car) + timetocrossacceleration(i, (y-car)))
            zip_lists = zip(leftcar,rightcar)
            for leftcar, rightcar in zip_lists:
                difference.append(rightcar-leftcar)
            difference = [round(i,rounds) for i in difference]
            print(difference)
            return round(sum(difference)/6,rounds)
    elif leftiterationsneeded > 1:
        if rightiterationsneeded < 1:
            for i in distances:
                leftcar.append(2*timetocrossconstant(i, car) + timetocrossconstant(i, (x-car)))
                leftcar.append(2*timetocrossacceleration(i, car) + timetocrossacceleration(i, (x-car)))
                rightcar.append(timetocrossconstant(i, car) + timetocrossconstant(i, y))
                rightcar.append(timetocrossacceleration(i, car) + timetocrossacceleration(i, y))
            zip_lists = zip(leftcar,rightcar)
            for leftcar, rightcar in zip_lists:
                difference.append(leftcar-rightcar)
            difference = [round(i,rounds) for i in difference]
            return round(sum(difference)/6,rounds)
        elif rightiterationsneeded > 1:
            for i in distances:
                leftcar.append(2*timetocrossconstant(i, car) + timetocrossconstant(i, (x-car)))
                leftcar.append(2*timetocrossacceleration(i, car) + timetocrossacceleration(i, (x-car)))
                rightcar.append(3*timetocrossconstant(i, car) + timetocrossconstant(i, (y-car)))
                rightcar.append(3*timetocrossacceleration(i, car) + timetocrossacceleration(i, (y-car)))
            zip_lists = zip(leftcar,rightcar)
            for leftcar, rightcar in zip_lists:
                difference.append(rightcar-leftcar)
            difference = [round(i,rounds) for i in difference]
            return round(sum(difference)/6,rounds)

        
print('Low conjestion: \n1-1:')            
print(conjestion(1,1,3))
print('\n1-5:')
print(conjestion(1,5,3))
print('\n5-1:')
print(conjestion(5,1,3))
print('\nHigh conjestion: \n1-10:')
print(conjestion(1,10,6))
print('\n10-1:')
print(conjestion(10,1,6))
print('\n5-10:')
print(conjestion(5,10,6))
print('\n10-5:')
print(conjestion(10,5,6))
print('\n5-5:')
print(conjestion(5, 5, 6))
print('\n10-10:')
print(conjestion(10, 10, 6))
