import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


class EcobiciMap:

    def __init__(self, df):
        self.df = df

    def create_map(self):

        # =========================
        # SIDEBAR - CONFIGURACIÓN
        # =========================

        st.sidebar.title("⚙️ Configuración del mapa")

        estaciones = ["Todas"] + sorted(self.df["name"].unique().tolist())

        estacion_seleccionada = st.sidebar.selectbox(
            "Selecciona una estación",
            estaciones
        )

        zoom_level = st.sidebar.slider(
            "Nivel de zoom",
            min_value=1,
            max_value=4,
            value=1
        )

        point_size = st.sidebar.slider(
            "Tamaño de estaciones",
            min_value=6,
            max_value=30,
            value=12
        )

        # =========================
        # CENTRO DEL MAPA
        # =========================

        centroid_lat = self.df["lat"].mean()
        centroid_lon = self.df["lon"].mean()

        if estacion_seleccionada == "Todas":

            center_lat = centroid_lat
            center_lon = centroid_lon

        else:

            estacion = self.df[self.df["name"] == estacion_seleccionada]

            if zoom_level == 1:
                center_lat = centroid_lat
                center_lon = centroid_lon
            else:
                center_lat = estacion["lat"].values[0]
                center_lon = estacion["lon"].values[0]

        # =========================
        # MAPA BASE
        # =========================

        fig = px.scatter_mapbox(
            self.df,
            lat="lat",
            lon="lon",
            hover_name="name",
            hover_data={
                "capacity": True,
                "num_bikes_available": True,
                "num_docks_available": True
            },
            zoom=12,
            height=650,
            showlegend=False
        )

        fig.update_traces(marker=dict(size=point_size))

        # =========================
        # MARCADOR ESTACIÓN
        # =========================

        if estacion_seleccionada != "Todas":

            estacion = self.df[self.df["name"] == estacion_seleccionada]

            fig.add_trace(
                go.Scattermapbox(
                    lat=estacion["lat"],
                    lon=estacion["lon"],
                    mode="markers",
                    marker=dict(
                        size=point_size + 10,
                        color="red"
                    ),
                    name="Estación seleccionada"
                )
            )

        # =========================
        # CONFIGURAR ZOOM
        # =========================

        zoom_dict = {
            1: 12,
            2: 13,
            3: 14,
            4: 15
        }

        fig.update_layout(
            mapbox_style="open-street-map",
            mapbox_zoom=zoom_dict[zoom_level],
            mapbox_center={"lat": center_lat, "lon": center_lon},
            title="Estaciones Ecobici - Ciudad de México",
            margin={"r":0,"t":40,"l":0,"b":0}
        )

        return fig
