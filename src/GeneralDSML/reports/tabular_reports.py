from typing import TypedDict, List, Dict, Any, Tuple
from pydantic import BaseModel


class ColumnReport(BaseModel):
    name: str | None
    missing_count: int | None
    missing_pct: float | None
    implicit_dtype: str | None
    rows_with_nulls: list[list[Any]] | None


class NumericalColumnReport(ColumnReport):
    mean: float | None
    median: float | None
    std: float | None
    min: float | None
    per25: float | None
    per75: float | None
    max: float | None
    outlier_rows: list[list[Any]] | None
    detected_distribution: tuple[str, dict[str, Any]] | None


class CategoricalColumnReport(ColumnReport):
    unique_values: list[Any] | None
    value_counts: dict[Any, int] | None
    outlier_rows: list[list[Any]] | None


class TextColumnReport(ColumnReport): ...


class DatetimeColumnReport(ColumnReport): ...


class TabularDataReport(BaseModel):
    n_rows: int | None
    n_columns: int | None
    head: list[list[Any]] | None
    tail: list[list[Any]] | None
    has_nulls: bool | None
    total_missing_count: int | None
    rows_with_nulls: list[list[Any]] | None
    numerical_columns: dict[str, NumericalColumnReport] | None
    categorical_columns: dict[str, CategoricalColumnReport] | None
    text_columns: dict[str, TextColumnReport] | None
    datetime_columns: dict[str, DatetimeColumnReport] | None
    conclusions: list[str] | None
