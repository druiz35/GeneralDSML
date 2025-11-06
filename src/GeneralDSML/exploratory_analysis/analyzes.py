from dataset_loading.dataset_loaders import TabularDataset
from descriptive_analysis.structural_analysis import TabularStructuralAnalysis
from descriptive_analysis.numerical_analysis import TabularNumericalAnalysis


class TabularExploratoryAnalysis:
    def __init__(self, dataset: TabularDataset):
        self.dataset = dataset
        self.structural_analysis = TabularStructuralAnalysis(dataset)
        self.numerical_analysis = TabularNumericalAnalysis(dataset, self.structural_analysis)

