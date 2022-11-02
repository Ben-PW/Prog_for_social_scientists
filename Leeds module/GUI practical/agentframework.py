# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:09:33 2022

@author: Banjoman
"""
import random

class Agent():
    def __init__(self, environment, agents, neighbourhood, i, x, y):
        # values within agent that determine location, taken from reading 'in.txt'
        self.x = x
        self.y = y
        # create shared environement for agents
        self.environment = environment
        self.store = 0
        # create shared list of agents
        self.agents = agents
        #self.neighbourhood = neighbourhood
        self.i = i
        
    def move(self):
        # random movement by 1 on each axis
        # random.random generates random integer between 0-1
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
    
    def eat(self): 
        # consume resources from environment
        # if 0 < x < 10 resource at location, add x quantity of resource at location to self.store
        if self.environment[self.y][self.x] > 0:
            if self.environment[self.y][self.x] <= 10:
                self.store += self.environment[self.y][self.x]
                self.environment[self.y][self.x] = 0
            else: 
                # if x > 10 resource at location, add only 10 resource to self.store
                self.environment[self.y][self.x] -= 10
                self.store += 10
            
    def chunder(self):
         # deposit resources back into environment when self store threshold is reached
        if self.store >= 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0
            # check agents are vomiting
            #print('splat')
    
    def distance_between(self, agent):
        # Calculate distance between self and other agents
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    def share(self, neighbourhood):
        # agents pool resources with agents within range of 'neighbourhood'
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))

