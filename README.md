# Databricks Learning

A hands-on journey through PySpark, Databricks and Azure Databricks.
Every concept is documented as a detailed notebook, so this repo works as
a personal reference and as learning material for others.

## Goal

Build deep, explainable knowledge of PySpark and Databricks, with a focus
on understanding how things work, not only how to write the code, and
prepare for the **Databricks Certified Data Engineer Associate** exam.

## Environment

- Databricks Free Edition (serverless compute)
- Notebooks synced with this GitHub repo through a Databricks Git folder

## Getting started

1. Sign up for [Databricks Free Edition](https://www.databricks.com/learn/free-edition)
2. In the workspace: **Workspace → Create → Git folder**, and paste this repo's URL
3. Open a notebook, connect to **Serverless**, and click **Run all**
4. Lessons that need files create their own schema and volume (`workspace.spark_basics.raw_files`) automatically

## Roadmap

See [learning-path.md](learning-path.md) for the full plan, and the
[certification study guide](docs/certification/data_engineer_associate.md)
for how the lessons map to the exam domains.

## Progress

| Folder | Topic | Status |
|---|---|---|
| [00_platform_tour](00_platform_tour/) | Platform tour | ✅ Complete (4 lessons) |
| [01_spark_basics](01_spark_basics/) | PySpark basics (30 lessons) | ✅ Complete (30 lessons) |
| [02_spark_internals](02_spark_internals/) | Spark internals | ✅ Complete (15 lessons) |
| [03_delta_lake](03_delta_lake/) | Delta Lake | ✅ Complete (14 lessons) |
| [04_databricks](04_databricks/) | Databricks platform | ✅ Complete (9 lessons) |
| [05_optimization](05_optimization/) | Performance and optimization | ✅ Complete (8 lessons) |
| [06_unity_catalog](06_unity_catalog/) | Unity Catalog | ✅ Complete (7 lessons) |
| 07_workflows | Jobs and pipelines | Not started |
| 08_streaming_and_ingestion | Streaming and ingestion | Not started |
| 09_azure_databricks | Azure Databricks | Not started |
| projects | Capstone projects | Not started |

## How each lesson is structured

Goal → why it matters → concept → real-world example → syntax → hands-on
sections with expected output → under the hood (`explain()` plans) →
mistakes and troubleshooting → interview Q&A → 🎓 certification corner
(exam-style questions) → practice problem → solution → summary and cheat sheet.

## Interview and exam prep

- [Question bank](interview_prep/question_bank.md): every interview question from every lesson. Rebuild it with `python tools/build_question_bank.py`
- [Certification study guide](docs/certification/data_engineer_associate.md): exam domains, weights, lesson mapping and an 8-week plan
