# Sección de importación de módulos
from Modules.UI.header import show_header
from Modules.UI.Data.ecobici_service import EcobiciLoader
import streamlit as st
import pandas as pd

# Sección para crear la GUI
show_header("Mi primera GUI en Streamlit")

ecobici = EcobiciLoader()
df = eco.merge_data()
st.write(df)
