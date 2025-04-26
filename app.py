import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv("C:\\Users\\MANUEL CONTRERAS\\Documents\\autos\\autos\\vehicles_us.csv") #Leer datos

st.header('Vehiculos') #Encabezado 

hist_button = st.button('Construir histograma') #Boton para crear histograma

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)
