
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np


def load_data(file_path="sales.csv"):
    """Load and validate monthly sales data."""

    data = pd.read_csv(file_path)

    required_columns = {"Date", "Sales"}
    if not required_columns.issubset(data.columns):
        raise ValueError("CSV must contain Date and Sales columns.")

    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Sales"] = pd.to_numeric(data["Sales"], errors="coerce")

    if data["Date"].isna().any() or data["Sales"].isna().any():
        raise ValueError("Dataset contains invalid or missing values.")

    if data["Date"].duplicated().any():
        raise ValueError("Dataset contains duplicate dates.")

    data = data.sort_values("Date")
    data.set_index("Date", inplace=True)
    data = data.asfreq("ME")

    if len(data) < 12:
        raise ValueError("At least 12 observations are required.")

    return data


def evaluate_model(data, test_size=6):
    """Evaluate ARIMA model using chronological train-test split."""

    train = data["Sales"].iloc[:-test_size]
    test = data["Sales"].iloc[-test_size:]

    model = ARIMA(train, order=(1, 1, 1))
    model_fit = model.fit(method_kwargs={"maxiter": 500})

    print("Evaluation model converged:", model_fit.mle_retvals.get("converged"))

    predictions = model_fit.forecast(steps=test_size)

    mae = mean_absolute_error(test, predictions)
    rmse = np.sqrt(mean_squared_error(test, predictions))

    print("\nModel Evaluation")
    print("----------------")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")

    return mae, rmse


def forecast_sales(data, steps=6):
    """Train on complete data and forecast future sales."""

    model = ARIMA(data["Sales"], order=(1, 1, 1))
    model_fit = model.fit(method_kwargs={"maxiter": 500})

    print("Forecast model converged:", model_fit.mle_retvals.get("converged"))

    forecast = model_fit.forecast(steps=steps)

    future_dates = pd.date_range(
        start=data.index[-1] + pd.offsets.MonthEnd(1),
        periods=steps,
        freq="ME"
    )

    return future_dates, forecast


def main():
    data = load_data()

    evaluate_model(data)

    future_dates, forecast = forecast_sales(data)

    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data["Sales"], label="Historical Sales")
    plt.plot(
        future_dates,
        forecast,
        label="Forecasted Sales",
        linestyle="--"
    )

    plt.title("Sales Forecasting using ARIMA")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print("\nForecasted Sales:")
    for date, sales in zip(future_dates, forecast):
        print(date.date(), ":", round(sales, 2))


if __name__ == "__main__":
    main()
