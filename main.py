import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def treat_excel(df):
    columns_to_erase = ['Id. de tarea ', 'Priority', 'Fecha de vencimiento', 'Es periódica', 'Con retraso']
    for column_name in columns_to_erase:
        del df[column_name]

    # Mostrar el dataset cargado
    st.write("El planner que cargaste:")
    st.write(df.head())

    # Crear la nube de palabras a partir de la columna 'Etiquetas'
    if 'Etiquetas' in df.columns:
        etiquetas = df['Etiquetas'].dropna()  # Eliminar valores nulos
        todas_etiquetas = ','.join(etiquetas)  # Unir todas las etiquetas en un solo string