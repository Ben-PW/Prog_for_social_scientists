# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:09:33 2022

@author: Banjoman
"""
######################################### Custom functions

# Function to calculate distance between agents
def distance_between(agents_row_a, agents_row_b):
    return(((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

#########################################

# Load environment
import random
import operator
import matplotlib.pyplot
import time
import agentframework

# Define number of agents and iterations
num_of_agents = 10
num_of_iterations = 100
agents = []

# Create random starting coordinates
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Create loop for random iterative movements
for n in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

    
# Visualise positions of agents via scatterplot
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

# Calculate distance between coordinates
start = time.process_time()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

end = time.process_time()

maxd = 0
mind = distance_between(agents[0], agents[1])
for i in range(0, num_of_agents):
    for j in range(i+1, num_of_agents):
        print(i,j)
        if (i > j):
            d = distance_between(agents[i], agents[j])
            if (d > maxd):
                maxd = d
            if (d < mind):
                mind = d

countmind = 0
for i in range(0, num_of_agents):
    for j in range(i+1, num_of_agents):
        d = distance_between(agents[i], agents[j])
        if (d == mind):
            countmind = countmind + 1
    
print("time elapsed calculating coordinates = " + str(end - start))