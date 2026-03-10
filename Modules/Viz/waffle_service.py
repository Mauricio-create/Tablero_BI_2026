import streamlit as st
import matplotlib.pyplot as plt
from pywaffle import Waffle


class EcobiciWaffle:

    def __init__(self, df):
        self.df = df

    def create_waffle(self, station_name):

        # =========================
        # SI NO SE HA SELECCIONADO ESTACIÓN
        # =========================

        if station_name == "Todas":
            st.info("ℹ️ Para visualizar el gráfico waffle debes seleccionar una estación en el panel izquierdo.")
            return None

        # =========================
        # FILTRAR ESTACIÓN
        # =========================

        df_filtrado = self.df[self.df["name"] == station_name]

        if df_filtrado.empty:
            st.warning("No se encontraron datos para la estación")
            return None

        fila = df_filtrado.index[0]

        values = self.df.iloc[fila][
            [
                "num_bikes_available",
                "num_bikes_disabled",
                "num_docks_available",
                "num_docks_disabled",
            ]
        ].values

        capacity = self.df.loc[fila, "capacity"]

        titulo = f"Estado de estación: {station_name}"

        # =========================
        # CALCULAR FILAS WAFFLE
        # =========================

        if capacity % 10 != 0:
            rows = capacity // 10 + 1
        else:
            rows = capacity // 10

        # =========================
        # CREAR WAFFLE
        # =========================

        fig = plt.figure(
            FigureClass=Waffle,
            rows=rows,
            values=values,
            colors=["green", "red", "blue", "orange"],
            icons="bicycle",
            icon_size=30,
            legend={
                "labels": [
                    "Bici disponible",
                    "Bici dañada",
                    "Puerto disponible",
                    "Puerto dañado",
                ],
                "loc": "lower center",
                "bbox_to_anchor": (0.5, -0.35),  # ← baja la leyenda
                "ncol": 2,
                "framealpha": 0,
                "fontsize": 12,
            },
            figsize=(8, 7),
        )

        # Espacio extra abajo para que no se encime
        fig.subplots_adjust(bottom=0.25)

        plt.title(titulo, fontsize=16)

        return fig
