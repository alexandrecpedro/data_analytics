import pandas as pd
import streamlit as st
from enums.chart_enum import BarChartEnum, DonutChartEnum
from enums.dashboard_enum import DashboardEnum
from enums.data_fields_enum import DataFieldsEnum
from ui.styles import UIStyles
from visuals.kpis_cards import KPICalculator
from visuals.charts import ChartBuilder

class DashboardLayout:
    """Defines Streamlit layout and component rendering."""

    def __init__(self, df: pd.DataFrame):
        self.df = df
        # Page Configuration and Initial Styling
        st.set_page_config(page_title=DashboardEnum.PAGE_TITLE.value, layout='wide')
        st.title(body=DashboardEnum.TITLE.value)

    def render(self):
        self._render_filters()
        self._render_kpis()
        self._render_charts()
        self._render_table()

    def _render_filters(self):
        # --- Sidebar Filters ---
        st.sidebar.header("📅 Filters")

        # Date Combo
        unique_dates = sorted(self.df[DataFieldsEnum.APPOINTMENT_DATE.value].dt.strftime('%d-%m-%Y').unique())
        self.date_option = st.sidebar.selectbox(label="Choose a date:", options=[DashboardEnum.OPTIONS.value] + unique_dates)

        # Units Combo
        units = sorted(self.df[DataFieldsEnum.UNIT.value].unique())
        self.unit_option = st.sidebar.selectbox(label="Choose a unit:", options=[DashboardEnum.OPTIONS.value] + units)

    def _filter_data(self):
        # --- Data Filtering ---
        filtered_df = self.df.copy(deep=True)
        if self.date_option != DashboardEnum.OPTIONS.value:
            filtered_df = filtered_df[
                filtered_df[DataFieldsEnum.APPOINTMENT_DATE.value].dt.strftime('%d-%m-%Y') == self.date_option]

        if self.unit_option != DashboardEnum.OPTIONS.value:
            filtered_df = filtered_df[filtered_df[DataFieldsEnum.UNIT.value] == self.unit_option]

        return filtered_df

    def _render_kpis(self):
        # --- KEY PERFORMANCE INDICATORS (KPIs) ---
        UIStyles.apply_kpi_style()

        filtered_df = self._filter_data()
        col_kpi1, col_kpi2, col_kpi3 = st.columns(3)

        ## KPI 1: Total Appointments
        total_appointments = KPICalculator.total_appointments(df=filtered_df)
        with col_kpi1:
            st.metric(label=BarChartEnum.UNIT_APPOINTMENTS_YAXIS_LABEL.value, value=total_appointments, delta=None)

        ## KPI 2: Active Units
        active_units = KPICalculator.active_units(df=filtered_df)
        with col_kpi2:
            st.metric(label='Active Units', value=active_units, delta=None)

        ## KPI 3: Total Revenue
        total_revenue = KPICalculator.total_revenue(df=filtered_df)
        with col_kpi3:
            st.metric(label='Total Revenue', value=total_revenue, delta=None)


    def _render_charts(self):
        # --- CHARTS ---
        ## Define the column distribution
        filtered_df = self._filter_data()
        col1, col2, col3 = st.columns(spec=3)

        ## Chart 1: Total appointments per unit and per date (Bar Chart)
        # col1.subheader(DashboardEnum.BAR_CHART_SUBHEADER.value)
        unit_appointments = filtered_df.groupby(DataFieldsEnum.UNIT.value).size().reset_index(
            name=DashboardEnum.TOTAL.value)
        unit_appointments_bar_chart = ChartBuilder.bar_chart(
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
        appointments_type = filtered_df.groupby(DataFieldsEnum.APPOINTMENT_TYPE.value).size().reset_index(
            name=DashboardEnum.TOTAL.value).copy()
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
        appointments_type_donut_chart = ChartBuilder.donut_chart(
            df=appointments_type,
            category_field=DataFieldsEnum.APPOINTMENT_TYPE.value,
            value_field=DashboardEnum.TOTAL.value,
            title=DonutChartEnum.APPOINTMENTS_TYPE_TITLE.value
        )
        col2.altair_chart(altair_chart=appointments_type_donut_chart, use_container_width=True)

        ## Chart 3: Total value per unit and per day (Bar Chart)
        total_value_unit = filtered_df.groupby(DataFieldsEnum.UNIT.value, as_index=False)[
            DataFieldsEnum.APPOINTMENT_VALUE.value].sum()
        total_value_unit_bar_chart = ChartBuilder.bar_chart(
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

    def _render_table(self):
        # --- APPOINTMENT DETAILS TABLE ---
        filtered_df = self._filter_data()
        st.subheader(body=f'{DashboardEnum.SUBHEADER.value} : {self.unit_option}')
        st.dataframe(data=filtered_df, use_container_width=True)