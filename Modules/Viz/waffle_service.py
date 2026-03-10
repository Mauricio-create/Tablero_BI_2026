import streamlit as st
import matplotlib.pyplot as plt
from pywaffle import Waffle


class EcobiciWaffle:

    def __init__(self, df):
        self.df = df

    def create_waffle(self, station_name):

        if station_name == "Todas":
            st.info("Selecciona una estación para ver el gráfico waffle")
            return None

        df_filtrado = self.df[self.df["name"] == station_name]

        if df_filtrado.empty:
            st.warning("No se encontraron datos para la estación")
            return None

        fila = df_filtrado.index[0]

        capacity = self.df.loc[fila, "capacity"]

        # calcular filas del waffle
        if capacity % 10 != 0:
            rows = capacity // 10 + 1
        else:
            rows = capacity // 10

        values = self.df.iloc[fila][
            [
                "num_bikes_available",
                "num_bikes_disabled",
                "num_docks_available",
                "num_docks_disabled",
            ]
        ].values

        fig = plt.figure(
            FigureClass=Waffle,
            rows=rows,
            values=values,
            colors=["green", "red", "blue", "orange"],
            icons="bicycle",
            icon_size=20,
            legend={
                "labels": [
                    "Bici disponible",
                    "Bici dañada",
                    "Puerto disponible",
                    "Puerto dañado",
                ],
                "loc": "lower left",
                "bbox_to_anchor": (0, -0.2),
                "ncol": 2,
                "framealpha": 0,
                "fontsize": 10,
            },
            figsize=(6, 5),
        )

        plt.title(station_name)

        return fig
