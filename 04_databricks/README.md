# 04 Databricks

Using the platform properly: workspace and code structure, compute, `dbutils`, parameters, secrets, SQL warehouses, dashboards, Genie and monitoring.

Much of this folder uses Databricks-only features (`dbutils`, the Databricks SDK, SQL warehouses, system tables). Cells that depend on features your workspace may not expose are wrapped and print a note instead of failing.

| Notebook | Key topics |
|---|---|
| [01_workspace_notebooks_repos](01_workspace_notebooks_repos.ipynb) | Project layout, workspace files, importing modules, Git folders |
| [02_compute_types](02_compute_types.ipynb) | Serverless, all-purpose, job compute, SQL warehouses, pools, policies |
| [03_dbutils](03_dbutils.ipynb) | fs, widgets, secrets, notebook.run/exit, jobs.taskValues |
| [04_parameters_and_widgets](04_parameters_and_widgets.ipynb) | Widgets, validation, SQL parameter markers, job parameters, backfills |
| [05_secrets_and_scopes](05_secrets_and_scopes.ipynb) | Secret scopes, redaction, ACLs, Key Vault-backed scopes |
| [06_sql_warehouse](06_sql_warehouse.ipynb) | Warehouse types, sizing vs scaling, Statement Execution API, query history |
| [07_dashboards_and_genie](07_dashboards_and_genie.ipynb) | AI/BI dashboards, Genie spaces, consumer-ready Gold tables |
| [08_monitoring_basics](08_monitoring_basics.ipynb) | Freshness and volume checks, system tables, cost, job runs, alerts |
| [09_databricks_interview_qa](09_databricks_interview_qa.ipynb) | Platform map, core answers, scenarios, quiz |
