# Charger un fichier csv
# Afficher quelques graphiques en fonctions des colonnes sélectionées
# Éditer le jeu de données puis le télécharger

import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="processing exercice",
    page_icon="🧑‍💻",
    layout="wide",
)

graph_types = ["None", "Histogramme", "Nuage de point", "Camembert", "Moustache"]

uploaded_file = st.file_uploader("Choississez un fichier", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    selected_columns = st.multiselect("Sélectionner les colonnes du dataframe", df.columns)
    
    if selected_columns != []:
        edited_df = st.data_editor(df[selected_columns])

    if st.checkbox('Configurer le graphique'):
        
        col1, col2 = st.columns(2)
        
        with col1:
            graph_type = st.selectbox("Sélectionnez le type de graphique que vous voulez afficher :", graph_types)
        
        # Afficher le graphique
        if graph_type == "Histogramme":
            with col2:
                data = st.multiselect("Choisissez une colonne pour l'histogramme :", selected_columns, key='hist')
            
            try:
                plot = sns.histplot(edited_df[data])
                st.pyplot(plot.figure)
            except:
                st.error("Vous avez sélectionné une mauvaise colonne", icon="❌")
        
        elif graph_type == "Nuage de point":
            with col2:
                col_x = st.selectbox("Choisissez la colonne pour l'axe X :", selected_columns)
                col_y = st.selectbox("Choisissez la colonne pour l'axe Y :", selected_columns)
                hue = st.selectbox("Choisissez la colonne pour la variable hue :", selected_columns)
            
            try:
                plot = sns.scatterplot(data=edited_df, x=col_x, y=col_y, hue=hue)
                st.pyplot(plot.figure)
            except:
                st.error("Vous avez sélectionné une mauvaise colonne")
        
        elif graph_type == "Camembert":
            with col2:
                data = st.selectbox("Choisissez une colonne pour le camembert :", selected_columns)
            
            try: 
                fig, ax = plt.subplots()
                edited_df[data].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
                ax.set_ylabel('')
                st.pyplot(fig)
            except:
                st.error("Vous avez sélectionné une mauvaise colonne")
        
        elif graph_type == "Moustache":
            with col2:
                data = st.selectbox("Choisissez une colonne pour le graphique en moustache :", selected_columns)
            
            try:
                plot = sns.boxplot(data=edited_df, x=data)
                st.pyplot(plot.figure)
            except:
                st.error("Vous avez sélectionné une mauvaise colonne")
    
    if selected_columns != []:
        st.download_button(
            "Télécharger les datas en csv",
            data = edited_df.to_csv(),
            file_name = "edited_dataframe.csv",
            mime = "text/csv"
        )