import os
import shutil
import argparse
from datetime import datetime

# Tipos de archivos a clasificar
EXTENSIONES = {
    'Documentos': ['.pdf', '.docx', '.txt'],
    'Hojas_de_calculo': ['.xlsx', '.csv'],
    'Imagenes': ['.jpg', '.jpeg', '.png'],
    'Presentaciones': ['.pptx'],
    'Otros': []
}

def obtener_categoria(extension):
    for categoria, extensiones in EXTENSIONES.items():
        if extension.lower() in extensiones:
            return categoria
    return 'Otros'

def organizar_archivos(origen, destino, por_fecha, modo_seco):
    if not os.path.exists(origen):
        print(f"❌ Carpeta de origen no encontrada: {origen}")
        return

    for archivo in os.listdir(origen):
        ruta_archivo = os.path.join(origen, archivo)

        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1]
            categoria = obtener_categoria(extension)

            carpeta_destino = os.path.join(destino, categoria)

            if por_fecha:
                # Agregar subcarpeta con año y mes
                timestamp = os.path.getmtime(ruta_archivo)
                fecha = datetime.fromtimestamp(timestamp)
                subcarpeta_fecha = f"{fecha.year}-{fecha.month:02d}"
                carpeta_destino = os.path.join(carpeta_destino, subcarpeta_fecha)

            os.makedirs(carpeta_destino, exist_ok=True)

            ruta_destino = os.path.join(carpeta_destino, archivo)

            if os.path.exists(ruta_destino):
                base, ext = os.path.splitext(archivo)
                contador = 1
                while True:
                    nuevo_nombre = f"{base}_{contador}{ext}"
                    ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)
                    if not os.path.exists(ruta_destino):
                        break
                    contador += 1

            if modo_seco:
                print(f"[SECO] Movería: {archivo} → {ruta_destino}")
            else:
                shutil.move(ruta_archivo, ruta_destino)
                print(f"Movido: {archivo} → {ruta_destino}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Organiza archivos por tipo y fecha.')
    parser.add_argument('--origen', required=True, help='Carpeta de origen con archivos desordenados')
    parser.add_argument('--destino', required=True, help='Carpeta donde se organizarán los archivos')
    parser.add_argument('--por_fecha', action='store_true', help='Organizar también por año/mes de modificación')
    parser.add_argument('--seco', action='store_true', help='Modo seco (no mueve archivos, solo muestra)')

    args = parser.parse_args()

    organizar_archivos(args.origen, args.destino, args.por_fecha, args.seco)