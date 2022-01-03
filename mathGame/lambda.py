import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['Wolf','Annihilator','Demon','Gogeta','Namek'],['HP','EXP','SPEED','DMG'])
print (df)
"""
df.drop('Z', axis= 1, inplace=True)
print (df)
df['W+Y'] = df['W'] + df['Y']
print (df)
"""
df = df[df['EXP']>0]
print (df)