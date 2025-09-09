# 📊 Week 4 — Day 21: Advanced SQL & Business Queries

## 📝 Overview
On this day of my **Bootcamp Remote**, I worked on advanced SQL topics and applied them to a realistic **Bookstore dataset** (customers, books, categories, orders, and order items).  
The goal was not only to practice syntax but also to extract **business insights** that are valuable in real-world BI / Data Analysis contexts.

---

## 🔧 What I built
- **Database schema** (`schema.sql`) with 5 related tables:
  - Customers, Categories, Books, Orders, Order_Items.
- **Data generation script** (`generate_data.py`) using Faker to create thousands of rows for realistic analysis.
- **SQL practice file** (`queries_practice21.sql`) with advanced queries:
  - JOINs across multiple tables
  - GROUP BY and HAVING
  - Subqueries
  - Aggregations (SUM, AVG, COUNT)
- **Business queries file** (`business_queries.sql`) with **8 business-driven questions**.

---

## 📈 Business Insights Extracted
Examples of insights obtained from the dataset:

1. **Top-selling category** by total sales.  
2. **Countries with the highest sales volume.**  
3. **Average spending per customer.**  
4. **Top 5 best-selling books.**  
5. **Categories surpassing 500 units sold.**  
6. **Customers who spend above the average client spending.**  
7. **Top 3 best-selling books per country** (using window functions).  
8. **Monthly sales trends over the last year.**

---

## 🚀 Skills Practiced
- Writing **complex SQL queries** across multiple tables.
- Using **aggregate functions** (SUM, AVG, COUNT) with `GROUP BY` and `HAVING`.
- Applying **subqueries** and **window functions** (`RANK`, `PARTITION BY`) for advanced analysis.
- Translating **business questions** into SQL queries.
- Organizing code into **clean, professional files** for GitHub portfolio.

---
