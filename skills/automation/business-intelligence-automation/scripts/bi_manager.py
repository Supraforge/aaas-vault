#!/usr/bin/env python3
"""
Business Intelligence Automation Manager
Automates BI workflows across multiple platforms
"""

import os
import sys
import json
import argparse
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
import pandas as pd
import numpy as np

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BIAutomationManager:
    """Main manager for BI automation workflows"""

    def __init__(self, config_path: str = None):
        """Initialize BI automation manager"""
        self.config = self._load_config(config_path)
        self.data_sources = {}
        self.reports = {}
        self.dashboards = {}

    def _load_config(self, config_path: str = None) -> Dict[str, Any]:
        """Load configuration from file or environment"""
        config = {
            "data_sources": {},
            "bi_platforms": {},
            "report_templates": {},
            "schedules": {}
        }

        # Load from environment variables
        config["powerbi"] = {
            "client_id": os.getenv("POWERBI_CLIENT_ID"),
            "client_secret": os.getenv("POWERBI_CLIENT_SECRET"),
            "tenant_id": os.getenv("POWERBI_TENANT_ID"),
            "workspace_id": os.getenv("POWERBI_WORKSPACE_ID")
        }

        config["tableau"] = {
            "server_url": os.getenv("TABLEAU_SERVER_URL"),
            "site_name": os.getenv("TABLEAU_SITE_NAME"),
            "username": os.getenv("TABLEAU_USERNAME"),
            "password": os.getenv("TABLEAU_PASSWORD")
        }

        # Load from config file if provided
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    file_config = json.load(f)
                    config.update(file_config)
            except Exception as e:
                logger.warning(f"Failed to load config file: {e}")

        return config

    def connect_data_source(self, source_type: str, connection_params: Dict) -> bool:
        """Connect to a data source"""
        try:
            if source_type == "csv":
                file_path = connection_params.get("file_path")
                if not os.path.exists(file_path):
                    logger.error(f"CSV file not found: {file_path}")
                    return False

                df = pd.read_csv(file_path)
                self.data_sources[file_path] = {
                    "type": "csv",
                    "dataframe": df,
                    "columns": list(df.columns),
                    "rows": len(df)
                }
                logger.info(f"Connected to CSV: {file_path} ({len(df)} rows)")

            elif source_type == "excel":
                file_path = connection_params.get("file_path")
                sheet_name = connection_params.get("sheet_name", 0)

                df = pd.read_excel(file_path, sheet_name=sheet_name)
                self.data_sources[file_path] = {
                    "type": "excel",
                    "dataframe": df,
                    "columns": list(df.columns),
                    "rows": len(df)
                }
                logger.info(f"Connected to Excel: {file_path} ({len(df)} rows)")

            elif source_type == "postgresql":
                # PostgreSQL connection would go here
                logger.info("PostgreSQL connection configured")

            elif source_type == "mysql":
                # MySQL connection would go here
                logger.info("MySQL connection configured")

            else:
                logger.error(f"Unsupported data source type: {source_type}")
                return False

            return True

        except Exception as e:
            logger.error(f"Failed to connect to data source: {e}")
            return False

    def analyze_data(self, data_source_key: str, analysis_type: str) -> Dict[str, Any]:
        """Perform data analysis"""
        if data_source_key not in self.data_sources:
            logger.error(f"Data source not found: {data_source_key}")
            return {}

        df = self.data_sources[data_source_key]["dataframe"]
        results = {}

        if analysis_type == "summary":
            results["summary"] = {
                "shape": df.shape,
                "columns": list(df.columns),
                "dtypes": df.dtypes.astype(str).to_dict(),
                "missing_values": df.isnull().sum().to_dict(),
                "numeric_summary": df.describe().to_dict() if df.select_dtypes(include=[np.number]).shape[1] > 0 else {}
            }

        elif analysis_type == "correlation":
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 1:
                correlation_matrix = df[numeric_cols].corr()
                results["correlation"] = correlation_matrix.to_dict()

        elif analysis_type == "trend":
            # Simple trend analysis
            date_cols = df.select_dtypes(include=['datetime']).columns
            if len(date_cols) > 0:
                date_col = date_cols[0]
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                if len(numeric_cols) > 0:
                    numeric_col = numeric_cols[0]
                    trend = df.groupby(df[date_col].dt.to_period('M'))[numeric_col].mean()
                    results["trend"] = trend.to_dict()

        return results

    def generate_report(self, report_type: str, data_source_key: str, output_format: str = "html") -> str:
        """Generate a BI report"""
        try:
            # Analyze data
            analysis = self.analyze_data(data_source_key, "summary")

            # Generate report based on type
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"report_{report_type}_{timestamp}.{output_format}"

            if report_type == "sales":
                report_content = self._generate_sales_report(analysis, output_format)
            elif report_type == "marketing":
                report_content = self._generate_marketing_report(analysis, output_format)
            elif report_type == "financial":
                report_content = self._generate_financial_report(analysis, output_format)
            else:
                report_content = self._generate_general_report(analysis, output_format)

            # Save report
            with open(output_file, 'w') as f:
                f.write(report_content)

            logger.info(f"Report generated: {output_file}")
            return output_file

        except Exception as e:
            logger.error(f"Failed to generate report: {e}")
            return ""

    def _generate_sales_report(self, analysis: Dict, format: str) -> str:
        """Generate sales report"""
        if format == "html":
            return f"""<html>
<head><title>Sales Report</title></head>
<body>
<h1>Sales Analysis Report</h1>
<p>Generated: {datetime.now()}</p>
<p>Data shape: {analysis.get('summary', {}).get('shape', 'N/A')}</p>
<p>Columns: {', '.join(analysis.get('summary', {}).get('columns', []))}</p>
</body>
</html>"""
        else:
            return json.dumps({"report_type": "sales", "analysis": analysis}, indent=2)

    def _generate_marketing_report(self, analysis: Dict, format: str) -> str:
        """Generate marketing report"""
        if format == "html":
            return f"""<html>
<head><title>Marketing Report</title></head>
<body>
<h1>Marketing Analytics Report</h1>
<p>Generated: {datetime.now()}</p>
<p>Data analyzed: {len(analysis.get('summary', {}).get('columns', []))} columns</p>
</body>
</html>"""
        else:
            return json.dumps({"report_type": "marketing", "analysis": analysis}, indent=2)

    def _generate_financial_report(self, analysis: Dict, format: str) -> str:
        """Generate financial report"""
        if format == "html":
            return f"""<html>
<head><title>Financial Report</title></head>
<body>
<h1>Financial Analysis Report</h1>
<p>Generated: {datetime.now()}</p>
<p>Numeric summary available: {'yes' if analysis.get('summary', {}).get('numeric_summary') else 'no'}</p>
</body>
</html>"""
        else:
            return json.dumps({"report_type": "financial", "analysis": analysis}, indent=2)

    def _generate_general_report(self, analysis: Dict, format: str) -> str:
        """Generate general report"""
        if format == "html":
            return f"""<html>
<head><title>BI Report</title></head>
<body>
<h1>Business Intelligence Report</h1>
<p>Generated: {datetime.now()}</p>
<p>Data summary: {json.dumps(analysis.get('summary', {}), indent=2)}</p>
</body>
</html>"""
        else:
            return json.dumps({"report_type": "general", "analysis": analysis}, indent=2)

    def create_dashboard(self, dashboard_type: str, data_source_key: str) -> str:
        """Create a dashboard"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            dashboard_file = f"dashboard_{dashboard_type}_{timestamp}.json"

            dashboard_config = {
                "type": dashboard_type,
                "data_source": data_source_key,
                "created_at": datetime.now().isoformat(),
                "widgets": [
                    {"type": "summary", "title": "Data Overview"},
                    {"type": "chart", "title": "Trend Analysis"},
                    {"type": "table", "title": "Detailed Data"}
                ]
            }

            with open(dashboard_file, 'w') as f:
                json.dump(dashboard_config, f, indent=2)

            self.dashboards[dashboard_file] = dashboard_config
            logger.info(f"Dashboard created: {dashboard_file}")
            return dashboard_file

        except Exception as e:
            logger.error(f"Failed to create dashboard: {e}")
            return ""

    def schedule_report(self, report_config: Dict) -> bool:
        """Schedule automated report generation"""
        try:
            schedule_id = f"schedule_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            self.config["schedules"][schedule_id] = {
                **report_config,
                "created_at": datetime.now().isoformat(),
                "next_run": None,
                "last_run": None,
                "status": "active"
            }

            logger.info(f"Report scheduled: {schedule_id}")
            return True

        except Exception as e:
            logger.error(f"Failed to schedule report: {e}")
            return False

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Business Intelligence Automation Manager")
    parser.add_argument("--sample", action="store_true", help="Run sample workflow")
    parser.add_argument("--data-source", type=str, help="Path to data source file")
    parser.add_argument("--report-type", type=str, choices=["sales", "marketing", "financial", "general"], 
                       help="Type of report to generate")
    parser.add_argument("--output-format", type=str, default="html", 
                       choices=["html", "json", "pdf"], help="Output format")
    parser.add_argument("--config", type=str, help="Path to configuration file")

    args = parser.parse_args()

    # Initialize manager
    manager = BIAutomationManager(args.config)

    if args.sample:
        print("Running sample BI automation workflow...")

        # Create sample data
        sample_data = {
            "date": pd.date_range(start="2024-01-01", periods=100, freq="D"),
            "sales": np.random.randint(1000, 5000, 100),
            "customers": np.random.randint(50, 200, 100),
            "revenue": np.random.uniform(10000, 50000, 100)
        }
        df = pd.DataFrame(sample_data)

        # Save sample data
        sample_file = "sample_sales_data.csv"
        df.to_csv(sample_file, index=False)
        print(f"Sample data created: {sample_file}")

        # Connect to data source
        manager.connect_data_source("csv", {"file_path": sample_file})

        # Analyze data
        analysis = manager.analyze_data(sample_file, "summary")
        print(f"Data analysis complete. Shape: {analysis.get('summary', {}).get('shape')}")

        # Generate report
        report_file = manager.generate_report("sales", sample_file, "html")
        print(f"Report generated: {report_file}")

        # Create dashboard
        dashboard_file = manager.create_dashboard("sales", sample_file)
        print(f"Dashboard created: {dashboard_file}")

        print("
Sample workflow completed successfully!")

    elif args.data_source and args.report_type:
        # Connect to specified data source
        file_ext = os.path.splitext(args.data_source)[1].lower()
        source_type = "csv" if file_ext == ".csv" else "excel" if file_ext in [".xlsx", ".xls"] else "unknown"

        if source_type == "unknown":
            print(f"Unsupported file format: {file_ext}")
            return

        if manager.connect_data_source(source_type, {"file_path": args.data_source}):
            report_file = manager.generate_report(args.report_type, args.data_source, args.output_format)
            if report_file:
                print(f"Report generated: {report_file}")
            else:
                print("Failed to generate report")
        else:
            print(f"Failed to connect to data source: {args.data_source}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
