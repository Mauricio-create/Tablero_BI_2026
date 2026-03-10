import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns



class EcobiciLoader:

    def __init__(self):
        self.url_gbfs = "https://gbfs.mex.lyftbikes.com/gbfs/gbfs.json"
        self.url_station_information = "https://gbfs.mex.lyftbikes.com/gbfs/es/station_information.json"
        self.url_station_status = "https://gbfs.mex.lyftbikes.com/gbfs/es/station_status.json"

        self.df_stations = None
        self.df_status = None
        self.df = None

    def get_feeds(self):
        """Obtiene los feeds disponibles del API"""
        response = requests.get(self.url_gbfs)
        data_json = response.json()

        feeds = []

        for item in data_json['data']['es']['feeds']:
            print(item['name'])
            print(item['url'])

            feeds.append({
                "name": item['name'],
                "url": item['url']
            })

        return pd.DataFrame(feeds)

    def load_station_information(self):
        """Carga la información de estaciones"""
        response = requests.get(self.url_station_information)
        data_stations = response.json()

        df = pd.DataFrame(data_stations['data']['stations'])

        # Revisar tipo de dato
        print("Tipo de dato de rental_methods:", df.rental_methods.dtype)

        # Revisar valores faltantes en listas
        print(df.rental_methods.apply(pd.Series).isna().sum())

        # Revisar valores faltantes generales
        print(df.isna().sum())

        # Seleccionar columnas relevantes
        df = df[['station_id', 'name', 'lat', 'lon', 'capacity']]

        self.df_stations = df

        return df

    def load_station_status(self):
        """Carga el estado actual de las estaciones"""
        response = requests.get(self.url_station_status)
        station_status = response.json()

        df_status = pd.DataFrame(station_status['data']['stations'])

        columnas = [
            'num_bikes_available',
            'num_bikes_disabled',
            'num_docks_available',
            'num_docks_disabled'
        ]

        df_status = df_status[columnas]

        self.df_status = df_status

        return df_status

    def merge_data(self):
        """Une información de estaciones con su estado"""
        if self.df_stations is None:
            self.load_station_information()

        if self.df_status is None:
            self.load_station_status()

        self.df = pd.concat([self.df_stations, self.df_status], axis=1)

        return self.df
