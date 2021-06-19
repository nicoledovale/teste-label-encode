#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:39:11 2021

@author: nicole
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

hashes_fd = pd.read_csv('hashes.csv')

labelencoder = LabelEncoder()

hashes_fd['hash'] = labelencoder.fit_transform(hashes_fd['hash'])
hashes_fd

hashes_fd.to_csv('encoding_hashes_2.csv', index=False)

#-----------------TESTE

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

hashes_fd = pd.read_csv('hashes-teste.csv')

labelencoder = LabelEncoder()

hashes_fd['hash'] = labelencoder.fit_transform(hashes_fd['hash'])
hashes_fd

hashes_fd.to_csv('encoding_hashes_teste_2.csv', index=False)