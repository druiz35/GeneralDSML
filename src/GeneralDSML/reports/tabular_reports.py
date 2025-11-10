from typing import TypedDict, List, Dict, Any, Tuple

class ColumnReport(TypedDict, total=False):
    name: str
    missing_count: int
    missing_pct: float
    implicit_dtype: str
    rows_with_nulls: List[List[Any]]

class NumericalColumnReport(TypedDict, ColumnReport, total=False):
    dtype: str = "numerical"
    mean: float
    median: float
    std: float
    min: float
    per25: float
    per50: float
    per75: float
    max: float
    outlier_rows: List[List[Any]]
    detected_distribution: Tuple[str, Dict[str, Any]]

class CategoricalColumnReport(TypedDict, ColumnReport, total=False): 
    dtype: str = "categorical"
    unique_values: List[Any]
    value_counts: Dict[Any, int]
    outlier_rows: List[List[Any]]

class TextColumnReport(TypedDict, ColumnReport, total=False): ...

class DatetimeColumnReport(TypedDict, ColumnReport, total=False): ...

class TabularDataReport(TypedDict, total=False):
    n_rows: int
    n_columns: int
    head: List[List[Any]]
    tail: List[List[Any]]
    has_nulls: bool
    total_missing_count: int
    rows_with_nulls: List[List[Any]]
    numerical_columns: Dict[str, NumericalColumnReport] 
    categorical_columns: Dict[str, CategoricalColumnReport]
    text_columns: Dict[str, TextColumnReport]
    datetime_columns: Dict[str, DatetimeColumnReport]
    conclusions: List[str]