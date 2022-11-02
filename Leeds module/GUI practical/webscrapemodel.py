# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:57:31 2022

@author: Banjoman
"""
# Load environment
import requests
import bs4
import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.animation
import time
import agentframework
import csv
import tkinter


r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html', verify=False)
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)


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

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, neighbourhood, i, x, y))

# Function to calculate distance between agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5


# Create agents and random starting coordinates
#for i in range(num_of_agents):
 #   agents.append(agentframework.Agent(environment, agents, neighbourhood, i, x, y))

# Create plot
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#def run():
 #   model_menu.entryconfig("Run model", state="disable")

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=update, repeat=False)
    canvas.draw()
    
root = tkinter.Tk()
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#Move agents
def update(frame_number):
    
    fig.clear()
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

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

    

tkinter.mainloop()

'''
# Create export environment data post agent scranning
txtout = open('out.txt', 'w', newline='')
writer = csv.writer(txtout, delimiter=',')
for row in environment:
    writer.writerow(row) # List of values.
txtout.close()
'''