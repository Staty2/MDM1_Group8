#!/usr/bin/env python3
from math import trunc
Speed_limit = input('what is the speed limit (in mph)? ')
Acceleration = input('what is the average 0-60? ')
Speed_limit = float(Speed_limit)/2.237
Acceleration = 26.82/float(Acceleration)
Bridge_length = input('what is the length of the bridge (in m)? ')
Waiting_time = input('how long are people willing to wait (in s)? ')

def onecarcross(Speed_limit,Acceleration,Bridge_length):
    Bridge_length = float(Bridge_length)
    if (Speed_limit**2)/(2*Acceleration) < Bridge_length:
        return round(1.5 + (2*(Bridge_length) + 10.8)/Speed_limit,2)
    elif (Speed_limit**2)/(2*Acceleration) > Bridge_length:
        return round(1.5 + ((2*(Bridge_length) + 10.8)/Acceleration)**1/2,2)

def numberofcars(Speed_limit,Acceleration,Bridge_length,Waiting_time):
    Bridge_length = float(Bridge_length)
    Waiting_time = float(Waiting_time)
    if (Speed_limit**2)/(2*Acceleration) < Bridge_length:
        onecarthrough = round(1.5 + (2*(Bridge_length) + 10.8)/Speed_limit,2)
        if Waiting_time - onecarthrough <= 1.5 + (10.8/Acceleration)**1/2:
            return 1
        elif Waiting_time - onecarthrough <= 1.5:
            return 0
        elif Waiting_time - onecarthrough > 1.5 + (10.8/Acceleration)**1/2:
            return trunc((1/3)*(Waiting_time - (2*Bridge_length + 10.8)/Speed_limit - (10.8/Acceleration)**(1/2)))
    elif (Speed_limit**2)/(2*Acceleration) > Bridge_length:
        onecarthrough = round(1.5 + ((2*(Bridge_length) + 10.8)/Acceleration)**1/2,2)
        if Waiting_time - onecarthrough <= 1.5 + (10.8/Acceleration)**1/2:
            return 1
        elif Waiting_time - onecarthrough <= 1.5:
            return 0
        elif Waiting_time - onecarthrough > 1.5 + (10.8/Acceleration)**1/2:
            return trunc((1/3)*(Waiting_time - ((2*Bridge_length + 10.8)/Acceleration)**(1/2) - (10.8/Acceleration)**(1/2)))
#the time for the first car to cross the line is 1.5 + (10.8/Acceleration)**1/2 the reation time is 1.5.

def redlighttime(numberofcars,Acceleration):
        return round(1.5 + (10.8/Acceleration)**(1/2) + 3*(numberofcars - 1) -1, 2)
#added minus one as, without it the light would go red as the car touches the line not 1.5 as .5 for reaching gears and stuff

def yellowlighttime(redlightime,Speed_limit):
        Speed_limit = float(Speed_limit)*0.2237
        return round(redlighttime - Speed_limit, 2)

# onecarcross = onecarcross(Speed_limit, Acceleration, Bridge_length)        
numberofcars = numberofcars(Speed_limit, Acceleration, Bridge_length, Waiting_time)
redlighttime = redlighttime(numberofcars, Acceleration)
yellowlighttime = yellowlighttime(redlighttime, Speed_limit)

# print('\nTime for one car to cross:', onecarcross)
print('\nNumber of cars making it through:', numberofcars)
print('Time till yellow light:', yellowlighttime)
print('Time till red light:', redlighttime)
