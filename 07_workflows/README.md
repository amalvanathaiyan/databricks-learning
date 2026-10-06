# 07 Workflows

Orchestration and production practices: Lakeflow Jobs (tasks, triggers, parameters, control flow, retries, alerts, repair), Lakeflow Declarative Pipelines with expectations, data quality design, modular notebook code, and testing with pytest and Databricks Asset Bundles.

Several lessons create real jobs and pipelines in your workspace with the Databricks SDK, in a folder `databricks-learning-workflows` under your user. Each one deletes what it created at the end (set `KEEP_JOB` / `KEEP_PIPELINE = True` to keep it for exploring). Tables live in the schema `workspace.workflows`.

| Notebook | Key topics |
|---|---|
| [01_jobs_basics](01_jobs_basics.ipynb) | Jobs, tasks, compute, triggers, idempotent tasks, creating and running a job with the SDK, cron schedules, jobs as code |
| [02_task_dependencies_parameters](02_task_dependencies_parameters.ipynb) | DAGs, `run_if`, task values, if/else condition tasks, for each tasks, dynamic value references |
| [03_retries_alerts_monitoring](03_retries_alerts_monitoring.ipynb) | Retries and idempotency, backoff, timeouts, duration warnings, notifications, repair runs, run history |
| [04_lakeflow_declarative_pipelines](04_lakeflow_declarative_pipelines.ipynb) | Streaming tables, materialized views, expectations, incremental updates, event log, hand-written comparison |
| [05_data_quality_expectations](05_data_quality_expectations.ipynb) | Rules as data, warn / drop / quarantine / fail, metrics, thresholds, Python expectations with a quarantine table |
| [06_notebook_workflows](06_notebook_workflows.ipynb) | Python modules, `%run`, `dbutils.notebook.run`, parallel notebook runs |
| [07_testing_and_code_structure](07_testing_and_code_structure.ipynb) | Pure functions, `assertDataFrameEqual`, pytest in a notebook, data tests, bundles and CI |
