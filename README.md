# 📈 StockVision

> **An end-to-end Financial Analytics Dashboard built with Python and Streamlit to analyze stock market performance, technical indicators, and risk metrics through interactive visualizations.**

---
## 🚧 Project Status

**Current Version:** **V1.0**

This project is actively under development.

### Current Scope (V1)

- ✅ End-to-end financial analytics dashboard
- ✅ Historical analysis for **one stock**
- ✅ Technical indicators (MA, RSI, Drawdown, Volatility, Returns)
- ✅ Interactive Streamlit dashboard
- ✅ Deployed application

## 🌐 Live Demo

🔗 **Live Application:** https://stockvison.streamlit.app/

---

## 📸 Dashboard Preview

> *(Replace these with your screenshots after saving them inside the `screenshots/` folder.)*

### Home Dashboard

![Dashboard](screenshots/dashboard.png)

### Price Analysis

![Price Chart](screenshots/price_chart.png)

### Risk Analysis

![Drawdown](screenshots/drawdown.png)

### RSI Analysis

![RSI](screenshots/rsi.png)

---

# 📖 About The Project

StockVision is an end-to-end financial analytics web application developed to help investors and learners analyze historical stock market performance using interactive dashboards.

The application processes historical stock data, performs feature engineering, calculates important financial indicators, and visualizes market behavior to support data-driven investment analysis.

This project follows an industry-inspired analytics workflow:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Financial Analytics
- Dashboard Development
- Deployment

---

# ✨ Features

### 📈 Price Analysis

- Historical Closing Prices
- 20-Day Moving Average
- 50-Day Moving Average

### 📊 Return Analysis

- Daily Returns
- Cumulative Returns

### ⚠ Risk Analysis

- Rolling Volatility
- Drawdown Analysis
- Maximum Drawdown

### 📉 Momentum Analysis

- Relative Strength Index (RSI)

### 🌐 Dashboard

- Interactive Plotly Charts
- Responsive Streamlit Interface
- Sidebar Navigation

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Plotly |
| Dashboard | Streamlit |
| Data Source | yfinance |
| Version Control | Git, GitHub |

---

# 📂 Project Structure

```text
StockVision/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── assets/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── StockVision-EDA.ipynb
│   └── feature_engineering.ipynb
│
└── screenshots/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Van004-ds/StockVision.git
```

Move into the project

```bash
cd StockVision
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📊 Financial Indicators Implemented

- Moving Average (20-Day)
- Moving Average (50-Day)
- Daily Returns
- Cumulative Returns
- Rolling Volatility
- Drawdown
- Maximum Drawdown
- Relative Strength Index (RSI)

---

# 🔮 Future Improvements

- Multi-stock comparison
- Live market data
- Portfolio analytics
- PostgreSQL integration
- Machine Learning-based forecasting
- News sentiment analysis
- User watchlist

---

# 👩‍💻 Author

**Vanshika Negi**

- GitHub: https://github.com/Van004-ds
- LinkedIn: https://www.linkedin.com/in/vanshikanegi/

---

⭐ If you found this project interesting, consider giving it a star!