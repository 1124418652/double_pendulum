#! usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import math
from scipy.integrate import odeint


class DoublePendulum(object):
    def __init__(self, l1 = 1, m1 = 1, l2 = 1, m2 = 1, g = 9.8):
        self.l1, self.m1, self.l2, self.m2, self.g = l1, m1, l2, m2, g
        self.init_status = [0.0, 0.0, 0.0, 0.0]
    
    def get_DoublePendulum_parameters(self):
        par = []
        par = input("input the value of l1,m1,l2,m2 and seperated with commas:\n")
        self.l1, self.m1, self.l2, self.m2 = par
        print("the initial parameters have been set successfully!\n")
        
    def diff_equations(self, var, t):
        """
        get the differential equations of double pendunlum
        """
        th_1, th_2, w_1, w_2 = var
        l1, m1, l2, m2, g = self.l1, self.m1, self.l2, self.m2, self.g
        dth_1 = w_1
        dth_2 = w_2
        
        #the equation of th_1 
        dw1_par1 = l1 * l1 * (m1 + m2)
        dw2_par1 = l1 * l2 * m2 * np.cos(th_1 - th_2)
        con_1 = dth_2**2 * l1 * l2 * m2 * np.sin(th_1 - th_2) + g * l1 * np.sin(th_1) * (m1 + m2)
        
        #the equation of th_2
        dw1_par2 = l1 * l2 * m2 * np.cos(th_1 - th_2)
        dw2_par2 = l2**2 * m2
        con_2 = (-dth_1**2 * l1 * np.sin(th_1 - th_2) + g * np.sin(th_2)) * l2 * m2
        
        """
        calculate the linear equations:
        dw1_par1 * dw_1 + dw2_par1 * dw_2 + con_1 = 0
        dw1_par2 * dw_2 + dw2_par2 * dw_2 + con_2 = 0
        """
        dw_1, dw_2 = np.linalg.solve([[dw1_par1, dw2_par1], [dw1_par2, dw2_par2]], [-con_1, -con_2])
        return np.array([dth_1, dth_2, dw_1, dw_2])
        
        
def calculate_diff_equ(doublependulum, t):
    track = odeint(doublependulum.diff_equations, doublependulum.init_status, t)
    th1_arr, th2_arr = track[:, 0], track[:, 1]
    l1, l2 = pendulum.l1, pendulum.l2
    x1 = l1 * np.sin(th1_arr)
    y1 = -l1 * np.cos(th1_arr)
    x2 = x1 + l2 * np.sin(th2_arr)
    y2 = y1 - l2 * np.cos(th2_arr)
    return [x1, y1, x2, y2]
    
    
if __name__ == "__main__":
    import pylab as pl
    
    pendulum = DoublePendulum()
    pendulum.get_DoublePendulum_parameters()
    pendulum.init_status[:2] = input("input the initial angle of ball1 and ball2:\n") 
    t = np.arange(0, 30, 0.02)
    x1, y1, x2, y2 = calculate_diff_equ(pendulum, t)
    pl.plot(x1, y1, label = "ball up")
    pl.plot(x2, y2, label = "ball down")
    pl.title("tracks of two balls system, and the initial angles are %r %r"%(pendulum.init_status[0], pendulum.init_status[1]))
    pl.legend()
    pl.axis("equal")
    pl.show()
    
    
    
    
    

        
        
