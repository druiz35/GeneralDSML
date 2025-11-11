from descriptive_analysis.structural_analysis import TabularStructuralAnalysis
import pandas as pd
from GeneralDSML.reports.tabular_reports import TabularDataReport


class TabularCategoricalAnalysis:
    def __init__(
        self, dataset: pd.DataFrame, structural_analysis: TabularStructuralAnalysis, report: TabularDataReport
    ):
        self.dataset = dataset
        self.structural_analysis = structural_analysis
        self.report = report

    def get_categorical_summary(self):
        """Returns a summary of categorical features in the dataset."""
        categorical_cols = self.structural_analysis.report["columns_info"]["categorical_columns"]
        categorical_features = self.dataset[categorical_cols]
        for col in categorical_cols:
            self.report[col] = {
                "unique_values": categorical_features[col].nunique(),
                "top_value": categorical_features[col].mode()[0],
                "top_value_freq": categorical_features[col].value_counts().iloc[0],
            }
