'''
Created on Mar 4, 2012

@author: dsussman
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from itertools import cycle
from scipy.stats.kde import gaussian_kde


class plot_bw(object):
    
    marker = None
    line = None
    
    def __init__(self):
        
        marker = [k for k,v in Line2D.markers.iteritems() if v!='nothing' and type(k)!=int]
        marker.append(None)
        self.marker = cycle(marker)
    
        self.line = cycle( ["-","--","-.",":"])
        
    def plot(self, x,y,label=''):
        plt.plot(x, y, linestyle=self.line.next(), marker=self.marker.next(),markersize=6, linewidth=3, color='k',label=label)
        
#    
#def plot_bw(x, y, labels, show_legend):
#    n_lines = len(labels)
#    
#    marker = [k for k,v in Line2D.markers.iteritems() if v!='nothing']
#    marker.append(None)
#    markers = cycle(marker)
#    
#    lines = cycle( ["-","--","-.",":"])
#    if not labels:
#        labels =  [repr(k) for k in xrange(n_lines)]
#        
#    
#    for k in xrange(n_lines):
#        plot.plot_date(x, y[k,:], linestyle=lines.next(), marker=markers.next(), label=labels[k])
#        
#    if show_legend:
#        plot.legend()


def pairs(x, y=None,d=4,label=None):
    hist = False
    if not y:
        y = x
        hist = True
        

    n,_ = np.shape(x)
    
    cmap = plt.cm.jet
    
    if label is not None:
        maxl = np.max(label)
        minl = np.min(label)
        label = 256*(label-minl)/(maxl-minl)
    else:
        label = np.ones(x.shape[0])

    for d1 in xrange(d):
        for d2 in xrange(d):
            plt.subplot(d,d,d*d1+d2+1)
            if d1==d2 and np.all(x==y):
                if label is None: 
                    kde(x[:,d1])
                else:
                    #plt.hold()
                    
                    [kde(x[np.equal(label,l),d1], c=cmap(l)) for l in set(label) if sum(np.equal(label,l))>2]
            else:
                plt.scatter(x[:,d2],y[:,d1],marker='x',c=label)


def kde(data,c=None):
    kernel = gaussian_kde(data)
    r = np.max(data)-np.min(data)
    xi = np.linspace(np.min(data)-r/50, np.max(data)+r/50, 1200)
    if c is None:
        plt.plot(xi,kernel(xi))
    else:
        plt.plot(xi,kernel(xi),c=c)
    
