# 📅 Week 3 Summary (Days 15 to 19)

## Day 15 (Monday)
- **PostgreSQL Introduction**: installation on Ubuntu WSL, creation of user and database `bootcamp_db`.  
- **ER Modeling and Normalization (3NF)** with tables `students`, `courses`, and `enrollments`.  
- Queries using `INNER JOIN` and table/column aliases.  
- **Mini E-commerce Project**:  
  - Created tables `customers`, `products`, `orders`, `order_details`.  
  - Inserted sample data and ran queries for customer totals and top-selling products.

---

## Day 16 (Tuesday)
- Advanced queries in **PostgreSQL** with the `employees` table:  
  - Subqueries, Common Table Expressions (CTEs), and window functions for department-level calculations.  
- Created indexes and interpreted execution plans with `EXPLAIN` and `EXPLAIN ANALYZE` to compare performance with and without indexing on a large dataset (10k rows).  
- Practical SQL exercises including:  
  - Aggregations (`AVG`, `SUM`, `MIN`, `MAX`)  
  - Filtering (`WHERE`), ordering (`ORDER BY`), limits (`LIMIT`)  
  - Subqueries and employee salary ranking.  

---

## Day 17 (Wednesday)
- **Intermediate Python**:  
  - Modules and packages, absolute vs. relative imports.  
  - Professional project organization with `main.py` and submodules (`operations`, `utils`).  
- **Error Handling**: `try/except` with specific and generic exceptions.  
- **Logging**: used the `logging` module with multiple levels (`INFO`, `WARNING`, `ERROR`, `CRITICAL`) and custom formats via `basicConfig`.  
- **Argparse (CLI)**: created terminal-executable scripts with dynamic parameters (`--a`, `--b`, `--op`).  
- **Practical Block (ETL Refactor)**:  
  - Split project into `src/` with `extract.py`, `transform.py`, `load.py`.  
  - Central `main.py` with argparse to run individual steps (`extract`, `transform`, `load`) or the full workflow (`all`).  

---

## Day 19 (Friday)
- **Block 1 (B1):** Created PostgreSQL schema for the **NovaRetail** case study, including primary/foreign keys and relationships among `customers`, `orders`, `order_details`, and `products`.  
- **Block 2 (B2):** Python scripts for data insertion:  
  - `insert_customers.py`, `insert_orders.py`, `insert_order_details.py`, `insert_products.py`  
  - Validation scripts: `data_quality_check.py`, `validate_data.py`  
- **Block 3 (B3):** Built a **Power BI Dashboard** with main KPIs:  
  - Revenue, Orders, Customers, Average Order Value  
  - Sales by category  
  - **Top 5 products by revenue**  

**Deliverables:**
- `NovaRetail_Sales_Dashboard.pbix` → Interactive dashboard  
- `NovaRetail_Sales_Dashboard.png` → Final dashboard preview  

![NovaRetail Dashboard](./day19/B3/NovaRetail_Sales_Dashboard.png)

