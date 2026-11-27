
# 📊 Sales Forecasting using ARIMA

## 📌 Project Overview

This project focuses on time-series sales forecasting using the ARIMA (AutoRegressive Integrated Moving Average) model.

It analyzes historical sales data, evaluates forecasting performance, and predicts future sales trends to support data-driven business decisions.

The project includes data validation, model evaluation, and visualization of historical and forecasted sales.

## 🎯 Objectives

- Analyze historical sales data.
- Build an ARIMA time-series forecasting model.
- Evaluate model performance using MAE and RMSE.
- Predict future sales values.
- Validate input data before model training.
- Visualize historical and forecasted sales trends.

## 🛠️ Technologies Used

- **Python** – Programming language.
- **Pandas** – Data preprocessing and date handling.
- **NumPy** – Numerical operations.
- **Matplotlib** – Data visualization.
- **Statsmodels** – ARIMA modeling.
- **Scikit-learn** – Model evaluation metrics.
- **Unittest** – Automated testing.

## 📂 Dataset Description

The dataset (`sales.csv`) contains:

- **Date** – Date of the recorded sales.
- **Sales** – Corresponding sales values.

The data is structured as a time series with monthly observations.

## 🧠 Methodology

1. Load historical sales data from the CSV file.
2. Validate required columns, dates, and sales values.
3. Convert dates into datetime format.
4. Set the date column as the time-series index.
5. Split the data chronologically into training and testing sets.
6. Train an ARIMA(1,1,1) model.
7. Evaluate predictions using MAE and RMSE.
8. Retrain the model using the complete dataset.
9. Forecast sales for the next six months.
10. Visualize historical and forecasted sales.

## 📈 Model Used

### ARIMA (AutoRegressive Integrated Moving Average)

ARIMA is a statistical forecasting model suitable for non-seasonal time-series data.

The project uses the ARIMA(1,1,1) configuration:

- **p = 1:** Autoregressive order.
- **d = 1:** Differencing order.
- **q = 1:** Moving average order.

## 📊 Model Evaluation

The model is evaluated using a chronological train-test split, where the latest six observations are reserved for testing.

The following metrics are calculated:

- **Mean Absolute Error (MAE):** Measures the average absolute difference between actual and predicted sales.
- **Root Mean Squared Error (RMSE):** Measures prediction error while giving greater weight to larger errors.

The metrics help assess the forecasting performance on unseen observations.

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <repository-url>
cd Sales-forecast
```

### 2. Install required libraries

```bash
python -m pip install pandas numpy matplotlib statsmodels scikit-learn
```

### 3. Run the forecasting script

```bash
python pep1.py
```

The program displays model evaluation metrics, generates a six-month sales forecast, and plots historical and forecasted sales.

## 🧪 Running Automated Tests

The project includes automated tests for data validation and forecasting functionality.

Run the tests using:

```bash
python -m unittest discover -s tests -v
```

The test suite checks:

- Valid dataset loading.
- Missing required columns.
- Invalid dates and sales values.
- Duplicate dates.
- Six-month forecast generation.

## 💼 Business Use Cases

- Sales planning and budgeting.
- Inventory management.
- Demand forecasting.
- Strategic business decision-making.

## ⚠️ Limitations

- Forecasting accuracy depends on historical data quality.
- ARIMA does not explicitly model seasonal patterns.
- Model performance depends on parameter selection.
- More historical observations may be needed for reliable long-term forecasts.

## 🔮 Future Enhancements

- Implement SARIMA for seasonal forecasting.
- Automatic parameter selection using AIC/BIC.
- Incorporate external variables such as holidays and promotions.
- Build interactive dashboards.
- Deploy as a web application.

## 📝 Conclusion

This project demonstrates time-series sales forecasting using ARIMA. By combining data validation, model evaluation, forecasting, and visualization, it provides a foundation for data-driven business decisions.

## 👨‍💻 Author

G. Bhavadharani
