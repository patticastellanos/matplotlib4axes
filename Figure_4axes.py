#!/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from get_data import get_data
################################################################################    
if __name__ == "__main__":
    """ This is a script to make a figure with 4 axes"""
    
    # Make data arrays
    alt,altp,pres,aero,no2 =  get_data()   
    
    # open figure
    figure = plt.figure()

    #make the first line plot
    ax = plt.subplot(111)
        
        
    # plot the NO2 profile
    ax.plot(no2,pres, 'm-',label='NO'+r'$_{2}$'+' Profile')
        
    # set the limits of the x and y axis
    ax.set_ylim(400,max(pres))
    ax.yaxis.set_ticks_position('left')
    ax.set_xlim(0,1.1*max(no2))
    
    # invert y-axis because pressure goes from high to low in the atmosphere
    ax.invert_yaxis()     
        
    # set the labels and colors for the X & Y Axes
    fontdict = {"size":10, "color": 'm'}
    ax.set_xlabel('NO'+r'$_{2}$'+' Concentration [pptv]',fontdict=fontdict)
    ax.spines['bottom'].set_color('m')
    ax.tick_params(axis='x', which='major', labelsize=9,color='m',labelcolor='m')
   
    fontdict = {"size":10}
    ax.set_ylabel('Pressure [hPa]',fontdict=fontdict)
    ax.tick_params(axis='both', which='major', labelsize=9)
        

    # set up the second x 
    newx = ax.twiny()
    newx.xaxis.set_ticks_position('top')
    newx.xaxis.set_label_position('top')
    
    #set up the second y axis inheriting the new x axis
    newxy = newx.twinx()        
    newxy.yaxis.set_ticks_position('right')
    newxy.yaxis.set_label_position('right')
    
    # plot the aerosol extinctin profile as a function of altitude
    newxy.plot(aero,alt,'b-',label='Aerosol Extinction')
        
    # set the limits for the x and y axes
    newxy.set_xlim([0,max(aero)])
    newxy.set_ylim([0,np.interp([400],pres,altp)])
        
    # set the labels and colors for the X & Y Axes  
    fontdict = {"size":10, "color": 'b'}
    newx.set_xlabel('532 nm Aerosol Extinction [km'+r'$^{-1}$]',labelpad=10,fontdict=fontdict)
    newx.tick_params(axis='both', which='major', labelsize=9, color='b',labelcolor='b')
    ax.spines['top'].set_color('b')
    
    fontdict = {"size":10}
    newxy.set_ylabel('Altitude [km]',rotation=270,labelpad=20,fontdict=fontdict)
    newxy.tick_params(axis='both', which='major', labelsize=9)
    


    # save the figure 
    ss = 16  #cm
    ss = ss*0.4
    figure.set_size_inches(ss,ss)
    plt.subplots_adjust(left=0.09,right=0.92,wspace=0.28,top=0.90,bottom=0.08,hspace=0.45)
    figure.savefig('Figure_4axes.pdf')
    figure.clear
    #plt.show()
    

    
    
