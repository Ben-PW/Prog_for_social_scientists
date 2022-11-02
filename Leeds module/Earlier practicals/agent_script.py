# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:09:33 2022

@author: Banjoman
"""
import agentframework
import random

class Agent():
    def __init__(self):
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)

a = agentframework.Agent()