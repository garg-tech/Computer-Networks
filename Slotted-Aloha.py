'''Slotted Aloha is MAC protocol. In this protocol the time is divided into slots and each station is allowed to transmit only at the beginning of the slot. If two or more stations transmit at the same slot, then the data will collide and the data will be lost. The stations will wait for a random amount of time and then try again. The stations will keep trying until the data is transmitted successfully. For the random wait time we will use Bina The backoff time is calculated as follows:
    backoff(n) = random(0, 2^n - 1)
    where n is the number of collisions. The backoff time is calculated as a random number between 0 and 2^n - 1. The number of collisions is incremented by 1 each time there is a collision for the corresponding station.

Let's assume there are 6 stations. Each station has some amount of frames to transmit which should be input by user.
Implement the Slotted Aloha program using Python. Take number of time slots to be 100. Print the number of successful transmissions and the number of collisions for each station. Also print the total number of successful transmissions and the total number of collisions. Use threading to simulate simultaneous transmissions or collisions. Use Lock and Semaphore to synchronize the access to the shared channel.
'''

import threading
import random
from collections import deque

class Station(threading.Thread):
    def __init__(self, id, frames, lock, channel):
        super().__init__()
        self.id = id
        self.frames = frames
        self.collisions = 0
        self.successes = 0
        self.lock = lock
        self.channel = channel

    def run(self):
        while self.frames > 0:
            self.transmit()

    def transmit(self):
        with self.lock:
            collisions = 0
        for other in stations:
            if other.is_transmitting():
                collisions += 1
            break

        if collisions == 0:
            self.successes += 1
            self.frames -= 1
            print(f"Station {self.id} transmitted successfully")
        else:
            self.collisions += 1
            print(f"Station {self.id} collided (collisions: {self.collisions})")
            self.backoff()

    def is_transmitting(self):
        return random.random() < 0.5  # Probability of transmission

    def backoff(self):
        if(self.collisions <= 5): 
            wait_time = random.randint(0, 2**self.collisions - 1)
        elif(self.collisions > 5):
            wait_time = random.randint(0, 2**5 - 1)
        elif(self.collisions > 8):
            pass
            
        # Simulate wait time (can be replaced with actual sleep if needed)
        print(f"Station {self.id} waiting for slot {wait_time}")

if __name__ == "__main__":
    num_stations = 6
    num_slots = 32
    frames = [int(input(f"Enter number of frames for Station {i+1}: ")) for i in range(num_stations)]
    
    lock = threading.Lock()
    channel = deque()

    stations = [Station(i+1, frames[i], lock, channel) for i in range(num_stations)]

    for station in stations:
        station.start()

    for station in stations:
        station.join()

    total_successes = sum(station.successes for station in stations)
    total_collisions = sum(station.collisions for station in stations)

    print("\nResults:")
    for station in stations:
        print(f"Station {station.id}: Successes: {station.successes}, Collisions: {station.collisions}")
    
    print(f"Total Successes: {total_successes}, Total Collisions: {total_collisions}")
    
    print("\nChannel Events:")
    for message in channel:
        print(message)
