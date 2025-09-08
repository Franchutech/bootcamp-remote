
---

# 📂 **B3/README.md**

```markdown
# Titanic ETL Pipeline — End-to-End Documentation

## Overview
This project implements a complete **ETL pipeline** on the Titanic dataset.  
The goal is to demonstrate data engineering and analysis practices, preparing the dataset for advanced analytics and visualization.

## Pipeline Stages

### 1. Extract
- Source: `titanic.csv` (raw dataset)
- Tool: Pandas (`pd.read_csv`)

### 2. Transform
Data cleaning and enrichment applied with Pandas:
- Normalized categorical variables (`Sex`, `Embarked`, `Pclass`)
- Imputed missing values (`Age`, `Cabin`, `Embarked`)
- Derived new features:
  - `Pclass_Label`
  - `Title` (from Name)
  - `Deck` (from Cabin)
  - `Cabin_Number`
  - `Location_Longitude` (Forward / Aft)
  - `Location_Lateral` (Port / Starboard)
  - `Has_Lifeboat_Access` (historical enrichment)
  - `FamilySize`

### 3. Load
- Target: PostgreSQL database
- Schema: `public`
- Table: `titanic_clean`
- Method: SQLAlchemy + Pandas `to_sql`

## Pipeline Diagram
```mermaid
flowchart TD
    A[Extract: Titanic CSV] --> B[Transform with Pandas]
    B --> |Cleaning & Feature Engineering| C[Load to PostgreSQL]
    C --> D[Public Schema: titanic_clean Table]
