###################################################################################################
# Copyright (C) 2021 by Microwave Remote Sensing Lab, IITBombay http://www.mrslab.in
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, see http://www.gnu.org/licenses/
###################################################################################################
import numpy
import numpy as np


class DprviAlgo:

    def __init__(self, low_threshold, lower_factor):
        self.low_threshold = low_threshold
        self.lower_factor = lower_factor
        #self.high_threshold = high_threshold

    def compute_dprvi(self, lower_data, upper_data, lower1_data, upper1_data):
        
        c11s = lower_data
        c12s = upper_data + 1j*lower1_data
        c21s = np.conjugate(c12s)
        c22s = upper1_data
        
        c2_det = (c11s*c22s-c12s*c21s)
        c2_trace = c11s+c22s
        m = (np.sqrt(1.0-(4.0*c2_det/np.power(c2_trace,2))))
        
        #trace = (c11s+c22s)
        #det = c11s*c22s-c12s*c21s
        sqdiscr = np.sqrt(np.abs(c2_trace*c2_trace - 4*c2_det));
        egv1 = (c2_trace + sqdiscr)*0.5;
        egv2 = (c2_trace - sqdiscr)*0.5;
        
        #sqdiscr = np.sqrt(np.abs(c2_trace*c2_trace - 4*c2_det));
        #egv1 = (c2_trace + sqdiscr)*0.5;
        #egv2 = (c2_trace - sqdiscr)*0.5;
        # egf = ([egv1,egv2])
        # egfmax = float(np.max(egf))
        #egfmax = max(egv1,egv2)
        beta = np.abs(egv1/(egv1+egv2))
        
        dprvi = np.abs(1 -(m*beta))
        
        
        #ndvi = (upper_data - lower_data) / (upper_data + lower_data)
        return dprvi
