#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 19:25:51 2021

@author: nicole
"""


#load model
import pickle
with open('finalized_LR_model_2.pkl', 'rb') as f:
    model = pickle.load(f)

import pandas as pd
from sklearn.metrics import confusion_matrix

# Importing the dataset
dataset_teste = pd.read_csv('encoding_hashes_teste_2.csv')
X_teste = dataset_teste.iloc[:, :-1].values
y_teste = dataset_teste.iloc[:, -1].values

print(X_teste)

pred = model.predict(X_teste)