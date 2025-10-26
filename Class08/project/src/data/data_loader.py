import pandas as pd
import streamlit as st

from enums.database_enum import DatabaseEnum
from enums.data_fields_enum import DataFieldsEnum

# Using Streamlit cache to prevent reload each interaction
@st.cache_data
def read_data():
    # Reading data from file
    try:
        df = pd.read_csv(
            filepath_or_buffer=DatabaseEnum.FILEPATH.value,
            sep=DatabaseEnum.SEPARATOR.value,
            encoding=DatabaseEnum.ENCODING.value,
            parse_dates=[DataFieldsEnum.APPOINTMENT_DATE.value],
        )
        return df
    except FileNotFoundError:
        st.error('File not found.')
        raise