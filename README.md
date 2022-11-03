# Prog_for_social_scientists
Repo for work done in Andy Turner's module

This repo contains all the files for the programming for social scientists module, the final version of the code can be found in the 'GUI practical' file. 

To run the code, the user will need to download the 'model', 'agentframework' and 'in' files and store them in the same folder. The 'model' file should then be run, either through the command line or a Python IDE.  

Running this code generates a number of Agents in a simulated environment, and will iterate simple behaviours such as moving, eating, sharing resources, and vomiting. The code will produce a GUI which will allow the user to run the code via user input, and will display an animated view of the agents as they act. 

## Contents

presented in descending order of code progress

'GUI practical'
* agentframework - final code for agent behaviour
* model - final code for module (starting positions for agents web-scraped and appended, animation attached to GUI)
* in - data for generating environment

'Animation'
* agentframework - code for agent behaviour
* model - code at end of animation practical (animation of behaviours added)
* in - data for generating environment

'Communication'
* agentframework - code for agent behaviour
* model - code at end of communication practical (more complex behaviours added)
* in - data for generating environment

'I/O'
* agentframework - code for agent behaviour
* model - code at end of I/O practical (raster data used to generate environment, code shrunk)
* in - data for generating environment

'Agents!'
* model - code at end of Agents! practical (basic behaviours created)

## Known issues

NB, issues relate only to the code in the 'GUI' folder, as this is the version of the code that is intended to be run. 

* Code generates two outputs, 'Model' (intended GUI output) and 'Figure 1'. Figure 1 is an additional GUI with additional menu elements intended to be attached to 'Model'
* Stopping condition built into update() and gen_func() functions occasionally means animation wont begin, please interrupt and restart code if this happens
* Potential bug with the 'share' behaviour - print statements were used to check whether agents were sharing, how far away the involved agents were from each other and how much they shared. Shares with relative distances of 0 were noted, which suggests they may have been sharing with themselves. 

## Future progress

I would like to integrate more user interactions in the GUI, such as allowing the user to alter the stopping conditions, agent number etc without having to alter the source code. Sorting out the 'Figure 1' issue would be a bonus here

I would also like to add an additional agent type with different base behaviours but which would interact with the agents already in the model. AN example could be 'sheepdog' agents, which could try and follow agents and herd them in a particular direction. 
