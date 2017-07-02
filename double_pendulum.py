#! usr/bin/env python
# -*- coding:utf-8 -*-
from sympy import *
from sympy import Derivative as D
import math
import numpy as np

var("x1 x2 y1 y2 l1 l2 m1 m2 th_1 th_2 dth_1 dth_2 ddth_1 ddth_2 t g tmp tmp2")

#the coordinates of the two balls are (x1,y1),(x2,y2)
x1 = l1 * sin(th_1(t))
y1 = -l1 * cos(th_1(t))
x2 = l1 * sin(th_1(t)) + l2 * sin(th_2(t))
y2 = -l1 * cos(th_1(t)) - l2 * cos(th_2(t))

v_x1 = diff(x1, t)
v_x2 = diff(x2, t)
v_y1 = diff(y1, t)
v_y2 = diff(y2, t)

#lagrange value
L = m1/2 * (v_x1**2 + v_y1**2) + m2/2 * (v_x2**2 + v_y2**2) - m1 * g * y1 - m2 * g * y2
print("the lagrange value is:\n")
pprint(simplify(L))

#calculate lagrange equation
def lagrange_equation(L, th):
    ddL_th = L.subs(D(th(t),t), tmp).diff(tmp,1).subs(tmp, D(th(t),t))
    dL_th = L.subs(D(th(t),t), tmp).subs(th(t),tmp2).diff(tmp2,1).subs(tmp2,th(t)).subs(tmp,D(th(t),t))
    L_equ = ddL_th.diff(t,1) - dL_th
    print("the lagrange equation is:\n")
    pprint(simplify(L_equ))
    return L_equ
    
    








