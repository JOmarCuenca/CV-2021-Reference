import numpy as np
import pandas as pd

store_inventory = {'Jabón': [10,15], 'Papel': [12,25], 'Guantes': [30,50], 'Medicina' : [40,350]}

temp = pd.Series(store_inventory.values(),index=store_inventory.keys())

print(temp)