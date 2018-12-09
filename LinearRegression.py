#    Copyright 2016 Stefan Steidl
#    Friedrich-Alexander-Universität Erlangen-Nürnberg
#    Lehrstuhl für Informatik 5 (Mustererkennung)
#    Martensstraße 3, 91058 Erlangen, GERMANY
#    stefan.steidl@fau.de


#    This file is part of the Python Classification Toolbox.
#
#    The Python Classification Toolbox is free software: 
#    you can redistribute it and/or modify it under the terms of the 
#    GNU General Public License as published by the Free Software Foundation, 
#    either version 3 of the License, or (at your option) any later version.
#
#    The Python Classification Toolbox is distributed in the hope that 
#    it will be useful, but WITHOUT ANY WARRANTY; without even the implied
#    warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#    See the GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with the Python Classification Toolbox.  
#    If not, see <http://www.gnu.org/licenses/>.


import numpy
import scipy.optimize


class LinearRegression(object):
    
    def __init__(self, lossFunction = 'l2', lossFunctionParam = 0.001, classification = False):
        self.__initialized = False #set to true when done
        self.lossFunction = lossFunction
        self.lossFunctionParam = lossFunctionParam
	    return None


    def fit(self, X, y):        
	  	if self.lossFunction == 'l2':
            n = numpy.size(X)
            print(n)
            mean_x, mean_y = numpy.mean(X), numpy.mean(y)
            SS_xy = numpy.sum(y*X - n*mean_x*mean_y)
            SS_xx = numpy.sum(X*X - n*mean_x*mean_x)
            b1 = SS_xy / SS_xx
            b0 = mean_y - b1*mean_x

        if self.lossFunction == 'huber':

        return (b0, b1)


    def huber_objfunc(self, X, y, params, a):
        return None


    def huber_objfunc_derivative(self, X, y, params, a):
        return None


    def huber(self, r, a):
        return None


    def huber_derivative(self, r, a):
        return None


    def paint(self, qp, featurespace):
        if self.__initialized:
            x_min, y_min, x_max, y_max = featurespace.coordinateSystem.getLimits()
            y1 = self.params[0] * x_min + self.params[1]
            x1, y1 = featurespace.coordinateSystem.world2screen(x_min, y1)
            y2 = self.params[0] * x_max + self.params[1]
            x2, y2 = featurespace.coordinateSystem.world2screen(x_max, y2)
            qp.drawLine(x1, y1, x2, y2)


    def predict(self, X):
        return None

