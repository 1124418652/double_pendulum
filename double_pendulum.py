#! usr/bin/env python
# -*- coding:utf-8 -*-
from sympy import *
from sympy import Derivative as D
import math


var("x1 x2 y1 y2 l1 l2 m1 m2 th_1 th_2 dth_1 dth_2 w_1 w_2 dw_1 dw_2 ddth_1 ddth_2 t g tmp tmp2")

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
print("\n")

#calculate lagrange equation
def lagrange_equation(L, th):
    ddL_th = L.subs(D(th(t),t), tmp).diff(tmp,1).subs(tmp, D(th(t),t))
    dL_th = L.subs(D(th(t),t), tmp).subs(th(t),tmp2).diff(tmp2,1).subs(tmp2,th(t)).subs(tmp,D(th(t),t))
    L_equ = ddL_th.diff(t,1) - dL_th
    print("the lagrange equation of %r is:\n"%th)
    pprint(simplify(L_equ))
    print("\n")
    return L_equ
    
"""
在返回的拉格朗日方程中含有二介导数，所以需要通过以下关系将其转化为一介微分方程组：
dth_1 = w1
dth_2 = w2
"""
change_list = [
    (D(th_1(t),t,t), dw_1),
    (D(th_2(t),t,t), dw_2),
    (D(th_1(t),t), dth_1),
    (D(th_2(t),t), dth_2),
    (th_1(t), th_1),
    (th_2(t), th_2)
]

#constructing differential equations
equ_1 = expand(simplify(lagrange_equation(L, th_1).subs(change_list)))
equ_2 = expand(simplify(lagrange_equation(L, th_2).subs(change_list)))

print("the differential equations are:\nequ_1:\n")
pprint(equ_1)
print("\nequ_2:\n")
pprint(equ_2)











