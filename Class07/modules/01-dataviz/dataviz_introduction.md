# DATAVIZ - INTRODUCTION

## 1. DATAVIZ

Data Visualization (Data Viz) is the graphical representation of information and data. 
By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way 
to see and understand trends, outliers, and patterns in data.

## 2. DATA STORYTELLING

### 2.1. PLOT TYPES

<table style="background-color:#071625; color:white; width:100%; border-collapse:collapse;">
    <thead>
        <tr>
            <th style="border:1px solid #1e2f5a; padding:8px;">PLOT</th>
            <th style="border:1px solid #1e2f5a; padding:8px;">PLOT TYPE</th>
            <th style="border:1px solid #1e2f5a; padding:8px;">USE CASE</th>
            <th style="border:1px solid #1e2f5a; padding:8px;">EXAMPLES</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">
                <img src="assets/01-bar_plot_img.png" alt="Bar Chart" width=149>
            </td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center; vertical-align:middle;">Bar / Column Chart</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">Used to compare and analyze values across different categories</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">Sales by region; revenue by product category</td>
        </tr>
        <tr>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">
                <img src="assets/02-line_plot_img.png" alt="Line Chart" width=158>
            </td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center; vertical-align:middle;">Line Chart</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">Used to display evolution or trends over time</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">Monthly revenue; performance metrics over time</td>
        </tr>
        <tr>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">
                <img src="assets/03-pie_plot_img.png" alt="Pie or Donut Chart" width=123>
            </td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center; vertical-align:middle;">Pie / Donut Chart</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">Used to show the proportion or share relative to a total value</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">Market share; percentage contribution by category</td>
        </tr>
        <tr>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">
                <img src="assets/04-scatter_plot_img.png" alt="Scatter Chart" width=199>
            </td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center; vertical-align:middle;">Scatter Chart</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">Show the correlation between variables</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">Marketing investment vs. sales</td>
        </tr>
        <tr>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">
                <img src="assets/05-gauge_plot_img.png" alt="Gauge Chart" width=165>
            </td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center; vertical-align:middle;">Gauge Chart</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">Displays progress toward a specific goal</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">% of Targets</td>
        </tr>
        <tr>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">
                <img src="assets/06-gantt_plot_img.png" alt="Gantt Chart" width=100>
            </td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center; vertical-align:middle;">Gantt Chart</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">Track schedules and deadlines</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">Project planning</td>
        </tr>
        <tr>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">
                <img src="assets/07-heatmap_plot_img.png" alt="Heatmap Chart" width="118">
            </td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center; vertical-align:middle;">Heatmap Chart</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">Represents frequency or intensity</td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:center;">Engagement by channel</td>
        </tr>
    </tbody>
</table>

### 2.2. LIBRARIES

<table style="background-color:#071625; color:white; width:100%; border-collapse:collapse; text-align:center; vertical-align:middle;">
    <thead>
        <tr>
            <th style="border:1px solid #1e2f5a; padding:8px;">#</th>
            <th style="border:1px solid #1e2f5a; padding:8px;">LIBRARY NAME</th>
            <th style="border:1px solid #1e2f5a; padding:8px;">DESCRIPTION</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #1e2f5a; padding:8px;">01</td>
            <td style="border:1px solid #1e2f5a; padding:8px;"><b>Matplotlib</b></td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:left;">
                The most traditional library for data visualization in Python. Supports 2D and 3D plots, both static and interactive.
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #1e2f5a; padding:8px;">02</td>
            <td style="border:1px solid #1e2f5a; padding:8px;"><b>Seaborn</b></td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:left;">
                A library built on top of Matplotlib, but with some advantages: simplification and integration with DataFrames.
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #1e2f5a; padding:8px;">03</td>
            <td style="border:1px solid #1e2f5a; padding:8px;"><b>Plotly</b></td>
            <td style="border:1px solid #1e2f5a; padding:8px; text-align:left;">
                A library that stands out for creating <b>interactive and dynamic charts</b>. It allows zooming, point selection, animations, and filters directly within the chart.
            </td>
        </tr>
    </tbody>
</table>

### 2.3. EXAMPLES 

<table style="color:white; border-collapse:collapse; text-align:center; vertical-align:middle;">
    <thead style="background-color:#071625;">
        <tr>
            <th style="border:1px solid #1e2f5a; padding:8px;">#</th>
            <th style="border:1px solid #1e2f5a; padding:8px;">LIBRARY NAME</th>
            <th style="border:1px solid #1e2f5a; padding:8px;">DESCRIPTION</th>
        </tr>
    </thead>
    <tbody style="background-color:#071625;">
        <tr>
            <td style="border:1px solid #1e2f5a; padding:8px;">01</td>
            <td style="border:1px solid #1e2f5a; padding:8px;">Matplotlib</td>
            <td style="border:1px solid #1e2f5a; padding:8px;">
                <a href="examples/matplotlib_chart.ipynb" style="color:#1E90FF; text-decoration:none;">Matplotlib</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #1e2f5a; padding:8px;">02</td>
            <td style="border:1px solid #1e2f5a; padding:8px;">Seaborn</td>
            <td style="border:1px solid #1e2f5a; padding:8px;">
                <a href="examples/seaborn_chart.ipynb" style="color:#1E90FF; text-decoration:none;">Seaborn</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #1e2f5a; padding:8px;">03</td>
            <td style="border:1px solid #1e2f5a; padding:8px;">Plotly</td>
            <td style="border:1px solid #1e2f5a; padding:8px;">
                <a href="examples/plotly_chart.ipynb" style="color:#1E90FF; text-decoration:none;">Plotly</a>
            </td>
        </tr>
    </tbody>
</table>

## 3. BIBLIOGRAPHICAL REFERENCES

- [01] [What is Data Visualization? Definition, Examples and Learning Resources](https://www.tableau.com/visualization/what-is-data-visualization)
- [02] [Matplotlib](https://matplotlib.org/)
- [03] [Seaborn](https://seaborn.pydata.org/)
- [04] [Plotly](https://plotly.com/)