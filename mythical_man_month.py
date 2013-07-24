#!/usr/bin/python 
# File: mythical_man_month.py  
# Author: Chiteri, Martin Akolo (chiteri@geek.co.ke)
# Date: 20th March, 2013 
# Purpose: A parallel program to solve the "Mythical Man-month" problem  
# Background: http://en.wikipedia.org/wiki/The_Mythical_Man-Month

import gevent 
from gevent import Greenlet 

MAXIMUM_WOMEN = 9 # A constant to hold the upper limit of women allowed in the solution 
ONE_MONTH = (60*60)*24*30 # A month calculated as the same duration in seconds

def give_partial_birth(mother_id): 
    '''A function that generates baby parts given a pregnant mum''' 
    if mother_id == MAXIMUM_WOMEN - 1: # Zero based numbering
        print "Finally lady %s has given birth. Gestation complete!"  % mother_id
    else: 
        print "Mother %s making partial baby ...." % mother_id 
	
if __name__ == "__main__": 
    # Look Ma, I can actually dig list comprehensions! 8-) 
    lightweight_babies = [ Greenlet.spawn(give_partial_birth, mother) for mother in range(0, MAXIMUM_WOMEN) ] 
    new_born = gevent.joinall(lightweight_babies, timeout=ONE_MONTH) # Merge  the "kidlets" within a month  
