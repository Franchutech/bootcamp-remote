# Titanic ETL — Data Exploration and Cleaning Decisions

## General Information
- Rows: 891
- Columns: 12
- Data types: 5 object, 5 int64, 2 float64
- Missing values:
  - Age → 177 nulls (714 complete records)
  - Cabin → 687 nulls (204 complete records)
  - Embarked → 2 nulls (889 complete records)

## Column Observations
- **PassengerId** → Unique identifier, complete.
- **Survived** → Target variable (0 = did not survive, 1 = survived), complete.
- **Pclass** → 3 categories (1, 2, 3), complete.
- **Name** → Complete, includes titles (Mr, Mrs…), useful for deriving additional features.
- **Sex** → 2 categories (`male`, `female`), complete.
- **Age** → 177 nulls, requires imputation.
- **SibSp** → Number of siblings/spouses aboard, complete.
- **Parch** → Number of parents/children aboard, complete.
- **Ticket** → Text, complete, requires further evaluation.
- **Fare** → Ticket fare, continuous numeric, complete.
- **Cabin** → 687 nulls, 147 unique values, can be split into `Deck` and `Cabin_Number`.
- **Embarked** → 2 nulls, categories `S`, `C`, `Q`.

## Cleaning Decisions

- **PassengerId** → Keep only as row identifier, not relevant for analysis.
- **Survived** → Keep as-is, target variable.
- **Pclass** → Keep numeric values, but derive `Pclass_Label`:
  - 1 → "First Class"  
  - 2 → "Second Class"  
  - 3 → "Third Class"
- **Name** → Keep, later derive `Title` (Mr, Mrs, Miss, Master, etc.).
- **Sex** → Normalize to capitalized `"Male"` / `"Female"`.
- **Age** → Impute nulls with historically plausible values:
  - Use `Parch` and `SibSp` to ensure coherence (parents cannot be underage, etc.).
  - Use `Title` in `Name` to guide realistic age ranges (e.g., *Master* = child).
- **SibSp & Parch** → Keep, also derive new column `FamilySize = SibSp + Parch + 1`.
- **Ticket** → Keep for now, may help to detect passenger groups.
- **Fare** → Keep, no missing values.
- **Cabin** → Impute missing values using historically informed logic:
  - Derive `Deck` from the cabin prefix.
  - Fill missing values randomly but respecting real historical distribution per class:
    - Decks A, B, C → mostly 1st class  
    - Decks D, E → mixed  
    - Decks F, G → mostly 2nd/3rd class
  - Derive new features:
    - `Cabin_Number` (numeric part of cabin)
    - `Location_Longitude` (Forward / Aft)
    - `Location_Lateral` (Port / Starboard)
- **Embarked** → Normalize to full port names:
  - "S" → "Southampton"  
  - "C" → "Cherbourg"  
  - "Q" → "Queenstown"  
  Fill nulls with mode (most frequent).

## Historical Enrichment
- **Cabin Position:** Low numbers → Forward; high numbers → Aft.  
  Even numbers → Port; odd numbers → Starboard.
- **Lifeboat Access:** Lifeboats were only on the **Boat Deck**. Derived column `Has_Lifeboat_Access` marks True/False.

---
