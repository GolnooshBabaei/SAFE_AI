import numpy as np
import pandas as pd

class SecurityRobustness:

    def __init__(self):
        pass

    def rga(self, y, yhat):
        df = pd.concat([y,yhat], axis=1, keys=['y', 'yhat'])
        ryhat = yhat.rank(method="min")
        df["ryhat"] = ryhat
        support = df.groupby('ryhat')['y'].mean().reset_index(name='support')
        