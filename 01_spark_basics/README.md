# 01 Spark Basics

30 PySpark lessons in 3 levels. Every notebook runs top to bottom in **Databricks Free Edition** (serverless) and creates its own sample data.

⭐ = interview-critical, so give these extra time.

## Level 1: Foundation

| # | Notebook | Key topics |
|---|---|---|
| 01 | [01_pyspark_introduction](01_pyspark_introduction.ipynb) | Spark vs PySpark vs Pandas, first DataFrame |
| 02 | [02_spark_session](02_spark_session.ipynb) | SparkSession, SparkContext, Spark Connect, deploy modes |
| 03 | [03_dataframes](03_dataframes.ipynb) | Creating and inspecting DataFrames, show vs collect, immutability |
| 04 | [04_schema_and_data_types](04_schema_and_data_types.ipynb) | `StructType`, DDL schemas, nested types, `cast` vs `try_cast`, ANSI mode |
| 05 | [05_select](05_select.ipynb) | Column references, expressions, `selectExpr`, dynamic selection, column pruning |
| 06 | [06_filter_where](06_filter_where.ipynb) | Conditions, `&` `\|` `~`, `isin`, `like`, null logic, predicate pushdown |
| 07 | [07_withcolumn](07_withcolumn.ipynb) | `withColumn(s)`, `lit`, renaming, the `withColumn`-in-a-loop anti-pattern |
| 08 | [08_when_otherwise](08_when_otherwise.ipynb) | Conditional logic, `CASE WHEN`, conditional aggregation |
| 09 | [09_drop_alias](09_drop_alias.ipynb) | `drop`, column and DataFrame aliases, self-joins, renaming strategies |
| 10 | [10_distinct_dropduplicates](10_distinct_dropduplicates.ipynb) | `distinct`, `dropDuplicates`, latest record per key |

## Level 2: Data transformation

| # | Notebook | Key topics |
|---|---|---|
| 11 | ⭐ [11_groupby](11_groupby.ipynb) | `GroupedData`, partial aggregation, shuffle, WHERE vs HAVING |
| 12 | ⭐ [12_aggregations](12_aggregations.ipynb) | `agg`, approximate distinct, percentiles, `pivot`, `rollup`, `cube` |
| 13 | [13_sorting](13_sorting.ipynb) | `orderBy`, null ordering, top-N, `sortWithinPartitions`, range partitioning |
| 14 | [14_string_functions](14_string_functions.ipynb) | Cleaning, splitting, regex extract/replace, fuzzy matching |
| 15 | [15_date_functions](15_date_functions.ipynb) | Parsing, arithmetic, truncation, time zones, date dimension |
| 16 | [16_null_handling](16_null_handling.ipynb) | Three-valued logic, `na.fill/drop/replace`, `coalesce`, nulls in joins |
| 17 | ⭐ [17_joins](17_joins.ipynb) | All join types, duplicate keys, non-equi joins, broadcast vs sort-merge |
| 18 | [18_union](18_union.ipynb) | `union` vs `unionByName`, missing columns, set operations |
| 19 | ⭐ [19_window_functions](19_window_functions.ipynb) | Ranking, `lag`/`lead`, frames, top-N per group, gaps and islands |
| 20 | ⭐ [20_udfs](20_udfs.ipynb) | Python, Arrow, pandas and SQL UDFs, and why built-ins win |

## Level 3: Data engineering

| # | Notebook | Key topics |
|---|---|---|
| 21 | [21_reading_csv](21_reading_csv.ipynb) | Options, schemas, bad records, quarantine pattern, `read_files` |
| 22 | [22_reading_json](22_reading_json.ipynb) | Multi-line JSON, nested data, `explode`, `from_json`, higher-order functions |
| 23 | [23_reading_parquet](23_reading_parquet.ipynb) | Columnar format, row groups, pruning, pushdown, `mergeSchema` |
| 24 | [24_writing_data](24_writing_data.ipynb) | Save modes, tables vs paths, file counts, idempotent overwrites |
| 25 | ⭐ [25_partitioning_files](25_partitioning_files.ipynb) | `partitionBy`, partition pruning, small files, liquid clustering |
| 26 | [26_spark_sql](26_spark_sql.ipynb) | SQL vs DataFrame API, CTEs, subqueries, safe parameters |
| 27 | [27_temporary_views](27_temporary_views.ipynb) | Temp, global temp and permanent views, materialized views |
| 28 | [28_error_handling](28_error_handling.ipynb) | Analysis vs execution errors, error classes, `try_*`, logging, retries |
| 29 | [29_data_quality_checks](29_data_quality_checks.ipynb) | Reusable checks, fail/warn/quarantine, Delta constraints |
| 30 | ⭐ [30_building_an_etl_pipeline](30_building_an_etl_pipeline.ipynb) | Bronze → Silver → Gold, quarantine, reconciliation, idempotency |

## Running the lessons in Free Edition

- Lessons 01–20 need no setup: data is created inside each notebook
- Lessons 21+ create a schema `workspace.spark_basics` and a volume `raw_files` (if they don't exist) and write their sample files to `/Volumes/workspace/spark_basics/raw_files/lessonNN`. Each lesson ends with an optional cleanup cell
- A few cells use Databricks-only features (`QUALIFY`, `read_files`, `dbutils`). They are marked in the text

## Lesson structure

Goal → why it matters → concept → real-world example → syntax → hands-on sections (each with *what it does* and *expected output*) → under the hood → mistakes and troubleshooting → interview Q&A → 🎓 certification corner → practice problem → solution → summary and cheat sheet → git commit.
