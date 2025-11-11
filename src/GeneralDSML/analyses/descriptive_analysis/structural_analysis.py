import pandas as pd
import json
from typing import Any, Dict, List
from GeneralDSML.dataset_loading.dataset_loaders import TabularDataset
from GeneralDSML.reports.tabular_reports import (
    TabularDataReport,
    NumericalColumnReport,
    CategoricalColumnReport,
    TextColumnReport,
    DatetimeColumnReport,
)
from datetime import datetime


class TabularStructuralAnalysis:
    def __init__(self, dataset: TabularDataset, report: TabularDataReport):
        self.dataset = dataset.dataset
        self.report = report

    def set_rows_and_columns(self):
        self.report.n_rows, self.report.n_columns = self.dataset.shape[0], self.dataset.shape[1]

    def set_head_and_tail(self):
        self.report.head = self.dataset.head().values.tolist()
        self.report.tail = self.dataset.tail().values.tolist()

    def get_column_type(self, col: str) -> str:
        return str(self.dataset[col].dtype)

    def get_nulls_per_column(self, col: str) -> int:
        return self.dataset[col].isnull().sum().sum()

    def get_rows_with_nulls_in_col(self, col: str) -> List[List[Any]]:
        return self.dataset[self.dataset[col].isnull()].values.tolist()

    """
    def infer_implicit_dtype(self, col):
        ...
    """

    def save_to_json(self, report_name: str | None = None) -> str:
        # Save to JSON
        if not report_name:
            report_name = f"structural_analysis_{datetime.now()}"
        with open(f"{report_name}.json", "w") as f:
            json.dump(self.report, f, indent=4)
        return f"Report saved to {report_name}.json"

    def analyze(self, report_name: str | None = None) -> TabularDataReport:
        # Get rows and columns
        self.set_rows_and_columns()

        # Get head and tail of dataset
        self.set_head_and_tail()

        # Check if dataset has nulls
        if self.dataset.isnull().any().any():
            self.report.has_nulls = True
        else:
            self.report.has_nulls = False

        # Go over each column gathering relevant structural information
        for col in self.dataset.columns:
            detected_type = self.get_column_type(col)
            missing_count = self.get_nulls_per_column(col)
            if self.report.n_rows:
                missing_pct = (self.get_nulls_per_column(col) / self.report.n_rows) * 100
            else:
                missing_pct = None
            implicit_dtype = ""
            rows_with_null = self.get_rows_with_nulls_in_col(col)
            if detected_type.startswith("float") or str(self.get_column_type(col)).startswith("int"):
                self.report.numerical_columns[col] = NumericalColumnReport(
                    name=col,
                    missing_count=missing_count,
                    missing_pct=missing_pct,
                    implicit_dtype=implicit_dtype,  # TODO: self.infer_implicit_dtype(col)
                    rows_with_nulls=rows_with_null,
                )
            elif detected_type.startswith("object"):
                self.report.categorical_columns[col] = CategoricalColumnReport(
                    name=col,
                    missing_count=missing_count,
                    missing_pct=missing_pct,
                    implicit_dtype=implicit_dtype,  # TODO: self.infer_implicit_dtype(col)
                    rows_with_nulls=rows_with_null,
                )
            elif detected_type.startswith("datetime"):
                self.report.datetime_columns[col] = DatetimeColumnReport(
                    name=col,
                    missing_count=missing_count,
                    missing_pct=missing_pct,
                    implicit_dtype=implicit_dtype,  # TODO: self.infer_implicit_dtype(col)
                    rows_with_nulls=rows_with_null,
                )
            else:
                self.report.text_columns[col] = TextColumnReport(
                    name=col,
                    missing_count=missing_count,
                    missing_pct=missing_pct,
                    implicit_dtype=implicit_dtype,  # TODO: self.infer_implicit_dtype(col)
                    rows_with_nulls=rows_with_null,
                )
        return self.report
