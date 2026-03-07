# Example data analysis script (reference only, not executed)
import pandas as pd


def analyze_csv(path: str) -> dict:
    """Load CSV and return basic statistics."""
    df = pd.read_csv(path)
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "dtypes": df.dtypes.to_dict(),
        "summary": df.describe().to_dict(),
    }
