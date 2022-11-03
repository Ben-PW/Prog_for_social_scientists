# Prog_for_social_scientists
Repo for work done in Andy Turner's module

This repo contains all the files for the programming for social scientists module, the final version of the code can be found in the 'GUI practical' file. 

To run the code, the user will need to download the 'model', 'agentframework' and 'in' files and store them in the same folder. The 'model' file should then be run. 

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

* Code generates two outputs, 'Model' (intended GUI output) and 'Figure 1'. Figure 1 is an additional GUI with additional menu elements intended to be attached to 'Model'
* Stopping condition built into update() and gen_func() functions occasionally means animation wont begin, please interrupt and restart code if this happens
