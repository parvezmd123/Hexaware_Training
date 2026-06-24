# Apache Airflow Setup & Execution Commands

## 1. Check Docker Installation

```powershell
docker --version
```

Checks whether Docker is installed and shows the Docker version.

---

## 2. Check Running Containers

```powershell
docker ps
```

Displays currently running Docker containers.

---

## 3. Test Docker Installation

```powershell
docker run hello-world
```

Runs a test container to verify Docker is working correctly.

---

# Project Setup

## 4. Navigate to Documents Folder

```powershell
cd Documents
```

Moves into the Documents directory.

---

## 5. Create Airflow Project Folder

```powershell
mkdir airflow-learning
```

Creates a new folder for the Airflow project.

---

## 6. Enter Project Folder

```powershell
cd airflow-learning
```

Moves into the Airflow project directory.

---

## 7. Check Current Location

```powershell
pwd
```

Displays the current working directory.

---

# Airflow Docker Setup

## 8. Download Airflow Docker Compose File

```powershell
Invoke-WebRequest -Uri "https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml" -OutFile "docker-compose.yaml"
```

Downloads the official Apache Airflow Docker configuration file.

---

## 9. Create Required Airflow Folders

```powershell
mkdir dags
mkdir logs
mkdir plugin
mkdir config
```

Creates folders used by Airflow:

* `dags` → DAG Python files
* `logs` → Task execution logs
* `config` → Configuration files
* `plugins` → Custom plugins

---

## 10. Create Environment File

```powershell
notepad .env
```

Creates `.env` file to store Airflow environment variables.

---

## 11. View Project Files

```powershell
dir -Force
```

Lists all files including hidden files like `.env`.

---

## 12. Rename Plugin Folder

```powershell
Rename-Item plugin plugins
```

Renames folder to match Airflow expected naming.

---

# Initialize Airflow

## 13. Initialize Airflow Database

```powershell
docker compose up airflow-init
```

Creates Airflow database tables and initializes the environment.

---

## 14. Start Airflow Services

```powershell
docker compose up -d
```

Starts Airflow containers in background mode.

---

## 15. Check Running Airflow Containers

```powershell
docker ps
```

Shows running Airflow services.

---

# DAG Management

## 16. Check DAG Files Inside Scheduler

```powershell
docker exec -it airflow-learning-airflow-scheduler-1 ls /opt/airflow/dags
```

Lists DAG files available inside Airflow scheduler container.

---

## 17. Run Python DAG File Manually

```powershell
docker exec -it airflow-learning-airflow-scheduler-1 python /opt/airflow/dags/exercise2.py
```

Executes a DAG Python file manually inside the container.

---

# View Generated Outputs

## 18. Read Employee File

```powershell
docker exec -it airflow-learning-airflow-worker-1 cat /tmp/employees.txt
```

Displays employee input data.

---

## 19. View Salary Report

```powershell
docker exec -it airflow-learning-airflow-worker-1 cat /tmp/report.txt
```

Displays generated salary report.

---

## 20. View Student Result

```powershell
docker exec -it airflow-learning-airflow-worker-1 cat /tmp/result.txt
```

Displays student marks processing result.

---

## 21. View Stock Alert

```powershell
docker exec -it airflow-learning-airflow-worker-1 cat /tmp/alerts.txt
```

Displays low-stock products.

---

## 22. View Attendance Report

```powershell
docker exec -it airflow-learning-airflow-worker-1 cat /tmp/attendance_report.txt
```

Displays attendance summary.

---

## 23. View CSV Revenue Summary

```powershell
docker exec -it airflow-learning-airflow-worker-1 cat /tmp/sales_summary.txt
```

Displays calculated sales revenue.

---

# Refresh Airflow DAGs

## 24. Restart Scheduler and DAG Processor

```powershell
docker compose restart airflow-dag-processor airflow-scheduler
```

Restarts Airflow components to detect newly added DAG files.

---

# Logs

## 25. View Worker Logs

```powershell
docker logs airflow-learning-airflow-worker-1 --tail 100
```

Displays latest worker execution logs.

---

## 26. View DAG Processor Logs

```powershell
docker logs airflow-learning-airflow-dag-processor-1 --tail 100
```

Shows DAG parsing and processing logs.

---

# Stop Airflow

## 27. Stop All Airflow Containers

```powershell
docker compose down
```

Stops and removes Airflow containers while keeping project files and volumes.
