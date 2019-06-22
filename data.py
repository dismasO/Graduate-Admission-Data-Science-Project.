##PACKAGES
import pandas as pd
import numpy as np, matplotlib.pyplot as plt, seaborn as sns
data = pd.read_csv('Graduate Admission Data.csv', sep=',')

##Basic info about the data

data.head(10)
data.info()
data = data.drop(['Serial No.'], axis=1)
