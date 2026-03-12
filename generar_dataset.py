import pandas as pd
import numpy as np

# Crear fechas
fechas = pd.date_range("2005-01-01","2024-12-31")

np.random.seed(42)

dataset = pd.DataFrame({
"fecha":fechas
})

dataset["mes"] = dataset["fecha"].dt.month

# TEMP MAR
dataset["temp_agua"] = 14 + 4*np.sin((dataset["fecha"].dt.dayofyear-80)*2*np.pi/365) + np.random.normal(0,0.7,len(dataset))

# OLEAJE
dataset["oleaje"] = np.random.gamma(2,1.2,len(dataset))

# VIENTO
dataset["viento"] = np.random.normal(15,5,len(dataset))

# LLUVIA
dataset["lluvia"] = np.random.exponential(2,len(dataset))

# PRESION
dataset["presion"] = np.random.normal(1015,6,len(dataset))

# COEF MAREA
dataset["coef_marea"] = np.random.randint(50,120,len(dataset))

# FASE LUNAR
dataset["fase_lunar"] = np.random.randint(0,29,len(dataset))

# VISIBILIDAD AGUA
dataset["visibilidad_agua"] = np.where(dataset["oleaje"]>2,"turbia","limpia")

# DIAS DESDE TEMPORAL
dataset["dias_desde_temporal"] = np.random.randint(0,10,len(dataset))

# TEMPORADA
dataset["temporada"] = np.where(dataset["mes"].isin([6,7,8]),"verano",
np.where(dataset["mes"].isin([9,10,11]),"otoño",
np.where(dataset["mes"].isin([12,1,2]),"invierno","primavera")))

# VEDAS SIMPLIFICADAS
dataset["veda_pulpo"] = dataset["mes"].isin([6,7])
dataset["veda_percebe"] = False
dataset["veda_lubina"] = False

# CAPTURAS SIMULADAS BASADAS EN CONDICIONES

dataset["captura_pulpo"] = np.where(
(dataset["temp_agua"]>16) &
(dataset["coef_marea"]>80) &
(dataset["visibilidad_agua"]=="turbia"),
np.random.gamma(2,8,len(dataset)),
np.random.gamma(0.5,2,len(dataset))
)

dataset["captura_lubina"] = np.where(
(dataset["oleaje"]>1) &
(dataset["oleaje"]<3),
np.random.gamma(2,5,len(dataset)),
np.random.gamma(0.5,2,len(dataset))
)

dataset["captura_percebe"] = np.where(
(dataset["coef_marea"]>90) &
(dataset["oleaje"]<2),
np.random.gamma(2,4,len(dataset)),
np.random.gamma(0.5,1,len(dataset))
)

dataset.to_csv("dataset_pesca_cantabrico.csv",index=False)

print("Dataset creado")
