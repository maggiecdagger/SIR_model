======
SIR_Model
======

Installation:

* Please use Python 2 not Python 3
* Recommend using Anaconda distribution of python to install (https://www.anaconda.com/download/#macos)
* To avoid version conflicts, please use conda virtual environment and install SIR_Model in it: 

$ git clone https://github.com/maggiecdagger/SIR_model.git

$ cd SIR_model

$ conda create -n SIR python=2

$ source activate SIR

(SIR) $ conda install scipy numpy sympy matplotlib Click Pillow

(SIR) $ python setup.py install


Activation:

(SIR) $ source activate SIR


To open the interface:

* need to make sure the .py and .png files are correctly added to the virtual environment:
(SIR) $ open SIR/SIR
  - copy all .py and .png files
  
(SIR) $ open /anaconda2/envs/SIR/lib/python2.7/site-packages

  - paste the .py and .png files in this directory.

(SIR) $ SIR enter


Deactivation:

(SIR) $ source deactivate
