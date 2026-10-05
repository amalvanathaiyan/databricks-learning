# 06 Unity Catalog

Governance on Databricks: the catalog hierarchy, managed and external storage, volumes, permissions, lineage and tags, views and functions, and row- and column-level protection of personal data.

Many Unity Catalog features (grants, volumes, tags, lineage, row filters, column masks) only exist on Databricks. Cells that depend on features your workspace may not expose are wrapped and print a note instead of failing. Things that need a cloud account (storage credentials, external locations) are explained with example DDL. Everything is created in the schema `workspace.governance`.

| Notebook | Key topics |
|---|---|
| [01_catalog_hierarchy](01_catalog_hierarchy.ipynb) | Metastore → catalog → schema → objects, three-level names, `USE`, `information_schema` |
| [02_managed_vs_external](02_managed_vs_external.ipynb) | Managed vs external tables, storage credentials, external locations, `DROP` behavior, `UNDROP` |
| [03_volumes](03_volumes.ipynb) | Managed and external volumes, `/Volumes` paths, `LIST`, `read_files`, `dbutils.fs`, files to tables |
| [04_permissions_grants](04_permissions_grants.ipynb) | Privileges, `GRANT` / `REVOKE` / `SHOW GRANTS`, inheritance, ownership, an access-check model |
| [05_lineage_tags_discovery](05_lineage_tags_discovery.ipynb) | Comments, tags, documentation coverage, lineage graph and lineage system tables |
| [06_views_and_functions](06_views_and_functions.ipynb) | Views, temp views, materialized views, SQL scalar and table functions, Python UDFs in UC |
| [07_pii_masking_row_filters](07_pii_masking_row_filters.ipynb) | Pseudonymization, dynamic views, column masks, row filters with mapping tables |
