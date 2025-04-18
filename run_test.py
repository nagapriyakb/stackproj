import os
import webbrowser
from datetime import datetime

# Folder for reports
report_dir = "Reports/html_reports"
os.makedirs(report_dir, exist_ok=True)

# Timestamped report file
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_path = os.path.join(report_dir, f"report_{timestamp}.html")

# Run tests and generate report
os.system(f"pytest test_cases/ --html={report_path}")

# Open the report in the default web browser
webbrowser.open(f"file://{os.path.abspath(report_path)}")
###
