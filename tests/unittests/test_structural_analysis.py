from src.GeneralDSML.descriptive_analysis.structural_analysis import TabularStructuralAnalysis
from src.GeneralDSML.dataset_loading.dataset_loaders import TabularDataset
import pytest


@pytest.fixture
def tabular_structural_analysis():
    path = "../tests/test_datasets/train.csv"
    dataset = TabularDataset(path)
    return TabularStructuralAnalysis(dataset=dataset)


def test_rows_and_columns(tabular_structural_analysis):
    tabular_structural_analysis.set_rows_and_columns()
    assert tabular_structural_analysis.report["n_rows"] == "80"
    assert tabular_structural_analysis.report["n_cols"] == "90"


# def test


if __name__ == "__main__":
    analysis = TabularStructuralAnalysis(dataset)
    analysis.generate_report(report_name="biopics_test")
