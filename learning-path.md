# Databricks + PySpark Learning Path (v2)

**Goal:** Build deep, explainable knowledge of PySpark, Databricks and Azure Databricks, and document every concept as a detailed notebook that works as both a personal reference and public learning material. Special focus: being able to *explain* concepts in interviews, not just write the code.

**Environment:** Databricks Free Edition (serverless compute) + GitHub repo `databricks-learning`
**Local folder:** `C:\Amal's Space\Training\Databricks-Learning`
**Estimated duration:** ~4 months at 1-2 hours per day (Azure phase adds ~2 weeks)

---

## How to use this plan

1. Work through the folders **in order**. Each has a checklist.
2. For every concept, create **one detailed notebook** in Databricks following the notebook standard below.
3. **Write the code and the interview answers from memory first**, then compare with references or Claude.
4. Verify your output against the "Expected output" you wrote in the notebook.
5. **Commit to Git after every lesson** (e.g. `add 17_joins lesson`). This builds a learning history and a portfolio.
6. Tick the checkboxes and update the progress tracker at the bottom.

---

## Notebook standard (use for every concept)

1. **Title and goal**: what you will learn, in one or two lines
2. **Why it matters**: where it appears in real pipelines
3. **Concept explained**: plain English, with a diagram if helpful
4. **Real-world example**: a concrete scenario (e.g. "10 million banking transactions arriving from Oracle")
5. **Syntax**: the minimal code pattern
6. **Hands-on**: simple example, then realistic, then edge cases (sample data generated inside the notebook so it runs top to bottom)
7. **Expected output**: what you should see, so you can verify
8. **Under the hood**: what Spark does internally (`explain()`, Spark UI observations)
9. **Common mistakes and troubleshooting log**: errors you hit and how you fixed them
10. **Interview Q&A**: 5-8 questions with short spoken-style answers
11. **Practice problem**: solve it before looking at any answer
12. **Summary and cheat sheet**: 5-10 bullet recap
13. **Git commit**: commit message written at the end of the notebook as a reminder

**Naming:** `NN_topic_name` (e.g. `17_joins`). Each folder has a `README.md` linking all its notebooks.

---

## Repository layout

```
databricks-learning/
├── README.md
├── learning-path.md                # this file
├── docs/
│   ├── setup.md
│   ├── glossary.md
│   └── cheatsheets/
├── 00_platform_tour/
├── 01_spark_basics/                # 30 lessons, 3 levels
├── 02_spark_internals/
├── 03_delta_lake/
├── 04_databricks/
├── 05_optimization/
├── 06_unity_catalog/
├── 07_workflows/
├── 08_streaming_and_ingestion/
├── 09_azure_databricks/
├── projects/
│   ├── project_1_medallion_pipeline/
│   └── project_2_own_domain/
├── interview_prep/
│   ├── question_bank.md
│   ├── scenarios.md
│   ├── coding_problems.md
│   └── mock_interview_log.md
└── assets/
```

---

## 00_platform_tour (2-3 days)

**Goal:** Get comfortable with the workspace before writing real code.

- [x] `00_01_workspace_and_ui`: sidebar, workspace, notebooks vs files, Git folders
- [x] `00_02_notebook_basics`: cells, magic commands (`%sql`, `%python`, `%md`, `%run`), `display()`
- [x] `00_03_serverless_compute_free_edition`: how compute works here, limits and quotas
- [x] `00_04_git_workflow`: commit, push and pull from the workspace, branching basics

**Deliverable:** `docs/setup.md` with screenshots.

---

## 01_spark_basics (30 lessons, 4-5 weeks)

### Level 1: Foundation

| # | Notebook | Key topics |
|---|---|---|
| 1 | `01_pyspark_introduction` | Spark vs PySpark vs Python/Pandas, why distributed processing |
| 2 | `02_spark_session` | Entry point, `spark` in Databricks, config, `spark.version` |
| 3 | `03_dataframes` | `createDataFrame`, `show`, `display`, `printSchema`, rows and columns |
| 4 | `04_schema_and_data_types` | `StructType`/`StructField`, common types, `inferSchema` trade-offs, `cast` |
| 5 | `05_select` | `select`, `selectExpr`, `col`, column expressions |
| 6 | `06_filter_where` | `filter`/`where`, conditions, `&`, `\|`, `~`, `isin`, `between`, `like` |
| 7 | `07_withcolumn` | `withColumn`, `withColumnRenamed`, `lit`, adding/deriving columns |
| 8 | `08_when_otherwise` | Conditional logic, nested conditions |
| 9 | `09_drop_alias` | `drop`, `alias`, renaming strategies |
| 10 | `10_distinct_dropduplicates` | `distinct` vs `dropDuplicates` (subset), dedup patterns |

### Level 2: Data transformation

| # | Notebook | Key topics |
|---|---|---|
| 11 | `11_groupby` | `groupBy`, multiple keys, shuffle implication |
| 12 | `12_aggregations` | `agg`, `sum/avg/count/min/max`, `countDistinct`, `rollup`, `cube`, `pivot` |
| 13 | `13_sorting` | `orderBy`/`sort`, asc/desc, null ordering, sort cost |
| 14 | `14_string_functions` | `concat`, `substring`, `regexp_replace`, `split`, `trim`, `upper/lower` |
| 15 | `15_date_functions` | `to_date`, `to_timestamp`, `date_add`, `datediff`, `date_format`, time zones |
| 16 | `16_null_handling` | `isNull`, `na.fill/drop/replace`, `coalesce`, null semantics in joins/aggregates |
| 17 | `17_joins` | Inner/left/right/full/cross/semi/anti, duplicate columns, join conditions |
| 18 | `18_union` | `union`, `unionByName`, schema mismatch handling |
| 19 | `19_window_functions` | `row_number`, `rank`, `dense_rank`, `lag`, `lead`, frames, top-N per group |
| 20 | `20_udfs` | Python UDF vs pandas UDF vs built-ins, why to avoid UDFs |

### Level 3: Data engineering

| # | Notebook | Key topics |
|---|---|---|
| 21 | `21_reading_csv` | Options (header, sep, schema), bad records, modes |
| 22 | `22_reading_json` | Single vs multi-line, nested data, `explode`, `from_json`, flattening |
| 23 | `23_reading_parquet` | Columnar format, schema in file, pushdown benefits |
| 24 | `24_writing_data` | Write modes, formats, `saveAsTable`, output file behavior |
| 25 | `25_partitioning_files` | `partitionBy`, partition pruning, choosing partition columns, bucketing |
| 26 | `26_spark_sql` | SQL vs DataFrame API, CTEs, subqueries |
| 27 | `27_temporary_views` | Temp vs global temp views, scope |
| 28 | `28_error_handling` | try/except patterns, bad-record handling, logging |
| 29 | `29_data_quality_checks` | Null/duplicate/range/schema checks, reusable validation functions |
| 30 | `30_building_an_etl_pipeline` | End-to-end small ETL: read, clean, transform, validate, write |

**Interview-critical (give extra time):** 11, 12, 17, 19, 20, 25.

- [x] All 30 notebooks complete, each with Interview Q&A and a practice problem
- [x] Questions added to `interview_prep/question_bank.md` (generated with `tools/build_question_bank.py`)

---

## 02_spark_internals (2 weeks)

**Goal:** Move from "I can write PySpark" to "I understand how Spark executes my code."

Execution flow to be able to draw and explain: Application → Driver → Job → Stages → Tasks → Executors → Output.

- [x] `01_driver_executors`: roles, cluster manager, how work is distributed
- [x] `02_jobs_stages_tasks`: how actions trigger jobs, stage boundaries, task counts
- [x] `03_transformations_actions`: full classification, common interview traps
- [x] `04_lazy_evaluation`: why Spark is lazy, benefits, proving it with `explain()`
- [x] `05_dag_and_query_plans`: logical vs physical plan, reading `explain("formatted")`
- [x] `06_narrow_wide_transformations`: examples, why wide ones cause shuffles
- [x] `07_shuffle`: what happens, why expensive, shuffle partitions setting
- [x] `08_partitioning_and_parallelism`: `repartition` vs `coalesce`, partition sizing, relationship between partitions, cores and tasks
- [x] `09_broadcast_and_join_strategies`: broadcast hash, sort-merge, shuffle hash; broadcast hints
- [x] `10_caching_persistence`: `cache` vs `persist`, storage levels, when it hurts
- [x] `11_serialization`: Java vs Kryo, why it matters, UDF serialization cost
- [x] `12_catalyst_and_tungsten`: optimizer stages, code generation, why DataFrames beat RDDs
- [x] `13_adaptive_query_execution`: coalescing partitions, skew join handling, dynamic broadcast
- [x] `14_spark_ui`: jobs, stages, tasks, SQL and storage tabs, what to look at first
- [x] `15_internals_interview_qa`: consolidated spoken answers

---

## 03_delta_lake (1.5 weeks)

**Goal:** Understand the storage layer behind the lakehouse.

- [x] `01_delta_fundamentals`: Parquet + transaction log, managed vs external tables
- [x] `02_creating_and_querying_tables`: SQL and `DeltaTable` API, `DESCRIBE DETAIL`
- [x] `03_acid_and_delta_log`: `_delta_log`, commits, checkpoints, optimistic concurrency
- [x] `04_schema_enforcement`: how and why Delta rejects bad writes
- [x] `05_schema_evolution`: `mergeSchema`, `overwriteSchema`, column mapping
- [x] `06_update_delete`: DML on Delta
- [x] `07_merge_upserts`: `MERGE INTO`, SCD Type 1 and Type 2
- [x] `08_time_travel_restore`: `VERSION AS OF`, `DESCRIBE HISTORY`, `RESTORE`
- [x] `09_optimize_vacuum`: `OPTIMIZE`, `VACUUM`, small-file problem, retention
- [x] `10_partitioning_zorder_clustering`: partitioning, Z-ordering, data skipping, liquid clustering
- [x] `11_change_data_feed`: enabling CDF, reading changes
- [x] `12_constraints_generated_columns`: `CHECK`, `NOT NULL`, generated and identity columns
- [x] `13_medallion_overview`: CSV/JSON/Parquet → Bronze → Silver → Gold concept
- [x] `14_delta_interview_qa`

---

## 04_databricks (1.5 weeks)

**Goal:** Apply what you learned using Databricks features properly.

- [x] `01_workspace_notebooks_repos`: workspace organization, Git folders
- [x] `02_compute_types`: serverless, all-purpose, job compute, pools (conceptual where limited)
- [x] `03_dbutils`: `fs`, `widgets`, `secrets`, `notebook`, `jobs.taskValues`
- [x] `04_parameters_and_widgets`: parameterized notebooks
- [x] `05_secrets_and_scopes`: secret scopes, never hardcoding credentials
- [x] `06_sql_warehouse`: serverless SQL warehouses, SQL editor
- [x] `07_dashboards_and_genie`: dashboards, parameters, Genie spaces
- [x] `08_monitoring_basics`: run history, logs, system tables (as available)
- [x] `09_databricks_interview_qa`

---

## 05_optimization (1 week)

- [x] `01_reading_query_profiles`: Databricks query profile and Spark UI together
- [x] `02_data_skew`: detection, salting, AQE skew handling, broadcast
- [x] `03_small_files_and_file_layout`: compaction, file sizing, partition strategy
- [x] `04_memory_and_spill`: spill, OOM patterns, what to change
- [x] `05_join_optimization`: choosing strategies, hints, pre-aggregation
- [x] `06_avoiding_udfs_and_shuffles`: rewriting for performance
- [x] `07_cost_awareness`: DBUs, serverless vs classic, practical habits
- [x] `08_slow_job_debugging_playbook`: "a job is slow, how do you debug it?" step by step

---

## 06_unity_catalog (1 week)

- [x] `01_catalog_hierarchy`: metastore → catalog → schema → table/view/volume/function
- [x] `02_managed_vs_external`: storage locations, managed vs external tables
- [x] `03_volumes`: files in volumes, vs DBFS and cloud paths
- [x] `04_permissions_grants`: `GRANT`, `REVOKE`, ownership, inheritance (as Free Edition allows)
- [x] `05_lineage_tags_discovery`: lineage, comments, tags
- [x] `06_views_and_functions`: views, materialized views, SQL UDFs
- [x] `07_pii_masking_row_filters`: column masks and row filters (conceptual if unavailable)

---

## 07_workflows (1.5 weeks)

- [ ] `01_jobs_basics`: tasks, schedules, triggers
- [ ] `02_task_dependencies_parameters`: multi-task DAGs, job parameters, task values
- [ ] `03_retries_alerts_monitoring`: retries, timeouts, notifications, run history
- [ ] `04_lakeflow_declarative_pipelines`: streaming tables, materialized views, expectations (formerly DLT)
- [ ] `05_data_quality_expectations`: drop/fail/warn behaviors, quarantine patterns
- [ ] `06_notebook_workflows`: `%run` vs `dbutils.notebook.run`, modular code
- [ ] `07_testing_and_code_structure`: unit-testing transformations, production repo structure

---

## 08_streaming_and_ingestion (1.5 weeks)

- [ ] `01_batch_ingestion_patterns`: full vs incremental loads
- [ ] `02_copy_into`: idempotent loads
- [ ] `03_auto_loader`: `cloudFiles`, schema inference/evolution, rescued data column
- [ ] `04_structured_streaming_basics`: triggers, output modes, checkpoints, watermarks
- [ ] `05_bronze_layer`: raw capture, metadata and audit columns
- [ ] `06_silver_layer`: cleansing, dedup, conformance, quality checks
- [ ] `07_gold_layer`: aggregates and business marts
- [ ] `08_incremental_and_late_data`: idempotency, upserts, late-arriving data
- [ ] `09_ingesting_apis_and_nested_json`

---

## 09_azure_databricks (2 weeks)

**Note:** Free Edition cannot do this part. Start with concepts and diagrams, and add hands-on work if you create an Azure free-trial account. Interviewers for Azure Data Engineer roles ask about these topics, so document them either way.

Target architecture to be able to draw and explain: Sources → ADF / ADLS Gen2 → Azure Databricks → Unity Catalog → Delta Lake → data pipeline → consumers.

- [ ] `01_azure_fundamentals_for_data`: subscription, resource group, regions, storage accounts
- [ ] `02_adls_gen2`: hierarchical namespace, containers, access tiers, folder design
- [ ] `03_azure_databricks_workspace`: workspace deployment, premium vs standard, VNet concepts
- [ ] `04_adf_to_databricks`: ADF pipelines triggering Databricks notebooks/jobs, parameter passing
- [ ] `05_managed_identity_and_entra_id`: managed identities, service principals, access connectors
- [ ] `06_key_vault_and_secret_scopes`: Key Vault-backed secret scopes
- [ ] `07_rbac_and_data_access`: Azure RBAC vs Unity Catalog permissions, external locations and credentials
- [ ] `08_networking_basics`: VNet injection, private endpoints, firewall concepts
- [ ] `09_monitoring_and_logging`: Azure Monitor, Log Analytics, alerts
- [ ] `10_ci_cd`: Git + Azure DevOps or GitHub Actions, Databricks Asset Bundles, environments
- [ ] `11_production_architecture`: dev/test/prod separation, cost control, a full reference design
- [ ] `12_azure_interview_qa`

---

## Projects (2 weeks)

### Project 1: Medallion pipeline (guided)
- [ ] Choose a public dataset (e.g. NYC taxi, e-commerce, or a bookings dataset)
- [ ] Ingest with Auto Loader into bronze
- [ ] Clean and deduplicate into silver with quality checks
- [ ] Build gold aggregates
- [ ] Orchestrate with a Job or declarative pipeline
- [ ] Build a dashboard on top
- [ ] Write a project README with architecture diagram, decisions and lessons learned

### Project 2: Your own domain (independent)
- [ ] Choose a domain you know well and design the data model yourself
- [ ] Build the pipeline without step-by-step guidance
- [ ] Document trade-offs and what you would do differently
- [ ] Be ready to present it as an interview portfolio piece

---

## Interview preparation (continuous, then 1-2 weeks of intensive review)

**Continuous:** after every notebook, add its Q&A to `interview_prep/question_bank.md`.

**Intensive review at the end:**
- [ ] Re-answer the full question bank aloud, without notes
- [ ] Solve all problems in `coding_problems.md` on a blank notebook
- [ ] Prepare 2-minute spoken explanations for:
  - What happens when I run `df.groupBy().count()`?
  - How does a shuffle work and why is it expensive?
  - Broadcast join vs sort-merge join?
  - How does Delta provide ACID guarantees?
  - Walk me through your medallion project
  - Walk me through an Azure Databricks production architecture
- [ ] Rehearse scenarios:
  - A join is slow. How do you debug it?
  - A job creates thousands of small files. What now?
  - One task takes much longer than the rest. Why?
  - How do you handle late-arriving or duplicate data?
  - How do you design an incremental load?
- [ ] At least 3 mock interviews (with Claude or a friend), feedback logged in `mock_interview_log.md`
- [ ] Consider the **Databricks Certified Data Engineer Associate** exam as a concrete target. See [docs/certification/data_engineer_associate.md](docs/certification/data_engineer_associate.md) for the May 2026 domains and lesson mapping

---

## Suggested timeline

| Folder | Topic | Duration |
|---|---|---|
| 00 | Platform tour | 2-3 days |
| 01 | Spark basics (30 lessons) | 4-5 weeks |
| 02 | Spark internals | 2 weeks |
| 03 | Delta Lake | 1.5 weeks |
| 04 | Databricks | 1.5 weeks |
| 05 | Optimization | 1 week |
| 06 | Unity Catalog | 1 week |
| 07 | Workflows | 1.5 weeks |
| 08 | Streaming and ingestion | 1.5 weeks |
| 09 | Azure Databricks | 2 weeks |
| - | Projects | 2 weeks |
| - | Intensive interview review | 1-2 weeks |

---

## Weekly rhythm (suggested)

| Day | Activity |
|---|---|
| Mon-Thu | Learn and build one notebook per day or two |
| Fri | Practice problems from memory, add Q&A to question bank |
| Sat | Review the week, clean notebooks, commit and push |
| Sun | Rest or light reading |

---

## Progress tracker

| Folder | Topic | Status | Started | Completed |
|---|---|---|---|---|
| 00 | Platform tour | Complete | | 2026-10-05 |
| 01 | Spark basics | Complete | | 2026-10-05 |
| 02 | Spark internals | Complete | | 2026-10-05 |
| 03 | Delta Lake | Complete | | 2026-10-05 |
| 04 | Databricks | Complete | | 2026-10-05 |
| 05 | Optimization | Complete | | 2026-10-05 |
| 06 | Unity Catalog | Complete | | 2026-10-05 |
| 07 | Workflows | Not started | | |
| 08 | Streaming and ingestion | Not started | | |
| 09 | Azure Databricks | Not started | | |
| - | Projects | Not started | | |
| - | Interview prep | Not started | | |

---

## Notes on Databricks Free Edition

- Compute is serverless only, with usage quotas, so classic-cluster topics (cluster configs, init scripts, pools) can only be covered conceptually. Mark these clearly in notebooks.
- Some enterprise governance and networking features are limited or unavailable. When a feature isn't available, document what it does and how it works on a paid workspace.
- Features and limits change over time. Check current Databricks documentation before writing each notebook and note the date you verified.
