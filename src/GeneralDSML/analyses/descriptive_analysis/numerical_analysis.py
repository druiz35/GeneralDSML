import pandas as pd
from dataset_loading.dataset_loaders import TabularDataset
from descriptive_analysis.structural_analysis import TabularStructuralAnalysis
from GeneralDSML.reports.tabular_reports import TabularDataReport, NumericalColumnReport


class TabularNumericalAnalysis:
    def __init__(
        self, tabular_dataset: TabularDataset, structural_analysis: TabularStructuralAnalysis, report: TabularDataReport
    ):
        self.dataset = tabular_dataset.dataset
        self.structural_analysis = structural_analysis
        self.report = report

    def set_numerical_summary(self) -> None:
        numerical_cols = self.structural_analysis.report.numerical_columns.keys()
        numerical_summary = self.dataset[numerical_cols].describe().transpose()
        for col in numerical_cols:
            col_report = NumericalColumnReport(
                mean=numerical_summary.loc[col, "mean"],
                median=numerical_summary.loc[col, "50%"],
                std=numerical_summary.loc[col, "std"],
                min=numerical_summary.loc[col, "min"],
                per25=numerical_summary.loc[col, "25%"],
                per75=numerical_summary.loc[col, "75%"],
                max=numerical_summary.loc[col, "max"],
                skewness=0,  # TODO: Implement skewness calculation
                kurtosis=0,  # TODO: Implement kurtosis calculation
                zeros_count=0,  # TODO: Implement zeros_count
                rows_with_zeros=list(),  # TODO: Implement rows_with_zeros
            )
            self.report.numerical_columns[col] = col_report

    def analyze(self) -> TabularDataReport:
        # Get summary statistics
        self.set_numerical_summary()

        # Generate graphs
        # TODO: ...

        # Statistical distributions tests
        # TODO: ...

        # Outlier detection
        # TODO: ...

        return self.report


class NumericalOutlierUtilities:
    def IQR_outlier_detector(self, numerical_columns: list[str], df: pd.DataFrame):
        accum = dict((col, []) for col in numerical_columns)
        for index, row in df.iterrows():
            for col in numerical_columns:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                low_lim = Q1 - 1.5 * IQR
                up_lim = Q3 + 1.5 * IQR
                if row[col] >= low_lim and row[col] <= up_lim:
                    continue
                else:
                    # print(f"OUTLIER DETECTADO! Col: {col} Index: {index}")
                    accum[col].append(row)
                    break
        return accum
