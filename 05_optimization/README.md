# 05 Optimization

Making jobs fast and cheap: reading query profiles, skew, small files and layout, memory and spill, joins, removing UDFs and shuffles, cost, and a complete slow-job debugging playbook.

Every lesson measures its changes. Timings at demo scale are small and vary between runs, so each lesson explains which differences grow with real data volumes. Tables live in the schema `workspace.optimization`.

| Notebook | Key topics |
|---|---|
| [01_reading_query_profiles](01_reading_query_profiles.ipynb) | Query profile and Spark UI, operators, rows and bytes, finding the slow part |
| [02_data_skew](02_data_skew.ipynb) | Detecting skew, AQE skew join, salting, broadcast, placeholder keys |
| [03_small_files_and_file_layout](03_small_files_and_file_layout.ipynb) | Small files, `OPTIMIZE`, file sizing, partitioning vs liquid clustering |
| [04_memory_and_spill](04_memory_and_spill.ipynb) | Executor memory, spill, OOM causes, bounded aggregates, driver safety |
| [05_join_optimization](05_join_optimization.ipynb) | Join checklist, pre-aggregation, broadcast, key types, semi/anti joins, dynamic pruning |
| [06_avoiding_udfs_and_shuffles](06_avoiding_udfs_and_shuffles.ipynb) | Built-in replacements for UDFs, window instead of join-back, redundant shuffles |
| [07_cost_awareness](07_cost_awareness.ipynb) | DBUs, cost estimates, `system.billing`, data scanned, incremental processing |
| [08_slow_job_debugging_playbook](08_slow_job_debugging_playbook.ipynb) | Diagnose, fix, verify and measure a slow job with a reusable `diagnose()` helper |
