import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv") #Lectura de datos

st.header('Análisis de anuncios de automóviles') #Encabezado 

# crear una casilla de verificación
histogram_model = st.checkbox('¿Cuales son modelos de los autos mas anunciados')

if histogram_model: # al seleccionar la casilla de verificación
            # escribir un mensaje
            st.write('Construir un histograma para la columna model')
            
            # crear un histograma
            fig = px.histogram(car_data, x="model")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

histogram_fuel = st.checkbox('¿Cual es el combustible mas utilizados por los autos anunciados?')
if histogram_fuel: # al seleccionar la casilla de verificación
            # escribir un mensaje
            st.write('Construir un histograma para la columna fuel')
            
            # crear un histograma
            fig = px.histogram(car_data, x="fuel")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
histogram_type = st.checkbox('¿Cuales son los tipos de autos mas anunciados?')
if histogram_type: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Construir un diagrama de dispersión para la columna price')

            # crear un diagrama de dispersión
            fig = px.histogram(car_data, x="type") # crear un gráfico de dispersión

            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
dispersion_price = st.checkbox('¿Cual es el rango de precios anunciados?')
if dispersion_price: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Construir un diagrama de dispersión para la columna price')

            # crear un diagrama de dispersión
            fig = px.scatter(car_data, y="price") # crear un gráfico de dispersión

            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)