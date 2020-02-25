# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 20:18:02 2020

@author: renyu
"""

#%%
import numpy as np
import matplotlib.pyplot as pl 
import scipy.stats as st
import pandas as pd
import sympy as sp

#%%
x=np.arange(0,30)
pmf= st.nbinom.pmf(k= x, n=10, p=.2)
pl.stem(x, pmf);pl.grid('on')

#%%
x=np.arange(0,30)
pmf= st.nbinom.pmf(k= x, n=10, p=.2)
pl.stem(x, pmf);pl.grid('on')

#%%
x=np.arange(0,30)
pmf= st.nbinom.pmf(k= 10, n=x, p=.2)
pl.stem(x, pmf);pl.grid('on')