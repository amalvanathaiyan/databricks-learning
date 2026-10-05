# Question Bank

Interview questions from every lesson, with short spoken-style answers.
Practise by covering the answer, saying yours out loud, then comparing.

**224 questions** across 34 lessons.

Generated from each notebook's **Interview Q&A** section by `tools/build_question_bank.py`.
Edit the notebooks, then run the script again.

## 00 Platform tour

### 00_01_workspace_and_ui

**1. What is a Databricks workspace?**

The web environment where you organize notebooks, files, compute, jobs and data assets for a team or project.

**2. What is the difference between the workspace and the catalog?**

The workspace holds code and files (notebooks, folders). The catalog (Unity Catalog) holds governed data objects like tables and volumes.

**3. Where does your code actually run?**

On compute attached to the notebook, which is serverless in Free Edition.

**4. What is a Git folder?**

A workspace folder linked to a Git repo, so you can commit, push and pull notebooks directly from Databricks.

**5. What is the three-level namespace in Unity Catalog?**

`catalog.schema.object`, for example `workspace.default.sales`. Every table, view, volume and function is addressed that way.

### 00_02_notebook_basics

**1. What is the difference between `show()` and `display()`?**

`show()` is a Spark method that prints a text table. `display()` is Databricks-specific and gives an interactive table with sorting and charts.

**2. How do you share data between Python and SQL cells?**

Register a temp view with `createOrReplaceTempView` in Python, then query it in a `%sql` cell.

**3. What is the difference between `%run` and `dbutils.notebook.run`?**

`%run` includes the other notebook's code and variables in the current notebook. `dbutils.notebook.run` starts it as a separate run with its own context and returns a value.

**4. What are widgets used for?**

Parameterizing notebooks, for example passing a date or environment name in from a job.

**5. Where must a magic command appear in a cell?**

On the first line. Otherwise the cell runs in the notebook's default language.

### 00_03_serverless_compute_free_edition

**1. What is serverless compute?**

Compute where Databricks manages the infrastructure: no cluster sizing, fast startup, and billing based on usage.

**2. All-purpose vs job compute?**

All-purpose is for interactive work and can be shared. Job compute is created for an automated run and terminates afterward, which is cheaper for production.

**3. Why use job compute for production instead of an all-purpose cluster?**

Lower cost, isolation from interactive workloads, and a clean environment for each run.

**4. What are instance pools?**

Pools of idle, pre-warmed VMs that reduce classic cluster startup time.

**5. What is the trade-off of serverless?**

Less control over configuration in exchange for simplicity and fast startup.

**6. Why can't you use `sparkContext` or RDDs on serverless notebooks?**

Serverless notebooks use Spark Connect, a client-server protocol where the notebook sends DataFrame and SQL plans to a remote Spark. Driver-side objects such as `sparkContext` aren't exposed to the client.

### 00_04_git_workflow

**1. Why use Git folders in Databricks?**

They link workspace notebooks to a repo so you get version control, branching and collaboration without leaving Databricks.

**2. What is the difference between commit and push?**

A commit saves a snapshot in your local history. A push sends those commits to the remote repo.

**3. Why work on branches instead of `main`?**

Branches isolate changes, allow review through pull requests, and keep `main` stable for production.

**4. What is a merge conflict and how do you handle it?**

It happens when two branches change the same lines. You open the file, choose or combine the correct content, then commit the resolution.

**5. What should never be committed?**

Secrets, credentials and large data files.

**6. How does code get from a Git folder to production on Databricks?**

Changes are merged to `main` through pull requests, then a CI/CD pipeline runs tests and deploys jobs and pipelines to staging and production workspaces, typically with Databricks Asset Bundles.

## 01 Spark basics

### 01_pyspark_introduction

**1. What is the difference between Python, PySpark and Apache Spark?**

Python is a programming language. Apache Spark is a distributed data processing engine. PySpark is the Python API that lets you write Spark applications in Python.

**2. What is SparkSession?**

The entry point to a Spark application. It is used to create DataFrames, read data, run SQL and configure Spark. In Databricks it is already available as `spark`.

**3. Why Spark instead of Pandas?**

Pandas runs on one machine and is limited by its memory. Spark distributes data and processing across a cluster, so it scales to much larger datasets.

**4. What is a DataFrame?**

A distributed collection of data organized into named columns, like a table, with a schema.

**5. Is Spark a database?**

No. It is a processing engine. It reads data from storage (files, tables) and processes it, but it doesn't store data itself.

### 02_spark_session

**1. What is SparkSession?**

The unified entry point to Spark. It is used to create DataFrames, read data, run SQL and manage configuration.

**2. What is the difference between SparkSession and SparkContext?**

SparkContext is the older low-level entry point that connects to the cluster and creates RDDs. SparkSession, introduced in Spark 2.0, wraps SparkContext, SQLContext and HiveContext into one object.

**3. What does `getOrCreate()` do?**

Returns the existing SparkSession if there is one, otherwise creates a new one.

**4. Do you need to create a SparkSession in Databricks?**

No, a session called `spark` is created for you.

**5. Can you have multiple SparkSessions?**

Yes. They can share one SparkContext but have separate SQL configs and temp views. In practice most applications use one.

**6. Where does the SparkSession run?**

In the driver. The executors only run tasks.

**7. What is the difference between client mode and cluster mode?**

In client mode the driver runs on the machine that submits the application. In cluster mode the driver runs inside the cluster, on a node chosen by the cluster manager. Executors run on the cluster in both modes.

**8. Which mode would you use for production and why?**

Cluster mode. The driver sits next to the executors, so there is less network latency, and the job keeps running even if the submitting machine disconnects.

**9. Which mode is used for interactive work like spark-shell or notebooks?**

Client mode, because the driver must be reachable so you can see results and type commands.

**10. What happens in client mode if the submitting machine goes down?**

The driver dies with it, so the application fails.

**11. What is local mode?**

The driver and executors run in one process on one machine. It's used for learning and testing, not for real workloads.

**12. What deploy mode does Databricks use?**

You don't choose one. The driver runs on the driver node inside the compute, which behaves like cluster mode.

**13. What is Spark Connect?**

A client-server architecture introduced in Spark 3.4. The client (for example a serverless notebook) builds DataFrame plans and sends them to a remote Spark server, which executes them. The client has no `sparkContext` or RDD access.

### 03_dataframes

**1. What is a Spark DataFrame?**

A distributed collection of data organized into named columns with a schema, like a table. It is immutable and lazily evaluated.

**2. How is a DataFrame different from an RDD?**

An RDD is a low-level collection of objects with no schema. A DataFrame has a schema, so Spark's Catalyst optimizer can plan and optimize operations. DataFrames are usually faster and easier to write.

**3. How is a Spark DataFrame different from a Pandas DataFrame?**

Spark's is distributed across a cluster and lazy. Pandas runs on one machine, keeps data in memory and executes immediately.

**4. What does it mean that DataFrames are immutable?**

You can't change a DataFrame in place. Each transformation returns a new DataFrame, and the original stays the same.

**5. What is the difference between `show()`, `take()` and `collect()`?**

`show()` prints rows for viewing. `take(n)` returns n rows to the driver as a list. `collect()` returns all rows to the driver, which can crash it on large data.

**6. Is `count()` a transformation or an action?**

An action, because it triggers a job and returns a result to the driver.

**7. Is `printSchema()` an action?**

No. It only reads metadata and doesn't process data.

**8. Why be careful with `toPandas()`?**

It collects the whole DataFrame into the driver's memory, so it can fail on large data.

**9. Is the data held in memory once you create a DataFrame?**

Not necessarily. A DataFrame is a plan plus a description of the data. Data is processed when an action runs, unless you cache it.

### 04_schema_and_data_types

**1. What is a schema in Spark?**

The structure of a DataFrame: each column's name, data type and nullability, stored as a `StructType` of `StructField`s. It is metadata, so reading it is free.

**2. Why would you define a schema explicitly instead of using `inferSchema`?**

Three reasons. Performance, because inference needs an extra pass over the data. Correctness, because inference can guess wrong, for example treating IDs as numbers. And stability, because the schema becomes a documented contract that doesn't change when a file changes.

**3. What is the difference between `StructType` and a DDL string?**

They describe the same thing. `StructType` is built from Python objects and is good for generating schemas in code. A DDL string like `"id INT, name STRING"` is shorter and uses the same syntax as SQL `CREATE TABLE`.

**4. When would you use `DecimalType` instead of `DoubleType`?**

For money and anything that needs exact precision. Doubles are binary floating point, so values like 0.1 can't be stored exactly and sums drift.

**5. What happens when a cast fails?**

With ANSI mode on, which is the default in Spark 4 and on Databricks serverless, the query fails with an error such as `CAST_INVALID_INPUT`. With ANSI off it returns null. `try_cast` always returns null on failure, so it is the explicit way to get lenient behavior.

**6. How do you access nested fields?**

Dot notation for structs (`address.city`), an index for arrays (`phones[0]`), and a key for maps (`attributes['tier']`).

**7. Does `nullable=False` guarantee there are no nulls?**

It is enforced when you build a DataFrame from local data, and Delta tables enforce `NOT NULL` constraints on write. But nullability from some sources is only a hint, so production pipelines still run explicit null checks.

### 05_select

**1. What does `select` do and is it a transformation or an action?**

It returns a new DataFrame with the chosen columns or expressions. It is a narrow transformation, so it is lazy and needs no shuffle.

**2. What is the difference between `select` and `selectExpr`?**

`select` takes column names or Column objects. `selectExpr` takes SQL expression strings, such as `"salary * 1.1 AS raise"`. They compile to the same plan.

**3. What are the ways to reference a column, and which do you prefer?**

A string, `F.col("x")`, `df.x` and `df["x"]`. I prefer `F.col` because it isn't bound to a DataFrame variable and works for any name. `df["x"]` is useful to disambiguate after joins.

**4. Why does selecting fewer columns make a query faster?**

Delta and Parquet are columnar. The optimizer pushes the column list down to the scan (column pruning), so Spark reads only those columns from storage and moves less data.

**5. What is the difference between `select` and `withColumn`?**

`withColumn` adds or replaces one column and keeps the rest. `select` defines the full output column list. To add many columns, one `select` is cleaner than many `withColumn` calls.

**6. How do you select a column whose name contains a dot or a space?**

Wrap it in backticks, for example `F.col("`order.date`")`. Without backticks a dot is read as struct field access.

**7. What is `F.lit()` used for?**

To create a column with a constant value, for example a source system name or a default flag.

### 06_filter_where

**1. What is the difference between `filter` and `where`?**

None. `where` is an alias for `filter`, added for SQL users. Both accept a Column condition or a SQL string.

**2. Why do you need parentheses around conditions in PySpark?**

Because Python gives `&` and `|` higher precedence than comparison operators, so `a > 1 & b < 2` is parsed wrongly. Wrapping each comparison in parentheses fixes it.

**3. Why can't you use Python's `and` / `or`?**

They call `bool()` on the Column, and a Column has no single True/False value until Spark evaluates it per row, so PySpark raises a `ValueError`.

**4. How does `filter` treat nulls?**

A comparison with null returns null, and `filter` keeps only rows where the condition is true, so those rows are dropped. You must handle nulls explicitly with `isNull`, `isNotNull`, `coalesce` or `eqNullSafe`.

**5. What is predicate pushdown?**

The optimizer moves filters down to the data source scan. With Parquet and Delta, the scan uses file statistics to skip files or row groups that can't match, so less data is read.

**6. Is `filter` a narrow or wide transformation?**

Narrow. Each partition is filtered on its own, with no data movement between executors.

**7. Does the position of a filter in your code matter for performance?**

Usually not much, because the optimizer pushes filters early. But it can't push a filter past a Python UDF or some complex operations, so filtering early in code is still a good habit.

### 07_withcolumn

**1. What does `withColumn` do?**

It returns a new DataFrame with a column added, or replaced if the name already exists. It is a lazy, narrow transformation that adds a Project node to the plan.

**2. What is `F.lit` and why is it needed?**

It wraps a Python constant into a Column. DataFrame methods expect Column expressions, so a bare string or number must be wrapped.

**3. Why is calling `withColumn` in a loop a problem?**

Each call creates a new DataFrame whose plan must be analyzed again, so the driver spends a long time planning and very large plans can overflow the stack. Use one `select` with a list of expressions, or `withColumns`.

**4. What is the difference between `withColumn` and `select`?**

`withColumn` keeps all existing columns and adds or replaces one. `select` defines the whole output column list. Both produce a Project in the plan.

**5. What happens if you rename a column that doesn't exist?**

Nothing. `withColumnRenamed` is a no-op for missing columns and raises no error, so typos can slip through.

**6. How would you add an audit timestamp and source column to every row?**

`df.withColumns({"ingest_ts": F.current_timestamp(), "source": F.lit("crm")})`. On Databricks, file-based sources also expose `_metadata.file_path` for the source file name.

### 08_when_otherwise

**1. How do you write if/else logic in PySpark?**

With `F.when(condition, value).when(...).otherwise(default)`, or with SQL `CASE WHEN` in `selectExpr` or `spark.sql`. Both become the same `CaseWhen` expression.

**2. What happens if no condition matches and there is no `otherwise`?**

The result is null for that row.

**3. Does the order of `when` clauses matter?**

Yes. They are evaluated top to bottom and the first true condition wins, so broader conditions must come after specific ones.

**4. How are nulls handled in `when` conditions?**

A condition that evaluates to null is treated as not true, so the row moves on to the next branch or to `otherwise`. Handle nulls explicitly with `isNull()` if they need their own result.

**5. Why prefer `when` over a Python UDF for conditional logic?**

`when` is a native Catalyst expression, so it is optimized and code-generated and runs in the JVM. A UDF serializes each row to Python and back, and the optimizer can't see inside it.

**6. How do you count rows matching a condition inside an aggregation?**

`F.sum(F.when(cond, 1).otherwise(0))`, or `F.count(F.when(cond, True))`, because `count` ignores nulls.

### 09_drop_alias

**1. What happens if you `drop` a column that doesn't exist?**

Nothing. It is a silent no-op, which is convenient but can hide typos, so critical drops should be asserted.

**2. What is the difference between a column alias and a DataFrame alias?**

A column alias names an expression in the output. A DataFrame alias names the whole DataFrame so columns can be qualified, like `e.id` and `m.id`, which is required for self-joins.

**3. How do you rename all columns of a DataFrame?**

Use `toDF(*new_names)` if I have the full list in order, `withColumnsRenamed(mapping)` for a dictionary, or `select([col(c).alias(f(c)) for c in df.columns])` for a rule such as lower-casing.

**4. How do you remove the duplicate key column after a join?**

Join with `on="key"` (a string or list), which keeps one copy automatically, or drop the other side's column with `drop(other_df["key"])`.

**5. Are `drop` and `alias` expensive?**

No. They only change the projection in the logical plan. Dropping columns can even make queries cheaper, because columnar readers skip them.

### 10_distinct_dropduplicates

**1. What is the difference between `distinct()` and `dropDuplicates()`?**

With no arguments they are the same. `dropDuplicates` also accepts a subset of columns and keeps one row per combination of those columns while returning all columns.

**2. Which row does `dropDuplicates(["id"])` keep?**

An arbitrary one. It is compiled into an aggregate with `first()`, so the result depends on partitioning and task order and isn't guaranteed.

**3. How do you keep the latest record per key?**

A window partitioned by the key, ordered by the timestamp descending plus a tie-breaker, then `row_number()` and filter where it equals 1. `max_by` in a groupBy is an alternative when I only need a few columns.

**4. Are `distinct` and `dropDuplicates` narrow or wide?**

Wide. Equal keys must meet on the same executor, so they cause a shuffle, with a partial aggregation before it to reduce data.

**5. How does `distinct` treat nulls?**

Nulls are treated as equal to each other for deduplication, so several null rows collapse into one.

**6. How do you deduplicate in a streaming pipeline?**

With `dropDuplicatesWithinWatermark` or `dropDuplicates` combined with a watermark, so Spark can drop old state. For upserts into a table, `MERGE` is used. Both come later in the streaming folder.

### 11_groupby

**1. What happens internally when you run `df.groupBy("country").count()`?**

Spark plans two stages. In the first, each task does a partial count per country inside its own partition. Then an Exchange shuffles those partial results so all rows with the same country hash to the same partition. In the second stage, each task adds up the partial counts to produce the final result. Nothing runs until an action is called.

**2. Is `groupBy` a narrow or wide transformation?**

Wide, because rows with the same key can be on any partition and must be brought together with a shuffle.

**3. Why is the partial aggregation important?**

It reduces the data before the shuffle. Instead of sending every row across the network, each partition sends one row per key. That is why `groupBy().sum()` scales much better than collecting all values per key.

**4. How many partitions does the result of a `groupBy` have?**

Initially `spark.sql.shuffle.partitions`, which defaults to 200. With Adaptive Query Execution, Spark coalesces small shuffle partitions at runtime, so the actual number is often much lower. On Databricks serverless it is tuned automatically.

**5. What is the difference between WHERE and HAVING?**

WHERE filters rows before grouping. HAVING filters groups after aggregation. In PySpark both are `filter`, placed before or after the `groupBy`.

**6. How are nulls handled in `groupBy`?**

Null keys form their own group. Inside aggregates, `count(col)`, `sum`, `avg`, `min` and `max` ignore null values, while `count(*)` counts every row.

**7. What causes a groupBy to be slow?**

Usually a large shuffle or data skew, where one key holds a big share of the rows so one task does most of the work. You fix it by filtering early, selecting fewer columns, letting AQE handle skew, or salting the key.

### 12_aggregations

**1. How do you compute several aggregates in one go, and why is it better than separate queries?**

`groupBy(...).agg(f1.alias(...), f2.alias(...))`. Spark computes all of them in one scan and one shuffle. Separate queries would scan and shuffle the data again for each metric.

**2. What is the difference between `countDistinct` and `approx_count_distinct`?**

`countDistinct` is exact, but it must shuffle and track every distinct value, which is expensive at scale. `approx_count_distinct` uses HyperLogLog++ sketches with fixed memory and a configurable relative error, about 5% by default. It is much cheaper.

**3. What is the difference between `rollup` and `cube`?**

`rollup(a, b)` produces hierarchical subtotals: (a, b), (a) and the grand total. `cube(a, b)` produces every combination: (a, b), (a), (b) and the grand total. Cube grows as 2 to the power of the number of columns.

**4. How do you tell a subtotal row from a real null in rollup output?**

Use `grouping(col)`, which is 1 when the column is aggregated away, or `grouping_id()` for a bitmask across all grouping columns.

**5. What does `pivot` do, and how do you make it efficient?**

It turns distinct values of a column into separate columns with an aggregate in each cell. Passing the list of values explicitly avoids an extra job to compute them and fixes the output schema.

**6. How does Spark compute `avg` in a distributed way?**

Each partition computes a partial sum and count. After the shuffle, they are combined into the total sum and total count, and the average is their ratio. Averaging partial averages would be wrong.

**7. What is the difference between `collect_list` and `collect_set`?**

`collect_list` keeps all values including duplicates. `collect_set` keeps only unique values. Neither guarantees order, and both can use a lot of memory on large groups.

### 13_sorting

**1. What is the difference between `orderBy` and `sort`?**

None. They are aliases and both perform a global sort.

**2. Why is a global sort expensive in Spark?**

Spark samples the data to choose range boundaries, then shuffles every row into a range partition, then sorts each partition. That is a full shuffle of all the data plus an extra sampling job.

**3. What is `sortWithinPartitions` and when would you use it?**

It sorts each partition independently with no shuffle. I use it before writing files to cluster similar values together for better compression and data skipping, when global order isn't needed.

**4. How does Spark optimize `orderBy().limit(n)`?**

It turns it into `TakeOrderedAndProject`. Each partition keeps only its top n rows, and the results are merged, so the full dataset is never sorted.

**5. Where do nulls go when sorting?**

Ascending puts nulls first and descending puts them last by default. You can override that with `asc_nulls_last`, `desc_nulls_first` and the other variants.

**6. Is the order of a DataFrame preserved after a join or groupBy?**

No. Any shuffle can reorder rows, so sorting should be the last step before output.

### 14_string_functions

**1. What is the difference between `concat` and `concat_ws`?**

`concat` joins values and returns null if any input is null. `concat_ws` takes a separator and skips null inputs, so it's usually safer for building names or keys.

**2. How do you extract part of a string with a regex in Spark?**

`regexp_extract(col, pattern, group_index)` returns the captured group. It returns an empty string when there is no match, not null. `regexp_extract_all` returns all matches as an array.

**3. How do you remove all non-numeric characters from a column?**

`regexp_replace(col, "[^0-9]", "")`.

**4. Are `substring` positions 0-based or 1-based?**

1-based, like SQL. But array indexing after `split` is 0-based with `[i]`, while `element_at` is 1-based.

**5. Why use built-in string functions instead of a Python UDF?**

Built-ins are Catalyst expressions that are optimized and code-generated in the JVM. A Python UDF serializes every row to a Python process and back, which is much slower and opaque to the optimizer.

**6. How would you find near-duplicate names?**

Normalize first (trim, lower case, remove punctuation), then compare with `levenshtein` or `soundex`, usually within a blocking key such as postcode to avoid comparing every pair.

### 15_date_functions

**1. What is the difference between `DATE`, `TIMESTAMP` and `TIMESTAMP_NTZ`?**

`DATE` is a calendar day. `TIMESTAMP` is an instant, stored as microseconds since the epoch in UTC and displayed in the session time zone. `TIMESTAMP_NTZ` is a wall-clock value with no time zone that is never converted.

**2. How do you handle dates that arrive in several formats?**

Parse each format with `try_to_timestamp` and take the first success with `coalesce`, then cast to date. Count the rows that are still null and route them to a quarantine table.

**3. What does the session time zone affect?**

How timestamps are displayed, and how strings without an explicit offset are parsed into timestamps. It doesn't change the stored instant. Pipelines should set it explicitly, usually to UTC.

**4. How do you compute the local business date for global data?**

Keep the timestamp in UTC, convert with `from_utc_timestamp(ts, 'Region/City')` and then take `to_date`. Use region IDs so daylight saving time is handled.

**5. What is the difference between `date_trunc` and `date_format`?**

`date_trunc` returns a timestamp rounded down to a unit such as a month, which is good for grouping and joins. `date_format` returns a string for display.

**6. How do you calculate the duration between two timestamps in minutes?**

`(unix_timestamp(end) - unix_timestamp(start)) / 60`, or `timestampdiff(MINUTE, start, end)` for whole minutes.

**7. Why can `WHERE year(order_date) = 2025` be slower than `WHERE order_date >= '2025-01-01' AND order_date < '2026-01-01'`?**

The range filter on the raw column can be pushed down to the scan and compared with file min/max statistics, so files outside the range are skipped. The function version usually can't be pushed down, so every file is read and filtered afterwards. Filters on partition columns are the exception, because they are evaluated against partition values.

### 16_null_handling

**1. How does Spark treat null in comparisons?**

It follows SQL three-valued logic. Any comparison with null returns null, which filters treat as not true. `` (`eqNullSafe`) is the null-safe equality, which returns true for null versus null.

**2. How do aggregate functions handle nulls?**

`sum`, `avg`, `min`, `max` and `count(col)` ignore nulls. `count(*)` counts all rows. So `avg` is the average of the known values, which may not be what the business wants.

**3. What is the difference between `na.fill` and `coalesce`?**

`na.fill` replaces nulls with constants, per column or by type. `coalesce` is an expression that returns the first non-null of several columns or values, so it can fall back to other columns, not just constants.

**4. What happens to null keys in a join?**

They never match with `=`, so they drop out of inner joins and get null partners in outer joins. Use `eqNullSafe` if nulls should match, but usually null keys are a data quality issue to fix.

**5. Why does `NOT IN` with a null in the list return no rows?**

`x NOT IN (a, NULL)` means `x <> a AND x <> NULL`, and `x <> NULL` is null, so the whole condition is null or false and never true. `NOT EXISTS` or an anti join avoids this.

**6. How do you count nulls in every column efficiently?**

One `select` with `count(when(col(c).isNull(), 1))` for each column. That is a single pass over the data, instead of one job per column.

**7. How do you avoid division by zero under ANSI mode?**

`try_divide(a, b)` returns null, as does `a / nullif(b, 0)`.

### 17_joins

**1. Explain the different join types in Spark.**

Inner keeps matches only. Left, right and full outer keep all rows from the left, right or both sides with nulls where there is no match. Left semi returns left rows that have a match, with left columns only. Left anti returns left rows with no match. Cross returns every combination.

**2. What is the difference between a left semi join and an inner join?**

A semi join returns only the left table's columns, and each left row appears at most once no matter how many matches it has. An inner join returns columns from both sides and repeats left rows for every match.

**3. How does a broadcast hash join work and when is it used?**

The smaller table is collected and copied to every executor, where it is put in a hash table. The large table is then joined partition by partition without being shuffled. Spark uses it automatically when a side is below `autoBroadcastJoinThreshold` (10 MB by default), when AQE detects a small side at runtime, or when you add a broadcast hint.

**4. How does a sort-merge join work?**

Both sides are shuffled by the join key so matching keys end up in the same partition. Each partition is sorted by key, and then the two sorted streams are merged. It is the default for large equi-joins because it scales and can spill to disk.

**5. Why might a join return more rows than the left table has?**

Because the right side has duplicate keys. Each left row is repeated once per matching right row. Deduplicate or aggregate the right side first.

**6. Why do rows disappear even with matching IDs?**

Common causes are null keys (null never equals null), type differences, leading zeros, whitespace or case differences. A left anti join shows exactly which keys failed to match.

**7. What is the difference between putting a condition in the ON clause and in WHERE for a left join?**

In the ON clause, it only affects which right rows match, and all left rows are kept. In WHERE, it runs after the join and removes left rows whose right side is null, which turns the left join into an inner join.

**8. How do you find records that exist in one table but not in another?**

A left anti join, or `NOT EXISTS` in SQL. Avoid `NOT IN` when the subquery can contain nulls.

### 18_union

**1. What is the difference between `union` and `unionByName`?**

`union` matches columns by position and ignores names. `unionByName` matches by name, and with `allowMissingColumns=True` it fills missing columns with nulls. I use `unionByName` whenever the inputs come from different sources.

**2. Does `union` remove duplicates?**

No. DataFrame `union` behaves like SQL `UNION ALL`. Use `.distinct()` to get SQL `UNION` semantics.

**3. Does `union` cause a shuffle?**

No. It is a narrow transformation that just concatenates the partitions of both inputs. Only a following `distinct` would shuffle.

**4. How do you combine a list of DataFrames?**

`functools.reduce(lambda a, b: a.unionByName(b), dfs)`. If they come from files, a single `spark.read` on all the paths is better.

**5. What is the difference between `subtract` and `exceptAll`?**

`subtract` returns distinct rows from the first DataFrame that aren't in the second, like `EXCEPT DISTINCT`. `exceptAll` keeps duplicates, so it respects how many times each row appears.

### 19_window_functions

**1. What is a window function and how is it different from `groupBy`?**

It computes a value for each row using a set of related rows, defined by partition, order and frame. `groupBy` collapses each group to one row, while a window function keeps all rows and adds the computed value next to them.

**2. What is the difference between `row_number`, `rank` and `dense_rank`?**

For ties: `row_number` always gives unique numbers (1, 2, 3, 4), `rank` gives tied rows the same number and skips the next ones (1, 2, 2, 4), and `dense_rank` gives tied rows the same number without gaps (1, 2, 2, 3).

**3. How do you get the top 3 products per category?**

`dense_rank` or `row_number` over `Window.partitionBy("category").orderBy(desc("sales"))`, then filter where the rank is at most 3. `row_number` gives exactly 3, `dense_rank` includes ties. In Databricks SQL I can use `QUALIFY`.

**4. How do you keep only the latest record per key?**

`row_number()` over a window partitioned by the key and ordered by the timestamp descending with a tie-breaker, then filter where it equals 1.

**5. What is the default window frame?**

With `orderBy` and no frame, it is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. Without `orderBy`, it is the whole partition. That's why `last()` with only `orderBy` returns the current row.

**6. What is the difference between `rowsBetween` and `rangeBetween`?**

`rowsBetween` counts physical rows before and after the current row. `rangeBetween` uses the values of the order column, so all rows within a value range are included, which handles ties and missing periods.

**7. How does Spark execute a window function?**

It shuffles the data by the partition columns, sorts each partition by the order columns, then computes the function in one pass. Windows with the same spec share the shuffle. A window without `partitionBy` moves all data to a single partition.

**8. How do you compute month-over-month growth?**

`lag("amount").over(Window.partitionBy("customer").orderBy("month"))`, then `(amount - prev) / prev`. The first month has no previous value, so it's null unless I give `lag` a default.

### 20_udfs

**1. Why should you avoid Python UDFs in PySpark?**

Every row must be serialized from the JVM to a Python worker and back, which is expensive. The optimizer also treats the UDF as a black box, so it can't push filters through it, can't include it in whole-stage code generation, and has no statistics about it. Built-in functions avoid all of this.

**2. What is a pandas UDF and why is it faster than a regular UDF?**

A vectorized UDF. Spark sends data in Apache Arrow batches, and the function processes a whole pandas Series at once with vectorized operations. That removes the per-row serialization and Python call overhead.

**3. When is a UDF still the right choice?**

When the logic can't be expressed with built-ins or SQL, for example calling a Python library for parsing, validation, encryption, or ML model inference. Then I prefer a pandas UDF and I filter the data first so fewer rows reach it.

**4. What happens if a UDF returns a different type than declared?**

For classic Python UDFs, the values may silently become null. The default return type is string. Arrow-optimized UDFs try to convert the value and raise an error if they can't.

**5. How do you use a Python UDF in SQL?**

Register it with `spark.udf.register("name", func)`. For logic that can be written in SQL, a SQL UDF (`CREATE FUNCTION ... RETURN expr`) is better, because it is inlined and runs at built-in speed. In Unity Catalog it can also be permanent and governed.

**6. What is an Arrow-optimized Python UDF?**

A regular row-at-a-time Python UDF (`useArrow=True`) that uses Arrow instead of pickle to move data between the JVM and Python. It is faster than a classic UDF and has stricter type handling, but slower than a pandas UDF.

**7. How do you spot a UDF in a query plan?**

Look for `BatchEvalPython` (classic Python UDF) or `ArrowEvalPython` (Arrow or pandas UDF) nodes. They break the whole-stage codegen stage.

### 21_reading_csv

**1. How do you read a CSV file in Spark, and which options matter most?**

`spark.read.format("csv")` with `header`, an explicit `schema`, `sep`, `mode`, `nullValue`, `dateFormat`, and `multiLine`/`quote`/`escape` for messy text. In production I always provide a schema.

**2. Why avoid `inferSchema` in production?**

It needs an extra pass over the data, so it's slow on large files. It can infer the wrong type (for example a string because of one `NA`), and the schema can change between runs when the data changes, which breaks downstream code.

**3. What are the CSV read modes?**

`PERMISSIVE` (default) keeps malformed rows with nulls and can store the raw line in a corrupt-record column. `DROPMALFORMED` silently drops them. `FAILFAST` raises an error on the first bad row.

**4. How do you handle bad records without failing the pipeline?**

Read in `PERMISSIVE` mode with `columnNameOfCorruptRecord` in the schema, land the result in a Bronze table, then split good and bad rows: good rows continue, bad rows go to a quarantine table with a timestamp, and I monitor the bad-row rate. On Databricks, `badRecordsPath` or the rescued data column are alternatives.

**5. How do you know which file a row came from?**

The hidden `_metadata` column, for example `_metadata.file_path` or `file_name`, plus `file_modification_time`. I store it in Bronze for lineage.

**6. How does Spark parallelize reading CSV?**

It splits files into chunks of about 128 MB, with one task per chunk. Files with `multiLine=True` or gzip compression can't be split, so each one is read by a single task.

### 22_reading_json

**1. How do you read multi-line JSON in Spark?**

With `option("multiLine", True)`. By default Spark expects JSON Lines, one object per line. Multi-line files can't be split, so each file is processed by one task.

**2. What is the difference between `explode` and `explode_outer`?**

Both create one row per array element. `explode` drops rows where the array is null or empty, while `explode_outer` keeps them with a null element.

**3. How do you flatten a nested JSON structure?**

Use dot notation or `struct.*` for nested objects, and `explode` or `posexplode` for arrays, usually producing separate tables for parent and child records linked by a key.

**4. How do you parse a JSON string stored in a column?**

`from_json(col, schema)` returns a typed struct. `get_json_object(col, '$.path')` extracts a single value as a string. `schema_of_json` helps derive the schema from a sample.

**5. How can you work with arrays without exploding them?**

Higher-order functions such as `transform`, `filter`, `exists`, `aggregate` and `array_contains` operate on the array inside each row, which avoids multiplying rows and re-aggregating.

**6. Why provide a schema when reading JSON?**

Inference needs an extra pass, can mis-type fields (for example `long` vs `decimal`), and changes when the data changes. A schema is faster and makes the contract explicit.

### 23_reading_parquet

**1. Why is Parquet better than CSV for analytics?**

It is columnar, so queries read only the columns they need. It stores the schema and types, so there's no inference. It keeps min/max statistics per row group, so filters can skip data. And it compresses much better because similar values are stored together.

**2. What is column pruning?**

The optimizer passes the list of required columns down to the reader. With columnar formats like Parquet, only those column chunks are read from storage.

**3. What is predicate pushdown in Parquet?**

Filters are passed to the Parquet reader, which compares them with each row group's min/max statistics and skips row groups that can't contain matching rows.

**4. What is a row group?**

A horizontal slice of a Parquet file, holding one column chunk per column plus statistics. It is the unit of skipping and the smallest unit a reader task works on.

**5. What does `mergeSchema` do, and why is it off by default?**

It reads the schemas of all files and combines them, so columns that exist only in some files are included. It is off by default because reading every footer is expensive on large datasets.

**6. How does Delta Lake relate to Parquet?**

Delta stores data as Parquet files and adds a transaction log (`_delta_log`) that records which files make up each table version. That gives ACID transactions, updates and deletes, schema enforcement, time travel and file-level statistics for data skipping.

### 24_writing_data

**1. What are the save modes in Spark?**

`errorifexists` (the default) fails if the target exists, `append` adds data, `overwrite` replaces it, and `ignore` does nothing if the target exists.

**2. What is the difference between `save(path)` and `saveAsTable(name)`?**

`save` writes files to a location only. `saveAsTable` writes the data and registers a table in the metastore or Unity Catalog, so it can be queried by name and governed. On Databricks, `saveAsTable` creates a managed Delta table by default.

**3. Why does Spark produce many small files, and how do you fix it?**

Each task writes its own file, so the file count follows the number of DataFrame partitions (times the output partitions). Fixes: `coalesce` or `repartition` before writing, `maxRecordsPerFile`, and on Delta, `OPTIMIZE` or auto-compaction and optimized writes.

**4. How do you make a daily batch write idempotent?**

Overwrite only the data for that day, with dynamic partition overwrite or Delta's `replaceWhere`, or use `MERGE` on a key. A plain `append` duplicates data when the job re-runs.

**5. What is the risk of `insertInto`?**

It matches columns by position, not by name, so a different column order puts values in the wrong columns or fails. Name-based appends are safer.

**6. Is a write a transformation or an action?**

An action. It triggers a job immediately.

**7. What is the difference between `coalesce(1)` and `repartition(1)` before writing?**

Both produce one output file. `coalesce(1)` avoids a shuffle but can push all upstream work into a single task. `repartition(1)` adds a shuffle but keeps the upstream work parallel.

### 25_partitioning_files

**1. What is partitioning in Spark storage, and why use it?**

`partitionBy` writes data into folders named after column values, like `country=IN/`. Queries that filter on those columns read only the matching folders (partition pruning), which reduces IO dramatically.

**2. How do you choose a partition column?**

A low-cardinality column that most queries filter on, typically a date, that produces large partitions (around 1 GB or more each). Never an ID or timestamp. For tables under about 1 TB, Databricks recommends not partitioning at all and using liquid clustering.

**3. What is the difference between partition pruning and predicate pushdown?**

Partition pruning skips whole folders using partition values in the folder names, at planning time. Predicate pushdown passes filters on regular columns to the file reader, which uses file or row-group statistics to skip data inside the selected files.

**4. What is the small-files problem and how does partitioning cause it?**

Each task writes a file per partition folder it touches. With high-cardinality partitions or many tasks, you get huge numbers of tiny files, and listing and opening them dominates query time. Fix it with coarser partitions, repartitioning by the partition column before writing, compaction (`OPTIMIZE`), or clustering instead of partitioning.

**5. What is the difference between `repartition` and `partitionBy`?**

`repartition` changes how rows are split across tasks in memory during the job. `partitionBy` controls the folder layout of the output on storage.

**6. What is bucketing, and is it used on Databricks?**

Bucketing hashes rows into a fixed number of files by key, so joins and aggregations on that key can avoid a shuffle. It works for Hive-format tables, but isn't supported for Delta or Unity Catalog. On Databricks you use liquid clustering, Z-ordering and AQE instead.

**7. What is liquid clustering?**

A Delta Lake layout feature (`CLUSTER BY`) that clusters data files by chosen columns without folder partitions. Keys can be changed without rewriting the table, and it works well for high-cardinality columns. Databricks recommends it for most new tables.

**8. What is dynamic partition pruning?**

When a partitioned table is joined to a filtered dimension, Spark uses the dimension's join keys at runtime to prune partitions of the fact table, even though the filter isn't directly on the fact table.

### 26_spark_sql

**1. Is Spark SQL slower or faster than the DataFrame API?**

Neither. Both are parsed into a logical plan and optimized by Catalyst into the same physical plan, so the same logic performs the same. The choice is about readability and maintainability.

**2. How do you run SQL on a DataFrame?**

Register it with `createOrReplaceTempView("name")` and query the view with `spark.sql`, or pass it directly with `spark.sql("SELECT ... FROM {df}", df=df)`.

**3. What is a CTE and does it improve performance?**

A named subquery defined with `WITH`. It improves readability. Spark normally inlines CTEs into the plan, so it isn't materialized or faster by itself.

**4. How does Spark execute an `EXISTS` or `IN` subquery?**

The optimizer rewrites it as a left semi join, and `NOT EXISTS` as a left anti join.

**5. How do you pass parameters to Spark SQL safely?**

With named parameter markers, such as `:name` and `args={"name": value}`, and `IDENTIFIER(:tbl)` for table or column names. Never format user values into the SQL string, because that breaks on quotes and allows SQL injection.

**6. Is `spark.sql` lazy?**

For queries, yes: it returns a DataFrame that runs on an action. DDL and DML statements such as `CREATE TABLE`, `INSERT` or `MERGE` execute immediately.

### 27_temporary_views

**1. What is the difference between a temp view and a global temp view?**

A temp view is visible only in the Spark session that created it and disappears when the session ends. A global temp view is shared across sessions of the same Spark application (cluster), lives in the `global_temp` schema, and disappears when the application stops.

**2. What is the difference between a view and a table?**

A table stores data. A view stores a query, which runs again every time the view is queried, so it always reflects current data and costs compute on each read.

**3. Does creating a temp view cache the data?**

No. It only registers the logical plan under a name. The query runs when the view is used.

**4. Why can a temp view cause a job to fail even though the notebook worked interactively?**

Each job task has its own Spark session, so a temp view from another task or notebook doesn't exist there. Shared intermediate results should be written as tables.

**5. What is a materialized view?**

A view whose results are precomputed and stored, then refreshed (incrementally when possible). Reads are fast like a table, and the logic stays declarative like a view. On Databricks they are managed by Lakeflow Declarative Pipelines or SQL warehouses.

**6. Can a permanent view reference a temp view?**

No. A permanent view is stored in the catalog and can be queried by others, so it can only depend on permanent objects.

### 28_error_handling

**1. When do errors occur in a Spark program?**

Analysis errors (missing tables or columns, type mismatches, syntax) occur when Spark resolves the plan. Execution errors (bad casts under ANSI, division by zero, corrupt files, out of memory) occur only when an action runs the job, because of lazy evaluation.

**2. How do you catch a specific Spark error in PySpark?**

Catch `AnalysisException` or the base `PySparkException` from `pyspark.errors`, and branch on `e.getCondition()` (the error class) or `e.getSqlState()` instead of the message text.

**3. How do you stop one bad row from failing a whole job?**

Use the `try_*` functions such as `try_cast` and `try_divide`, which return null instead of failing, then count and quarantine those rows. For files, use `PERMISSIVE` mode with a corrupt-record column.

**4. Should a pipeline ever swallow exceptions?**

No. It should log the error with context and re-raise, so the job is marked failed and alerts fire. It can handle expected, recoverable cases explicitly, for example a retry of a transient error or quarantining bad rows below a threshold.

**5. How do you implement retries correctly?**

Retry only transient failures (timeouts, throttling), with a maximum number of attempts and exponential backoff. Logic or data errors are not retried. On Databricks, job tasks also have built-in retry settings.

**6. Why prefer logging over print in pipelines?**

Logs carry a timestamp, level and source, can be filtered and collected by the job's log system, and give consistent, searchable output.

### 29_data_quality_checks

**1. What data quality checks would you put in a pipeline?**

Completeness (required columns not null), uniqueness of keys, validity (allowed values and formats), ranges, referential integrity against dimension tables, freshness, volume compared with history, and schema against a contract.

**2. What do you do with rows that fail a check?**

It depends on severity. Critical failures such as duplicate keys or a broken schema stop the pipeline. Row-level problems go to a quarantine table with the reason, so good rows continue and bad ones can be fixed and replayed. Minor drift raises a warning.

**3. How do you make data quality checks efficient on big data?**

Express rules as column expressions and evaluate them all in one aggregation, instead of one job per check. Flag rows once with a reasons column, then split good and bad rows from that.

**4. What is the difference between a Delta constraint and a pipeline check?**

A Delta constraint (`CHECK`, `NOT NULL`) is enforced by the table on every write, by any writer, and rejects the whole transaction if a row violates it. A pipeline check is code you run, which can warn, quarantine or fail with more flexible logic.

**5. What are expectations in Lakeflow Declarative Pipelines?**

Declarative data quality rules on pipeline datasets, with three actions: keep and record violations (warn), drop violating rows, or fail the update. Results are recorded in the pipeline's event log.

**6. How do you check freshness?**

Compare the maximum event or ingestion timestamp with the current time and alert if it is older than the agreed SLA.

### 30_building_an_etl_pipeline

**1. Walk me through the medallion architecture.**

Bronze stores raw data as received, plus audit columns such as source file and load time, so it can be replayed. Silver holds cleaned, typed, deduplicated and validated data, one row per entity, often enriched with dimensions. Gold holds business-level aggregates and marts for reporting. Each layer is built from the previous one.

**2. How do you make a batch pipeline idempotent?**

Make every write replace exactly the data of the batch it processes: dynamic partition overwrite or `replaceWhere` per batch date, or `MERGE` on a business key. Then re-running a batch produces the same result instead of duplicates. I test it by running the pipeline twice and comparing outputs.

**3. How do you handle bad records without failing the whole pipeline?**

Land everything in Bronze as strings with a corrupt-record column, convert in Silver with `try_*` functions, attach reasons to rows that break rules, write them to a quarantine table, and fail the run only if the bad-row ratio exceeds a threshold.

**4. How do you deduplicate in Silver?**

Define the business key and an ordering that identifies the latest version (ingestion date, source file or an update timestamp), then keep `row_number() == 1` per key.

**5. How do you prove the pipeline didn't lose data?**

Reconciliation: Bronze rows must equal Silver rows plus quarantined rows plus removed duplicates, and Gold totals must match Silver totals. The run fails if they don't.

**6. What would you change to run this on large, daily-growing data?**

Ingest incrementally with Auto Loader, upsert Silver with `MERGE`, partition or cluster tables by date, orchestrate the layers as tasks in a Lakeflow Job with retries and alerts, and move the functions into a tested Python package.
