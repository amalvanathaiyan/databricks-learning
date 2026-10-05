# Databricks Certified Data Engineer Associate: Study Guide

How this repo maps to the exam, what to study in what order, and how to practise.

> **Check the official guide first.** Databricks revised the exam on **4 May 2026**. The domain weights below come from the
> [May 2026 exam guide](https://www.databricks.com/sites/default/files/2026-03/databricks-certified-data-engineer-associate-exam-guide-may-4-2026.pdf)
> as summarised by several 2026 study sites. Confirm them on the
> [certification page](https://www.databricks.com/learn/certification/data-engineer-associate) before you book.
> Last checked: 2026-10-05.

## Exam at a glance

| | |
|---|---|
| Questions | About 45 multiple choice |
| Time | 90 minutes |
| Cost | USD 200 plus tax |
| Format | Online proctored or test centre |
| Code in questions | Mostly SQL, with some PySpark |
| Validity | 2 years |
| Recommended experience | About 6 months of hands-on data engineering on Databricks |

## The 7 domains

| # | Domain | Weight | ≈ Questions | Where it is covered in this repo |
|---|---|---|---|---|
| 1 | Databricks Intelligence Platform | 6% | 3 | `00_platform_tour`, `04_databricks` |
| 2 | Data Ingestion and Loading | 21% | 9 | `01_spark_basics` 21–25, `08_streaming_and_ingestion` |
| 3 | Data Transformation and Modeling | 22% | 10 | `01_spark_basics` 04–20 and 26–30, `03_delta_lake`, `08` (medallion layers) |
| 4 | Working with Lakeflow Jobs | 16% | 7 | `07_workflows` |
| 5 | Implementing CI/CD | 10% | 4–5 | `00_04_git_workflow`, `07_workflows` 07, `09_azure_databricks` 10 |
| 6 | Troubleshooting, Monitoring and Optimization | 10% | 4–5 | `02_spark_internals`, `05_optimization`, `04_databricks` 08 |
| 7 | Governance and Security | 15% | 7 | `06_unity_catalog`, `04_databricks` 05 |

Ingestion plus transformation is **43%** of the exam, which is why the Spark basics and Delta folders come first.

## What each domain tests, and the lessons for it

Status: ✅ written · 🔜 planned (see `learning-path.md`)

### 1. Databricks Intelligence Platform (6%)

- Lakehouse architecture, the workspace, notebooks, the main personas and tools
- Compute: all-purpose vs job compute, SQL warehouses, **serverless**
- Where Spark, Delta Lake and Unity Catalog fit together

| Lesson | Status |
|---|---|
| `00_01_workspace_and_ui`, `00_02_notebook_basics`, `00_03_serverless_compute_free_edition` | ✅ |
| `01_pyspark_introduction`, `02_spark_session` | ✅ |
| `04_databricks` (all 9 lessons) | ✅ |

### 2. Data Ingestion and Loading (21%)

- Reading files: CSV, JSON, Parquet. Options, schemas, bad records
- `read_files`, **COPY INTO**, **Auto Loader** (`cloudFiles`), schema inference and evolution, rescued data
- **Lakeflow Connect** (standard and managed connectors), JDBC/ODBC sources
- Semi-structured data: nested JSON, `from_json`, `explode`, `:` path syntax
- Schema enforcement and evolution in Delta

| Lesson | Status |
|---|---|
| `21_reading_csv`, `22_reading_json`, `23_reading_parquet`, `24_writing_data`, `25_partitioning_files`, `30_building_an_etl_pipeline` | ✅ |
| `03_delta_lake/04_schema_enforcement`, `05_schema_evolution` | ✅ |
| `08_streaming_and_ingestion/01`–`03` (batch patterns, COPY INTO, Auto Loader), `09` (APIs and nested JSON) | 🔜 |

### 3. Data Transformation and Modeling (22%)

- DataFrame and SQL transformations: select, filter, joins, aggregations, windows, deduplication
- Medallion architecture: Bronze, Silver, Gold
- Gold-layer objects: views, **materialized views**, **streaming tables**
- Data quality checks and expectations
- Delta DML: `MERGE`, `UPDATE`, `DELETE`. SCD Type 1 and 2

| Lesson | Status |
|---|---|
| `04_schema_and_data_types` to `20_udfs` | ✅ |
| `26_spark_sql` to `30_building_an_etl_pipeline` | ✅ |
| `03_delta_lake` (all 14 lessons) | ✅ |
| `08` 05–08 (medallion layers, incremental and late data) | 🔜 |

### 4. Working with Lakeflow Jobs (16%)

- Jobs, tasks and task types, dependencies (DAGs), triggers and schedules
- Job parameters, task values, retries, timeouts, notifications, repair runs
- **Lakeflow Declarative Pipelines** (formerly Delta Live Tables): streaming tables, materialized views, expectations

| Lesson | Status |
|---|---|
| `00_02_notebook_basics` (widgets, `%run`) | ✅ |
| `07_workflows/01`–`06` | 🔜 |

### 5. Implementing CI/CD (10%)

- Git folders: branches, commits, pull requests
- **Databricks Asset Bundles**: project layout, `databricks.yml`, targets (dev/staging/prod), deploy and run
- Testing transformation code, environment separation

| Lesson | Status |
|---|---|
| `00_04_git_workflow` | ✅ |
| `07_workflows/07_testing_and_code_structure`, `09_azure_databricks/10_ci_cd` | 🔜 |

### 6. Troubleshooting, Monitoring and Optimization (10%)

- Reading the Spark UI and query profile. Jobs, stages, tasks, shuffles
- Skew, spill, small files. `OPTIMIZE`, liquid clustering, data skipping
- Run history, system tables, logs

| Lesson | Status |
|---|---|
| Under-the-hood sections of lessons 04–25 (plans, shuffles, join strategies) | ✅ |
| `02_spark_internals` (all 15 lessons: plans, shuffles, joins, AQE, Spark UI and query profile) | ✅ |
| `04_databricks/08_monitoring_basics` | ✅ |
| `05_optimization` (all 8 lessons: profiles, skew, files, spill, joins, UDFs, cost, debugging playbook) | ✅ |

### 7. Governance and Security (15%)

- Unity Catalog hierarchy: metastore, catalog, schema, table, view, volume, function
- Managed vs external tables, volumes, external locations and storage credentials
- `GRANT` / `REVOKE`, ownership, privilege inheritance
- Lineage, tags, row filters and column masks, Delta Sharing
- Secrets and secret scopes

| Lesson | Status |
|---|---|
| `00_01_workspace_and_ui` (hierarchy intro) | ✅ |
| `27_temporary_views` (views, permanent views in Unity Catalog) | ✅ |
| `04_databricks/05_secrets_and_scopes` | ✅ |
| `06_unity_catalog/01`–`07` | 🔜 |

## How to study with this repo

Every lesson ends with a **🎓 Certification corner** of exam-style questions. Answers are hidden until you click **Show answer**.

1. **Learn:** work through a lesson top to bottom in Free Edition (**Run all**), then do the practice problem before opening the solution
2. **Recall:** answer the Certification corner questions without scrolling up
3. **Speak:** answer the lesson's Interview Q&A out loud. All questions are collected in [`interview_prep/question_bank.md`](../../interview_prep/question_bank.md)
4. **Review weekly:** re-do the Certification corners of the past week's lessons and note every miss in your own log
5. **Final two weeks:** take the official practice exam on Databricks Academy, then re-study the domains where you scored lowest

## Suggested 8-week exam track

If certification is the priority, take this order instead of strictly following the folder numbers:

| Week | Focus | Lessons |
|---|---|---|
| 1 | Platform, DataFrames, core transformations | `00_*`, `01`–`10` |
| 2 | Aggregations, joins, windows, UDFs | `11`–`20` |
| 3 | Files, writing, partitioning, Spark SQL, ETL | `21`–`30` |
| 4 | Delta Lake | `03_delta_lake` |
| 5 | Ingestion: COPY INTO, Auto Loader, streaming, medallion | `08_streaming_and_ingestion` |
| 6 | Lakeflow Jobs and Declarative Pipelines, CI/CD | `07_workflows`, `00_04`, Asset Bundles |
| 7 | Unity Catalog and governance, monitoring and optimization | `06_unity_catalog`, `05_optimization` |
| 8 | Review: practice exam, question bank, weak domains | All Certification corners |

## Free Edition coverage

Most exam topics can be practised hands-on in Free Edition. A few can only be learned conceptually there:

| Topic | Free Edition |
|---|---|
| Spark, Delta, SQL, Auto Loader, COPY INTO, volumes | ✅ Hands-on |
| Jobs, Lakeflow Declarative Pipelines, dashboards | ✅ Hands-on (within quotas) |
| Unity Catalog grants on your own objects, views, functions | ✅ Mostly hands-on |
| Classic clusters, instance pools, init scripts | ❌ Concept only |
| Account-level admin, identity federation, networking | ❌ Concept only |

## Exam-day tips

- Read the **last sentence** of each question first: it tells you what is actually being asked
- Watch for "most efficient", "least effort" and "without data loss" qualifiers. They decide between two plausible answers
- Prefer the **managed, Databricks-native** option (Auto Loader over hand-written file tracking, Unity Catalog over legacy ACLs, liquid clustering over manual partitioning) unless the question says otherwise
- Know the SQL forms: `MERGE INTO`, `COPY INTO`, `CREATE OR REPLACE TABLE ... AS`, `GRANT ... ON ... TO`, `DESCRIBE HISTORY`, `OPTIMIZE`, `VACUUM`
- Flag and move on. With about 2 minutes per question there is time for a second pass
