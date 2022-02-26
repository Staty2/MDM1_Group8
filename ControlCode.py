#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 19:28:25 2022

@author: felix
"""
import random

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
    distances = [5,20,60]
    rounds = 3
    left = x
    right = y
    leftx = []
    righty = []
    timeright = []
    timeleft = []
    leftfull = []
    rightfull = []
    while left>0:
        going = random.randint(1,x)
        leftx.append(going)
        left -= going
        x -= going
    while right >0:
        going = random.randint(1,y)
        righty.append(going)
        right -= going
        y -= going
    if len(leftx) > len(righty):
        for i in range(0,(len(righty))):
            timeright.append(leftx[i])
            timeright.append(righty[i])
            timeleft.append(righty[i])
        for i in range(0,len(leftx)):
            timeleft.append(leftx[i])
    elif len(righty) > len(leftx):
        for i in range(0,(len(leftx))):
            timeleft.append(leftx[i])
            timeleft.append(righty[i])
            timeright.append(leftx[i])
        for i in range(0,len(righty)):
            timeright.append(righty[i])
    elif len(righty) == len(leftx):
        for i in range(0,(len(leftx))):
            timeleft.append(leftx[i])
            timeleft.append(righty[i])
            timeright.append(leftx[i])
            timeleft.append(righty[i])
    for j in distances:
        for i in timeleft:
            leftfull.append(timetocrossconstant(j, i))
            leftfull.append(timetocrossacceleration(j, i))
        for z in timeright:
            rightfull.append(timetocrossconstant(j, z))
            rightfull.append(timetocrossacceleration(j, z))
    return abs(round(sum(rightfull)/(6)-sum(leftfull)/(6),rounds))

def accuratetime(x,y):
    n = 20000
    rounds = 3
    accuratetime = 0
    while n>0:
        accuratetime += conjestion(x,y)
        n -=1
    n = 20000
    return round(accuratetime/n,rounds)

print('Low conjestion: \n1-1:')            
print(accuratetime(1,1))
print('\n1-5:')
print(accuratetime(1,5))
print('\n5-1:')
print(accuratetime(5,1))
print('\n5-5:')
print(accuratetime(5, 5))
print('\nHigh conjestion: \n1-10:')
print(accuratetime(1,10))
print('\n10-1:')
print(accuratetime(10,1))
print('\n5-10:')
print(accuratetime(5,10))
print('\n10-5:')
print(accuratetime(10,5))
print('\n10-10:')
print(accuratetime(10, 10))

    
        
        