from typing import TypedDict, List, Dict, Any, Tuple
from pydantic import BaseModel


class ColumnReport(BaseModel):
    name: str | None = None
    missing_count: int | None = None
    missing_pct: float | None = None
    implicit_dtype: str | None = None
    rows_with_nulls: list[list[Any]] | None = None


class NumericalColumnReport(ColumnReport):
    mean: float | None = None
    median: float | None = None
    std: float | None = None
    min: float | None = None
    per25: float | None = None
    per75: float | None = None
    max: float | None = None
    skewness: float | None = None
    kurtosis: float | None = None
    zeros_count: int | None = None
    rows_with_zeros: list[list[Any]] | None = None
    outlier_rows: list[list[Any]] | None = None
    detected_distribution: tuple[str, dict[str, Any]] | None = None
    visualizations_paths: list[str] = list()


class CategoricalColumnReport(ColumnReport):
    unique_values: list[Any] | None = None
    value_counts: dict[Any, int] | None = None
    outlier_rows: list[list[Any]] | None = None


class TextColumnReport(ColumnReport): ...


class DatetimeColumnReport(ColumnReport): ...


class TabularDataReport(BaseModel):
    n_rows: int | None = None
    n_columns: int | None = None
    head: list[list[Any]] | None = None
    tail: list[list[Any]] | None = None
    has_nulls: bool | None = None
    total_missing_count: int | None = None
    rows_with_nulls: list[list[Any]] = list()
    numerical_columns: dict[str, NumericalColumnReport] = dict()
    categorical_columns: dict[str, CategoricalColumnReport] = dict()
    text_columns: dict[str, TextColumnReport] = dict()
    datetime_columns: dict[str, DatetimeColumnReport] = dict()
    conclusions: list[str] | None = list()
