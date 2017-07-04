#! usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib
import numpy as np
matplotlib.use('WXAgg')
import matplotlib.pyplot as plt
from calculate import DoublePendulum, calculate_diff_equ

fig = pl.figure(figsize = (4,4))
line1, = pl.plot([0,0], [0,0], "-o")
line2, = pl.plot([0,0], [0,0], "-o")
pl.axis("equal")
pl.xlim(-4, 4)
pl.ylim(-4, 2)

pendulum = doublependulum()
pendulum.get_DoublePendulum_parameters()
pendulum.init_status[:] = 1.0, 2.0, 0, 0

x1, y1, x2, y2 = [], [], [], []
idx = 0

def update_line(event):
    global x1, y1, x2, y2, idx
    if idx == len(x1):
        x1, y1, x2, y2 = calculate_diff_equ(pendulum, np.arange(0, 1, 0.05))
        idx = 0
    line1.set_xdata([0, x1[idx]])
    line1.set_ydata([0, y1[idx]])
    line2.set_xdata([x1[idx], x2[idx]])
    line2.set_ydata([y1[idx], y2[idx]])
    fig.canvas.draw()
    idx += 1
    
import wx
id = wx.NewId()
actor = fid.canvas.manager.frame
timer = wx.Timer(actor, id = id)
timer.Start(1)
wx.EVT_TIMER(actor, id, update_line)
pl.show()
        
        
        
        
        
        
        
        
