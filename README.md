# Industrial Quality Analysis 🏭📊

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-SQLite-lightgrey?logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C8CBF)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

## 📌 Business Problem

Manufacturing companies lose significant revenue to rework, scrap, and undetected defect patterns. This project simulates a **real-world quality control scenario** in an industrial production environment, using data analysis to answer critical business questions:

- Which production lines have the highest defect rates?
- Are defects increasing or decreasing over time?
- Which defect types account for the majority of quality issues (Pareto 80/20)?
- Which shifts and lines concentrate the most non-conformities?
- What is the estimated rework cost per production line?

> 💡 **Context:** This project draws on 10+ years of hands-on experience analyzing industrial KPIs and operational processes in a manufacturing environment — translating domain expertise into data-driven insights.

---

## 🗂️ Project Structure

```
analise-qualidade-industrial/
│
├── data/                  # Raw and processed datasets
├── sql/                   # SQL queries for business analysis
├── scripts/               # Python scripts for analysis and visualization
├── outputs/               # Generated charts and visualizations
├── generate_data.py       # Synthetic dataset generator (1,000 inspection records)
└── README.md
```

---

## 🔧 Methodology

| Step | Description | Tool |
|------|-------------|------|
| 1. Data Generation | Simulated manufacturing dataset with 1,000 inspection records | Python |
| 2. Storage | Relational database with tables: products, lines, inspections | SQLite |
| 3. SQL Analysis | Business queries: defect rate, rework cost, trends | SQL |
| 4. Python Analysis | Data manipulation, cleaning, and statistical exploration | Pandas |
| 5. Visualization | Trend charts, Pareto, and Heatmaps | Matplotlib / Seaborn |

---

## 🔍 SQL Analysis — Key Business Queries

Five core queries were built to answer operational questions directly:

1. **Defect rate by production line** — identify which lines need priority intervention
2. **Monthly defect trend** — detect seasonality or recurring problems
3. **Most frequent defect types** — support Pareto prioritization
4. **Defects by shift** — identify whether night/morning shifts show different patterns
5. **Estimated rework cost per line** — quantify financial impact and support maintenance decisions

---

## 📊 Results & Visualizations

### Defect Trend Over Time
Monthly tracking of non-conformities to detect seasonality and recurring issues.

![Defect Trend](outputs/tendencia_defeitos.png)

---

### Pareto Chart — Defect Types
Applying the 80/20 rule to identify which defect types drive the majority of quality problems.

![Pareto Chart](outputs/pareto_defeitos.png)

---

### Heatmap — Defects by Shift × Production Line
Visual representation of where and when defects occur most frequently — enabling targeted corrective action.

![Heatmap](outputs/heatmap_defeitos.png)

---

## 📈 Business Conclusions

- **Production lines with highest defect rates were identified via SQL**, enabling focused maintenance and process review.
- **Rework cost analysis** helped prioritize which lines and products require urgent intervention.
- **Night shift showed distinct defect patterns**, suggesting the need for targeted training or review of lighting and process conditions.
- The **Pareto analysis confirmed that ~3 defect types account for over 80% of non-conformities** — a clear signal for where quality investment should focus.

---

## 🛠️ Tech Stack

- **Python** (Pandas, Matplotlib, Seaborn)
- **SQL** (SQLite)
- **GitHub** (version control & portfolio)

---

## 👤 About the Author

Data Analyst with 10+ years of experience in industrial operations and process analysis. Transitioning into a full data analytics role, combining domain expertise in manufacturing with hands-on skills in SQL, Python, and BI tools.

🔗 [LinkedIn](https://www.linkedin.com/in/edinaldo-abreu) · [GitHub](https://github.com/NaldoAbreu)
