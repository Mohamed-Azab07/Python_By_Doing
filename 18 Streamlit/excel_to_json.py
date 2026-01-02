import streamlit as st
import pandas as pd
from io import StringIO

def convert_excel_to_json(excel_file):
    df = pd.read_excel(excel_file)
    csv_data = df.to_csv(index=False)
    return StringIO(csv_data)


st.title("Excel to CSV Converter")
st.write("Upload an Excel file to convert it to CSV format")


uploaded_file = st.file_uploader("Choose an Excel file:", type=["xlsx", "xls"])




if uploaded_file is not None:
    csv_df = convert_excel_to_json(uploaded_file)
    st.dataframe(csv_df)
    st.download_button(label="Download CSV", data=csv_df, file_name="europe.csv", mime='text/csv')