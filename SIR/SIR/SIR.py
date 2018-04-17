#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 23:32:25 2018

@author: Maggie P Cai
"""

from __future__ import print_function
import click



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

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(context_settings=CONTEXT_SETTINGS)

def enter(): 
    '''

    '''
top = Tk()
top.geometry("300x500")
top.title("SIR Model")
top_textframe = Frame(top)

buttonFont=tkFont.Font(family="Helvetica", size=18, weight="bold")
labelFont=tkFont.Font(family="Helvetica", size=14, weight="bold")
eqFont=tkFont.Font(family="Helvetica", size=20)

@enter.command('enter')



def main():
    '''
    main
    '''
    
#infection
infection_var = StringVar()
infection_var.set(" α ")

infection_label = Label( top, textvariable=infection_var,font=labelFont, relief=RAISED, background='yellow')
infection_label.pack(side=LEFT)

infection_entry = Entry(top, bd=2,width=3)
infection_entry.pack(side=LEFT)
############

#removed
removed_var = StringVar()
removed_var.set(" β ")

removed_label = Label( top, textvariable=removed_var, font=labelFont,relief=RAISED, background='yellow')
removed_label.pack(side=LEFT)


removed_entry = Entry(top, bd=2,width=3)
removed_entry.pack(side=LEFT)


#initial conditions
S0_var = StringVar()
S0_var.set(" S(0) ")

S0_label = Label( top, textvariable=S0_var,font=labelFont, relief=RAISED, background='orange')
S0_label.pack(side=LEFT)

S0_entry = Entry(top, bd=2,width=4)
S0_entry.pack(side=LEFT)

I0_var = StringVar()
I0_var.set(" I(0) ")

I0_label = Label( top, textvariable=I0_var,font=labelFont, relief=RAISED, background='orange')
I0_label.pack(side=LEFT)

I0_entry = Entry(top, bd=2,width=4)
I0_entry.pack(side=LEFT)

R0_var = StringVar()
R0_var.set(" R(0) ")

R0_label = Label(top, textvariable=R0_var,font=labelFont, relief=RAISED, background='orange')
R0_label.pack(side=LEFT)

R0_entry = Entry(top, bd=2,width=4)
R0_entry.pack(side=LEFT)

Start_var = StringVar()
Start_var.set(" Start ")

Start_label = Label(top, textvariable=Start_var,font=labelFont, relief=RAISED, background='green')
Start_label.pack(side=LEFT)

Start_entry = Entry(top, bd=2,width=4)
Start_entry.pack(side=LEFT)

Stop_var = StringVar()
Stop_var.set(" Stop ")

Stop_label = Label(top, textvariable=Stop_var,font=labelFont, relief=RAISED, background='green')
Stop_label.pack(side=LEFT)

Stop_entry = Entry(top, bd=2,width=4)
Stop_entry.pack(side=LEFT)

Steps_var = StringVar()
Steps_var.set(" Steps ")

Steps_label = Label(top, textvariable=Steps_var,font=labelFont, relief=RAISED, background='green')
Steps_label.pack(side=LEFT)

Steps_entry = Entry(top, bd=2,width=4)
Steps_entry.pack(side=LEFT)

enter_button= Button(top, text="Enter",font=buttonFont, height=1, padx=1.5,pady=1.5,width=8, command = lambda:entry(S0_entry,I0_entry,R0_entry,infection_entry,removed_entry, Start_entry, Stop_entry, Steps_entry))
enter_button.pack(side=LEFT)
enter_button.flash()


canvas1 = Canvas(top)
canvas1.create_text(85,80,text="System:"+"\n"+"  dS / dt = -α * S * I"+"\n"+"  dI / dt = α * S * I - β * I"+"\n"+"  dR / dt = β * I"+"\n"+"\n"+"  α: infection by contact"+"\n"+"  β: death by infection",font=labelFont,activefill='red',justify=LEFT)
canvas1.create_text(105,185,text="Initial Conditions, Parameters:",font=labelFont,activefill='red',justify=LEFT)
canvas1.pack()

infection_label.place(x=5,y=285)
removed_label.place(x=60,y=285)
infection_entry.place(x=5,y=315)
removed_entry.place(x=60,y=315)
enter_button.place(x=5,y=440)
S0_label.place(x=5,y=205)
S0_entry.place(x=5,y=235)
I0_label.place(x=60,y=205)
I0_entry.place(x=60,y=235)
R0_label.place(x=115,y=205)
R0_entry.place(x=115,y=235)
Start_label.place(x=5,y=360)
Start_entry.place(x=5,y=395)
Stop_label.place(x=65,y=360)
Stop_entry.place(x=65,y=395)    
Steps_label.place(x=125,y=360)
Steps_entry.place(x=125,y=395)
    
#if __name__ == "__main__":
#    main()
    

top.mainloop()


