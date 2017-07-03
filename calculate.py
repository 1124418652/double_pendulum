# -*- coding:utf-8 -*-
import numpy as np
import math
from scipy.integrate import odeint


class DoublePendulum(object):
    def __init__(self, l1 = 1, m1 = 1, l2 = 1, m2 = 1, g = 9.8):
        self.l1, self.m1, self.l2, self.m2, self.g = l1, m1, l2, m2, g
    
    def get_DoublePendulum_value(self):
        val = []
        val = input("input the value of l1,m1,l2,m2 and seperated by spaces:\n")
        self.l1, self.m1, self.l2, self.m2 = val
        print("the initial value has been set successfully!\n")
        
    
