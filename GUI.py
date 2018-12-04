# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:09:33 2018

@author: Administrator
"""

import random
import matplotlib.animation 
import matplotlib
import requests
import bs4
import agentframework2

import time
import tkinter
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import matplotlib.backends.backend_tkagg

start = time.clock()


num_of_agents = 10
num_of_iterations = 100
agents = []
neighbourhood = 20



fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#IO. Read in the environment
f = open("in.txt")
environment = []
for line in f:
    parsed_line = str.split(line,",")
    data_line = []
    for word in parsed_line:
        data_line.append(float(word))
    environment.append(data_line)
print(environment)
f.close()



# Make the agents.
for i in range(num_of_agents):
    #agents.append([random.randint(0,299),random.randint(0,299)])
    agents.append(agentframework2.Agent(environment,agents))



def update(frame_number):
    
    fig.clear()
    #setup plot
    matplotlib.pyplot.ylim(299, 0)
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    


    
#plot the agent
#matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety(),facecolors='none', edgecolors='black')




    
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
    

#innitial GHI main window
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 
 
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    canvas.show()

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)



root.mainloop()