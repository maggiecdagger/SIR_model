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
import PIL.Image
import PIL.ImageTk
import os
import functions
from functions import *
import inspect
from inspect import *
from functools import partial

def main():
    top = Tk()
    top.geometry("1000x1200")
    top.title("Beyond SIR")
    top_textframe = Frame(top)

    buttonFont=tkFont.Font(family="Helvetica", size=18, weight="bold")
    buttonFont2 = tkFont.Font(family="Helvetica", size=12, weight="bold")
    labelFont=tkFont.Font(family="Helvetica", size=12, weight="bold")
    eqFont=tkFont.Font(family="Helvetica", size=20)

    canvas = Canvas(top, width=1000, height=1200, bg = '#4e7a7a')
    canvas.create_text(300,60,text="In this part, consider the 'real-life' event below:"+"\n"
                       +"A new strain of virus M521, M521mut has escaped the safety protocol of a UNC BME lab."+"\n"
                       +"CDC has been informed and is closely monitoring the spread of the strain."+"\n"
                       +"The rival neighbor of the outbreak lab has also been working on an anti-M521 pill for years."+"\n"
                       +"However, this antivirual drug can only guarantee temporary immunity against the new strain.",font=labelFont,justify=LEFT)
    
    canvas.create_text(450,160, text="Some facts about M521mut:"+"\n"
                       +"1) The susceptible individuals first go through a latent period after infection, and before becoming infectious."+"\n"
                       +"2) An infected individual is either quarantined or offered the anti-viral drug, and acquires temporary immunity either way."+"\n"
                       +"  (hint: which population does one belong to when they acquire temporary immunity?)"+"\n",font=labelFont,justify=LEFT)
    
    canvas.create_text(400,260,text="Other facts:"+"\n"
                       +"1) We can assume in the beginning of the outbreak, only the susceptible population is non-zero."+"\n"
                       +"2) The susceptible population grows at a constant rate."+"\n"
                       +"3) There is a natural mortality rate in all populations."+"\n"
                       +"4) There is a M521mut specific mortality rate (to all infected populations only, excluding latent)."+"\n"
                       +"5) A quarantined individual is still infected."+"\n"
                       +"   However, they could acquire temporary immunity after being quarantined for a certain amount of time."+"\n"
                       +"6) Individuals in the removed population could lose immunity and become susceptible again .",font=labelFont,justify=LEFT)
      


    pars_label = Label(top, text=" Number of Parameters: ",font=labelFont)
    pars_label.configure(width=20, background='#f2ec8a', relief = FLAT)
    pars_label_window = canvas.create_window(40, 340,anchor=NW, window=pars_label)
    
    pars_entry = Entry(top, bd=1, width=5, bg="#f2ec8a")
    pars_entry_window = canvas.create_window(40, 370,anchor=NW, window=pars_entry)


    pars_name_label = Label(top, bd=0, text="symbol",width=8, bg='#4e7a7a')
    pars_name_label_window = canvas.create_window(30, 400,anchor=NW, window=pars_name_label)
        
    pars_num_label = Label(top, bd=0, text="value",width=8, relief=FLAT, bg='#4e7a7a')
    pars_num_label_window = canvas.create_window(100, 400,anchor=NW, window=pars_num_label)

    paras_list = OrderedDict()
    
    enterpars_button= Button(top, text="+",font=buttonFont, height=1, padx=1.5,pady=1.5,width=2,
                             command = lambda:create_paras(top, pars_entry))
    enterpars_button.configure(activebackground="#f2ec8a")
    enterpars_button_window = canvas.create_window(100,370, anchor=NW, window=enterpars_button)
                      
 
    vars_label = Label( top, text=" Number of Variables: ",font=labelFont, width=20, relief=FLAT, background='#b74514')
    vars_label_window = canvas.create_window(430, 340, anchor=NW, window=vars_label)
    
    vars_entry = Entry(top, bd=1, width=5, bg="#b74514")
    vars_entry_window = canvas.create_window(430, 370, anchor=NW, window=vars_entry)
        
    eqn_ic_list = OrderedDict()
    
    entervars_button= Button(top, text="+",font=buttonFont, height=1, padx=1.5,pady=1.5,width=2,
                             command = lambda:create_sys_input_box(top, vars_entry))
    entervars_button.configure(activebackground="#b74514")
    entervars_button_window = canvas.create_window(490, 370, anchor=NW, window=entervars_button)

    paras_list.update()
    eqn_ic_list.update()

    model_button = Button(top, text="Coding"+"\n"+"Instruction",font=buttonFont, height=2, padx=1.5,pady=1.5,
                         width=15, relief=RAISED,bg="#4643db",
                         command = coding_instruction)
#    model_button.configure(activebackground='#4643db')
    model_label_window = canvas.create_window(750, 220, anchor=NW, window=model_button)
    
    
    final_button= Button(top, text="Start Graphing",font=buttonFont, height=1, padx=1.5,pady=1.5,width=15,
                             command = ext_entry)
    final_button.flash()
    final_button_window = canvas.create_window(750, 270, anchor=NW, window=final_button)
    canvas.pack()    
    top.mainloop()

#equations
def create_sys_input_box (master, p):
    while True:
        i= p.get()
        if all(c in '+-.0123456789' for c in i):
            break
    # a float contains a period (US)
    if '.' in i:
        m= float(i)
    else:
        m= int(i)
        
    for n in range(0, m):
            v1_label = Label( master, bd=0, text="d",width=1, relief=RAISED)
            v1_label.pack(side=LEFT)
            v1_label.place(x=361,y=400+n*30)

            v_entry = Entry(master, bd=0, width=2, bg="#cc5b2a")
            v_entry.pack(side=LEFT)
            v_entry.place(x=375,y=400+n*30)
        
            v2_label = Label( master, bd=0, text="/ dt = ",width=4, relief=RAISED)
            v2_label.pack(side=LEFT)
            v2_label.place(x=400,y=400+n*30)
        
            eq_entry = Entry(master, bd=1, width=35, bg="#cc5b2a")
            eq_entry.pack(side=LEFT)
            eq_entry.place(x=435,y=400+n*30)

            ic_label = Label( master, bd=0, text="IC",width=4, relief=RAISED)
            ic_label.pack(side=LEFT)
            ic_label.place(x=805,y=370)

            ic_entry = Entry(master, bd=0, width=5, bg="#cc5b2a")
            ic_entry.pack(side=LEFT)
            ic_entry.place(x=805,y=400+n*30)

    
def create_paras (master, p):
    while True:
        i= p.get()
        if all(c in '+-.0123456789' for c in i):
            break
    # a float contains a period (US)
    if '.' in i:
        m= float(i)
    else:
        m= int(i)
    for n in range(0, m):  
        name = Entry(master, bd=0, width=5, bg="#f7f3bb")
        name.pack(side=LEFT)
        name.place(x=40,y=420+30*n)
        num = Entry(master, bd=0, width=5, bg="#f7f3bb")
        num.pack(side=LEFT)
        num.place(x=120,y=420+30*n)


def coding_instruction ():
    '''
'''
    new = Toplevel()
    new.geometry("1000x1000")
    new.title("Coding Instruction")
    top_textframe = Frame(new)

    buttonFont=tkFont.Font(family="Helvetica", size=18, weight="bold")
    buttonFont2 = tkFont.Font(family="Helvetica", size=12, weight="bold")
    labelFont=tkFont.Font(family="Helvetica", size=12, weight="bold")
    eqFont=tkFont.Font(family="Helvetica", size=20)

    canvas = Canvas(new, width=1000, height=1000, bg = '#8b89ed')
    canvas.create_text(300,150,text="1) Open ‘function.py’ script in terminal by typing in:"+"\n"
                       +"    open /anaconda2/envs/SIR/lib/python2.7/site-packages/functions.py"+"\n"
                       +"2) Once in ‘function.py’, scroll down to method ‘ext_solvr’,"+"\n"
                       +"    type in the values of your parameters in P[], in the order of the parameter list"+"\n"
                       +"    you have put in in the ‘Beyond SIR’ window."+"\n"
                       +"    e.g. P = [0.1, 0.2, 0.3, 0.4, 0.5]"+"\n"
                       +"3) Now put your variables into X, e.g. A,B,C,D,E = X"+"\n"
                       +"4) Then put your equations into M in terms of P[n] (parameters) and your variables (e.g. A, B, C, D, E)"+"\n"
                       +"5) Now scroll up to 'ext_entry' and make changes in lines as indicated by the arrows:"+"\n"
                       +"    i) Put in your initial conditions into num_init, in the order of the IC list"+"\n"
                       +"    you have put in in the ‘Beyond SIR’ window."+"\n"
                       +"      e.g. num_init = [1,2,3,4,5]"+"\n"
                       +"    ii) Put in your parameter values into args, in the order of the parameter list"+"\n"
                       +"    you have put in in the ‘Beyond SIR’ window."+"\n"
                       +"      e.g. args = (0.1, 0.2, 0.3, 0.4, 0.5)"+"\n"
                       +"    iii) Change your legend to your variables:"+"\n"
                       +"      e.g. a.legend(ax,['A','B','C','D','E'],loc=0)"+"\n"
                       +"6) Go back to the 'Beyond SIR' window. Click on 'Start Graphing'."+"\n"
                       +"    Save your graph with a proper title."
                       ,font=labelFont,justify=LEFT)
    example_img1 = PIL.Image.open("/anaconda2/envs/SIR/lib/python2.7/site-packages/exampleImg_1.png")
    photo1 = PIL.ImageTk.PhotoImage(example_img1)
    canvas.create_image(50, 290, anchor=NW, image=photo1)

    example_img2 = PIL.Image.open("/anaconda2/envs/SIR/lib/python2.7/site-packages/exampleImg_2.png")    
    photo2 = PIL.ImageTk.PhotoImage(example_img2)
    canvas.create_image(50, 490, anchor=NW, image=photo2)
    
    example_img3 = PIL.Image.open("/anaconda2/envs/SIR/lib/python2.7/site-packages/exampleImg_3.png")    
    photo3 = PIL.ImageTk.PhotoImage(example_img3)
    canvas.create_image(350, 490, anchor=NW, image=photo3)
    
    canvas.pack()
    new.mainloop()
    
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
