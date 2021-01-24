# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 09:10:41 2021

@author: antoi
"""

import numpy as np

inputData = np.load("Data\inputData.npy", allow_pickle=True).flat[0]
subjectSplit = np.load("Data\subjectSplit.npy", allow_pickle=True).flat[0]