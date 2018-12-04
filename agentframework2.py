# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 09:55:04 2018

@author: Administrator
"""

import random

class Agent():
    def __init__ (self, environment, agents):
        self.x = random.randint(0,299)
        self.y = random.randint(0,299)
        self.environment = environment
        self.store = 0
        self.agents = agents
        
    def move(self):
        
        if random.random() < 0.5:
            self.y = (self.y + 1) % 299
        else:
            self.y = (self.y - 1) % 299
            
        if random.random() < 0.5:
            self.x = (self.x + 1) % 299
        else:
            self.x = (self.x - 1) % 299
            
    def eat(self):
        if self.data[self.y][self.x] > 10:
            self.data[self.y][self.x] -= 10
            self.store += 10
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
    
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    
    