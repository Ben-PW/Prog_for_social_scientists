# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 12:29:29 2022

@author: u48730bp
"""

################################# BACTERIA FRAMEWORK

"""

Created on Tue Oct 11 13:46:59 2022

 

@author: Banjoman

"""

 

import random

 

class Bacteria():

    def __init__(self, environment, x, y):

        self.x = x

        self.y = y

        self.environment = environment

        self.height = 75

       

    def move(self):

        rand = random.random()

        if rand <= 0.1:

            self.y = (self.y + 1) % 300

        elif rand > 0.1 and rand <= 0.2:

            self.y = (self.y - 1) % 300

        elif rand > 0.2 and rand <= 0.95:

            self.x = (self.x + 1) % 300

        else:

            self.x = (self.x - 1) % 300

               

    def risefall(self):

        if self.height >= 75:

            carry_on = True

           

        if self.height >= 75:

            rand = random.random()

            if rand <= 0.2:

                self.height += self.height

            elif rand > 0.2 and rand <= 0.3:

                pass

            else:

                self.height -= self.height

   