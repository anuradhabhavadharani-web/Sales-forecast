
import unittest
import os
import tempfile
import pandas as pd

from pep1 import load_data, forecast_sales


class TestSalesForecasting(unittest.TestCase):

    def setUp(self):
        self.sample_data = pd.DataFrame({
            "Date": pd.date_range(
                start="2022-01-31",
                periods=18,
                freq="ME"
            ),
            "Sales": range(100, 118)
        })

    def create_temp_csv(self, data):
        temp_file = tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".csv",
            delete=False
        )
        data.to_csv(temp_file.name, index=False)
        temp_file.close()
        return temp_file.name

    def test_valid_data_loading(self):
        file_path = self.create_temp_csv(self.sample_data)

        try:
            data = load_data(file_path)
            self.assertEqual(len(data), 18)
            self.assertIn("Sales", data.columns)
        finally:
            os.remove(file_path)

    def test_missing_columns(self):
        invalid_data = pd.DataFrame({
            "Date": ["2022-01-31"],
            "Revenue": [100]
        })

        file_path = self.create_temp_csv(invalid_data)

        try:
            with self.assertRaises(ValueError):
                load_data(file_path)
        finally:
            os.remove(file_path)

    def test_invalid_values(self):
        invalid_data = pd.DataFrame({
            "Date": ["invalid-date"],
            "Sales": ["invalid-sales"]
        })

        file_path = self.create_temp_csv(invalid_data)

        try:
            with self.assertRaises(ValueError):
                load_data(file_path)
        finally:
            os.remove(file_path)

    def test_duplicate_dates(self):
        invalid_data = pd.DataFrame({
            "Date": ["2022-01-31", "2022-01-31"],
            "Sales": [100, 110]
        })

        file_path = self.create_temp_csv(invalid_data)

        try:
            with self.assertRaises(ValueError):
                load_data(file_path)
        finally:
            os.remove(file_path)

    def test_six_month_forecast(self):
        data = self.sample_data.copy()
        data.set_index("Date", inplace=True)
        data = data.asfreq("ME")

        future_dates, forecast = forecast_sales(data, steps=6)

        self.assertEqual(len(future_dates), 6)
        self.assertEqual(len(forecast), 6)


if __name__ == "__main__":
    unittest.main()
