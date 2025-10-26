import pandas as pd
from enums.data_fields_enum import DataFieldsEnum
from utils.formatting import formatted_currency

class KPICalculator:
    """Performs calculations for the dashboard KPIs."""

    @staticmethod
    def total_appointments(df: pd.DataFrame):
        return df.shape[0]

    @staticmethod
    def active_units(df: pd.DataFrame):
        return df[DataFieldsEnum.UNIT.value].nunique()

    @staticmethod
    def total_revenue(df: pd.DataFrame):
        total_revenue = df[DataFieldsEnum.APPOINTMENT_VALUE.value].sum()
        total_revenue_fmt = formatted_currency(currency_value=total_revenue)
        return total_revenue_fmt