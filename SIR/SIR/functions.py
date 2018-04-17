#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 23:32:25 2018

@author: Maggie P Cai
"""
from sympy import *
import numpy as np
from scipy import integrate
import matplotlib
matplotlib.use('TkAgg')

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
    import tkFont
else:
    import tkinter as Tk
    import tkinter.font as tkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import pickle
from Tkinter import *
import os
def entry(S0_entry,I0_entry,R0_entry,infection_entry,removed_entry, Start_entry, Stop_entry, Steps_entry):
    init, time = initial_conditions_entry(S0_entry,I0_entry,R0_entry, Start_entry, Stop_entry, Steps_entry)
    t = np.linspace(time[0],time[1],time[2])
    args = (infection_entry, removed_entry)
    X = integrate.odeint(solvr, init, t, args)
    print(X)

    fig = Figure()
    a = fig.add_subplot(111)
    ax=a.plot(X)
    a.legend(ax,['Susceptible','Infected','Removed'],loc=0)
    a.set_xlabel('time steps')
    a.set_ylabel('population')
    P=parameters_entry(infection_entry,removed_entry)
    _a=str(P[0])
    _b=str(P[1])
    alpha=r'$\alpha=%s$'%(_a)
    beta=r'$\beta=%s$'%(_b)
    _S0=str(init[0])
    _I0=str(init[1])
    _R0=str(init[2])
    S0='S(0) = %s' %(_S0)
    I0='I(0) = %s' %(_I0)
    R0='R(0) = %s' %(_R0)   
    a.set_title("Initial conditions: "+S0+",   "+I0+",   "+R0+"\n"+"Parameters: "+alpha+",   "+beta)
    root=Tk()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2TkAgg(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
    
def parameters_entry(infection_entry, removed_entry): #extracts user inputs of infection and removal rates
    R=[0,0]
#         strip() removes any leading or trailing whitespace
#        text_contents = infection_rate
#         make sure that all char can be in a typical number
    while True:
        infection_rate= infection_entry.get()
        removed_rate= removed_entry.get()
        if all(c in '+-.0123456789' for c in infection_rate)and all(c in '+-.0123456789' for c in removed_rate):
            break
    # a float contains a period (US)
    if '.' in infection_rate:
        i= float(infection_rate)
    else:
        i= int(infection_rate)
        
    if '.' in removed_rate:
        r= float(removed_rate)
    else:
        r= int(removed_rate)
    R[0]=i
    R[1]=r
    return R
 
def initial_conditions_entry(a,b,c,d,e,f): #extracts user inputs of infection and removing rates
    C=[0,0,0]
    T=[0,0,0]
    while True:
        S0_= a.get()
        I0_= b.get()
        R0_= c.get()
        Start_= d.get()
        Stop_= e.get()
        Steps_= f.get()
        if all(c in '+-.0123456789' for c in S0_)and all(c in '+-.0123456789' for c in I0_)and all(c in '+-.0123456789' for c in R0_):
            break
    # a float contains a period (US)
    if '.' in S0_:
        S0= float(S0_)
    else:
        S0= int(S0_)
        
    if '.' in I0_:
        I0= float(I0_)
    else:
        I0= int(I0_)
    
    if '.' in R0_:
        R0= float(R0_)
    else:
        R0= int(R0_)

    if '.' in Start_:
        Start_= float(Start_)
    else:
        Start_= int(Start_)

    if '.' in Stop_:
        Stop_= float(Stop_)
    else:
        Stop_= int(Stop_)
        
    if '.' in Steps_:
        Steps_= float(Steps_)
    else:
        Steps_= int(Steps_)
        
    C[0]=S0
    C[1]=I0
    C[2]=R0

    T[0]=Start_
    T[1]=Stop_
    T[2]=Steps_
    return C, T    


def solvr(X, t, infection_entry, removed_entry):
    S, I, R = X
    P=parameters_entry(infection_entry, removed_entry)
    return [-P[0]*S*I,P[0]*S*I-P[1]*I,P[1]*I]
    
