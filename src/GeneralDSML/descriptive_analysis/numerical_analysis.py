import pandas as pd
import numpy as np
from descriptive_analysis.structural_analysis import TabularStructuralAnalysis

class TabularNumericalAnalysis:
    def __init__(self, dataset: pd.DataFrame, structural_analysis: TabularStructuralAnalysis):
        self.dataset = dataset
        self.structural_analysis = structural_analysis
    
    def get_numerical_summary(self):
        """Returns a summary of numerical features in the dataset."""
        numerical_features = self.dataset.select_dtypes(include=[np.number])
        summary = numerical_features.describe().transpose()
        return summary 

class NumericalOutlierAnalysis:
    def IQR_outlier_detector(self, df):
        cols = self.structural_analysis.report["columns_info"]["numeric_columns"]
        accum = dict((col, []) for col in cols)
        for index, row in df.iterrows():
            for col in cols:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3-Q1
                low_lim = Q1 - 1.5*IQR
                up_lim = Q3 + 1.5*IQR
                if row[col] >= low_lim and row[col] <= up_lim:
                    continue
                else:
                    #print(f"OUTLIER DETECTADO! Col: {col} Index: {index}")
                    accum[col].append(row)
                    break
        return accum


