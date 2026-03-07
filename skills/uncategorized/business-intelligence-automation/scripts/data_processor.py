#!/usr/bin/env python3
"""
Data Processor for BI Automation
Handles data cleaning, transformation, and preparation
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class DataProcessor:
    """Process and transform data for BI analysis"""

    def __init__(self):
        self.processed_data = {}

    def load_data(self, file_path: str, file_type: str = "auto") -> pd.DataFrame:
        """Load data from file"""
        try:
            if file_type == "auto":
                file_ext = Path(file_path).suffix.lower()
                if file_ext == ".csv":
                    df = pd.read_csv(file_path)
                elif file_ext in [".xlsx", ".xls"]:
                    df = pd.read_excel(file_path)
                elif file_ext == ".json":
                    df = pd.read_json(file_path)
                else:
                    raise ValueError(f"Unsupported file format: {file_ext}")
            else:
                if file_type == "csv":
                    df = pd.read_csv(file_path)
                elif file_type == "excel":
                    df = pd.read_excel(file_path)
                elif file_type == "json":
                    df = pd.read_json(file_path)
                else:
                    raise ValueError(f"Unsupported file type: {file_type}")

            logger.info(f"Data loaded: {file_path} ({len(df)} rows, {len(df.columns)} columns)")
            return df

        except Exception as e:
            logger.error(f"Failed to load data: {e}")
            raise

    def clean_data(self, df: pd.DataFrame, cleaning_rules: dict = None) -> pd.DataFrame:
        """Clean data according to rules"""
        df_clean = df.copy()

        # Default cleaning rules
        default_rules = {
            "remove_duplicates": True,
            "handle_missing": "fill",  # fill, drop, or ignore
            "fill_value": 0,
            "convert_dates": True,
            "standardize_text": True
        }

        rules = {**default_rules, **(cleaning_rules or {})}

        # Remove duplicates
        if rules["remove_duplicates"]:
            initial_rows = len(df_clean)
            df_clean = df_clean.drop_duplicates()
            removed = initial_rows - len(df_clean)
            if removed > 0:
                logger.info(f"Removed {removed} duplicate rows")

        # Handle missing values
        if rules["handle_missing"] == "fill":
            fill_value = rules["fill_value"]
            df_clean = df_clean.fillna(fill_value)
            missing_count = df.isnull().sum().sum()
            if missing_count > 0:
                logger.info(f"Filled {missing_count} missing values with {fill_value}")
        elif rules["handle_missing"] == "drop":
            initial_rows = len(df_clean)
            df_clean = df_clean.dropna()
            removed = initial_rows - len(df_clean)
            if removed > 0:
                logger.info(f"Dropped {removed} rows with missing values")

        # Convert date columns
        if rules["convert_dates"]:
            date_cols = []
            for col in df_clean.columns:
                try:
                    # Try to convert to datetime
                    df_clean[col] = pd.to_datetime(df_clean[col], errors='ignore')
                    if pd.api.types.is_datetime64_any_dtype(df_clean[col]):
                        date_cols.append(col)
                except:
                    pass
            if date_cols:
                logger.info(f"Converted columns to datetime: {date_cols}")

        # Standardize text
        if rules["standardize_text"]:
            text_cols = df_clean.select_dtypes(include=['object']).columns
            for col in text_cols:
                df_clean[col] = df_clean[col].astype(str).str.strip().str.title()
            if len(text_cols) > 0:
                logger.info(f"Standardized text in columns: {list(text_cols)}")

        return df_clean

    def transform_data(self, df: pd.DataFrame, transformations: list) -> pd.DataFrame:
        """Apply transformations to data"""
        df_transformed = df.copy()

        for transform in transformations:
            transform_type = transform.get("type")

            if transform_type == "aggregate":
                group_cols = transform.get("group_by", [])
                agg_cols = transform.get("aggregate", {})

                if group_cols and agg_cols:
                    df_transformed = df_transformed.groupby(group_cols).agg(agg_cols).reset_index()
                    logger.info(f"Aggregated data by {group_cols}")

            elif transform_type == "pivot":
                index_cols = transform.get("index", [])
                columns_col = transform.get("columns")
                values_col = transform.get("values")

                if index_cols and columns_col and values_col:
                    df_transformed = df_transformed.pivot_table(
                        index=index_cols,
                        columns=columns_col,
                        values=values_col,
                        aggfunc='sum'
                    ).reset_index()
                    logger.info(f"Pivoted data on {columns_col}")

            elif transform_type == "calculate":
                formula = transform.get("formula")
                new_col = transform.get("new_column")

                if formula and new_col:
                    # Simple formula evaluation (in production, use safer evaluation)
                    try:
                        df_transformed[new_col] = eval(formula, {"df": df_transformed})
                        logger.info(f"Calculated new column: {new_col} = {formula}")
                    except Exception as e:
                        logger.warning(f"Failed to calculate {formula}: {e}")

            elif transform_type == "filter":
                condition = transform.get("condition")
                if condition:
                    try:
                        initial_rows = len(df_transformed)
                        df_transformed = df_transformed.query(condition)
                        filtered = initial_rows - len(df_transformed)
                        if filtered > 0:
                            logger.info(f"Filtered {filtered} rows with condition: {condition}")
                    except Exception as e:
                        logger.warning(f"Failed to filter with condition {condition}: {e}")

        return df_transformed

    def save_data(self, df: pd.DataFrame, output_path: str, format: str = "csv") -> str:
        """Save processed data"""
        try:
            if format == "csv":
                df.to_csv(output_path, index=False)
            elif format == "excel":
                df.to_excel(output_path, index=False)
            elif format == "json":
                df.to_json(output_path, orient="records", indent=2)
            else:
                raise ValueError(f"Unsupported output format: {format}")

            logger.info(f"Data saved: {output_path} ({len(df)} rows)")
            return output_path

        except Exception as e:
            logger.error(f"Failed to save data: {e}")
            raise

def main():
    """Main function for data processing"""
    import argparse

    parser = argparse.ArgumentParser(description="Data Processor for BI Automation")
    parser.add_argument("--input", required=True, help="Input data file path")
    parser.add_argument("--output", help="Output file path (default: processed_{input})")
    parser.add_argument("--format", default="csv", choices=["csv", "excel", "json"], 
                       help="Output format")
    parser.add_argument("--clean", action="store_true", help="Apply data cleaning")
    parser.add_argument("--transform", help="JSON file with transformation rules")

    args = parser.parse_args()

    processor = DataProcessor()

    try:
        # Load data
        df = processor.load_data(args.input)
        print(f"Loaded data: {len(df)} rows, {len(df.columns)} columns")

        # Clean data
        if args.clean:
            df = processor.clean_data(df)
            print(f"After cleaning: {len(df)} rows")

        # Apply transformations
        if args.transform:
            with open(args.transform, 'r') as f:
                transformations = json.load(f)
            df = processor.transform_data(df, transformations)
            print(f"After transformations: {len(df)} rows")

        # Save data
        output_path = args.output or f"processed_{Path(args.input).name}"
        saved_path = processor.save_data(df, output_path, args.format)
        print(f"Data saved to: {saved_path}")

    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    main()
