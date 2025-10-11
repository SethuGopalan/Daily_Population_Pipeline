# Daily Population Pipeline

**Objective:** Ingest a population CSV daily, clean it, model tables (staged/curated), validate quality, and make it queryable for dashboards.

**Data flow:** raw → staged → curated

**Planned stack:**
- Storage/Compute: DuckDB (file-based)
- Transform: dbt-duckdb
- Orchestrate: Prefect (local)
- Quality: Great Expectations
- Viz: Power BI or Apache Superset (later)

**Milestones:**
1) Scaffold ✅
2) Ingest CSV → raw
3) Data contract & schema checks
4) dbt models (staged/curated)
5) Data tests & expectations
6) Prefect flow (schedule + retries)
7) Dashboard
