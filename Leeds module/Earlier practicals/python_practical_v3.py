# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:09:33 2022

@author: Banjoman
"""
# Load environment
import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import time
import agentframework
import csv

# Define number of agents and iterations
num_of_agents = 10
num_of_iterations = 1000
neighbourhood = 20
agents = []

#a = agentframework.Agent()
#print(a.y, a.x)

# Importing data section
environment = []
txt = open('in.txt', newline = '')
reader = csv.reader(txt, quoting = csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
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

# Randomise list of agents so sequence isn't the same every loop
#agent_list = list(range(num_of_agents))
#(random.shuffle(agent_list))

random.shuffle(agents)

# Create plot for agent positions
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Iterate agent behaviour as frames of animation
def update(frame_number):
    print("iteration", frame_number)
    fig.clear()
    
    #ax.imshow(environment)
    
    #for j in range(num_of_iterations):
    #for i in agent_list:
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].chunder()
        agents[i].share(neighbourhood)
            
    #for i in range(agent_list):
    for i in range(num_of_agents):
        #ax.scatter(agents[i].x,agents[i].y)
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(agents[i].x,agents[i].y)
        
# Animate

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

matplotlib.pyplot.show()

'''
# Move agents
for j in range(num_of_iterations):
    for i in agent_list:

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

# Create export environment data post agent scranning
txtout = open('out.txt', 'w', newline='')
writer = csv.writer(txtout, delimiter=',')
for row in environment:
    writer.writerow(row) # List of values.
txtout.close()

with open("out.txt", 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for row in environment:
        writer.writerow(row)
    

# Calculate distance between coordinates
start = time.process_time()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

end = time.process_time()

def getmaxd (agents):
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
                    #mindagent = [agents[i], agents[j]]
    return maxd, mind

def getmind (agents):
    countmind = 0
    mind = distance_between(agents[0], agents[1])
    for i in range(0, num_of_agents):
        for j in range(i+1, num_of_agents):
            d = distance_between(agents[i], agents[j])
            if (d == mind):
                countmind = countmind + 1
    return countmind
    
print("time elapsed calculating coordinates = " + str(end - start))
'''