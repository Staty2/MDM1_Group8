#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 23:27:13 2022

@author: felix
"""
from math import floor

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
    rounds = 3
    distances = [5,20,60]
    xdif = x - car 
    ydif = y - car
    runsx = floor(x/car)
    runsy = floor(y/car)
    difference = []
    leftcar = []
    rightcar = []
    if xdif < 0:
        if ydif < 0:
            for i in distances:
                difference.append(timetocrossconstant(i, y))
                difference.append(timetocrossacceleration(i, y))
            return round(sum(difference)/6,rounds)
        if ydif >= 0:
            for i in distances:
                leftcar.append(timetocrossconstant(i, x))
                leftcar.append(timetocrossacceleration(i, x))
                rightcar.append(((2*runsy)+1)*timetocrossconstant(i, car) + timetocrossconstant(i, y-runsy))
                rightcar.append(((2*runsy)+1)*timetocrossacceleration(i, car) + timetocrossacceleration(i, y-runsy))
            zip_lists = zip(leftcar,rightcar)
            for leftcar, rightcar in zip_lists:
                difference.append(abs(rightcar-leftcar))
            return round(sum(difference)/6,rounds)
    elif xdif >= 0:
        if ydif < 0:
            for i in distances:
                leftcar.append(2*runsx*timetocrossconstant(i, car) + timetocrossconstant(i, x-runsx))
                leftcar.append(2*runsx*timetocrossacceleration(i, car) + timetocrossacceleration(i, x-runsx))
                rightcar.append(timetocrossconstant(i, car) + timetocrossconstant(i, y))
                rightcar.append(timetocrossacceleration(i, car) + timetocrossacceleration(i, x))
            zip_lists = zip(leftcar,rightcar)
            for leftcar, rightcar in zip_lists:
                difference.append(abs(rightcar-leftcar))
            return round(sum(difference)/6,rounds)
        if ydif >= 0:
            for i in distances:
                leftcar.append(2*runsx*timetocrossconstant(i, car) + timetocrossconstant(i, x-runsx))
                leftcar.append(2*runsx*timetocrossacceleration(i, car) + timetocrossacceleration(i, x-runsx))
                rightcar.append(((2*runsy)+1)*timetocrossconstant(i, car) + timetocrossconstant(i, y-runsy))
                rightcar.append(((2*runsy)+1)*timetocrossacceleration(i, car) + timetocrossacceleration(i, y-runsy))
            zip_lists = zip(leftcar,rightcar)
            for leftcar, rightcar in zip_lists:
                difference.append(abs(rightcar-leftcar))
            return round(sum(difference)/6,rounds)      

print('Low conjestion: \n1-1:')            
print(conjestion(1,1,3))
print('\n1-5:')
print(conjestion(1,5,3))
print('\n5-1:')
print(conjestion(5,1,3))
print('\n5-5:')
print(conjestion(5, 5, 3))
print('\nHigh conjestion: \n1-10:')
print(conjestion(1,10,6))
print('\n10-1:')
print(conjestion(10,1,6))
print('\n5-10:')
print(conjestion(5,10,6))
print('\n10-5:')
print(conjestion(10,5,6))
print('\n10-10:')
print(conjestion(10, 10, 6))
print('\n10-10:')
print(conjestion(12, 10, 4))              