import streamlit as st
import pandas as pd
from main import *

#Creo variable de interfaz en True para contar con dos estados: cuando es None,
#se muestra la interfaz normal; cuando sí tiene un archivo, cambia la interfaz (para mostrar las características del planner)

st.title('Asistente revisor de contenidos')
st.markdown('---')
st.html('<h2>¿Cómo funciona?</h2>')
st.html("""<p>Este es un espacio que permite <strong>revisar las publicaciones de redes sociales</strong> 
        directamente <strong>subiéndole el planner</strong> que actualizan los CMs del equipo.</p>""")
st.markdown('---')
st.html('<h2>Sube aquí el planner ⬇</h2>')
uploaded_file = st.file_uploader("Sube acá el planner que descargaste, el excel", type=["xlsx"])

if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)
    treat_excel(data)