# 🚗 Vehicle Inventory Stratification and Filtration System

## 🎯 1. Project Overview and Objectives

This project focuses on enhancing the vehicle hire firm's data accessibility by developing a robust system for **data stratification** and dynamic inventory querying. The primary goal is to provide end-users with a structured, queryable dataset, ensuring they can efficiently filter and analyse the available vehicle inventory.

### Core Objectives:

1.  **Data Ingestion:** Establish a reliable process for reading and processing the base automotive data repository.
2.  **Stratification:** Return structured listings stratified by **manufacturer**, **year of production**, **specific vehicle model**, and **defined value bands**.
3.  **User Query Capability:** Enable users to efficiently query available vehicles by specifying criteria such as value bands, manufacturing year, and model type.
4.  **Analytical Foundation:** Utilise a rigorous methodology to prepare and analyse the data, ensuring the integrity and quality of the final stratified dataset.

---

## 📈 2. Scope and Business Value

### Enhanced Project Description:

The vehicle hire firm requires the development of a data stratification model specifically designed to enhance user-facing analytical capabilities and improve search efficiency within their fleet inventory.

A high-quality, curated dataset will be generated to permit dynamic, multi-dimensional filtering of vehicles. This capability will enable users to precisely filter the catalogue based on essential attributes, including **specific vehicle model**, **year of manufacture**, and **primary vehicle manufacturer**. This segmentation is crucial for supporting faster, more informed operational decision-making.

---

## 💾 3. Data Source

The project will utilise a standard comma-separated values (CSV) file containing comprehensive vehicle records.

| Data Source             | Description                                                        | Key Attributes                                  | Access Link           |
|:------------------------|:-------------------------------------------------------------------|:------------------------------------------------|:----------------------|
| **base_automoveis.csv** | Contains the core inventory data including vehicle specifications. | Manufacturer, Value (Price), Date of Production | `base_automoveis.csv` |

---

## ⚙️ 4. Technical Roadmap (Proposed Scope)

The following stages outline the technical execution plan for delivering the stratified dataset:

| Category             | Task / Deliverable                                  | Status |
|:---------------------|:----------------------------------------------------|:-------|
| **Data Ingestion**   | Ingestion of the CSV Data Repository                | To Do  |
| **Initial Analysis** | Exploratory Data Analysis (EDA)                     | To Do  |
| **Data Quality**     | Null Value Handling / Imputation                    | To Do  |
| **Transformation**   | Calculation of Averages and Percentages             | To Do  |
| **Filtration**       | Application of Filtration Parameters                | To Do  |
| **Structuring**      | Data Manipulation (Querying, Grouping, and Sorting) | To Do  |
| **Export**           | Data Export (to CSV format)                         | To Do  |

---

## 🛠️ 5. Methodology and Tools

### Technical Approach:

The **Pandas library** in Python will be utilised as the primary tool to execute a rigorous sequence of data pre-analysis and preparation steps (including, but not limited to, data profiling and consistency checks) prior to generating the final, requested stratified data stratum.

### Project Management:

To maintain transparency and ensure seamless workflow integration, the **Trello platform** will be systematically employed for comprehensive project organisation, task allocation, and progress tracking.

[Trello - Project](https://trello.com/b/ImHUT7F5/pandas-course)