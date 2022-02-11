#once we know how many cars are on the bridge and their timings this can limit the number of cars on one side calling the cross function
#reference https://stackoverflow.com/questions/24834158/deadlock-in-python-single-lane-bridge-implementation
class OneLaneBridge(object):
    from threading import Semaphore
#Semaphores cant go less than 0 or greater than a number we set, acquire will decrease the semaphore count until it reaches 0, release increases the count and wakes up a thread on the semaphore 
#A one-lane bridge allows multiple cars to pass in either direction, but at any point in time, all cars on the bridge must be going in the same direction.
#Cars wishing to cross should call the cross function, once they have crossed they should call finished()

def __init__(self):
    self.dir = -1
    self.bridge_access = Semaphore()
    self.cars_on_bridge = 0
    self.mutex = Semaphore()

def cross(self,direction):
    """wait for permission to cross the bridge.  direction should be either
    north (0) or south (1)."""

    self.mutex.acquire()
    if(self.dir == -1):
        self.dir = direction

    if(direction == self.dir):
        if(self.cars_on_bridge == 0):
            self.bridge_access.acquire()
        self.cars_on_bridge += 1
    else:
        self.mutex.release()
        self.bridge_access.acquire()
        self.mutex.acquire()
        self.cars_on_bridge += 1
        self.dir = direction
        self.mutex.release()

    self.mutex.release()

#using the TrafficLightTimings.py we can put in limits on how many cars go through before we acquire (reduce to 0 again before flipping the lights)