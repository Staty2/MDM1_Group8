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
    #x is cars on left #y is cars on right
    distances = [5,20,60]
    rounds = 3
    leftx = []
    righty = []
    timeright = []
    timeleft = []
    leftfull = []
    rightfull = []
    while x>0:
        going = random.randint(1,x) #creates a random interger in range 1 to x (including x)
        leftx.append(going) #places that random interger into leftx list
        x -= going #takes the cars that have gone away from cars on the left
    while y>0:
        going = random.randint(1,y) 
        righty.append(going)
        y -= going
    if len(leftx) > len(righty): #this is because they both take different combinations to reach 0 
        for i in range(0,(len(righty))): #right is less than left so this takes parts from left that are equal to the number parts in right and places them into time right
            timeright.append(leftx[i])
            timeright.append(righty[i])
            timeleft.append(righty[i]) #basically places all of right into time left 
        for i in range(0,len(leftx)):
            timeleft.append(leftx[i]) #places all of left into time left
    elif len(righty) > len(leftx): #same but switched
        for i in range(0,(len(leftx))): 
            timeleft.append(leftx[i])
            timeleft.append(righty[i])
            timeright.append(leftx[i])
        for i in range(0,len(righty)):
            timeright.append(righty[i])
    elif len(righty) == len(leftx): # if they are equal just place both leftx and righty into both time left and time right
        for i in range(0,(len(leftx))):
            timeleft.append(leftx[i])
            timeleft.append(righty[i])
            timeright.append(leftx[i])
            timeleft.append(righty[i])
    for j in distances: #cycles through all the distances
        for i in timeleft: 
            leftfull.append(timetocrossconstant(j, i))  #calculates the time of each group of cars under distance with speed = 10mph
            leftfull.append(timetocrossacceleration(j, i)) #calculates the time of each group of cars under distance with speed = 10mph
        for z in timeright:
            rightfull.append(timetocrossconstant(j, z))
            rightfull.append(timetocrossacceleration(j, z))
    return abs(round(sum(rightfull)/(6)-sum(leftfull)/(6),rounds)) #only 6 different sceanrios therefore average is totaltime/6. abs as right - left could be negetive but just want difference.

def accuratetime(x,y): # adds up conjestion(x,y) n times and then divides by n to get more accurate average
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

    
        
        