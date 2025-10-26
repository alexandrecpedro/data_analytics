import altair as alt
import pandas as pd
import plotly.express as px
import streamlit as st

from enums.chart_enum import BarChartEnum, DonutChartEnum
from enums.database_enum import DatabaseEnum
from enums.dashboard_enum import DashboardEnum
from enums.data_fields_enum import DataFieldsEnum

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

def bar_chart(
        df: pd.DataFrame,
        xaxis: str,
        yaxis: str,
        color_field: str,
        title: str,
        text: str,
        xaxis_title: str,
        yaxis_title: str
):
    """Building bar chart"""
    fig = px.bar(
        data_frame=df,
        x=xaxis,
        y=yaxis,
        color=color_field,
        title=title,
        text=text,
    )

    fig.update_layout(
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        xaxis=dict(
            showgrid=False,
            color='white',               # cor dos ticks no dark mode
            title=xaxis_title,
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='gray',  # grid sutil para dark mode
            gridwidth=1,
            color='white',  # cor dos ticks no dark mode
            title=yaxis_title,
        )
    )

    return fig

def donut_chart(
        df: pd.DataFrame,
        category_field: str,
        value_field: str,
        title: str
):
    """Building donut chart with real rotation via Vega-Lite spec"""
    # 1. Calculate Percentages
    df[DonutChartEnum.PERCENTAGE.value] = df[value_field] / df[value_field].sum()

    # 2. Base Chart
    theta = alt.Theta(value_field, stack=True)
    title = alt.Title(text=title, anchor='start') # anchor - aligns the title from the left
    base = alt.Chart(data=df).encode(theta=theta).properties(title=title)

    # 3. Donut Chart
    mark_arc_inner_radius = DonutChartEnum.MARK_ARC_INNER_RADIUS.value
    mark_arc_outer_radius = DonutChartEnum.MARK_ARC_OUTER_RADIUS.value

    domain = sorted(df[DataFieldsEnum.APPOINTMENT_TYPE.value].unique())
    colors_map = alt.Scale(
        domain=domain,
        range=['#0F4C81', '#74B3CE', '#FF0000', '#FFB3BA']
    )

    mark_arc_color_legend_title = DonutChartEnum.APPOINTMENTS_TYPE_LEGEND_TITLE.value
    mark_arc_color_legend = alt.Legend(title=mark_arc_color_legend_title)
    mark_arc_color = alt.Color(category_field, scale=colors_map, legend=mark_arc_color_legend)

    mark_arc_order = alt.Order(value_field, sort='descending')

    percentage = DonutChartEnum.PERCENTAGE.value
    percentage_fmt = DonutChartEnum.APPOINTMENTS_TYPE_FORMAT_VALUES.value

    mark_arc_tooltip_appointment_type = alt.Tooltip(category_field, title=DonutChartEnum.APPOINTMENTS_TYPE_TOOLTIP_TITLE.value)
    mark_arc_tooltip_total = alt.Tooltip(value_field, title=DashboardEnum.TOTAL.value)
    mark_arc_tooltip_percentage = alt.Tooltip(percentage, format=percentage_fmt, title=percentage)
    mark_arc_tooltip = [
        mark_arc_tooltip_appointment_type,
        mark_arc_tooltip_total,
        mark_arc_tooltip_percentage
    ]

    donut = (base.mark_arc(outerRadius=mark_arc_outer_radius, innerRadius=mark_arc_inner_radius)
        .encode(color=mark_arc_color, order=mark_arc_order, tooltip=mark_arc_tooltip)
    )

    # 4. Add percentage text (Data Labels)
    mark_text_radius = DonutChartEnum.MARK_TEXT_RADIUS.value
    mark_text_text = alt.Text(percentage, format=percentage_fmt)
    mark_text_order = alt.Order(value_field, sort='descending')
    mark_text_color = alt.value(DonutChartEnum.MARK_TEXT_COLOR.value)

    text = (base.mark_text(radius=mark_text_radius)
        .encode(text=mark_text_text, order=mark_text_order, color=mark_text_color)
    )

    final_chart = donut + text
    return final_chart

def dashboard(df: pd.DataFrame):
    # Setting page layout
    st.set_page_config(page_title=DashboardEnum.PAGE_TITLE.value, layout='wide')
    st.title(body=DashboardEnum.TITLE.value)

    # Date Combo
    unique_dates = sorted(df[DataFieldsEnum.APPOINTMENT_DATE.value].dt.strftime('%d-%m-%Y').unique())
    date_option = st.sidebar.selectbox(label='Choose a date: ', options=[DashboardEnum.OPTIONS.value] + unique_dates)

    # Units Combo
    units = sorted(df[DataFieldsEnum.UNIT.value].unique())
    unit_option = st.sidebar.selectbox(label='Choose an unit: ', options=[DashboardEnum.OPTIONS.value] + units)

    # Apply filters
    filtered_df = df.copy(deep=True)
    if date_option != DashboardEnum.OPTIONS.value:
        filtered_df = filtered_df[filtered_df[DataFieldsEnum.APPOINTMENT_DATE.value].dt.strftime('%d-%m-%Y') == date_option]

    if unit_option != DashboardEnum.OPTIONS.value:
        filtered_df = filtered_df[filtered_df[DataFieldsEnum.UNIT.value] == unit_option]

    # Building Charts
    ## Define the column distribution
    col1, col2, col3 = st.columns(spec=3)

    ## Total appointments per unit and per date (Bar Chart)
    # col1.subheader(DashboardEnum.BAR_CHART_SUBHEADER.value)
    unit_appointments = filtered_df.groupby(DataFieldsEnum.UNIT.value).size().reset_index(name=DashboardEnum.TOTAL.value)
    unit_appointments_bar_chart = bar_chart(
        df=unit_appointments,
        xaxis=DataFieldsEnum.UNIT.value,
        yaxis=DashboardEnum.TOTAL.value,
        color_field=DataFieldsEnum.UNIT.value,
        title=f'{BarChartEnum.UNIT_APPOINTMENTS_TITLE.value} ({date_option})',
        text=DashboardEnum.TOTAL.value,
        xaxis_title=BarChartEnum.UNIT_APPOINTMENTS_XAXIS_LABEL.value,
        yaxis_title=BarChartEnum.UNIT_APPOINTMENTS_YAXIS_LABEL.value,
    )
    col1.plotly_chart(figure_or_data=unit_appointments_bar_chart, use_container_width=True)

    ## Total appointments per unit and per specialty (Donut Chart)
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

    ## Total value per unit and per day (Bar Chart)
    total_value_unit = filtered_df.groupby(DataFieldsEnum.UNIT.value, as_index=False)[DataFieldsEnum.APPOINTMENT_VALUE.value].sum()
    total_value_unit_bar_chart = bar_chart(
        df=total_value_unit,
        xaxis=DataFieldsEnum.UNIT.value,
        yaxis=DataFieldsEnum.APPOINTMENT_VALUE.value,
        color_field=DataFieldsEnum.UNIT.value,
        title=BarChartEnum.REVENUE_UNITS_TITLE.value,
        text=DataFieldsEnum.APPOINTMENT_VALUE.value,
        xaxis_title=BarChartEnum.REVENUE_UNITS_XAXIS_LABEL.value,
        yaxis_title=BarChartEnum.REVENUE_UNITS_YAXIS_LABEL.value,
    )
    col3.plotly_chart(figure_or_data=total_value_unit_bar_chart, use_container_width=True)

    ## Appointment details
    st.subheader(body=f'{DashboardEnum.SUBHEADER.value} : {unit_option}')
    st.dataframe(data=filtered_df, use_container_width=True)

def main():
    df = read_data()
    dashboard(df=df)

if __name__ == '__main__':
    main()