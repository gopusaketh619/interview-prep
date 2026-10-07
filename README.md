# Interview Prep

Personal interview and certification prep: algorithms, data engineering, and AWS certification material.

| Area | What's inside | Start here |
|------|---------------|------------|
| [dsa/](dsa/) | 137 DSA problems in 16 topics, templates, study guide, 12-week plan | [dsa/README.md](dsa/README.md) |
| [data_engineering/](data_engineering/) | 50-problem SQL suite (DuckDB), Kafka/Snowflake and platform/governance guides | [data_engineering/README.md](data_engineering/README.md) |
| [certifications/](certifications/) | AWS Certified AI Practitioner (AIF-C01) guides and practice tests | [aws_ai_practitioner_aif_c01/README.md](certifications/aws_ai_practitioner_aif_c01/README.md) |
| [scratch/](scratch/) | Throwaway experiments | |

## Layout

```
dsa/
  docs/                 study guide, study plan, python tricks, complexity reference
  topics/               one folder per topic, numbered problems + *_template.py
data_engineering/
  sql_practice/         python3 run.py --all
  guides/               interview guides (markdown)
certifications/
  aws_ai_practitioner_aif_c01/
scratch/
```

## Quick start

```bash
python3 dsa/topics/array/sliding_window/01_max_average_subarray.py   # one DSA problem
cd data_engineering/sql_practice && python3 run.py --all             # SQL progress board
```
