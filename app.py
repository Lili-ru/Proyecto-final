import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
import os

# Configuración de Kaggle
api = KaggleApi()
api.authenticate()

# Descarga el dataset
print("Descargando dataset...")
api.dataset_download_files('jessemostipak/hotel-booking-demand', path='./data', unzip=True)
print("Descarga completada")
