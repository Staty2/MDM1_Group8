#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:42:02 2022

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

def conjestion(x,y):
    x = float(x) #x = the cars on the left
    y = float(y) #y = the cars on the right
    secondswaiting = 3
    rounds = 3
    totaltime = []
    # the difference between slowest and fastest times for 6 cars to get across a bridge was 16.333 and 28.993 however the times get exponentially bigger the length of the bridge does so proportionally the majority of times are in the lower third of the gap between those two timetakens which is 19.893 ~ 20s
    #found using how many cars can get thru in 20s on 5m, 10mph

    time1= round(timetocrossconstant(5, 10, x) + timetocrossconstant(5, 10, y) ,rounds)
    print('at 10mph on 5m bridge:', time1)
    time2= round(timetocrossacceleration(5, x) + timetocrossacceleration(5, y) ,rounds)
    print('at 60mph on 5m bridge:', time2)
    time3= round(timetocrossconstant(20, 10, x) + timetocrossconstant(20, 10, y) ,rounds)
    print('at 10mph on 20m bridge:', time3)
    time4= round(timetocrossacceleration(20, x) + timetocrossacceleration(20, y) ,rounds)
    print('at 60mph on 20m bridge:', time4)
    time5= round(timetocrossconstant(60, 10, x) + timetocrossconstant(60, 10, y) ,rounds)
    print('at 10mph on 60m bridge:', time5)
    time6= round(timetocrossacceleration(60, x) + timetocrossacceleration(60, y) ,rounds)
    print('at 60mph on 60m bridge:', time6)
    totaltime.append(time1)
    totaltime.append(time2)
    totaltime.append(time3)
    totaltime.append(time4)
    totaltime.append(time5)
    totaltime.append(time6)
    print(round(sum(totaltime)/((x+y)*6),rounds))
    
print('Low conjestion: \n1-1:')            
conjestion(1,1)
print('\n1-5:')
conjestion(1,5)
print('\n5-1:')
conjestion(5,1)
print('\nHigh conjestion: \n1-10:')
conjestion(1,10)
print('\n10-1:')
conjestion(10,1)
print('\n5-10:')
conjestion(5,10)
print('\n10-5:')
conjestion(10,5)
print('\n5-5:')
conjestion(5, 5)
print('\n10-10:')
conjestion(10, 10)
