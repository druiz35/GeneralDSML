from datasets import load_dataset
import pandas as pd
# from sklearn.datasets import load_svmlight_file


class TabularDataset:
    def __init__(self, path: str):
        self.path = path

    def load_from_file_extension(self) -> None:
        if ".csv" in self.path:
            self.load_from_csv()
        elif ".xlsx" in self.path:
            self.load_from_excel()
        elif ".json" in self.path:
            self.load_from_json()

    def load_from_csv(self) -> None:
        self.dataset = pd.read_csv(self.path)

    def load_from_excel(self) -> None:
        self.dataset = pd.read_excel(self.path)

    def load_from_json(self) -> None:
        self.dataset = pd.read_json(self.path)


class ImageDataset:
    pass


class TextDataset:
    def __init__(self, path):
        self.path = path

    def load_with_huggingface(self, path):
        self.dataset = load_dataset("text", data_files=path)
