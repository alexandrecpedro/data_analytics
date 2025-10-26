import streamlit as st

def kpi_card_style():
    """
    Injects CSS to customize the Key Performance Indicator (KPI) cards
    for dark mode and central alignment.
    """
    st.markdown("""
        <style>
            /* Main KPI Container Style (Background, Border) */
            div[data-testid="stMetric"] {
                padding: 10px 0;
                margin: 0;
                border: 1px solid #333333;
                border-radius: 5px;
                background-color: #1a1a1a; /* Custom dark background */
                text-align: center !important;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }

            /* Metric Label (Ensures central alignment and white color) */
            div[data-testid="stMetricLabel"] {
                color: #ffffff !important;
                font-size: 1.1rem !important;
                font-weight: 500 !important;
                text-align: center !important;
                display: block;
                margin-bottom: 5px;
            }

            /* Metric Value (Ensures central alignment, font size, and green color) */
            div[data-testid="stMetricValue"] {
                width: 100%;
                text-align: center !important;
                font-size: 2.5rem;
                color: #4CAF50 !important; /* Green value color */
            }
        </style>
    """,
    unsafe_allow_html=True)

def set_background_image(image_url: str):
    """
    Applies a background image to the Streamlit application using CSS injection.

    The image is retrieved via a public URL, covering the entire view.
    """
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover; 
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )