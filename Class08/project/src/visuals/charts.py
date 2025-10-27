import altair as alt
import pandas as pd
import plotly.express as px

from enums.chart_enum import DonutChartEnum
from enums.data_fields_enum import DataFieldsEnum
from enums.dashboard_enum import DashboardEnum

class ChartBuilder:
    """Creates and customizes Plotly and Altair charts."""

    @staticmethod
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
        """Building bar chart with visible gridlines and extended top grid line"""
        fig = px.bar(
            data_frame=df,
            x=xaxis,
            y=yaxis,
            color=color_field,
            title=title,
            text=text,
        )

        # --- Generate an additional grid line ---
        y_max = df[yaxis].max()
        tick_step = (y_max / 5) if y_max > 0 else 0
        y_max_extended = y_max + tick_step

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
                range=[0, y_max_extended],
            )
        )

        return fig

    @staticmethod
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

    @staticmethod
    def pie_chart(
            df: pd.DataFrame,
            names: str,
            values: str,
            title: str,
            title_font_size: int,
            title_font_color: str,
            title_x: float,
            paper_bgcolor: str,
            plot_bgcolor: str,
            font_color: str,
            legend_font_color: str,
            legend_bgcolor: str,
            hole: float = 0.0,
            color_discrete_sequence: list[str] = px.colors.qualitative.Set3,
    ):
        """Building pie chart"""
        chart = px.pie(
            data_frame=df,
            names=names,
            values=values,
            title=title,
            hole=hole,
            color_discrete_sequence=color_discrete_sequence,
        )

        chart.update_layout(
            title_x=title_x,
            title_font=dict(size=title_font_size, color=title_font_color),
            paper_bgcolor=paper_bgcolor,
            plot_bgcolor=plot_bgcolor,
            font=dict(color=font_color),
            legend=dict(
                font=dict(color=legend_font_color),
                bgcolor=legend_bgcolor,
            )
        )

        return chart

