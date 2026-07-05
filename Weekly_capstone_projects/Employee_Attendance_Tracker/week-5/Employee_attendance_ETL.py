import pandas as pd
import numpy as np
import os

attendance = pd.read_csv("attendance.csv")
tasks = pd.read_csv("tasks.csv")

attendance["clock_in"] = pd.to_datetime(attendance["clock_in"])
attendance["clock_out"] = pd.to_datetime(attendance["clock_out"])

attendance["work_hours"] = (
    attendance["clock_out"] -
    attendance["clock_in"]
).dt.total_seconds()/3600

attendance["work_hours"] = attendance["work_hours"].fillna(0)

df = attendance.merge(
    tasks,
    on="employee_id",
    how="left"
)

df["productivity_score"] = np.where(
    df["work_hours"]==0,
    0,
    df["tasks_completed"]/df["work_hours"]
)

top_absentees = (
    df.groupby(
        ["employee_id","employee_name"]
    )["absent_days"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

lowest_departments = (
    df.groupby("department")
    ["productivity_score"]
    .mean()
    .sort_values()
)

os.makedirs("reports",exist_ok=True)

top_absentees.to_csv(
    "reports/top5_absentees.csv"
)

lowest_departments.to_csv(
    "reports/lowest_departments.csv"
)

department_summary = (
    df.groupby("department")
    .agg(
        Average_Work_Hours=("work_hours","mean"),
        Average_Productivity=("productivity_score","mean"),
        Average_Quality=("quality_score","mean"),
        Total_Completed=("tasks_completed","sum")
    )
)

department_summary.to_csv(
    "reports/department_summary.csv"
)

with open(
    "reports/attendance_report.txt",
    "w"
) as f:

    f.write("EMPLOYEE ATTENDANCE REPORT\n\n")

    f.write("TOP 5 ABSENTEES\n")
    f.write("--------------------------\n")
    f.write(top_absentees.to_string())

    f.write("\n\n")

    f.write("LOWEST PRODUCTIVITY DEPARTMENTS\n")
    f.write("--------------------------\n")
    f.write(lowest_departments.to_string())

print("Attendance Report Generated Successfully")
