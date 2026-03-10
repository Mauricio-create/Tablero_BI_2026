from Modules.UI.header import show_header
from Modules.UI.Data.ecobici_service import EcobiciLoader
from Modules.Viz.viz_service import EcobiciMap
from Modules.Viz.waffle_service import EcobiciWaffle

import streamlit as st


st.set_page_config(layout="wide")

show_header("Mi primera GUI en Streamlit")

# =========================
# Cargar datos
# =========================

ecobici = EcobiciLoader()
df = ecobici.merge_data()

# =========================
# Crear visualizaciones
# =========================

mapa = EcobiciMap(df)
fig_map, estacion = mapa.create_map()
waffle = EcobiciWaffle(df)
fig_waffle = waffle.create_waffle(estacion)

# =========================
# Layout vertical
# =========================

# MAPA
st.plotly_chart(fig_map, use_container_width=True)

# WAFFLE
if fig_waffle:
    st.pyplot(fig_waffle, use_container_width=True)
