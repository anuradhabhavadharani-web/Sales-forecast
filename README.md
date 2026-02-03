📊 Sales Forecasting using ARIMA / SARIMA

📌 Project Overview

This project focuses on **time-series sales forecasting** using **ARIMA and SARIMA models**.
It analyzes historical sales data and predicts future sales trends to support **data-driven business decisions**.

The project demonstrates how statistical models can be used to capture **trends and seasonality** in time-dependent data.

🎯 Objectives

* Analyze historical sales data
* Build a time-series forecasting model
* Predict future sales values
* Visualize historical and forecasted sales trends

🛠️ Technologies Used

* **Python**
* **Pandas** → Data preprocessing and date handling
* **Matplotlib** → Data visualization
* **Statsmodels** → ARIMA / SARIMA modeling

📂 Dataset Description

The dataset (`sales.csv`) contains:

* **Date** → Time period of sales
* **Sales** → Sales values

The data is structured as a **time series**, making it suitable for ARIMA/SARIMA modeling.

🧠 Methodology

1. Load sales data from CSV file
2. Convert the date column to datetime format
3. Set the date as the index
4. Apply ARIMA for non-seasonal data
5. Apply SARIMA for seasonal patterns (optional extension)
6. Forecast sales for future time periods
7. Visualize actual vs predicted sales

📈 Models Used

### 🔹 ARIMA (AutoRegressive Integrated Moving Average)

* Suitable for non-seasonal time-series data
* Captures trend and noise

### 🔹 SARIMA (Seasonal ARIMA)

* Extension of ARIMA
* Handles **seasonal patterns** in sales data

▶️ How to Run the Project

### 1️⃣ Install Required Libraries

```bash
pip install pandas matplotlib statsmodels
```

### 2️⃣ Run the Script

```bash
python sales_forecasting.py
```

---

📊 Output

* Line graph showing:

  * Historical sales data
  * Forecasted future sales
* Printed forecasted values with corresponding dates

💼 Business Use Cases

* Sales planning and budgeting
* Inventory management
* Demand forecasting
* Strategic business decision-making

⚠️ Limitations

* Assumes linear patterns in data
* Requires careful parameter tuning
* Performance depends on data quality and stationarity

🔮 Future Enhancements

* Automatic parameter selection using AIC/BIC
* Incorporate external variables (holidays, promotions)
* Build interactive dashboards
* Deploy as a web application

📝 Conclusion

This project demonstrates how **ARIMA and SARIMA models** can be effectively used for **sales forecasting**. It provides valuable insights into future trends and supports informed business decisions using time-series analysis.

👨‍💻 Author

G.Bhavadharani
