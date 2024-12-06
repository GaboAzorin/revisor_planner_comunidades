import streamlit as st
from main import *

st.title('Asistente revisor de contenidos')
st.markdown('---')
st.html('<h2>¿Cómo funciona?</h2>')
st.html("""<p>Este es un espacio ayuda a la editora y la coordinadora en la revisión de contenidos del equipo.
    De momento, sirve para <strong>revisar las publicaciones de redes sociales</strong> 
    directamente <strong>subiéndole el excel del planner</strong> que actualizan los CMs del equipo (hay que descargarlo y subirlo).</p>""")
st.image("./download_planner_gif.gif", width=450, caption='Así se descarga un excel de un planner.')
st.markdown('---')
st.html('<h2>Sube aquí el planner ⬇</h2>')
uploaded_file = st.file_uploader("Sube acá el planner que descargaste, el excel", type=["xlsx"])

if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)
    treat_excel(data)