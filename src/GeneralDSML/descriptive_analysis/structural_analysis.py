import pandas as pd
import numpy as np


class TabularStructuralAnalysis:
    def __init__(self, dataset):
        self.dataset = dataset
        self.report = {}
    
    def set_rows_and_columns(self):
        self.report["n_rows"], self.report["n_cols"] = self.get_rows_and_columns()
        return self.dataset.shape[0], self.dataset.shape[1]

    def generate_report(self): 
        self.set_rows_and_columns()
        self.set_head_and_tail()
        self.report["columns_info"] = {}
        cols_info = self.report["columns_info"]
        if self.dataset.isnull():
            self.report["hasNulls"] = True
        else:
            self.report["hasNulls"] = False
        self.add_general_column_info()
        for col in self.dataset.columns:
            self.add_column_info(col)
            cols_info[col]["dtype"] = self.get_column_type(col)
            # cols_info[col]["implicit_dtype"] = self.infer_implicit_dtype(col)
            cols_info[col]["n_nulls"] = self.get_column_nulls(col)
            self.report["rows_with_nulls"].update(self.get_rows_with_nulls_in_col(col))

    def add_column_info(self, col):
        self.report["columns_info"]["cols"][col] = {
            "dtype": None,
            "implicit_dtype": None,
            "n_nulls": None,
            "rows_with_nulls": set(),
        }
    
    def add_general_column_info(self):
        self.report["columns_info"] = {
            "numerical_columns": [],
            "categorical_columns": [],
            "datetime_columns": [],
            "text_columns": []
        }

    """
    def infer_implicit_dtype(self, col):
        ...
    """

    def set_head_and_tail(self):
        self.report["head"] = self.dataset.head().tolist()
        self.report["tail"] = self.dataset.tail().tolist()

    def get_column_type(self, col): 
        return self.dataset[col].dtype

    def get_nulls_per_column(self, col):
        return self.dataset[col].isnull().sum().sum()

    def get_rows_with_nulls_in_col(self, col):
        return self.dataset[self.dataset[col].isnull()].tolist()
