#! usr/bin/env python
# -*- coding:utf-8 -*-
from sympy import *
from sympy import Derivative as D
import math
import numpy as np

var("x1 x2 y1 y2 l1 l2 m1 m2 th_1 th_2 dth_1 dth_2 ddth_1 ddth_2 t g tmp")

x1 = l1 * sin(th_1(t))
y1 = -l1 * cos(th_1(t))
x2 = l1 * sin(th_1(t)) + l2 * sin(th_2(t))
y2 = -l1 * cos(th_1(t)) - l2 * cos(th_2(t))

v_x1 = D(x1, t).doit()
print(v_x1)




