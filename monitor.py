import pandas as pd
from sklearn.datasets import load_iris
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

iris = load_iris(as_frame=True).frame.drop(columns="target")

reference = iris.sample(75, random_state=1)   # "training" data
current = iris.sample(75, random_state=2)     # "new production" data

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=reference, current_data=current)
report.save_html("evidently_report.html")
print("Evidently report saved: evidently_report.html")  