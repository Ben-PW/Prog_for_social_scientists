# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 12:34:03 2022

@author: u48730bp
"""

############################### BACTERIA FRAMEWORK

import random

 

class Bacteria():

    def __init__(self, environment, x, y):

        self.x = x

        self.y = y

        self.environment = environment

        self.height = 75

       

    def move(self):

        #rand = random.random()

        if random.random() <= 0.1:

            self.y = (self.y + 1) % 300

            print('y+1')

        elif random.random() > 0.1 and random.random() <= 0.2:

            self.y = (self.y - 1) % 300

            print('y-1')

        elif random.random() > 0.2 and random.random() <= 0.95:

            self.x = (self.x + 1) % 300

            print('x+1')

        else:

            self.x = (self.x - 1) % 300

            print('x-1')

           

                

                

        

    def risefall(self):

        if self.height > 0:

            carry_on = True

           

            if self.height >= 75:

                #rand = random.random()

                if random.random() <= 0.2:

                    self.height = (self.height + 1)

                    print('rising')

                elif random.random() > 0.2 and random.random() <= 0.3:

                    pass

                else:

                    self.height = (self.height - 1)

                    print('falling (75+)')

            else:

                    self.height = (self.height - 1)

                    print('falling (75-')

        else:

            carry_on = False

            print('Bacteria landed')

 