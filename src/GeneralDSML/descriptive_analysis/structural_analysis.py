import pandas as pd
import json
from GeneralDSML.dataset_loading.dataset_loaders import TabularDataset
from datetime import datetime


class TabularStructuralAnalysis:
    def __init__(self, dataset: TabularDataset):
        self.dataset = dataset.dataset
        self.report = {}

    def set_rows_and_columns(self):
        self.report["n_rows"], self.report["n_cols"] = self.dataset.shape[0], self.dataset.shape[1]

    def set_head_and_tail(self):
        self.report["head"] = self.dataset.head().values.tolist()
        self.report["tail"] = self.dataset.tail().values.tolist()

    def get_column_type(self, col):
        return self.dataset[col].dtype

    def get_nulls_per_column(self, col):
        return self.dataset[col].isnull().sum().sum()

    def get_rows_with_nulls_in_col(self, col):
        return self.dataset[self.dataset[col].isnull()].values.tolist()

    def add_column_info(self, col):
        self.report["columns_info"]["cols"][col] = {
            "dtype": None,
            "implicit_dtype": None,
            "n_nulls": None,
            "rows_with_nulls": list(),
        }

    def add_general_column_schema(self):
        self.report["columns_info"] = {
            "numerical_columns": [],
            "categorical_columns": [],
            "datetime_columns": [],
            "text_columns": [],
            "cols": {},
        }

    """
    def infer_implicit_dtype(self, col):
        ...
    """

    def generate_report(self, report_name=None):
        # Get rows and columns
        self.set_rows_and_columns()

        # Get head and tail of dataset
        self.set_head_and_tail()

        # Check if dataset has nulls
        if self.dataset.isnull().any().any():
            self.report["hasNulls"] = True
        else:
            self.report["hasNulls"] = False

        # Initialize columns_info dict
        self.report["columns_info"] = {}

        # Add general column schema to columns_info
        self.add_general_column_schema()
        cols_info = self.report["columns_info"]["cols"]

        # Go over each column gathering relevant structural information
        for col in self.dataset.columns:
            # Add schema for particular column
            self.add_column_info(col)

            # Get column dtype
            cols_info[col]["dtype"] = str(self.get_column_type(col))

            # Get AI assisted implicit_dtype
            # cols_info[col]["implicit_dtype"] = self.infer_implicit_dtype(col)

            # Add to numerical, categorical, datetime and text columns

            # Get number of nulls for the given column
            cols_info[col]["n_nulls"] = str(self.get_nulls_per_column(col))

            # Get rows with nulls in the current column
            cols_info[col]["rows_with_nulls"].extend(self.get_rows_with_nulls_in_col(col))

        # Save to JSON
        if not report_name:
            report_name = f"structural_analysis_{datetime.now()}"
        with open(f"{report_name}.json", "w") as f:
            json.dump(self.report, f, indent=4)
        return f"Report saved to {report_name}.json"
