# 02 Spark Internals

From "I can write PySpark" to "I understand how Spark executes my code". Every notebook runs in **Databricks Free Edition** (serverless). Where serverless hides something (the Spark UI, `sparkContext`, caching, most configs), the lesson shows how to observe it anyway: plans, `spark_partition_id()`, timings and the query profile.

⭐ = core interview material.

| # | Notebook | Key topics |
|---|---|---|
| 01 | ⭐ [01_driver_executors](01_driver_executors.ipynb) | Driver, executors, cluster manager, what runs where, Spark Connect |
| 02 | ⭐ [02_jobs_stages_tasks](02_jobs_stages_tasks.ipynb) | Actions → jobs → stages → tasks, counting stages from plans, waves |
| 03 | [03_transformations_actions](03_transformations_actions.ipynb) | Classification, metadata operations, interview traps |
| 04 | ⭐ [04_lazy_evaluation](04_lazy_evaluation.ipynb) | Pushdown, pruning, pipelining, early stop, recomputation |
| 05 | [05_dag_and_query_plans](05_dag_and_query_plans.ipynb) | Plan phases, `explain` modes, operators, reading plans bottom-up |
| 06 | [06_narrow_wide_transformations](06_narrow_wide_transformations.ipynb) | Dependencies, `coalesce` vs `repartition`, avoiding shuffles |
| 07 | ⭐ [07_shuffle](07_shuffle.ipynb) | Map/reduce sides, cost, shuffle partitions, AQE coalescing |
| 08 | [08_partitioning_and_parallelism](08_partitioning_and_parallelism.ipynb) | Read splits, repartition/coalesce, skew detection, the `coalesce(1)` trap |
| 09 | ⭐ [09_broadcast_and_join_strategies](09_broadcast_and_join_strategies.ipynb) | Broadcast hash, sort-merge, shuffled hash, nested loop, hints |
| 10 | [10_caching_persistence](10_caching_persistence.ipynb) | `cache`/`persist`, storage levels, serverless alternatives, disk cache |
| 11 | [11_serialization](11_serialization.ipynb) | Tungsten rows, Kryo, pickle vs Arrow, closures, `PicklingError` |
| 12 | [12_catalyst_and_tungsten](12_catalyst_and_tungsten.ipynb) | Optimizer rules, codegen, statistics, Photon |
| 13 | ⭐ [13_adaptive_query_execution](13_adaptive_query_execution.ipynb) | Coalescing, join switching, skew join splitting |
| 14 | ⭐ [14_spark_ui](14_spark_ui.ipynb) | Spark UI tabs, query profile, debugging checklist, specimen queries |
| 15 | ⭐ [15_internals_interview_qa](15_internals_interview_qa.ipynb) | Execution flow diagram, six 2-minute answers, scenarios, quiz |

Execution flow to be able to draw and explain:
**Application → Driver → Job → Stages → Tasks → Executors → Output**
