#!/usr/bin/env python3
import math
Speed_limit = input('what is the speed limit (in mph)? ')
Acceleration = input('what is the average 0-60? ')
Speed_limit = float(Speed_limit)/2.237
Acceleration = 26.82/float(Acceleration)
Bridge_length = input('what is the length of the bridge (in m)? ')
Waiting_time = input('how long are people willing to wait (in s)? ')

def numberofcars(Speed_limit,Acceleration,Bridge_length,Waiting_time):
    Bridge_length = float(Bridge_length)
    Waiting_time = float(Waiting_time)
    if (Speed_limit**2)/(2*Acceleration) < Bridge_length:
        return math.trunc((1/3)*(Waiting_time - (2*Bridge_length + 10.8)/Speed_limit - (10.8/Acceleration)**(1/2)))
    elif (Speed_limit**2)/(2*Acceleration) > Bridge_length:
        return math.trunc((1/3)*(Waiting_time - ((2*Bridge_length + 10.8)/Acceleration)**(1/2) - (10.8/Acceleration)**(1/2)))

def redlighttime(numberofcars,Acceleration):
    return round(1.5 + (10.8/Acceleration)**(1/2) + 3*(numberofcars - 1), 2)

def yellowlighttime(redlightime,Speed_limit):
    Speed_limit = float(Speed_limit)*0.2237
    return round(redlighttime - Speed_limit, 2)

numberofcars = numberofcars(Speed_limit, Acceleration, Bridge_length, Waiting_time)
redlighttime = redlighttime(numberofcars, Acceleration)
yellowlighttime = yellowlighttime(redlighttime, Speed_limit)

print('\nNumber of cars making it through:', numberofcars)
print('Time till yellow light:', yellowlighttime)
print('Time till red light:', redlighttime)

