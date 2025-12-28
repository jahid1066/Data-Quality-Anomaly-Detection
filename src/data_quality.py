import pandas as pd

def missing_values_report(df: pd.DataFrame) -> pd.DataFrame:
    report = pd.DataFrame({
        'missing_count': df.isnull().sum(),
        'missing_percentage': df.isnull().mean() * 100
    })
    return report


def duplicate_rows_count(df: pd.DataFrame) -> int:
    return df.duplicated().sum()


def basic_statistics(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe().T


def data_quality_summary(df: pd.DataFrame) -> dict:
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "duplicates": duplicate_rows_count(df),
        "missing_values": df.isnull().sum().sum()
    }
