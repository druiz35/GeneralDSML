import pandas as pd
from datasets import load_dataset
from sklearn.datasets import load_svmlight_file

class TabularDataset:
    def load_from_csv(self, path):
        self.dataset = pd.read_csv(path)

    def load_from_excel(self, path): 
        self.dataset = pd.read_excel(path)

    def load_from_json(self, path):
        self.dataset = pd.read_json(path)

class ImageDataset:
    pass

class TextDataset:
    def load_with_huggingface(self, path):
        self.dataset = load_dataset("text", data_files=path)
