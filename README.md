# Convertidor-CSV-a-SHAPE
Código para recortas archivos shapefile a partir de un CSV determinado.

El manejo de archivos shapefile en plataformas como QGIS suele ser complicado debido al gran volumen de información que contiene la capa; sin embargo, se puede usar python para recortar la capa y obtener información específica de la capa.

El código presenta un caso para la RED NACIONAL DE CAMINOS de México, en donde se filtran datos de la capa shapefile completa y crea únicamente. Se necesitan varios pasos para usar el código:

1. Obtener la capa shapefile y extraer la tabla de información de la capa (preferentemente en formato excel)
2. Filtrar el archivo excel bajo los criterios que desea filtrar
3. Colocar los archivos SHP y XLSX en el código
4. Colocar el título de columna en donde se hizo el filtro (se debe conocer la tabla de atributos)
5. Ejecutar el código

Puede sonar un poco complicado sabiendo que en los mismos programas se pueden filtrar, pero resulta una solución rápida para obtener archivos shapefile más livianos.
