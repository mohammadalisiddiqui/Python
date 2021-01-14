# -*- coding: utf-8 -*-
"""newdata.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vq2KLwBFvL9VpKkn12i4wQHq02VyefO3
"""

import pandas as pd

a = pd.read_csv("newdata.csv")
b = pd.read_csv("marine.csv")
drop_a = a.drop(columns=["variable","source","data_value"])
drop_b = b.drop(columns=["category","variable","magnitude"])
print(a)
print(drop_a)
print(b) 
print(drop_b)

