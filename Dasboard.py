import streamlit as st 
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title="My Dashboard",
    page_icon="😎",
    layout="wide",
)

df = pd.read_csv("https://raw.githubusercontent.com/Quera-fr/Python-Programming/refs/heads/main/data.csv")

st.title('My Dashboard')

st.subheader('Presentation de data')

st.write('Presentation des data avec streamlit')

# Datafram
if st.checkbox('Afficher le df'):
    st.write(df)

# Formulaire
if st.checkbox('Afficher le formulaire'):
    name = st.text_input('Entrez votre nom')
    if name != "":
        st.write(f"Salut, {name}")

# Image dans la sidebar
st.sidebar.image("https://cdn.cookielaw.org/logos/09f2ba89-076e-413b-b34f-a8d20370f3f5/35c98a5f-cba8-4b1a-959f-c5a7c260dfda/e0191cfb-2e2a-43c1-a11f-929eb86731a0/logo.png", width=300)

# Video dans la sidebar
st.sidebar.video("https://www.youtube.com/watch?v=LUcyjBQy3vc")

with st.form(key='my_form'):
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Selectionner une profession
        profession = st.selectbox("Sélectionner une profession", df.Profession.unique())
        
        # Selectionner une tranche d'âge
        ages = st.slider(
            'Sélectionner une tranche d\'âge',
            df.Age.min(), df.Age.max(),
            (df.Age.min(), df.Age.max())
        )
        
        submit_button = st.form_submit_button(label='Valider')
        
    with col2:
        # Filter les données en fonction de la profession et de la tranche d'âge
        data_age = df[
            (df.Profession == profession) &
            (df.Age >= ages[0]) &
            (df.Age <= ages[1])
        ].Age
        
        if submit_button:
            plot = sns.histplot(data_age, bins=ages[1]-ages[0] if ages[1]-ages[0] != 0 else 1)
            st.pyplot(plot.figure)