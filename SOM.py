# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:35:21 2020

@author: YASH
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom
from pylab import bone,pcolor,colorbar,plot,show

dj=pd.read_csv("LDA_o.csv")
X=dj.iloc[:,:-1].values
Y=dj.iloc[:,-1].values

som=MiniSom(x=20,y=20,input_len=11,sigma=1.0,learning_rate=0.5)
som.random_weights_init(X)
som.train_random(data=X,num_iteration=100)

bone()
pcolor(som.distance_map().T)
colorbar()
markers = ['o', 'v', '1', '3', '8', 's', 'p', 'x', 'D', '*']
colors = ["r", "g", "b", "y", "c", (0,0.1,0.8), (1,0.5,0), (1,1,0.3), "m", (0.4,0.6,0)]


for i,x in enumerate(X):
    w=som.winner(x)
    
    #plot(w[0]+.5,w[1]+.5,markers[Y[i]], markerfacecolor='None', markeredgecolor=colors[Y[i]], markersize=10, markeredgewidth=2)

#axis([0,som.weights.shape[0],0,som.weights.shape[1]])
show()
