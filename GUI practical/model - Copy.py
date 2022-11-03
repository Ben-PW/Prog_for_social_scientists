# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:43:32 2022

@author: Banjoman
"""

# Load environment
import random
#import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
#import time
import agentframework
import csv
import tkinter
import requests
import bs4

################################## Functions

# Function to calculate distance between agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

# Function to iterate agent behaviour and create frames of animation
def update(frame_number):
    
    fig.clear()
    global carry_on
    
    for i in range(num_of_agents):

        agents[i].move()
        agents[i].eat()
        agents[i].chunder()
        agents[i].share(neighbourhood)

    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
  
    # Visualise positions of agents via scatterplot
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)  
        
# Function to return frame number passed into run()
def gen_func(b = [0]):
    a = 0
    global carry_on    
    while (a < 100) & (carry_on) : 
        yield a			# Returns control and waits next call.
        a = a + 1

# Function to create animation        
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_func, repeat=False)
    canvas.draw()

################################# End of functions

# Set gobal carry_on variable to true to facilitate stopping condition
carry_on = True  

# Define number of agents and iterations

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
      
# webscrape data for model

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html', verify=False)
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"}) # find all instances of class 'y'
td_xs = soup.find_all(attrs={"class" : "x"}) # find all instances of class 'x'
#print(td_ys)
#print(td_xs)


# Importing raster data to create environment

environment = []
txt = open('in.txt', newline = '')
reader = csv.reader(txt, quoting = csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = [] # define each row in data as a list
    for value in row:
        rowlist.append(value) # append each value in the row to the list
    environment.append(rowlist) # append each list of values to the environment list
txt.close()

# Append scraped x and y values to agents

for i in range(num_of_agents):
    y = int(td_ys[i].text) # y values in agent[i] = y value in table row[i]
    x = int(td_xs[i].text) # x values in agent[i] = x value in table row[i]
    agents.append(agentframework.Agent(environment, agents, neighbourhood, i, x, y))


# Create plot

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Create animation using run()

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)


############## Creating GUI for animation

# Create base GUI
root = tkinter.Tk()

# Title GUI = 'Model'
root.wm_title("Model")

# Configure GUI to use raster data plot as element of GUI
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
#canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(animation, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Add menu element to GUI
menu_bar = tkinter.Menu(root)

# Configure menu element to be menu bar
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)

# Configure menu to cascade options 
menu_bar.add_cascade(label="Model", menu=model_menu)

# Cascading option gives 'Run model' prompt, tied to run()
model_menu.add_command(label="Run model", command=run)
    
#def gen_function() -> obj 
#root = tkinter.Tk()


tkinter.mainloop()


# Create export environment data post agent behaviours
txtout = open('out.txt', 'w', newline='')
writer = csv.writer(txtout, delimiter=',')
for row in environment:
    writer.writerow(row) # List of values.
txtout.close()

'''
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 



'''