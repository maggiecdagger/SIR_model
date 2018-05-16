#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  18 00:29:17 2018

@author: Maggie P Cai
"""

from __future__ import print_function
import click
import collections
from collections import *
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
import functions
from functions import *
import inspect
from inspect import *
from functools import partial

def main():
    top = Tk()
    top.geometry("1000x1000")
    top.title("Beyond SIR")
    top_textframe = Frame(top)

    buttonFont=tkFont.Font(family="Helvetica", size=18, weight="bold")
    buttonFont2 = tkFont.Font(family="Helvetica", size=12, weight="bold")
    labelFont=tkFont.Font(family="Helvetica", size=12, weight="bold")
    eqFont=tkFont.Font(family="Helvetica", size=20)

    canvas = Canvas(top, width=1000, height=1000, bg = '#4e7a7a')
    canvas.create_text(300,60,text="In this part, consider the real-life event below:"+"\n"
                       +"A new strain of virus M521, M521mut has escaped the safety protocol of a UNC BME lab."+"\n"
                       +"CDC has been informed and is closely monitoring the spread of the strain."+"\n"
                       +"The rival neighbor of the outbreak lab has also been working on an anti-M521 pill for years."+"\n"
                       +"However, this antivirual drug can only guarantee temporary immunity against the new strain.",font=labelFont,justify=LEFT)
    
    canvas.create_text(450,200, text="Some facts about M521mut:"+"\n"
                       +"1) the susceptible individuals first go through a latent period after infection, and before becoming infectious."+"\n"
                       +"2) an infected individual is either quarantined or offered the anti-viral drug, and acquires temporary immunity either way."+"\n"
                       +"  (hint: which population does one belong to when they acquire temporary immunity?)"+"\n",font=labelFont,justify=LEFT)
    
    canvas.create_text(400,320,text="Other facts:"+"\n"
                       +"1) we can assume in the beginning of the outbreak, only the susceptible population is non-zero."+"\n"
                       +"2) the susceptible population grows at a constant rate."+"\n"
                       +"3) there is a natural mortality rate in all populations."+"\n"
                       +"4) there is a M521mut specific mortality rate (to all infected populations only, excluding latent)."+"\n"
                       +"5) a quarantined individual is still infected."+"\n"
                       +"   However, they could acquire temporary immunity after being quarantined for a certain amount of time."+"\n"
                       +"6) individuals in the removed population could lose immunity and become susceptible again .",font=labelFont,justify=LEFT)
      


    pars_label = Label(top, text=" Number of Parameters: ",font=labelFont)
    pars_label.configure(width=20, background='#f2ec8a', relief = FLAT)
    pars_label_window = canvas.create_window(40, 400,anchor=NW, window=pars_label)
    
    pars_entry = Entry(top, bd=1, width=5, bg="#f2ec8a")
    pars_entry_window = canvas.create_window(40, 430,anchor=NW, window=pars_entry)


    pars_name_label = Label(top, bd=0, text="symbol",width=8, bg='#4e7a7a')
    pars_name_label_window = canvas.create_window(30, 460,anchor=NW, window=pars_name_label)
        
    pars_num_label = Label(top, bd=0, text="value",width=8, relief=FLAT, bg='#4e7a7a')
    pars_num_label_window = canvas.create_window(100, 460,anchor=NW, window=pars_num_label)

    paras_list = OrderedDict()
    
    enterpars_button= Button(top, text="+",font=buttonFont, height=1, padx=1.5,pady=1.5,width=2,
                             command = lambda:create_paras(top, paras_list))
    enterpars_button.configure(activebackground="#f2ec8a")
    enterpars_button_window = canvas.create_window(100,430, anchor=NW, window=enterpars_button)
                      
 
    vars_label = Label( top, text=" Number of Variables: ",font=labelFont, width=20, relief=FLAT, background='#b74514')
    vars_label_window = canvas.create_window(430, 400, anchor=NW, window=vars_label)
    
    vars_entry = Entry(top, bd=1, width=5, bg="#b74514")
    vars_entry_window = canvas.create_window(430, 430, anchor=NW, window=vars_entry)


    eqn_ic_list = OrderedDict()
    
    entervars_button= Button(top, text="+",font=buttonFont, height=1, padx=1.5,pady=1.5,width=2,
                             command = lambda:create_sys_input_box(top, eqn_ic_list))
    entervars_button.configure(activebackground="#b74514")
    entervars_button_window = canvas.create_window(490, 430, anchor=NW, window=entervars_button)

    paras_list.update()
    eqn_ic_list.update()
    final_button= Button(top, text="Add Model to the Python Code",font=buttonFont, height=1, padx=1.5,pady=1.5,width=25,
                             command = lambda:ext_entry())
    final_button.pack(side=LEFT)
    final_button.flash()
    final_button.place(x=350, y=600)
    canvas.pack()    
    top.mainloop()

#equations
def create_sys_input_box (master, eqn_ic_list):
        n = len(eqn_ic_list)
        print(n)        

        v1_label = Label( master, bd=0, text="d",width=1, relief=RAISED)
        v1_label.pack(side=LEFT)
        v1_label.place(x=361,y=460+n*30)

        v_entry = Entry(master, bd=0, width=2, bg="#cc5b2a")
        v_entry.pack(side=LEFT)
        v_entry.place(x=375,y=460+n*30)
        
        v2_label = Label( master, bd=0, text="/ dt = ",width=4, relief=RAISED)
        v2_label.pack(side=LEFT)
        v2_label.place(x=400,y=460+n*30)
        
        eq_entry = Entry(master, bd=1, width=35, bg="#cc5b2a")
        eq_entry.pack(side=LEFT)
        eq_entry.place(x=435,y=460+n*30)

        ic_label = Label( master, bd=0, text="IC",width=4, relief=RAISED)
        ic_label.pack(side=LEFT)
        ic_label.place(x=805,y=440)

        ic_entry = Entry(master, bd=0, width=5, bg="#cc5b2a")
        ic_entry.pack(side=LEFT)
        ic_entry.place(x=805,y=460+n*30)

        ready_button = Button(master, text="Ready (After every line of input)", height=1, padx=1.5,pady=1.5,width=26,
                           command = lambda: extract_eqn_ic(v_entry.get(), eq_entry.get(), ic_entry.get(), eqn_ic_list))    
        ready_button.pack(side=LEFT)
        ready_button.flash()
        ready_button.place(x=540,y=430)
        

    
def create_paras (master, paras_list):
    n = len(paras_list)
    name = Entry(master, bd=0, width=5, bg="#f7f3bb")
    name.pack(side=LEFT)
    name.place(x=40,y=480+30*n)
    num = Entry(master, bd=0, width=5, bg="#f7f3bb")
    num.pack(side=LEFT)
    num.place(x=120,y=480+30*n)
    
    pars_button = Button(master, text="Enter", height=1, padx=1.5,pady=1.5,width=10,
                     command = lambda:extract_paras(name.get(),num.get(),paras_list))     
    pars_button.pack(side=LEFT)
    pars_button.flash()
    pars_button.place(x=230, y=480)

##not used
def extract_paras_num (pars_entry): #create list of k and v
    n = pars_entry.get()
    while true:
        if all(c in '+-.0123456789' for c in n):
            break
    # a float contains a period (US)
    if '.' in n:
        m=float(n)
    else:
        m= int(n)
    return m
