import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

data = pd.read_csv("sales.csv")
data["Date"] = pd.to_datetime(data["Date"])
data.set_index("Date", inplace=True)

model = ARIMA(data["Sales"], order=(1, 1, 1))
model_fit = model.fit()

forecast = model_fit.forecast(steps=6)

future_dates = pd.date_range(
    start=data.index[-1] + pd.offsets.MonthEnd(),
    periods=6,
    freq="M"
)

plt.figure(figsize=(10, 5))
plt.plot(data.index, data["Sales"], label="Historical Sales")
plt.plot(future_dates, forecast, label="Forecasted Sales", linestyle="--")
plt.title("Sales Forecasting")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.show()

print("Forecasted Sales:")
for d, s in zip(future_dates, forecast):
    print(d.date(), ":", round(s, 2))
