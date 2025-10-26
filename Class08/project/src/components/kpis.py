import pandas as pd
from enums.data_fields_enum import DataFieldsEnum
from utils.formatting import formatted_currency

def total_appointments_kpi(df: pd.DataFrame):
    return df.shape[0]

def active_units_kpi(df: pd.DataFrame):
    return df[DataFieldsEnum.UNIT.value].nunique()

def total_revenue_kpi(df: pd.DataFrame):
    total_revenue = df[DataFieldsEnum.APPOINTMENT_VALUE.value].sum()
    total_revenue_fmt = formatted_currency(currency_value=total_revenue)
    return total_revenue_fmt