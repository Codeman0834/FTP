# Team Final Project (TFP): AR-to-Revenue Forensic Analysis

## 📌 Project Overview
This project analyzes **Accounts Receivable (AR)** relative to **Revenue** using the SEC **2009 Q4 Financial Statement Data** (`sub.txt`, `num.txt`, `tag.txt`). The goal is to identify **potential anomalies** in the AR-to-Revenue ratio using both descriptive analytics and machine learning techniques.

The project investigates:
- How AR compares to Revenue across companies
- Whether unusually high AR-to-Revenue values act as red flags
- Which firms show abnormal behavior using **One-Class SVM anomaly detection**
- How patterns appear visually in line graphs, boxplots, and scatterplots

The analysis helps evaluate potential **earnings manipulation** and **financial reporting quality**.

---

## 📂 Project Structure
```
TFP/
├── Data/               # Raw SEC files (sub.txt, num.txt, tag.txt)
├── Figures/            # Saved figures: boxplots, line graphs, scatterplots
├── TFP.ipynb           # Main notebook with full analysis
└── README.md           # Project documentation
```

---

## 🧪 Methods Used
### **1. Data Preparation**
- Loaded SEC 2009 Q4 datasets (`sub`, `num`)
- Merged on `adsh` (unique filing identifier)
- Filtered tags containing `"Revenue"` and `"Receivable"`
- Calculated AR-to-Revenue ratio per company

### **2. Data Cleaning**
- Removed missing / zero revenue values
- Handled duplicate tagged values
- Converted report values to numeric

### **3. Feature Engineering**
- Created variable: 
  ```python
  paired['AR_to_Revenue'] = paired['AR'] / paired['Revenue']
  ```

### **4. Outlier Detection**
Used **One-Class SVM** to identify suspicious observations:
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
ocsvm = OneClassSVM(kernel="rbf", gamma="auto", nu=0.05)
```
- `anomaly = -1` → suspicious
- `anomaly = 1` → normal

### **5. Visualizations Generated**
- **Boxplot** of AR-to-Revenue
- **Line graph** of AR and Revenue trends
- **Scatterplot** highlighting anomalies
- **Line graph** of average AR vs average Revenue

All figures saved to the **Figures/** folder.

---

## 📊 Key Findings
- Most firms show **AR-to-Revenue ratios near zero** (normal).
- A small cluster shows **extremely high AR-to-Revenue**, flagged by the model.
- These outliers often correspond to firms with abnormally low reported revenue.
- The One-Class SVM successfully isolates high-risk filings.

---

## 🛠️ Technologies Used
- Python 3.x
- pandas, numpy
- matplotlib
- scikit-learn (OneClassSVM, StandardScaler)
- Jupyter Notebook
- SEC EDGAR dataset (2009 Q4)

---

## 📈 Figures Included (examples)
- `boxplot_ar_to_revenue.png`
- `linegraph_ar_revenue.png`
- `avg_linegraph.png`
- `scatter_anomalies.png`

---

## ✔️ Conclusion
The TFP project demonstrates how **forensic analytics** can identify unusual financial reporting across companies using:
- Ratio analysis
- Visualization
- Machine learning anomaly detection

This workflow can be extended to:
- Other financial ratios (Inventory/COGS, Payables/Expenses)
- Multiple fiscal periods
- Multi-company comparisons

---

## 📬 Contact / Info
Questions about the analysis or dataset can be directed to:
**Cody Schnetzler** – Data Science Major (University of Arkansas)

---

## 🚀 Next Steps
- Add more SEC time periods (2008–2010)
- Implement a Random Forest anomaly baseline
- Build dashboard using Plotly or R Shiny
