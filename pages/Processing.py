import streamlit as st 
import pandas as pd

uploaded_file = st.file_uploader("Choississez un fichier", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    selected_columns = st.multiselect("Sélectionnez les colonnes du dataframe", df.columns)
    
    edited_df = st.data_editor(df[selected_columns])
    
    st.download_button(
        "Télécharger les datas en csv",
        data = edited_df.to_csv(),
        file_name = "edited_dataframe.csv",
        mime = "text/csv"
    )