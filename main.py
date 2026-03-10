# Sección de importación de módulos
from Modules.UI.header import show_header
from Modules.UI.Data.ecobici_service import EcobiciLoader
from Modules.viz_service import EcobiciMap
import streamlit as st
import pandas as pd

# Sección para crear la GUI
show_header("Mi primera GUI en Streamlit")

ecobici = EcobiciLoader()
df = ecobici.merge_data()
mapa = EcobiciMap(df)
fig = mapa.create_map()

# Mostrar mapa
st.plotly_chart(fig, use_container_width=True)
