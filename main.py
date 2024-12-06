import pandas as pd
import streamlit as st
from collections import Counter

def treat_excel(df):
    columns_to_erase = ['Id. de tarea ', 'Priority', 'Fecha de vencimiento', 'Es periódica', 'Con retraso']
    for column_name in columns_to_erase:
        del df[column_name]

    # Mostrar el dataset cargado
    st.write("El planner que cargaste:")
    st.write(df.head())

    # Vamos a ver qué etiquetas hay
    if 'Etiquetas' in df.columns:
        etiquetas = df['Etiquetas'].dropna()  # Eliminar valores nulos
    
        # Crear una lista para almacenar todas las etiquetas
        lista_etiquetas = []
        for etiqueta in etiquetas:
            # Dividir las etiquetas que vienen separadas por comas y eliminar espacios innecesarios
            lista_etiquetas.extend([e.strip() for e in etiqueta.split(';')])
        
        # Contar las veces que aparece cada etiqueta usando Counter
        conteo_etiquetas = Counter(lista_etiquetas)

        # Mostrar el conteo de etiquetas
        st.write("Conteo de etiquetas únicas:")
        st.write(dict(conteo_etiquetas))