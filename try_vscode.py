import torch
import pandas as pd
import numpy as np

print(torch.__version__)

a=5

print(f'this {a}')

def myfunc(a): ##
    b=a+5
    return b

c=myfunc(7)
print(c)

a=pd.DataFrame(np.random.randint(low=0,high=9,size=(5,8)))

print(a)

# new features

