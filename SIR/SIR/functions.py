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

import compiler
from compiler import *

def entry(S0_entry,I0_entry,R0_entry,infection_entry,removed_entry, Start_entry, Stop_entry, Steps_entry):
    init, time = initial_conditions_entry(S0_entry,I0_entry,R0_entry, Start_entry, Stop_entry, Steps_entry)
    t = np.linspace(time[0],time[1],time[2])
    args = (infection_entry, removed_entry)
    X = integrate.odeint(solvr, init, t, args)
    
    fig = Figure()
    a = fig.add_subplot(3,1,1)
    ax=a.plot(t,X[:,0])
    a.legend(ax,['Susceptible'],loc=0)
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

    b = fig.add_subplot(3,1,2)
    bx=b.plot(t,X[:,1])
    b.legend(bx,['Infected'],loc=0)
    b.set_ylabel('population')
 
    c = fig.add_subplot(3,1,3)
    cx=c.plot(t,X[:,2])
    c.legend(cx,['Removed'],loc=0)
    c.set_ylabel('population')
    c.set_xlabel('time')

    root=Tk()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2TkAgg(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

#basic model    
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
    print("this is functions initial conditions entry")
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
    E = [-P[0]*S*I,P[0]*S*I-P[1]*I,P[1]*I]
    print(type(E[0]))
    return E
    #return [0.5*S-S*I*0.01,-0.5*I+S*I*0.01,0] y0=[80,100,0] a=0.5 b=0.01 t0=0 tf=50
    #the Lokta-Volterra model works

    

#############################################################################################################

#extension model

def old_ext_entry(paras_list, eqn_ic_list): #do time steps later
    num_init = []
    for v1, v2 in eqn_ic_list.values():
        while true:
            if all(c in '+-.0123456789' for c in v2):
                break
    # a float contains a period (US)
        if '.' in v2:
            v2= float(v2)
        else:
            v2= int(v2)
        num_init.append(v2)

    num_args = []
    for v in paras_list.values():
        while true:
            if all(c in '+-.0123456789' for c in v):
                break
    # a float contains a period (US)
        if '.' in v:
            v= float(v)
        else:
            v= int(v)
        num_args.append(v)
        
    t = np.linspace(0,50,5000)
    print("inputs into odeint in ext")
    print(num_init)
    print(num_args)

# need to find a way to convert equation inputs to callable type
    X = integrate.odeint(ext_solvr, num_init, t)
    
    fig = Figure()
    a = fig.add_subplot(111)
    ax=a.plot(t,X)
    a.set_xlabel('time')
    a.set_ylabel('population')
    root=Tk()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2TkAgg(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

def ext_entry():
    num_init = [200,4,0,0,0]

    args = (0.3, 0.1, 0.3, 0.3, 1.8, 0.3, 0.2, 0.2, 3.8)
        
    t = np.linspace(0,15,5000)

# need to find a way to convert equation inputs to callable type
    X = integrate.odeint(ext_solvr, num_init, t, args)
    
    fig = Figure()
    a = fig.add_subplot(111)
    ax=a.plot(t,X)
    a.set_xlabel('time')
    a.set_ylabel('population')
    a.legend(ax,['S','E','I','Q','R'],loc=0)
    root=Tk()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2TkAgg(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)


def extract_eqn_ic (var,eqn,ic, eqn_ic_list):
    eqn_ic_list[var]=[eqn, ic]
    return eqn_ic_list

def extract_paras(name,num,paras_list):
    paras_list[name]=num
    return paras_list


def ext_solvr(X, t, *args):
    P = [0.3, 0.1, 0.3, 0.3, 1.8, 0.3, 0.2, 0.2, 3.8] #what are your parameters?
    S,E,I,Q,R = X #what are the names of your variables (populations)?
    M=[P[0]-P[3]*S*I-P[1]*S+P[6]*R,
       P[3]*S*I-(P[1]+P[2])*E,
       P[2]*E-(P[1]+P[7]+P[4]+P[8])*I,
       P[8]*I-(P[1]+P[7]+P[5])*Q,
       P[4]*I+P[5]*Q-(P[1]+P[6])*R] #put in your equations here; in the order of the variables as in X above
    print(M)
    return M


