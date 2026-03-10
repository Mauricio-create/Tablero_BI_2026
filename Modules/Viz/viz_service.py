import plotly.express as px


class EcobiciMap:

    def __init__(self, df):
        """
        Constructor de la clase
        df: DataFrame con información de estaciones
        """
        self.df = df

    def create_map(self):
        """
        Genera el mapa de estaciones Ecobici en CDMX
        """

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
            zoom=11,
            height=600
        )

        fig.update_layout(
            mapbox_style="open-street-map",
            title="Estaciones Ecobici - Ciudad de México",
            margin={"r":0,"t":40,"l":0,"b":0}
        )

        return fig
