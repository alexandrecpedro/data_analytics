import pandas as pd
import streamlit as st

from components.charts import bar_chart, donut_chart
from components.kpis import active_units_kpi, total_appointments_kpi, total_revenue_kpi
from data.data_loader import read_data
from enums.chart_enum import BarChartEnum, DonutChartEnum
from enums.dashboard_enum import DashboardEnum
from enums.data_fields_enum import DataFieldsEnum
from style.styling import kpi_card_style

# ----------------------------------------------------------------------
# DASHBOARD
# ----------------------------------------------------------------------
def dashboard(df: pd.DataFrame):
    """Configures the page, applies filters, and renders all components."""

    # Page Configuration and Initial Styling
    st.set_page_config(page_title=DashboardEnum.PAGE_TITLE.value, layout='wide')

    # --- Apply Background and KPI Styling ---
    # set_background_image("YOUR_IMAGE_URL_HERE")
    kpi_card_style()

    st.title(body=DashboardEnum.TITLE.value)

    # --- Sidebar Filters ---
    # Date Combo
    unique_dates = sorted(df[DataFieldsEnum.APPOINTMENT_DATE.value].dt.strftime('%d-%m-%Y').unique())
    date_option = st.sidebar.selectbox(label='Choose a date: ', options=[DashboardEnum.OPTIONS.value] + unique_dates)

    # Units Combo
    units = sorted(df[DataFieldsEnum.UNIT.value].unique())
    unit_option = st.sidebar.selectbox(label='Choose an unit: ', options=[DashboardEnum.OPTIONS.value] + units)

    # --- Data Filtering ---
    filtered_df = df.copy(deep=True)
    if date_option != DashboardEnum.OPTIONS.value:
        filtered_df = filtered_df[filtered_df[DataFieldsEnum.APPOINTMENT_DATE.value].dt.strftime('%d-%m-%Y') == date_option]

    if unit_option != DashboardEnum.OPTIONS.value:
        filtered_df = filtered_df[filtered_df[DataFieldsEnum.UNIT.value] == unit_option]

    # --- 1. KEY PERFORMANCE INDICATORS (KPIs) ---
    col_kpi1, col_kpi2, col_kpi3 = st.columns(3)

    ## KPI 1: Total Appointments
    total_appointments = total_appointments_kpi(df=filtered_df)
    with col_kpi1:
        st.metric(label=BarChartEnum.UNIT_APPOINTMENTS_YAXIS_LABEL.value, value=total_appointments, delta=None)

    ## KPI 2: Active Units
    active_units = active_units_kpi(df=filtered_df)
    with col_kpi2:
        st.metric(label='Active Units', value=active_units, delta=None)

    ## KPI 3: Total Revenue
    total_revenue = total_revenue_kpi(df=filtered_df)
    with col_kpi3:
        st.metric(label='Total Revenue', value=total_revenue, delta=None)

    # --- 2. CHARTS ---
    ## Define the column distribution
    col1, col2, col3 = st.columns(spec=3)

    ## Chart 1: Total appointments per unit and per date (Bar Chart)
    # col1.subheader(DashboardEnum.BAR_CHART_SUBHEADER.value)
    unit_appointments = filtered_df.groupby(DataFieldsEnum.UNIT.value).size().reset_index(name=DashboardEnum.TOTAL.value)
    unit_appointments_bar_chart = bar_chart(
        df=unit_appointments,
        xaxis=DataFieldsEnum.UNIT.value,
        yaxis=DashboardEnum.TOTAL.value,
        color_field=DataFieldsEnum.UNIT.value,
        title=BarChartEnum.UNIT_APPOINTMENTS_TITLE.value,
        text=DashboardEnum.TOTAL.value,
        xaxis_title=BarChartEnum.UNIT_APPOINTMENTS_XAXIS_LABEL.value,
        yaxis_title=BarChartEnum.UNIT_APPOINTMENTS_YAXIS_LABEL.value,
    )
    # col1.plotly_chart(figure_or_data=unit_appointments_bar_chart, use_container_width=True)
    col1.plotly_chart(figure_or_data=unit_appointments_bar_chart, config={"responsive": True})

    ## Chart 2: Total appointments per unit and per specialty (Donut Chart)
    appointments_type = filtered_df.groupby(DataFieldsEnum.APPOINTMENT_TYPE.value).size().reset_index(name=DashboardEnum.TOTAL.value).copy()
    # appointments_type_bar_chart = bar_chart(
    #     df=appointments_type,
    #     xaxis=DashboardEnum.TOTAL.value,
    #     yaxis=DataFieldsEnum.APPOINTMENT_TYPE.value,
    #     color_field=DataFieldsEnum.APPOINTMENT_TYPE.value,
    #     title=BarChartEnum.APPOINTMENTS_TYPE_TITLE.value,
    #     text=DashboardEnum.TOTAL.value,
    #     xaxis_title=BarChartEnum.APPOINTMENTS_TYPE_XAXIS_TITLE.value,
    #     yaxis_title=BarChartEnum.APPOINTMENTS_TYPE_YAXIS_TITLE.value,
    # )
    appointments_type_donut_chart = donut_chart(
        df=appointments_type,
        category_field=DataFieldsEnum.APPOINTMENT_TYPE.value,
        value_field=DashboardEnum.TOTAL.value,
        title=DonutChartEnum.APPOINTMENTS_TYPE_TITLE.value
    )
    col2.altair_chart(altair_chart=appointments_type_donut_chart, use_container_width=True)

    ## Chart 3: Total value per unit and per day (Bar Chart)
    total_value_unit = filtered_df.groupby(DataFieldsEnum.UNIT.value, as_index=False)[DataFieldsEnum.APPOINTMENT_VALUE.value].sum()
    total_value_unit_bar_chart = bar_chart(
        df=total_value_unit,
        xaxis=DataFieldsEnum.UNIT.value,
        yaxis=DataFieldsEnum.APPOINTMENT_VALUE.value,
        color_field=DataFieldsEnum.UNIT.value,
        title=BarChartEnum.REVENUE_UNITS_TITLE.value,
        text=DataFieldsEnum.APPOINTMENT_VALUE.value,
        xaxis_title=BarChartEnum.REVENUE_UNITS_XAXIS_LABEL.value,
        yaxis_title=BarChartEnum.REVENUE_UNITS_YAXIS_LABEL.value
    )
    # col3.plotly_chart(figure_or_data=total_value_unit_bar_chart, use_container_width=True)
    col3.plotly_chart(figure_or_data=total_value_unit_bar_chart, config={"responsive": True})

    # --- 3. APPOINTMENT DETAILS TABLE ---
    st.subheader(body=f'{DashboardEnum.SUBHEADER.value} : {unit_option}')
    st.dataframe(data=filtered_df, use_container_width=True)

def main():
    df = read_data()
    dashboard(df=df)

if __name__ == '__main__':
    main()