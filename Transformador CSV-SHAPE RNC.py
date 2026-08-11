import geopandas as gpd
import pandas as pd

# 1. Leer shapefile original de la RNC (lo que quieras modificar)
rnc = gpd.read_file(r"C:\Users\rodri\Downloads\Autopistas\Autopistas\Carreteras_Y_Crimen\data\Red_vial_data\red_vial.shp") #CAPA SHAPE ORIGINAL
# 2. Leer tu CSV (los datos que ya tienes filtrados)
df = pd.read_csv(r"C:\Users\rodri\OneDrive\Documentos\mapa carreteras\Shape casi listo\shape casi listo.csv") #CSV FILTRO

# 3. Asegurar que ID_RED sea el mismo tipo en ambos (el ID debe corresponder al shapefile que tengas)
rnc["TIPO_VIAL"] = rnc["TIPO_VIAL"].astype(int)
df["TIPO_VIAL"] = df["TIPO_VIAL"].astype(int)

# 4. Join (unión de atributos) (lo mismo que en el apartado 3)
merged = rnc.merge(df, on="TIPO_VIAL", how="inner")

# 5. Guardar shapefile final
merged.to_file(r"C:\Users\rodri\OneDrive\Documentos\mapa carreteras\Shape casi listo\shape casi listo_3.shp") #SHAPE RESULTANTE

print("✅ Shapefile generado correctamente")



#nota: incluir un filtro para que me dé un csv más completo de carreteras 
# NOTA: MODIFICAR LAS RUTAS DE ACCESO, ESTE CASO ES UN EJERCICIO DE LA RED NACIONAL DE CAMINOS