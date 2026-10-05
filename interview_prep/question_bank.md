# Question Bank

Interview questions from every lesson, with short spoken-style answers.
Practise by covering the answer, saying yours out loud, then comparing.

**530 questions** across 80 lessons.

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

## 02 Spark internals

### 01_driver_executors

**1. Explain the Spark architecture.**

A Spark application has one driver and many executors. The driver runs the main program, builds the plan, splits it into jobs, stages and tasks, and schedules the tasks. Executors run on worker nodes, execute tasks in parallel on their cores, and hold shuffle data and cached blocks. A cluster manager such as YARN, Kubernetes or Databricks allocates the executor resources.

**2. What does the driver do?**

It holds the SparkSession, analyzes and optimizes the query, creates the DAG of stages, schedules tasks on executors, tracks their progress, retries failures, and receives results of actions such as `collect`.

**3. What is an executor?**

A JVM process on a worker node that runs tasks for one application. It has a fixed number of cores, which are task slots, and memory for execution, shuffle and caching.

**4. How are cores, partitions and tasks related?**

Each task processes one partition on one core. The number of tasks in a stage equals the number of partitions, and the number of tasks running at once is limited by the total executor cores.

**5. What happens if an executor fails?**

The driver reschedules its tasks on other executors. Lost shuffle or cached data is recomputed from the lineage. If the driver fails, the whole application fails.

**6. Where does a Python UDF run?**

On the executors, in Python worker processes started next to each executor. The function is serialized on the driver and shipped with the tasks.

**7. What is Spark Connect?**

A client-server architecture where the client sends logical plans over gRPC to a remote Spark driver and receives results as Arrow batches. Databricks serverless notebooks use it, so there is no local `sparkContext`.

### 02_jobs_stages_tasks

**1. What is the difference between a job, a stage and a task?**

A job is created for each action. It's split into stages at shuffle boundaries, where each stage is a set of narrow transformations that can run without moving data. Each stage runs as tasks, one per partition, and each task runs on one core.

**2. What creates a new stage?**

A shuffle, which is an `Exchange` in the physical plan. Operations such as `groupBy`, `join` (non-broadcast), `distinct`, `repartition` and `orderBy` need one.

**3. How many tasks does a stage have?**

One per partition. The first stage has one task per input split, and a stage after a shuffle has one per shuffle partition, which AQE may coalesce.

**4. What happens when there are more tasks than cores?**

Tasks run in waves. Each core takes the next task when it finishes one, and the stage ends when the slowest task finishes.

**5. Why might calling `count()` and then `show()` be slow?**

Each action is a separate job that recomputes the plan from the source, unless the data is cached or materialized.

**6. What is a skipped stage?**

A stage whose shuffle output already exists from a previous job, so Spark reuses it instead of recomputing it.

### 03_transformations_actions

**1. What is the difference between a transformation and an action?**

A transformation describes a new DataFrame and is lazy: Spark only adds it to the plan. An action asks for a result, such as returning rows or writing data, which triggers optimization and execution of the whole plan as a job.

**2. Give examples of narrow and wide transformations.**

Narrow: `select`, `filter`, `withColumn`, `union`, `coalesce`, which don't move data between partitions. Wide: `groupBy`, `join`, `distinct`, `orderBy`, `repartition`, which need a shuffle.

**3. Is `show()` an action?**

Yes. It runs a job to compute and fetch the first rows.

**4. Is `cache()` an action?**

No. It's lazy: it marks the DataFrame for caching, and the next action materializes it. On Databricks serverless it isn't supported.

**5. Is `printSchema()` an action?**

No. It only reads the analyzed plan's schema, so no job runs.

**6. Can `spark.read` trigger a job?**

Yes. Reading with schema inference (CSV `inferSchema`, or JSON without a schema) runs a job immediately to sample the data. With an explicit schema it is lazy.

### 04_lazy_evaluation

**1. What is lazy evaluation in Spark?**

Transformations aren't executed when they're called. Spark records them in a logical plan, and only when an action is called does it optimize the whole plan and execute it.

**2. Why is Spark lazy? What are the benefits?**

Seeing the whole query lets the optimizer push filters down, prune unused columns, combine consecutive operations into one pass, choose join strategies, and stop early for `limit`. It also avoids computing anything that is never used.

**3. What are the downsides of lazy evaluation?**

Each action recomputes the plan from the source unless the result is materialized, and errors appear at the action rather than where they were caused, which makes debugging harder.

**4. How can you prove Spark is lazy?**

Time the definition of transformations (instant) against the action, or create a DataFrame whose execution would fail, such as dividing by zero, and show that defining it and printing its schema work while the action fails.

**5. Can two actions on the same DataFrame return different results?**

Yes, if the plan contains non-deterministic functions such as `uuid()`, because each action recomputes them. Materialize the result to make it stable. `rand()` gets its seed when the expression is created, so it repeats within the same DataFrame but changes when the DataFrame is rebuilt without a seed.

### 05_dag_and_query_plans

**1. What are the stages of query planning in Spark?**

Parsing produces an unresolved logical plan. The analyzer resolves names and types against the catalog. The Catalyst optimizer applies rule-based (and some cost-based) optimizations to produce an optimized logical plan. The planner turns that into a physical plan with concrete operators, and whole-stage code generation compiles parts of it. AQE can then re-optimize at runtime.

**2. How do you read a physical plan?**

Bottom-up, from the scans to the result. I check the scans for `ReadSchema`, `PushedFilters` and `PartitionFilters`, count the `Exchange` operators to see the shuffles and stages, and check which join strategy was chosen.

**3. What does `Exchange` mean in a plan?**

A shuffle: data is redistributed between partitions, for example `hashpartitioning` for a groupBy or join, or `rangepartitioning` for a sort. Each exchange is a stage boundary.

**4. What does the `*(1)` prefix mean?**

The operator is part of whole-stage code generation stage 1: those operators are fused into one generated Java function that processes rows in a single loop.

**5. What is the difference between the logical and the physical plan?**

The logical plan describes **what** to compute (relational operations). The physical plan describes **how**: which join algorithm, which aggregation strategy, where to shuffle.

**6. What is a DAG in Spark?**

The directed acyclic graph of stages that the DAG scheduler builds from the physical plan, split at shuffle boundaries, with edges showing which stage's output feeds the next.

### 06_narrow_wide_transformations

**1. What is the difference between narrow and wide transformations?**

In a narrow transformation each output partition depends on one input partition, so there's no data movement and steps are pipelined in one stage. In a wide transformation an output partition depends on many input partitions, so data must be shuffled across the cluster and a new stage starts.

**2. Give examples of each.**

Narrow: `select`, `filter`, `withColumn`, `union`, `coalesce`, `explode`. Wide: `groupBy`, `join` (non-broadcast), `distinct`, `orderBy`, `repartition`, window functions with `partitionBy`.

**3. Is `coalesce` narrow or wide? And `repartition`?**

`coalesce` is narrow, because it merges existing partitions without a shuffle. `repartition` is wide, because it shuffles every row to create new, balanced partitions.

**4. How can a join avoid a shuffle?**

By broadcasting the small side, so the big side is joined partition by partition without moving. Or if both sides are already partitioned by the join key, for example after a repartition or with bucketing on classic Hive tables.

**5. Why do wide transformations affect fault tolerance?**

A lost partition after a shuffle depends on all parent partitions. Spark keeps shuffle files so it doesn't recompute everything, but if those files are lost with an executor, the map tasks must be re-run.

### 07_shuffle

**1. What is a shuffle?**

The redistribution of data across partitions so that rows with the same key end up in the same partition. It's needed by wide transformations such as `groupBy`, `join`, `distinct` and `orderBy`, and it creates a stage boundary.

**2. How does a shuffle work internally?**

Each map task computes the target partition for every row, buffers and sorts by partition, and writes a data file and an index file to local disk. After all map tasks finish, each reduce task fetches its blocks from every map output over the network, merges them, and continues processing.

**3. Why is a shuffle expensive?**

It serializes data, writes it to disk, transfers it over the network, reads and deserializes it again, uses memory that can cause spill, and forces a barrier between stages.

**4. How do you reduce shuffle cost?**

Filter and select early, broadcast small join sides, avoid unnecessary repartition, orderBy and distinct, rely on partial aggregation, choose a sensible number of shuffle partitions, and handle skewed keys.

**5. What does `spark.sql.shuffle.partitions` control?**

The number of partitions after a shuffle in DataFrame and SQL operations, 200 by default. With AQE, Spark coalesces small partitions at runtime, so the actual number is often lower.

**6. What is spill?**

When a task's data doesn't fit in its execution memory, Spark writes intermediate data to disk and merges it later. It's slower and usually means partitions are too large or skewed.

### 08_partitioning_and_parallelism

**1. How are partitions, cores and tasks related?**

Each partition is processed by one task, and each task runs on one core. The number of partitions sets how many tasks a stage has, and the number of cores sets how many run at once.

**2. What is the difference between `repartition` and `coalesce`?**

`repartition` does a full shuffle and produces evenly sized partitions, and it can increase or decrease the count. `coalesce` only decreases the count by merging existing partitions without a shuffle, which is cheaper but can leave uneven partitions and can pull upstream work into fewer tasks.

**3. How does Spark decide the number of partitions when reading files?**

It splits large splittable files into chunks of `spark.sql.files.maxPartitionBytes` (128 MB by default) and packs small files together, counting an open cost per file. Non-splittable files such as gzip are read whole by one task.

**4. How many partitions should a job have?**

Enough to keep partitions around 100–200 MB and to have at least 2–3 times as many tasks as cores. Then I check sizes for skew. With AQE, Spark coalesces shuffle partitions automatically.

**5. When would you use `repartition` by a column?**

To co-locate rows with the same key before several operations on that key, or before `partitionBy` writes, so each output folder gets a small number of files.

**6. What does `repartitionByRange` do?**

It samples the data to choose boundaries and puts rows into partitions by ranges of the column, so each partition holds a contiguous, sorted range. It's useful before writing data that will be filtered by that column.

### 09_broadcast_and_join_strategies

**1. Broadcast join vs sort-merge join?**

A broadcast hash join sends a copy of the small table to every executor, so the large table is joined in place with no shuffle. It's very fast, but only if the small side fits in memory. A sort-merge join shuffles both sides by the join key, sorts them, and merges them. It scales to any size, but pays for two shuffles and sorts. Spark broadcasts automatically below `autoBroadcastJoinThreshold` (10 MB), or when hinted, or when AQE detects a small side at runtime.

**2. What join strategies does Spark have?**

Broadcast hash, sort-merge, shuffled hash, broadcast nested loop, and cartesian product. The first three need an equi-join condition. The last two handle non-equi conditions.

**3. How do you force a broadcast join?**

With `F.broadcast(df)` or `df.hint("broadcast")` in PySpark, or `/*+ BROADCAST(t) */` in SQL. Then I verify `BroadcastHashJoin` in the plan.

**4. When should you not broadcast?**

When the small side is large (hundreds of MB to GB), because it's collected on the driver and copied to every executor. Also, the preserved side of an outer join can't be broadcast.

**5. How does AQE affect join strategy?**

After the shuffle stages run, AQE knows the real sizes. It can convert a planned sort-merge join into a broadcast join if one side turns out small, and split skewed partitions in sort-merge joins.

**6. What happens with a join on a `<` or `between` condition?**

Spark can't use hash or sort-merge, so it uses a broadcast nested loop join if one side is small, or a cartesian product otherwise, which compares every pair and can be extremely slow.

### 10_caching_persistence

**1. What is the difference between `cache()` and `persist()`?**

`cache()` is `persist()` with the default storage level, which is `MEMORY_AND_DISK` for DataFrames. `persist()` lets you choose a level, such as `MEMORY_ONLY`, `DISK_ONLY` or a replicated variant.

**2. Is `cache()` an action?**

No, it's lazy. It marks the DataFrame, and the next action computes and stores it.

**3. When should you cache?**

When an expensive DataFrame is reused by several actions, for example in iterative algorithms or when many outputs come from one joined dataset, and it fits comfortably in cluster memory.

**4. When should you not cache?**

When the data is used once, is cheap to recompute, is too large for memory, or must reflect changing sources. And always unpersist when finished.

**5. What happens to cached data if an executor fails?**

Its cached partitions are lost and Spark recomputes them from the lineage the next time they're needed, unless a replicated storage level kept a copy elsewhere.

**6. How do you handle reuse on Databricks serverless, where caching isn't supported?**

Write the intermediate result to a Delta table and read it back. Repeated reads benefit from the automatic disk cache, and the table can be shared across tasks and sessions.

**7. What is the Databricks disk cache?**

An automatic cache that stores copies of remote Parquet and Delta files on the workers' local SSDs, so repeated reads avoid cloud storage. It validates files, so it doesn't serve stale data.

### 11_serialization

**1. Where does serialization happen in Spark?**

When tasks and their closures are shipped to executors, when data is shuffled or cached, when data moves between the JVM and Python (UDFs, `toPandas`, `createDataFrame` from pandas), and when results are returned to the driver or client.

**2. What is the difference between Java serialization and Kryo?**

Java serialization works for any `Serializable` class but is slow and produces large output. Kryo is faster and more compact, especially with registered classes. It mainly matters for RDDs of objects. DataFrames use Tungsten's binary format instead.

**3. Why do DataFrames serialize more efficiently than RDDs?**

Because the schema is known, rows are stored in Tungsten's compact binary format and can be shuffled, cached, hashed and compared without generic object serialization.

**4. Why is a Python UDF slow, from a serialization point of view?**

Every row is serialized from the JVM to a Python worker and the results are serialized back. Classic UDFs use pickle row by row. pandas and Arrow UDFs move columnar Arrow batches, which is much cheaper.

**5. What causes `PicklingError: Could not serialize object`?**

A function sent to executors references an object that can't be pickled, such as a lock, a database connection, a file handle or the SparkSession. Create those objects inside the function or once per partition.

**6. How do you share a large lookup table with executors?**

Put it in a DataFrame and join, letting Spark broadcast it if it's small. On classic compute, broadcast variables are another option, but they aren't available with Spark Connect.

### 12_catalyst_and_tungsten

**1. What is the Catalyst optimizer?**

Spark SQL's extensible query optimizer. It analyzes a query against the catalog, applies rule-based optimizations such as predicate pushdown, column pruning, constant folding and combining filters, uses statistics for cost-based choices like join strategy, and produces a physical plan.

**2. What are the phases of Catalyst?**

Analysis (resolve names and types), logical optimization (rule-based rewrites), physical planning (choose operators, with cost-based decisions), and code generation for execution.

**3. What is Tungsten?**

Spark's execution engine work focused on CPU and memory efficiency: a compact binary row format, off-heap memory management, whole-stage code generation that fuses operators into a single function, and vectorized columnar reads.

**4. What is whole-stage code generation?**

Spark compiles a chain of operators within a stage into one generated Java function with a tight loop, avoiding per-row virtual calls between operators. In plans, operators in the same generated function share a `*(n)` prefix.

**5. Why are DataFrames faster than RDDs?**

DataFrames have a schema, so Catalyst can optimize the whole query and Tungsten can store rows in a compact binary format and generate efficient code. RDD operations are opaque functions over objects, executed as written, with object serialization overhead.

**6. Why can't Catalyst optimize UDFs?**

A UDF is a black box: Catalyst doesn't know its logic, so it can't push it down, fold it, combine it or include it in code generation.

**7. What is Photon?**

Databricks' native, vectorized query engine written in C++. It executes SQL and DataFrame operators faster than the JVM engine without code changes, and it's used by serverless compute and SQL warehouses.

### 13_adaptive_query_execution

**1. What is Adaptive Query Execution?**

A Spark 3 feature that re-optimizes the physical plan at runtime using real statistics from completed shuffle stages, instead of relying only on estimates made before execution.

**2. What are the main AQE optimizations?**

Coalescing small shuffle partitions into fewer, larger ones; switching a sort-merge join to a broadcast hash join when a side turns out small; and splitting skewed partitions in sort-merge joins.

**3. How does AQE detect a skewed partition?**

A partition is skewed if it's larger than a factor (5 by default) times the median partition size and also larger than a threshold (256 MB by default). AQE then splits it and replicates the matching data from the other side.

**4. Why does `explain()` show `isFinalPlan=false`?**

Because the plan can still change at runtime. The final adaptive plan is visible in the Spark UI's SQL tab or the Databricks query profile after the query runs.

**5. What can't AQE fix?**

Problems before the first shuffle (such as file-read partitioning or a single huge file), skew in aggregations, poor data layout, and inefficient code such as Python UDFs.

**6. Do you still need to tune `spark.sql.shuffle.partitions` with AQE?**

Much less. AQE coalesces small partitions, so a reasonably high value works well. For very large shuffles you may still raise it, so the initial partitions aren't too big before coalescing.

### 14_spark_ui

**1. A Spark job is slow. How do you debug it?**

I find the slowest job and stage in the Spark UI or query profile. Then I check the task distribution in that stage: if the max is far above the median, it's skew. Then shuffle read/write and spill: large shuffles mean too much data moved, and spill means partitions are too big. Then task count against cores, for under- or over-partitioning. Then the SQL plan: join strategy, pushed filters, and rows per operator. And finally executor health, such as GC time and failures. Then I fix the biggest cause and measure again.

**2. What are the main tabs of the Spark UI?**

Jobs, Stages, SQL/DataFrame, Storage, Environment and Executors.

**3. How do you spot data skew in the Spark UI?**

In the Stages tab, the task metric summary shows a max duration and input far above the median, typically one or a few tasks running much longer than the rest.

**4. What does spill mean, and what do you do about it?**

Data that didn't fit in execution memory was written to disk during a sort, aggregation or join. I increase the number of shuffle partitions, reduce the data per row, or fix skew.

**5. How do you monitor queries on Databricks serverless?**

With the query profile of each statement (time, rows, bytes and spill per operator, with the final plan), the Query History page, and system tables such as `system.query.history` for analysis across runs.

**6. Why might the plan in `explain()` differ from the Spark UI?**

With AQE, `explain()` shows the initial plan. The UI's SQL tab and the query profile show the final plan after runtime re-optimization, such as coalesced partitions, converted joins and skew splits.

### 15_internals_interview_qa

**1. What happens when I run `df.groupBy("country").count()` and then call `.show()`?**

Nothing runs on `groupBy` or `count`: they only build a logical plan. `show()` is the action, so the driver creates a job. Catalyst optimizes the plan, for example pruning unused columns and pushing filters into the scan, and plans a two-step aggregation. The DAG scheduler cuts the plan at the shuffle into two stages. In stage one, each task reads one input partition and does a partial count per country inside that partition, then writes the partial results to shuffle files, hashed by country. In stage two, each task fetches the blocks for its countries from every map task and adds up the partial counts. AQE may coalesce the 200 shuffle partitions into a few because the result is small. Finally `show()` fetches the first 20 rows back to the driver.

**2. How does a shuffle work, and why is it expensive?**

A shuffle redistributes rows so that all rows with the same key land in the same partition. Each map task computes a target partition for every row, buffers and sorts by target, and writes one data file plus an index to local disk. Once all map tasks are done, each reduce task fetches its blocks from every map output over the network and merges them. It's expensive because of serialization, disk writes and reads, network transfer, memory pressure that can cause spill, and the barrier between stages. I reduce it by filtering and selecting before wide operations, broadcasting small join sides, removing redundant repartitions and sorts, and handling skew.

**3. Broadcast join vs sort-merge join?**

A broadcast hash join collects the small table to the driver and sends a copy to every executor, which builds a hash table. The large table is then joined partition by partition without being shuffled, which makes it the fastest strategy when one side is small. Spark uses it below the 10 MB threshold, with a hint, or when AQE sees a small side at runtime. A sort-merge join shuffles both sides by the join key, sorts each partition, and merges them. It scales to any size and can spill to disk, but costs two shuffles and two sorts. It's the default for large equi-joins. Broadcasting a table that's too big can crash the driver, and you can't broadcast the preserved side of an outer join.

**4. What is lazy evaluation and why does Spark use it?**

Transformations only record steps in a plan. Execution starts when an action is called. Because Spark sees the whole query first, Catalyst can push filters into the scan, prune unused columns, combine and reorder steps, choose join strategies and fuse narrow operators into one generated function, and `limit` can stop early. The costs: each action recomputes from the source unless results are materialized, and data errors only appear at the action.

**5. Explain jobs, stages and tasks.**

Each action creates a job. The job is split into stages at shuffle boundaries, which are the `Exchange` operators in the plan, so a simple query with one groupBy has two stages. Each stage runs as a set of tasks, one per partition, and each task runs on one executor core. If there are more tasks than cores, they run in waves, and the stage finishes when its slowest task does, which is why skew matters.

**6. What is Adaptive Query Execution?**

AQE re-optimizes the plan at runtime. After each shuffle stage finishes, Spark knows the real partition sizes and re-plans the rest: it coalesces small shuffle partitions into fewer tasks, converts a sort-merge join into a broadcast join when one side turns out small, and splits skewed partitions in joins. It's on by default in Spark 3 and always on for Databricks serverless. `explain()` shows the initial plan, and the Spark UI or query profile shows the final one.

**7. What does the driver do?**

It runs the main program, holds the SparkSession, plans the query, schedules tasks on executors, and collects results.

**8. What is an executor?**

A process on a worker node that runs tasks on its cores and stores shuffle and cached data for one application.

**9. Narrow vs wide transformation?**

Narrow: each output partition depends on one input partition, so there's no shuffle. Wide: it needs data from many partitions, so there's a shuffle and a new stage.

**10. `repartition` vs `coalesce`?**

`repartition` shuffles to create balanced partitions and can increase or decrease the count. `coalesce` merges partitions without a shuffle and can only decrease the count.

**11. What is `spark.sql.shuffle.partitions`?**

The number of partitions after a shuffle, 200 by default. AQE coalesces small ones at runtime.

**12. `cache` vs `persist`?**

`cache` is `persist` with `MEMORY_AND_DISK`. Both are lazy and filled by the next action. They aren't supported on serverless, where you write a Delta table instead.

**13. What is Catalyst?**

Spark SQL's optimizer: analysis, rule-based logical optimization, physical planning with statistics, then code generation.

**14. What is Tungsten?**

The execution engine work on CPU and memory efficiency: binary row format, whole-stage code generation and vectorized reads.

**15. Why are DataFrames faster than RDDs?**

The schema lets Catalyst optimize the whole query and Tungsten use compact binary rows and generated code. RDD lambdas are opaque and run as written.

**16. Why avoid Python UDFs?**

Rows are serialized to Python workers and back, and the optimizer can't push down, fold or code-generate them.

**17. What is data skew?**

An uneven distribution of rows across partitions, usually because of hot keys, which makes a few tasks much slower than the rest.

**18. What is spill?**

Data written to disk because it didn't fit in execution memory during a sort, aggregation or join.

**19. What does `Exchange` mean in a plan?**

A shuffle, and therefore a stage boundary.

**20. What is whole-stage code generation?**

Fusing a chain of operators into one generated Java function, shown as `*(n)` in plans.

**21. What is Spark Connect?**

A client-server protocol where a thin client sends plans to a remote Spark driver. It's used by Databricks serverless notebooks, so there's no `sparkContext`.

**22. What is Photon?**

Databricks' native vectorized C++ query engine, which accelerates SQL and DataFrame operations without code changes.

**23. One task in a stage takes 30 minutes while the others take 30 seconds. What do you do?**

That's skew. I confirm it in the stage's task summary or the query profile, then find the hot key with a `groupBy(key).count()`. Fixes: let AQE skew join handling split it, broadcast the smaller side if possible, filter out or separately process the hot key, or salt the key by adding a random suffix and aggregating in two steps.

**24. A job writes 20,000 tiny files. Why, and how do you fix it?**

Each task writes a file per output partition it touches, so many partitions, or high-cardinality `partitionBy` columns, produce tiny files. I coalesce or repartition to a sensible number before writing, repartition by the partition column, choose coarser partition columns, and on Delta run `OPTIMIZE` or enable auto compaction, or use liquid clustering.

**25. A join is slow. How do you debug it?**

I check the plan for the join strategy and whether the small side was broadcast, the size of the shuffle on each side, skew in the join key, rows exploding after the join because of duplicate keys, and whether filters and column pruning happen before the join. Then I fix the biggest issue: broadcast, filter earlier, deduplicate keys, or handle skew.

**26. The driver crashes with out-of-memory. What are the likely causes?**

`collect()` or `toPandas()` on large data, a very large broadcast, too many tiny tasks or files for the driver to track, or a huge `display()`. I aggregate or limit before bringing data back, and avoid oversized broadcasts.

**27. The same notebook gives different results when re-run. Why?**

Non-deterministic expressions such as `uuid()` are recomputed per action, unordered operations such as `dropDuplicates` or `first` pick arbitrary rows, or sorts have ties. I add deterministic ordering and tie-breakers, and materialize results that must be stable.

## 03 Delta Lake

### 01_delta_fundamentals

**1. What is Delta Lake?**

An open-source storage layer that stores data as Parquet files plus a transaction log. The log brings ACID transactions, schema enforcement and evolution, `UPDATE`/`DELETE`/`MERGE`, time travel, and file-level statistics to data lakes. It's the default table format on Databricks.

**2. How does Delta provide ACID guarantees?**

Every change writes new data files first, then commits by atomically creating the next numbered JSON file in `_delta_log`, which lists the files added and removed. Readers only see files from committed versions, so writes are atomic and isolated. Concurrent writers use optimistic concurrency control: if two try to create the same version, one retries after checking for conflicts. Committed versions are durable in cloud storage.

**3. What is the difference between a managed and an external table?**

For a managed table, Unity Catalog manages both metadata and storage, and dropping the table deletes the data. An external table's data lives at a path you specify, and dropping it removes only the metadata. Managed tables are recommended, because they get automatic optimizations.

**4. What happens to the old data when you overwrite a Delta table?**

The new version references the new files and marks the old ones as removed in the log, but the files stay on storage until `VACUUM` deletes them after the retention period. So old versions can still be queried or restored.

**5. Why can't you read a Delta table with `spark.read.parquet`?**

You'd read every Parquet file in the folder, including files that later commits removed. Only the transaction log knows which files are part of the current version.

### 02_creating_and_querying_tables

**1. What is the difference between `CREATE OR REPLACE TABLE` and `DROP TABLE` followed by `CREATE TABLE`?**

`CREATE OR REPLACE` is a single atomic operation that writes a new version, so the history and time travel survive, and readers never see a missing table. `DROP` plus `CREATE` creates a brand-new table with no history, and there's a moment when the table doesn't exist.

**2. What is the difference between `INSERT INTO` and `INSERT OVERWRITE`?**

`INSERT INTO` appends rows. `INSERT OVERWRITE` replaces all existing data (or the matching partitions) in a new version, keeping the table definition and history.

**3. What is CTAS, and what are its trade-offs?**

`CREATE TABLE ... AS SELECT` creates and fills a table from a query in one step. It's convenient, but the schema is inferred from the query, so you don't declare constraints or exact types upfront unless you cast.

**4. How do you find out how a table was defined?**

`SHOW CREATE TABLE`, `DESCRIBE TABLE EXTENDED` for columns, comments and details, `DESCRIBE DETAIL` for format, files, size and properties, and `DESCRIBE HISTORY` for how it changed.

**5. Why add comments to tables and columns?**

They document meaning, units and ownership where everyone sees them: Catalog Explorer, lineage, and AI tools such as Genie use them to understand the data.

### 03_acid_and_delta_log

**1. How does Delta Lake provide ACID guarantees?**

Writers create new Parquet files and then commit by atomically creating the next numbered JSON file in `_delta_log`, listing the files added and removed. That makes each change atomic. Readers build a snapshot from the log and only see committed files, which gives isolation. Schema checks and constraints run before the commit, for consistency. Cloud storage makes commits durable. Concurrent writers use optimistic concurrency control.

**2. What is in a Delta commit file?**

One JSON action per line: `add` and `remove` for data files (with per-file statistics), `metaData` for the schema and properties, `protocol` for the required reader and writer versions, and `commitInfo` with the operation, user and metrics.

**3. What is a checkpoint in the Delta log?**

A Parquet file, written every 10 commits by default, that stores the full table state at that version. Readers start from the latest checkpoint instead of replaying every JSON commit.

**4. What is optimistic concurrency control in Delta?**

Writers don't lock the table. They prepare their changes and try to commit the next version. If another commit got there first, Delta checks whether the changes conflict. Non-conflicting changes, such as appends, are retried automatically, and conflicting ones fail with a concurrent modification exception.

**5. What happens if a write fails halfway?**

Its commit file is never created, so the files it wrote are invisible and the table stays at the previous version. `VACUUM` later removes the orphan files.

**6. How does an `UPDATE` work if Parquet files are immutable?**

Delta rewrites the files containing matching rows (copy-on-write), removing the old files and adding new ones in one commit. With deletion vectors, it can instead mark rows as deleted and write only the changed rows.

### 04_schema_enforcement

**1. What is schema enforcement in Delta Lake?**

Delta validates every write against the table's schema and rejects writes with extra columns, incompatible types, or nulls in `NOT NULL` columns. The check happens before commit, so a bad write leaves the table unchanged.

**2. What kinds of differences does Delta accept on write?**

Missing nullable columns, which are filled with null (or the column's default). DataFrame writes otherwise need matching types, while SQL `INSERT` casts values using ANSI assignment rules, for example `INT` into `BIGINT`. New columns and incompatible types are rejected.

**3. Why is schema enforcement useful?**

It stops upstream changes from silently corrupting downstream tables, and it fails fast at load time with a clear error instead of breaking reports later.

**4. How is this different from writing Parquet files?**

A Parquet folder accepts files with any schema. Problems only appear when reading, as dropped columns, nulls or type errors. Delta keeps one schema in the log and validates every write.

**5. How do you allow intentional schema changes?**

With schema evolution: `mergeSchema` on an append, `overwriteSchema` on an overwrite, `WITH SCHEMA EVOLUTION` or auto-merge for `MERGE`, or explicit `ALTER TABLE ... ADD COLUMNS`.

### 05_schema_evolution

**1. What is the difference between schema enforcement and schema evolution?**

Enforcement rejects writes that don't match the table schema. Evolution deliberately lets the schema change, for example adding new columns, through options such as `mergeSchema`, `overwriteSchema` or `ALTER TABLE`.

**2. What is the difference between `mergeSchema` and `overwriteSchema`?**

`mergeSchema` is used with appends (and merges) to add new columns to the existing schema, keeping the existing data. `overwriteSchema` is used with an overwrite to replace the schema entirely, including dropping columns or changing types, because all the data is replaced.

**3. How do you rename or drop a column in a Delta table without rewriting the data?**

Enable column mapping by name (`delta.columnMapping.mode = 'name'`), then use `ALTER TABLE ... RENAME COLUMN` or `DROP COLUMN`. Those become metadata-only changes.

**4. How do you handle new columns in a `MERGE`?**

On Databricks, with `MERGE WITH SCHEMA EVOLUTION`, or with the session setting `spark.databricks.delta.schema.autoMerge.enabled`. New source columns used by `UPDATE SET *` or `INSERT *` are then added to the target.

**5. Where would you allow automatic schema evolution in a medallion architecture?**

In Bronze and usually Silver, where capturing new source fields is valuable. Gold tables keep explicit schemas, because dashboards and consumers depend on them.

### 06_update_delete

**1. How does Delta perform an `UPDATE` when Parquet files are immutable?**

By default with copy-on-write: it finds the files containing matching rows, writes new versions of those files with the changes, and commits removing the old files and adding the new ones atomically. With deletion vectors, it marks the old rows as deleted in a small side file and writes only the changed rows, which is much cheaper.

**2. What are deletion vectors?**

A Delta feature that records deleted or updated row positions per data file in a compact bitmap, instead of rewriting the file. Readers filter those rows out. The files are physically rewritten later, by `OPTIMIZE` or `REORG`.

**3. Does `DELETE` physically remove the data?**

Not immediately. The rows disappear from the current version, but older files stay for time travel until `VACUUM` removes files older than the retention period. With deletion vectors, `REORG TABLE ... APPLY (PURGE)` rewrites files to physically drop the rows.

**4. How do you update a table using values from another table?**

With `MERGE INTO target USING source ON key WHEN MATCHED THEN UPDATE SET ...`, because Delta's `UPDATE` can't join to another table.

**5. How can you see how expensive a DML operation was?**

In `DESCRIBE HISTORY`, the `operationMetrics` show updated, deleted and copied rows, files added and removed, and deletion vectors added.

### 07_merge_upserts

**1. What does `MERGE INTO` do in Delta Lake?**

It matches source rows to target rows on a condition and, in a single atomic transaction, updates or deletes matched rows, inserts unmatched source rows, and optionally deletes target rows that have no source match. It's the standard way to do upserts and apply CDC.

**2. How do you make an incremental load idempotent?**

Use `MERGE` on the business key instead of appending, with a deduplicated source. Running the same batch twice then updates the same rows to the same values instead of duplicating them.

**3. What is the difference between SCD Type 1 and Type 2?**

Type 1 overwrites attributes with the latest values and keeps no history. Type 2 keeps every version as a separate row with validity dates and a current flag, so you can report on history.

**4. How do you implement SCD Type 2 with `MERGE`?**

Stage the changed records twice: once with the real key, which matches the current row and closes it by setting `is_current` to false and the end date, and once with a null merge key, which never matches and is therefore inserted as the new current version. New keys only need the insert copy.

**5. What happens if the source has two rows for the same key?**

The `MERGE` fails, because one target row can't be updated by multiple source rows. You deduplicate the source first, for example with `row_number()` ordered by timestamp.

**6. How do you speed up a slow `MERGE`?**

Keep the source small and deduplicated, add target predicates such as date ranges so fewer files are scanned, cluster or Z-order the target by the merge key, broadcast a small source, avoid updating unchanged rows, and enable deletion vectors.

### 08_time_travel_restore

**1. What is time travel in Delta Lake?**

The ability to query a table as of an earlier version number or timestamp, using `VERSION AS OF` or `TIMESTAMP AS OF`, because the log records which files made up each version and old files are retained until `VACUUM`.

**2. How do you undo a bad write to a Delta table?**

Find the last good version with `DESCRIBE HISTORY`, confirm by querying it, then run `RESTORE TABLE t TO VERSION AS OF n`. That creates a new version equal to the old state, and the history is preserved.

**3. What limits how far back you can time travel?**

Log retention (`delta.logRetentionDuration`, 30 days by default) and file retention (`delta.deletedFileRetentionDuration`, 7 days by default). After `VACUUM` deletes files older than the file retention, versions that need them can't be read.

**4. What is the difference between a shallow clone and a deep clone?**

A shallow clone copies only the metadata and references the source's data files, so it's fast and cheap but depends on the source files. A deep clone copies both data and metadata into an independent table.

**5. Give use cases for time travel.**

Rolling back bad writes, auditing what changed and when, reproducing ML training data or reports on a pinned version, and debugging pipelines by comparing versions.

### 09_optimize_vacuum

**1. What is the small-files problem and how does Delta solve it?**

Many small files make queries slow, because of per-file overhead in listing, opening and reading footers, and they waste metadata. Delta solves it with `OPTIMIZE`, which compacts files into larger ones, and on Databricks with optimized writes, auto compaction and predictive optimization.

**2. What is the difference between `OPTIMIZE` and `VACUUM`?**

`OPTIMIZE` rewrites small files into bigger ones and commits a new version, with the same data. `VACUUM` permanently deletes files that the current version no longer references and that are older than the retention period, which frees storage but limits time travel.

**3. What is the default `VACUUM` retention and why does it exist?**

7 days (`delta.deletedFileRetentionDuration`). It protects concurrent readers, long-running queries and streaming jobs that may still need older files, and it keeps a week of time travel.

**4. Does `OPTIMIZE` affect streaming readers of a table?**

No. Its commits are marked as not changing data (`dataChange = false`), so streams don't reprocess the compacted files.

**5. What is predictive optimization?**

A Databricks feature for Unity Catalog managed tables that automatically runs `OPTIMIZE`, `VACUUM` and statistics collection when it determines they're beneficial, removing the need to schedule maintenance yourself.

### 10_partitioning_zorder_clustering

**1. What is data skipping in Delta Lake?**

Delta stores min and max values per column for each data file in the transaction log. At query time it compares filters with those ranges and skips files that can't contain matching rows, without opening them.

**2. What does Z-ordering do?**

`OPTIMIZE ... ZORDER BY (cols)` rewrites data so that rows with similar values of the chosen columns are stored in the same files, using a space-filling curve for several columns. Each file then covers narrow ranges, which makes data skipping effective.

**3. What is liquid clustering and why is it recommended?**

A Delta layout feature declared with `CLUSTER BY`. Data is clustered by the chosen keys and maintained incrementally by `OPTIMIZE` or predictive optimization. Keys can be changed without rewriting the table. It replaces both partitioning and Z-ordering, handles high-cardinality columns well, and with `CLUSTER BY AUTO` Databricks can even choose the keys.

**4. When would you still partition a Delta table?**

For very large tables (terabytes) with a low-cardinality column that almost every query filters on, typically a date, so that each partition is at least around 1 GB. Otherwise liquid clustering is the better default.

**5. Partitioning vs Z-ordering?**

Partitioning splits data into folders by column value and prunes whole folders, which suits low-cardinality columns. Z-ordering co-locates values inside files to improve file-level skipping, which suits high-cardinality columns. They can be combined, with Z-ordering within partitions, but liquid clustering now replaces both.

### 11_change_data_feed

**1. What is the change data feed in Delta Lake?**

A table feature (`delta.enableChangeDataFeed`) that records row-level changes for each commit: inserts, deletes, and updates as pre- and post-images, with the version and timestamp. You read it with `readChangeFeed` or `table_changes()`.

**2. What are the values of `_change_type`?**

`insert`, `delete`, `update_preimage` (the row before the update) and `update_postimage` (the row after).

**3. How would you use CDF to update a Gold aggregate incrementally?**

Store the last Silver version processed, read changes since then, find the affected keys, recompute those keys from Silver (or apply deltas), `MERGE` them into Gold, and save the new version. Or let a streaming query with a checkpoint track the version.

**4. CDF vs time travel?**

Time travel returns a whole table snapshot at a version. CDF returns only the rows that changed between versions, with the type of change, which is what incremental processing needs.

**5. Is CDF available for changes made before it was enabled?**

No, only for commits after it's enabled, and only while the change files are within the retention period.

### 12_constraints_generated_columns

**1. What constraints does Delta Lake enforce?**

`NOT NULL` and `CHECK` constraints are enforced on every write, and a violating write fails entirely. Primary and foreign keys in Unity Catalog are informational and not enforced.

**2. What is a generated column?**

A column whose value is computed from other columns by an expression declared in the table, such as `GENERATED ALWAYS AS (year(order_ts))`. Delta computes it on write, or validates it if a writer supplies a value.

**3. How do you create surrogate keys in Delta?**

With an identity column, `BIGINT GENERATED ALWAYS AS IDENTITY`. Delta assigns unique, increasing values. They can have gaps, so don't rely on them being consecutive.

**4. What happens when you add a `CHECK` constraint to a table with existing invalid rows?**

The `ALTER TABLE` fails. Delta validates existing data when the constraint is added.

**5. Why use table constraints if the pipeline already validates data?**

They protect the table from every writer, including ad hoc notebooks and other jobs, and they document the rules in the table itself. Pipeline checks handle quarantine and reporting, and constraints are the final guarantee.

### 13_medallion_overview

**1. Walk me through a medallion pipeline you'd build on Databricks.**

Raw files land in a volume or cloud storage. Bronze ingests them append-only, with Auto Loader in production, keeping raw values plus audit columns such as source file, load time and batch. Silver casts and cleans the data, deduplicates to the latest record per business key, validates it (quarantining bad rows), and upserts with `MERGE` into a table with constraints and change data feed enabled. Gold aggregates Silver into business marts, updated incrementally from Silver's change feed with `MERGE`. Each layer is a Delta table, so every step is atomic, auditable and restorable.

**2. What belongs in Bronze vs Silver vs Gold?**

Bronze holds raw data as received, with audit columns, append-only. Silver holds cleaned, typed, deduplicated and validated entities, one row per key. Gold holds aggregated, business-level tables for reporting and serving.

**3. How do you make each layer idempotent?**

Bronze tracks which files were loaded (Auto Loader checkpoints). Silver uses `MERGE` on the business key with a deduplicated source and timestamp conditions. Gold uses `MERGE` on its grain, or recomputes affected partitions, and processing state (versions or checkpoints) records what's done.

**4. Why use change data feed between Silver and Gold?**

So Gold processes only the rows that changed since its last run, instead of rescanning all of Silver, which keeps the cost proportional to the changes.

**5. How do you handle late or out-of-order events?**

Keep event timestamps, deduplicate by latest event time, and only update Silver when the incoming event is newer than the stored one. Gold is then recomputed for the affected keys, including past dates.

### 14_delta_interview_qa

**1. What is Delta Lake and why use it instead of plain Parquet?**

Delta Lake is an open table format that stores data as Parquet files plus a transaction log. The log gives ACID transactions, so failed writes never leave partial data and concurrent writers don't corrupt the table. It also gives schema enforcement and evolution, `UPDATE`, `DELETE` and `MERGE`, time travel and rollback, file-level statistics for data skipping, and a reliable streaming source and sink. Plain Parquet folders have none of that.

**2. How does Delta provide ACID guarantees?**

Every change writes new Parquet files and then commits by atomically creating the next numbered JSON file in `_delta_log`, listing the files added and removed. Atomicity comes from that single commit file. Readers build a snapshot from committed versions only, which gives isolation. Schema checks and constraints run before the commit, for consistency, and storage makes commits durable. Concurrent writers use optimistic concurrency control: if the version is taken, Delta checks for logical conflicts and retries or fails.

**3. How do time travel and RESTORE work?**

Each version is defined by the log, and removed files stay on storage until `VACUUM`. So `VERSION AS OF` or `TIMESTAMP AS OF` replays the log to that version and reads its files. `RESTORE` makes an old version current by writing a new commit, so the history is preserved. Time travel is limited by log retention (30 days by default) and file retention (7 days, enforced by `VACUUM`).

**4. Explain MERGE and how you use it for SCD Type 2.**

`MERGE` matches a source to a target on a key and, in one transaction, updates or deletes matched rows, inserts new ones, and optionally deletes target rows missing from the source. The source must be unique per key. For SCD2, I stage each changed record twice: once with its key, which matches and closes the current row by setting the end date and the current flag to false, and once with a null merge key, which doesn't match and is inserted as the new current row.

**5. What do OPTIMIZE and VACUUM do?**

`OPTIMIZE` compacts small files into larger ones, optionally clustering them, and commits a new version with the same data, which fixes the small-files problem. `VACUUM` permanently deletes data files not referenced by the current version and older than the retention period (7 days by default), which frees storage but ends time travel to versions that needed them. On Databricks, predictive optimization runs both for managed tables.

**6. Partitioning vs Z-ordering vs liquid clustering?**

All three improve data skipping by controlling which values share files. Partitioning splits data into folders by a low-cardinality column and prunes whole folders, which is good only for very large tables. Z-ordering rewrites files so nearby values of high-cardinality columns share files, but it's a full rewrite each time. Liquid clustering, with `CLUSTER BY`, does the same clustering incrementally, lets you change keys without rewriting, and replaces both. It's the recommended default.

**7. What is in the `_delta_log`?**

JSON commit files with `add`, `remove`, `metaData`, `protocol` and `commitInfo` actions, plus Parquet checkpoints every 10 commits.

**8. Managed vs external table?**

For a managed table, Unity Catalog manages the storage, and `DROP` deletes the data. An external table's data lives at your path, and `DROP` removes only the metadata.

**9. Schema enforcement vs schema evolution?**

Enforcement rejects writes that don't match the schema. Evolution allows changes on purpose, with `mergeSchema`, `overwriteSchema`, `ALTER TABLE`, or `MERGE WITH SCHEMA EVOLUTION`.

**10. `mergeSchema` vs `overwriteSchema`?**

`mergeSchema` adds new columns on append. `overwriteSchema` replaces the whole schema on overwrite.

**11. How do you rename a column without rewriting data?**

Enable column mapping (`delta.columnMapping.mode = 'name'`), then `ALTER TABLE ... RENAME COLUMN`.

**12. What are deletion vectors?**

Bitmaps that mark deleted rows in existing files, so `DELETE`, `UPDATE` and `MERGE` avoid rewriting whole files.

**13. What is the change data feed?**

Row-level changes per commit (insert, update pre- and post-image, delete), read with `readChangeFeed` or `table_changes()` for incremental processing.

**14. Which constraints does Delta enforce?**

`NOT NULL` and `CHECK`. Unity Catalog primary and foreign keys are informational.

**15. What is an identity column?**

`GENERATED ALWAYS AS IDENTITY`: unique, increasing surrogate keys assigned by Delta, possibly with gaps.

**16. What does `DESCRIBE HISTORY` show?**

Every version with its timestamp, user, operation, parameters and metrics.

**17. What does `DESCRIBE DETAIL` show?**

Format, location, number of files, size, partition and clustering columns, properties, and protocol versions.

**18. Default retention periods?**

Log retention is 30 days (`delta.logRetentionDuration`). Deleted file retention is 7 days (`delta.deletedFileRetentionDuration`).

**19. What does `OPTIMIZE` do to streaming readers?**

Nothing. Its commits are marked `dataChange = false`, so streams don't reprocess compacted files.

**20. Shallow vs deep clone?**

A shallow clone copies metadata and references the source's files. A deep clone copies data and metadata, so it's independent.

**21. A bad deployment overwrote a Gold table an hour ago. What do you do?**

Check `DESCRIBE HISTORY` to find the bad write and the last good version, compare the two versions to confirm, then `RESTORE TABLE ... TO VERSION AS OF` the good version. Then fix the job and add a check that would have caught it.

**22. Queries on a Delta table have become slow over a few weeks. How do you investigate?**

Check `DESCRIBE DETAIL` for the file count and average size, because many small files call for `OPTIMIZE` or auto compaction. Check whether the common filters can skip data, and if not, cluster by those columns. Check the query profile for files and bytes read. Also look at whether deletion vectors have accumulated without `OPTIMIZE`, and at whether storage and history have grown without `VACUUM`.

**23. Two jobs writing to the same table sometimes fail with `ConcurrentAppendException`. Why, and what do you do?**

Both modified overlapping files, so optimistic concurrency detected a conflict. I'd make them touch different partitions or clusters with explicit predicates, run them in sequence, or enable row-level concurrency with deletion vectors on Databricks.

**24. A source starts sending a new column. What happens and what should you do?**

Appends fail because of schema enforcement. If the column is wanted, enable `mergeSchema` (or schema evolution in Auto Loader and `MERGE`) for Bronze and Silver, and add it explicitly to Gold when the business needs it.

**25. How do you make a daily load idempotent?**

Use `MERGE` on the business key with a deduplicated source, or overwrite exactly the batch's data with `replaceWhere` or dynamic partition overwrite. Then re-running produces the same result.

**26. The team must delete a customer's data for GDPR. What steps do you take on Delta?**

`DELETE` the rows in every table holding them. With deletion vectors, `REORG TABLE ... APPLY (PURGE)` rewrites the files. Then `VACUUM` after the retention period, so old files containing the data are physically removed. Also consider change data feed files and clones.

## 04 Databricks

### 01_workspace_notebooks_repos

**1. How do you structure code in a Databricks project?**

In a Git folder: thin notebooks as entry points that read parameters and call functions, Python modules in `src/` with the transformation logic, unit tests in `tests/`, and an Asset Bundle definition for jobs and environments. Data lives in Unity Catalog tables and volumes, not in the workspace.

**2. What is the difference between `%run` and importing a module?**

`%run` executes another notebook in the current context, sharing all its variables. Importing a workspace `.py` module shares only what you import, works with standard Python tooling, and is unit-testable, so it's preferred for production logic.

**3. What are Git folders?**

Workspace folders linked to a remote Git repository, where you can switch branches, commit, push and pull from the Databricks UI. They're the basis for code review and CI/CD.

**4. What are workspace files?**

Non-notebook files stored in the workspace, such as `.py`, `.sql`, `.yml` or `.json`. They let you build normal Python packages and keep config next to notebooks.

**5. Where should data files go?**

In Unity Catalog volumes (files) and tables (tabular data), with governance and lineage, not in workspace folders or Git.

### 02_compute_types

**1. What types of compute does Databricks offer?**

Serverless compute for notebooks, jobs and pipelines, classic all-purpose clusters for interactive work, classic job clusters created per job run, SQL warehouses for SQL and BI, and instance pools that keep idle VMs warm to speed up classic cluster starts.

**2. Why use job clusters or serverless jobs instead of an all-purpose cluster for production?**

They exist only for the run, so you don't pay for idle time and the DBU rate is lower. Each run gets a clean, isolated environment that interactive users can't disturb.

**3. What is a SQL warehouse?**

Compute optimized for SQL queries, dashboards and BI tools, sized in T-shirt sizes with auto-stop and scaling for concurrency. Serverless warehouses start in seconds.

**4. What are the trade-offs of serverless compute?**

You get fast start-up, no infrastructure management and usage-based billing. In exchange you give up control over runtime details, node types, init scripts and some APIs, such as RDDs, `sparkContext` and caching.

**5. What is a cluster policy?**

An admin-defined set of rules and defaults for cluster creation, such as allowed node types, maximum workers, required tags and auto termination. It controls cost and enforces standards.

**6. What is the difference between standard and dedicated access mode?**

Standard (shared) access mode isolates each user's code so many users can share a Unity Catalog-enabled cluster safely. Dedicated access mode assigns the cluster to one user or group, which supports workloads that need full access.

### 03_dbutils

**1. What is `dbutils`?**

The Databricks utilities available in notebooks, for file operations (`fs`), parameters (`widgets`), secrets (`secrets`), notebook orchestration (`notebook`) and passing values between job tasks (`jobs.taskValues`).

**2. How do you pass parameters into a notebook?**

Define widgets with `dbutils.widgets.text` or `dropdown` and read them with `dbutils.widgets.get`. When a job runs the notebook, job or task parameters with the same names fill the widgets.

**3. How do you use credentials in a notebook securely?**

Store them in a secret scope and read them with `dbutils.secrets.get(scope, key)`. The value is redacted in outputs and never appears in code or Git.

**4. What is the difference between `%run` and `dbutils.notebook.run`?**

`%run` executes another notebook inline in the same context, with no parameters or return value. `dbutils.notebook.run` starts it as a separate run with parameters and a timeout, and returns the value passed to `dbutils.notebook.exit`.

**5. How do tasks in a job share information?**

Through task values: `dbutils.jobs.taskValues.set` in one task and `get` in a downstream task, or references such as `{{tasks..values.}}` in parameters and conditions. For larger data, through tables.

### 04_parameters_and_widgets

**1. How do you parameterize a Databricks notebook?**

Create widgets with defaults at the top (`text`, `dropdown`, `combobox`, `multiselect`), read them with `dbutils.widgets.get`, convert and validate them into a config object, and use those values in the code. Jobs pass parameters with the same names, which override the defaults.

**2. What type are widget values?**

Always strings, including multiselect, which is comma-separated. Convert them explicitly.

**3. How do you use parameters in SQL safely?**

With named parameter markers (`:name`), passed with `args=` in `spark.sql` or taken from widgets in SQL cells, and `IDENTIFIER(:name)` for table or column names. Never string formatting.

**4. How does a job pass values to a notebook?**

Through job or task parameters. Each one whose name matches a widget sets that widget's value for the run. Dynamic value references such as `{{job.start_time.iso_date}}` provide run-specific values.

**5. How do you design a notebook for backfills?**

Make the processing date a parameter, make every write idempotent for that date (for example `replaceWhere` or `MERGE`), and run the notebook once per date, in a loop or as separate job runs.

### 05_secrets_and_scopes

**1. How do you manage credentials in Databricks?**

In secret scopes: Databricks-backed, or Azure Key Vault-backed on Azure. Secrets are created through the CLI, API or Terraform, read in code with `dbutils.secrets.get`, redacted in outputs, and protected by scope ACLs. For storage and external databases I prefer Unity Catalog storage credentials and connections, so no keys appear in code at all.

**2. What does redaction do, and is it enough?**

Printed secret values are replaced with `[REDACTED]` in notebook output. It prevents accidental exposure, but anyone with `READ` on the scope can still use the value in code, so ACLs and least privilege are what really protect it.

**3. What permissions exist on a secret scope?**

`READ` to read secrets, `WRITE` to add and update them, and `MANAGE` to also change ACLs and delete the scope.

**4. What is a Key Vault-backed secret scope?**

A scope on Azure Databricks that reads secrets directly from an Azure Key Vault, so secrets are created, rotated and audited in Azure, and Databricks only references them.

**5. What do you do if a token was committed to Git?**

Revoke or rotate it immediately, because it's compromised even if the commit is removed. Then store the new one in a secret scope, and consider scanning the repository and enabling secret scanning.

### 06_sql_warehouse

**1. What is a Databricks SQL warehouse?**

Compute dedicated to SQL workloads: the SQL editor, dashboards, alerts, Genie and BI tools via JDBC/ODBC. It runs Photon, scales out for concurrency, auto-stops when idle, and serverless warehouses start in seconds.

**2. How do you size a SQL warehouse?**

Choose the size (T-shirt) for query complexity and data volume, and the min/max number of clusters for concurrency. If queries queue, add clusters. If single queries are slow, check the query first, then increase the size.

**3. Serverless vs pro vs classic warehouses?**

Serverless is managed by Databricks, starts in seconds and has the most features. Pro and classic run in your cloud account and start in minutes. Classic has the fewest features.

**4. When would you use a SQL warehouse instead of a notebook on a cluster?**

For SQL-only analytics: dashboards, BI tools, ad hoc SQL and Genie, especially with many concurrent users. Notebooks are for pipelines, Python work and exploration.

**5. How can applications query Databricks without Spark?**

Through a SQL warehouse, with the Statement Execution REST API, the Databricks SQL connectors (Python, JDBC/ODBC), or the SDKs.

### 07_dashboards_and_genie

**1. What are AI/BI dashboards in Databricks?**

Dashboards built from SQL datasets and visual widgets, with filters and parameters, running on a SQL warehouse. They can be published with embedded or viewer credentials, shared with users and groups, and scheduled for email delivery.

**2. What is a Genie space?**

A natural-language interface over selected Unity Catalog tables. Users ask questions, Genie generates and runs SQL on a warehouse, and returns the answer with the SQL. Authors improve it with instructions and example queries.

**3. What can a data engineer do to make Genie and dashboards accurate?**

Provide clean Gold tables with clear names, a single grain, consistent units and column comments. Add views for common aggregations. Document business definitions in Genie instructions, add trusted example SQL, and test known questions.

**4. How do permissions work for dashboards?**

Data access is governed by Unity Catalog. A published dashboard can run queries with the publisher's embedded credentials, or with each viewer's own credentials, in which case viewers need `SELECT` on the underlying data.

**5. Why keep heavy transformations out of dashboard queries?**

Every refresh re-runs them on the warehouse, which is slow and costly, and logic gets duplicated across dashboards. Computing it once in Gold tables is faster, cheaper and consistent.

### 08_monitoring_basics

**1. How do you monitor data pipelines on Databricks?**

At three levels. Jobs: run history, durations and failure notifications on every job. Queries: query history and profiles for slow statements. Data: freshness, volume and quality checks on key tables, using Delta history, expectations, table monitors and custom checks that fail a job to trigger alerts. System tables give a SQL view across all of it, including cost.

**2. What are system tables?**

Databricks-managed tables in the `system` catalog with operational data: billing usage and prices, query history, job runs, audit logs, lineage and more. They let you analyse cost, performance and access with SQL and build dashboards and alerts.

**3. How would you find which job causes a cost increase?**

Query `system.billing.usage` grouped by day and by usage metadata such as the job ID, compare periods, and join `system.billing.list_prices` for cost. Then check that job's run timeline for changes in frequency or duration.

**4. How do you detect that a table is no longer being updated?**

With a freshness check: compare the latest commit timestamp from `DESCRIBE HISTORY` (or the latest event time in the data) with the expected schedule, and alert when it's older than the threshold.

**5. How do you send alerts?**

Job and task notifications on failure, duration thresholds or success, Databricks SQL alerts on query results, and health-check jobs that fail when a check fails, routed to email, Slack or webhooks.

### 09_databricks_interview_qa

**1. Describe the Databricks platform architecture.**

The control plane, managed by Databricks, hosts the web UI, notebooks, jobs and APIs. The compute plane runs the workloads: serverless compute in Databricks' account, or classic clusters in your cloud account. Data stays in your cloud storage as Delta tables and volumes, governed by Unity Catalog, which manages permissions, lineage and audit across workspaces. On top sit the tools: notebooks, jobs and pipelines, SQL warehouses, dashboards and Genie.

**2. How do you choose compute for a workload?**

Serverless notebooks for interactive work, serverless jobs or job clusters for scheduled pipelines, SQL warehouses for SQL, dashboards and BI, and classic clusters only when I need specific hardware, libraries or APIs. Production never runs on always-on all-purpose clusters, because job compute is cheaper and isolated.

**3. How do you structure a Databricks project for production?**

A Git folder with thin notebooks as entry points, transformation logic in Python modules with unit tests, configuration through parameters (widgets and job parameters), secrets in secret scopes, data in Unity Catalog tables and volumes, and deployment with Asset Bundles through CI/CD to dev, test and prod.

**4. How do you handle parameters and secrets in notebooks?**

Parameters come from widgets, filled by job parameters, and are validated at the top into a config object. In SQL they're passed as parameter markers and `IDENTIFIER()`. Secrets live in secret scopes and are read with `dbutils.secrets.get`, redacted in output, with ACLs controlling access. For storage and databases I prefer Unity Catalog credentials and connections.

**5. How do you monitor a Databricks platform?**

Job notifications and run history for pipelines, query history and profiles for SQL performance, freshness and volume checks from Delta history plus data quality checks for data, and system tables for cost, usage, job runs and audit, with dashboards and alerts on top.

**6. Control plane vs compute plane?**

The control plane is the Databricks-managed UI, APIs and job scheduler. The compute plane is where data is processed: serverless or your cloud account's clusters.

**7. What is a Git folder?**

A workspace folder linked to a remote Git repository, for branches, commits and pull requests in Databricks.

**8. `%run` vs `dbutils.notebook.run`?**

`%run` runs a notebook inline in the same context. `dbutils.notebook.run` runs it separately with parameters and returns a value.

**9. How do job tasks share values?**

Through `dbutils.jobs.taskValues`, or tables for larger data.

**10. Widget value types?**

Always strings.

**11. What does `dbutils.secrets.get` show when printed?**

`[REDACTED]`.

**12. Size vs scaling on a SQL warehouse?**

Size is for query complexity. Scaling (number of clusters) is for concurrency.

**13. What is the Statement Execution API?**

A REST API for running SQL on a SQL warehouse from applications, without Spark.

**14. What is Genie?**

Natural-language questions over Unity Catalog tables, answered with generated SQL on a warehouse.

**15. What are system tables?**

Tables in the `system` catalog with billing, query history, job runs, audit and lineage data.

**16. What is an instance pool?**

Idle, warm VMs that speed up classic cluster starts.

**17. What is a cluster policy?**

Admin rules that limit and default cluster settings, for cost and governance.

**18. The monthly Databricks bill doubled. How do you investigate?**

Query `system.billing.usage` by day, product and job or warehouse to find what grew, and join list prices for cost. Then look at that workload's runs, such as schedule changes, longer durations or a warehouse that never stops. Fix the cause and add a cost dashboard or alert.

**19. A notebook works for you but fails as a scheduled job. What do you check?**

That parameters and widgets are defined with defaults, that the job's identity has permissions on the tables, volumes and secrets, that it doesn't depend on temp views or state from another notebook, the compute and environment differences (libraries, serverless restrictions), and that paths aren't relative to a personal folder.

**20. An API token was found in a notebook in Git. What do you do?**

Revoke and rotate the token immediately, store the new one in a secret scope with tight ACLs, update the code to `dbutils.secrets.get`, and add secret scanning to the repository.

**21. Analysts complain the dashboard is slow every Monday morning.**

Check Query History for queuing versus long execution. If queries queue, increase the warehouse's max clusters. If single queries are slow, look at the profiles and pre-aggregate or cluster the Gold tables, and check that results can be cached.

**22. How would you let 200 business users explore sales data without writing SQL?**

Build clean, documented Gold tables and views with a clear grain, then publish an AI/BI dashboard for the standard KPIs and a Genie space with instructions and example queries for ad hoc questions, all governed by Unity Catalog permissions.

## 05 Optimization

### 01_reading_query_profiles

**1. How do you start investigating a slow query on Databricks?**

I open its query profile (or the Spark UI on classic compute), sort operators by time, and look at the top ones: rows in and out, bytes and files read, shuffle sizes, spill, and the task time distribution. That tells me whether the problem is reading too much, moving too much, exploding rows, skew, or memory.

**2. What signals in a profile point to missing data skipping?**

A scan reading most files and bytes of a table even though the query filters on a column: few or zero files pruned. Usually the filter wraps the column in a function, uses a UDF, or the data isn't clustered on that column.

**3. How do you spot a bad join in a profile?**

The join outputs far more rows than its inputs (duplicate keys), it's a sort-merge join with a huge shuffle where one side is small (missing broadcast), or one task takes much longer than the others (skew).

**4. What is spill and where do you see it?**

Data written to disk because it didn't fit in memory during a sort, aggregation or join. It's reported per operator in the profile and per stage in the Spark UI.

**5. What's the difference between `explain()` and a query profile?**

`explain()` shows the plan before execution, without metrics. The profile shows the final executed plan, including AQE changes, with real metrics per operator.

### 02_data_skew

**1. One task takes much longer than the others. Why, and what do you do?**

Usually data skew: after a shuffle, one partition holds far more data because a key is very frequent. I confirm it with the task time distribution and key counts. Then I fix it: let AQE's skew join handle it, broadcast the smaller side, process the hot keys separately, or salt the key so the hot key spreads over several partitions.

**2. What is salting?**

Adding a random number (0 to N-1) to a skewed key on the big side, and replicating the other side's rows for each salt value, so the hot key is split across N partitions. For aggregations, aggregate by key and salt first, then by key.

**3. Why don't simple sums suffer much from skew?**

Spark does partial aggregation in each map task, so only one row per key per task is shuffled. Aggregates that keep all values, such as `collect_list` or exact distinct counts, can't shrink like that and do suffer.

**4. How does AQE handle skew?**

After the map stage it knows the partition sizes. In sort-merge joins it splits partitions larger than a factor of the median and above a size threshold into smaller ones, and reads the matching data from the other side for each split.

**5. How do you find skewed keys?**

`groupBy(key).count().orderBy(desc)` on the join or grouping key, partition sizes after a shuffle, and the task metrics in the profile or Spark UI.

### 03_small_files_and_file_layout

**1. A job creates thousands of small files. Why, and what do you do?**

Each write task produces files, so many tasks, many output partitions or frequent micro-batches create many small files. I fix the source by reducing write parallelism with `coalesce`/`repartition`, enabling optimized writes and auto compaction, and avoiding high-cardinality partitioning. I fix existing tables with `OPTIMIZE` (with liquid clustering) and then `VACUUM`, and I let predictive optimization maintain them.

**2. Why are small files bad?**

Every file costs listing, metadata, an open and a footer read, and many files mean more tasks and more planning time. With thousands of tiny files, this overhead dominates the actual reading, and the log and statistics grow too.

**3. What is a good file size for Delta tables?**

Roughly tens of megabytes up to about 1 GB. `OPTIMIZE` targets about 1 GB by default, and frequently merged tables benefit from smaller files.

**4. How do you measure a table's layout?**

`DESCRIBE DETAIL` for the file count and size, the `_metadata` column for per-file sizes and min/max of filter columns, and the query profile for files read and pruned.

**5. What are optimized writes and auto compaction?**

Databricks table properties. Optimized writes shuffle data before writing so each partition gets fewer, larger files. Auto compaction runs a small `OPTIMIZE` after writes when it finds many small files.

### 04_memory_and_spill

**1. What is spill in Spark?**

When a task's execution memory is full during a sort, aggregation or join, Spark writes intermediate data to local disk and merges it later. The job continues but slows down because of disk I/O and serialization.

**2. How is executor memory organized?**

Part of the heap is reserved, a unified region (60% of the rest by default) is shared by execution (shuffles, joins, sorts, aggregations) and storage (cache, broadcasts), which can borrow from each other, and the remainder is user memory. Off-heap overhead covers Python workers, Arrow buffers and native memory.

**3. What causes executor OOM errors, and how do you fix them?**

Oversized partitions, skewed keys, collecting huge groups (`collect_list`), exploding arrays, large broadcasts and memory-heavy UDFs. I reduce data per task (filter early, more partitions), fix skew, replace unbounded collections with bounded aggregates, avoid explosions, and adjust UDF batch sizes, before adding memory.

**4. What causes driver OOM?**

Bringing too much data to the driver with `collect()`, `toPandas()` or large `display()` calls, broadcasting big tables, or very large plans and file listings. Keep driver results small and write large outputs to tables.

**5. How do you see spill?**

In the Spark UI's stage metrics ("Spill (memory)" and "Spill (disk)") on classic compute, and in the query profile's per-operator spill metrics on serverless and SQL warehouses.

### 05_join_optimization

**1. A join is slow. How do you debug it?**

I open the query profile and check the join strategy, the rows in and out (explosion), the shuffle bytes on each side, and the task time distribution (skew). Then I apply the checklist: filter and select before joining, pre-aggregate the big side if only totals are needed, broadcast a small side, make sure keys are unique, typed consistently and free of placeholder values, and handle skewed keys. Then I measure again.

**2. Why pre-aggregate before a join?**

If the result only needs totals per key, aggregating the big side first reduces it to one row per key, so the join shuffles and compares far less data, with the same result.

**3. When should you use a semi or anti join?**

To check whether matching rows exist (semi) or don't exist (anti). They return each left row at most once and only the left columns, avoiding duplicates and an extra distinct.

**4. What happens when join keys have different data types?**

Spark adds a cast on one side for every row, which costs CPU, can prevent pushdown and data skipping, and can fail at runtime with ANSI mode if values don't convert.

**5. What is dynamic file pruning?**

When a fact table is joined to a filtered dimension, Databricks uses the dimension's matching key values at runtime to skip fact files (or partitions) that can't match, which works best when the fact table is clustered or partitioned by the join key.

### 06_avoiding_udfs_and_shuffles

**1. How would you speed up a PySpark job that uses several Python UDFs?**

Replace each UDF with built-in functions: regex functions for parsing, `from_json` for JSON, map expressions or broadcast joins for lookups, date functions, and higher-order functions for arrays. Built-ins run in the JVM or Photon, are optimized and code-generated, and avoid Python serialization. Only if a Python library is truly needed, use a pandas UDF.

**2. How do you add a group total to every row efficiently?**

With a window function partitioned by the group key, for example `sum("amount").over(Window.partitionBy("region"))`, which needs one shuffle. A `groupBy` followed by a join back needs more.

**3. How do you find unnecessary shuffles?**

Count the `Exchange` operators in `explain()` or the query profile, and ask for each one whether it's required by a later operation. Typical waste: `repartition` before a `groupBy` on another key, `orderBy` in the middle, `distinct` before an aggregation that already deduplicates, and several separate aggregations of the same data.

**4. When is a pandas UDF acceptable?**

When the logic needs a Python library or numerical code with no built-in equivalent. It's vectorized over Arrow batches, so it's much faster than a row-by-row UDF, though still slower than built-ins.

### 07_cost_awareness

**1. What is a DBU?**

A Databricks Unit: a normalized unit of processing capacity per hour. Each compute type consumes DBUs at a rate, and each SKU (jobs, all-purpose, SQL, serverless) has its own price per DBU. On classic compute you also pay the cloud provider for the VMs.

**2. How would you reduce the cost of a Databricks pipeline?**

First measure with `system.billing.usage` and the query profiles to find the top consumers. Then: run scheduled work on job compute or serverless instead of all-purpose, set auto-termination, right-size or autoscale clusters, process incrementally instead of full reloads, read less data (filters, clustering, pruning), remove waste in code (UDFs, skew, extra shuffles), avoid failed reruns, and use Photon where it shortens runs enough.

**3. How do you find which jobs cost the most?**

Query `system.billing.usage` grouped by `usage_metadata.job_id` (or `warehouse_id`, `cluster_id`) and join to `system.billing.list_prices` for estimated list cost, then rank them.

**4. Why is serverless often cheaper even with a higher DBU price?**

There's no idle time or startup waste: you pay only while work runs, and the infrastructure is included. For bursty, short or interactive workloads, that usually outweighs the rate difference.

**5. How do tags help with cost?**

Custom tags on clusters, jobs, warehouses and serverless budget policies appear in the billing usage records, so spend can be attributed to teams, projects or environments.

### 08_slow_job_debugging_playbook

**1. A job that took 20 minutes now takes 3 hours. How do you debug it?**

First I find out what changed: data volume, code, cluster or upstream data. Then I open the Spark UI or query profile to find the slowest stage and operator, and check for skew (max task time vs median), spill, retries and the number of tasks. I read the plan for Python UDFs, extra shuffles, wrong join strategies, casts on join keys and filters that weren't pushed down, and I check the input for small files. I fix the biggest issue first, verify the output is identical, measure again, and document it.

**2. How do you confirm that a performance fix didn't change the results?**

Compare outputs from the old and new versions: row counts, key aggregates, and a full `exceptAll` comparison on a sample or on the whole output when it's affordable.

**3. What signs of trouble do you look for in a physical plan?**

`BatchEvalPython`/`ArrowEvalPython` (Python UDFs), many `Exchange` nodes (shuffles), `RoundRobinPartitioning` and `rangepartitioning` from unnecessary `repartition` and `orderBy`, `SortMergeJoin` where a broadcast would do, `cast` in join conditions, and filters that sit above joins or UDFs instead of near the scan.

**4. Why does adding nodes often not help a skewed job?**

The stage waits for its slowest task, and a hot key's rows all go to one task. More nodes only make the other tasks finish earlier. Fixing the skew (AQE skew join, filtering placeholder keys, salting, broadcasting) is what shortens the stage.
