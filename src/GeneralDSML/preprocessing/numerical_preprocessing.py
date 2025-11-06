import pandas as pd
import numpy as np


class NumericalDataPreprocessor:
    def __init__(self, df):
        self.df = df
        self.cleaned_df = None

    def scaler(self): ...

    def normalizer(self): ...

    def outlier_healer(self): ...
