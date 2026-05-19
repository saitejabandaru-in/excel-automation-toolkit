<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:4F7CAC,100:1C2B36&height=180&section=header&text=Excel%20Automation%20Toolkit&fontSize=38&fontColor=E6EEF3&animation=fadeIn&fontAlignY=45" />
</p>

<p align="center">
  📊 Excel + Python Automation &nbsp;|&nbsp; ⚙️ VBA Pipelines &nbsp;|&nbsp; 📈 Business Intelligence
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Excel-Automation-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/Python-Pandas-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/VBA-Macros-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/BI-Dashboards-brightgreen?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat-square"/>
</p>

# 📊 Excel Automation Toolkit

This project is a **hybrid Excel + Python automation framework** built to streamline business reporting, data cleaning, and dashboard generation.

It modernizes Excel by integrating:
- **VBA macros for control & UI**
- **Python + Pandas for data processing**
- **Excel dashboards for decision-making**

This reflects how Excel is used in **real corporate analytics environments**.

---

## 🧠 What this system does

This toolkit automates the entire business analytics workflow:

```
Excel Input Files
   ↓
VBA Macros
   ↓
Python Data Pipelines (Pandas)
   ↓
Processed Data
   ↓
Excel Dashboards
```

No more manual cleaning, copy-pasting, or broken formulas.

---

## ⚙️ Key Features

✔ Automated data import & validation  
✔ VBA-driven workflow execution  
✔ Python-based preprocessing & feature engineering  
✔ Pandas analytics and aggregation  
✔ Auto-generated Excel reports  
✔ Interactive dashboards for business users  

---

## 🗂️ Project Structure

```
excel_automation_toolkit/
  ├── cli.py
  ├── data_loader.py
  ├── preprocessing.py
  ├── feature_engineering.py
  ├── report_generator.py
  ├── dashboard_sync.py
  └── pipeline.py

excel/
  ├── templates/      # Excel templates & dashboards
  └── macros/         # VBA automation scripts

python/
  ├── data_loader.py
  ├── preprocessing.py
  ├── feature_engineering.py
  ├── report_generator.py
  └── dashboard_sync.py

data/
  ├── raw/            # Input files
  └── processed/     # Cleaned & enriched data

tests/
  └── test_pipeline.py
```

---

## 🚀 How to Run

1. Install the package locally from the repository:
```bash
pip install .
```

For development:
```bash
pip install -e ".[dev]"
```

2. Run the sample automation from the command line:
```bash
excel-automation run \
  --input data/raw/sample_sales.csv \
  --output data/processed/automation_report.xlsx \
  --date-column "Order Date" \
  --numeric-column Revenue \
  --numeric-column Units \
  --dimension Region \
  --amount-column Revenue
```

3. Or import the VBA module into your Excel dashboard workbook:
```
excel/macros/RunAutomation.bas
```

4. Click **“Run Automation”**
The VBA macro will:
- Export data
- Trigger Python pipelines
- Re-import clean data
- Refresh dashboards

The generated workbook includes:
- `Raw Data`
- `Processed Data`
- `Summary`
- `Metadata`

You can also run the module directly:

```bash
python -m excel_automation_toolkit run --input data/raw/sample_sales.csv
```

---

## 🧪 Tests

Install development dependencies and run:

```bash
pip install -e ".[dev]"
pytest
```

Build and validate release artifacts:

```bash
python -m build
python -m twine check dist/*
```

Tagged releases are automated through GitHub Actions. Push a semantic version tag such as `v0.1.0` to build the source distribution, wheel, and GitHub release assets.

---

## 📈 What this demonstrates

This project shows strong skills in:

✔ Business automation  
✔ Excel + VBA engineering  
✔ Python data pipelines  
✔ Pandas analytics  
✔ BI dashboarding  
✔ End-to-end workflow design  

This is exactly how **finance, operations, and analytics teams** use Excel at scale.

---

## 👨‍💻 Author

**Sai Teja Bandaru**  
Data Analytics & Automation Engineer

https://www.saitejabandaru.com/

---

## ⭐ If you find this useful
Give the repo a ⭐ — it helps others discover automation-driven analytics!
