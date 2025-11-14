import numpy as np
import pandas as pd
from typing import Tuple

def train_test_split(df: pd.DataFrame, test_ratio: float=0.2) -> Tuple[pd.DataFrame, pd.DataFrame]:
    random_indexes = np.random.permutation(len(df)) # Mixed indexes
    test_indexes_len = int(len(df) * test_ratio)    # The amount of indexes for test
    train_set_indexes = random_indexes[test_indexes_len:]   # Train set indexes
    test_set_indexes = random_indexes[:test_indexes_len]    # Test set indexes
    return df.iloc[train_set_indexes], df.iloc[test_set_indexes]