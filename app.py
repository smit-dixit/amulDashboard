import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")

dfm = pd.read_excel(
        io="data2.xlsm",
        engine="openpyxl",
        sheet_name="Column Heads",
        usecols="A:D",
        nrows=96,
    )

df = pd.read_excel(
        io="dataSheet.xlsm",
        engine="openpyxl",
        sheet_name="Dash Sheet",
        skiprows=1,
        usecols="A:DE",
        nrows=68,
    )



pd.set_option('display.max_columns', None)

whType = st.sidebar.multiselect(
    "WH Type",
    options=dfm["WHType"].unique()
)

dfm_selection = dfm.query(
    "WHType == @whType"
)

city = st.sidebar.multiselect(
    "Select the City:",
    options=df["Branch"].unique()
)


filtered = st.sidebar.multiselect (
    "Filter columns", 
    options=dfm_selection["Branch"].unique()
)

df_selection = df.query(
    "Branch == @city"
)



#st.sidebar.slider('Height of Warehouse', value=[min(df_selection['Height of Warehouse Roof W1']), max(df_selection['Height of Warehouse Roof W1'])], step = 1.00)

slr = dfm_selection.query("ColoumnRelavance == 1")

st.sidebar.select_slider(str(slr["Branch"][0]), options=(df_selection[str(slr["Branch"][0])].tolist()), value=(df_selection[str(slr["Branch"][0])].tolist()[0], df_selection[str(slr["Branch"][0])].tolist()[-1]) )
st.sidebar.select_slider(str(slr["Branch"][1]), options=(df_selection[str(slr["Branch"][1])].tolist()), value=(df_selection[str(slr["Branch"][1])].tolist()[0], df_selection[str(slr["Branch"][1])].tolist()[-1]) )
st.sidebar.select_slider(str(slr["Branch"][2]), options=(df_selection[str(slr["Branch"][2])].tolist()), value=(df_selection[str(slr["Branch"][2])].tolist()[0], df_selection[str(slr["Branch"][2])].tolist()[-1]) )
st.sidebar.select_slider(str(slr["Branch"][3]), options=(df_selection[str(slr["Branch"][3])].tolist()), value=(df_selection[str(slr["Branch"][3])].tolist()[0], df_selection[str(slr["Branch"][3])].tolist()[-1]) )


test = df_selection.astype(str)

st.table(test[filtered])

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 