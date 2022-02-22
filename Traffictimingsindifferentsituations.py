#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:47:20 2022

@author: felix
"""
def timetocrossconstant(meters,speed,cars):
    meters = float(meters)
    speed = float(speed/2.237)
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
    leftiterationsneeded = float(x/car)
    rightiterationsneeded = float(y/car)
    totaltime = []
    if leftiterationsneeded < 1:
        if rightiterationsneeded < 1:
            time1= round(timetocrossconstant(5, 10, car) + timetocrossconstant(5, 10, y),rounds)
            print('at 10mph on 5m bridge:', time1)
            time2= round(timetocrossacceleration(5, car) + timetocrossacceleration(5, y),rounds)
            print('at 60mph on 5m bridge:', time2)
            time3= round(timetocrossconstant(20, 10, car) + timetocrossconstant(20, 10, y),rounds)
            print('at 10mph on 20m bridge:', time3)
            time4= round(timetocrossacceleration(20, car) + timetocrossacceleration(20, y),rounds)
            print('at 60mph on 20m bridge:', time4)
            time5= round(timetocrossconstant(60, 10, car) + timetocrossconstant(60, 10, y),rounds)
            print('at 10mph on 60m bridge:', time5)
            time6= round(timetocrossacceleration(60, car) + timetocrossacceleration(60, y),rounds)
            print('at 60mph on 60m bridge:', time6)
            totaltime.append(time1)
            totaltime.append(time2)
            totaltime.append(time3)
            totaltime.append(time4)
            totaltime.append(time5)
            totaltime.append(time6)
            print(round(sum(totaltime)/((x+y)*6),rounds))
        if rightiterationsneeded > 1:
            time1= round(3*timetocrossconstant(5, 10, car) + timetocrossconstant(5, 10, (y-car)),rounds)
            print('at 10mph on 5m bridge:', time1)
            time2= round(3*timetocrossacceleration(5, car) + timetocrossacceleration(5, (y-car)),rounds)
            print('at 60mph on 5m bridge:', time2)
            time3= round(3*timetocrossconstant(20, 10, car) + timetocrossconstant(20, 10, (y-car)),rounds)
            print('at 10mph on 20m bridge:', time3)
            time4= round(3*timetocrossacceleration(20, car) + timetocrossacceleration(20, (y-car)),rounds)
            print('at 60mph on 20m bridge:', time4)
            time5= round(3*timetocrossconstant(60, 10, car) + timetocrossconstant(60, 10, (y-car)),rounds)
            print('at 10mph on 60m bridge:', time5)
            time6= round(3*timetocrossacceleration(60, car) + timetocrossacceleration(60, (y-car)),rounds)
            print('at 60mph on 60m bridge:', time6)
            totaltime.append(time1)
            totaltime.append(time2)
            totaltime.append(time3)
            totaltime.append(time4)
            totaltime.append(time5)
            totaltime.append(time6)
            print(round(sum(totaltime)/((x+y)*6),rounds))
    elif leftiterationsneeded > 1:
        if rightiterationsneeded < 1:
            time1= round(2*timetocrossconstant(5, 10, car) + timetocrossconstant(5, 10, (x-car)),rounds)
            print('at 10mph on 5m bridge:', time1)
            time2= round(2*timetocrossacceleration(5, car) + timetocrossacceleration(5, (x-car)),rounds)
            print('at 60mph on 5m bridge:', time2)
            time3= round(2*timetocrossconstant(20, 10, car) + timetocrossconstant(20, 10, (x-car)),rounds)
            print('at 10mph on 20m bridge:', time3)
            time4= round(2*timetocrossacceleration(20, car) + timetocrossacceleration(20, (x-car)),rounds)
            print('at 60mph on 20m bridge:', time4)
            time5= round(2*timetocrossconstant(60, 10, car) + timetocrossconstant(60, 10, (x-car)),rounds)
            print('at 10mph on 60m bridge:', time5)
            time6= round(2*timetocrossacceleration(60, car) + timetocrossacceleration(60, (x-car)),rounds)
            print('at 60mph on 60m bridge:', time6)
            totaltime.append(time1)
            totaltime.append(time2)
            totaltime.append(time3)
            totaltime.append(time4)
            totaltime.append(time5)
            totaltime.append(time6)
            print(round(sum(totaltime)/((x+y)*6),rounds))
        if rightiterationsneeded > 1:
            time1= round(2*timetocrossconstant(5, 10, car) + timetocrossconstant(5, 10, (x-car)) + timetocrossconstant(5, 10, (y-car)),rounds)
            print('at 10mph on 5m bridge:', time1)
            time2= round(2*timetocrossacceleration(5, car) + timetocrossacceleration(5, (x-car)) + timetocrossacceleration(5, (y-car)),rounds)
            print('at 60mph on 5m bridge:', time2)
            time3= round(2*timetocrossconstant(20, 10, car) + timetocrossconstant(20, 10, (x-car)) + timetocrossconstant(20, 10, (y-car)),rounds)
            print('at 10mph on 20m bridge:', time3)
            time4= round(2*timetocrossacceleration(20, car) + timetocrossacceleration(20, (x-car)) + timetocrossacceleration(20, (y-car)),rounds)
            print('at 60mph on 20m bridge:', time4)
            time5= round(2*timetocrossconstant(60, 10, car) + timetocrossconstant(60, 10, (x-car)) + timetocrossconstant(60, 10, (y-car)),rounds)
            print('at 10mph on 60m bridge:', time5)
            time6= round(2*timetocrossacceleration(60, car) + timetocrossacceleration(60, (x-car)) + timetocrossacceleration(60, (y-car)),rounds)
            print('at 60mph on 60m bridge:', time6)
            totaltime.append(time1)
            totaltime.append(time2)
            totaltime.append(time3)
            totaltime.append(time4)
            totaltime.append(time5)
            totaltime.append(time6)
            print(round(sum(totaltime)/((x+y)*6),rounds))

print('Low conjestion: \n1-1:')            
conjestion(1,1,3)
print('\n1-5:')
conjestion(1,5,3)
print('\n5-1:')
conjestion(5,1,3)
print('\nHigh conjestion: \n1-10:')
conjestion(1,10,6)
print('\n10-1:')
conjestion(10,1,6)
print('\n5-10:')
conjestion(5,10,6)
print('\n10-5:')
conjestion(10,5,6)
print('\n5-5:')
conjestion(5, 5, 6)
print('\n10-10:')
conjestion(10, 10, 6)
print('\n10-10:')
conjestion(12, 10, 6)