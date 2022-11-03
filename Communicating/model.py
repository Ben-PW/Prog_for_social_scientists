# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:43:32 2022

@author: Banjoman
"""

# Load environment
#import random
#import operator
import matplotlib.pyplot
import matplotlib.animation
#import time
import agentframework
import csv

# Define number of agents and iterations
num_of_agents = 10
num_of_iterations = 1000
neighbourhood = 20
agents = []

#a = agentframework.Agent()
#print(a.y, a.x)

# Importing raster data section
environment = []
txt = open('in.txt', newline = '')
reader = csv.reader(txt, quoting = csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = [] # define each row in data as a list
    for value in row:
        rowlist.append(value) # append each value in the row to the list
    environment.append(rowlist) # append each list of values to the environment list
txt.close()

# Check data import
# matplotlib.pyplot.imshow(environment)
# matplotlib.pyplot.show()


# Function to calculate distance between agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5


# Create agents and random starting coordinates
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, neighbourhood, i))

# Action agent behaviours
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        agents[i].move()
        agents[i].eat()
        agents[i].chunder()
        agents[i].share(neighbourhood)


  
# Visualise positions of agents via scatterplot
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

# Create export environment data post agent actions
txtout = open('out.txt', 'w', newline='')
writer = csv.writer(txtout, delimiter=',')
for row in environment:
    writer.writerow(row) # List of values.
txtout.close()
