# Organizador de Archivos en Python 🗂️

Este script organiza automáticamente los archivos de una carpeta según su tipo (PDFs, imágenes, Excel, etc.) y, opcionalmente, por fecha de modificación (año/mes).

---

## 📌 Características

- Clasifica archivos por tipo (documentos, imágenes, hojas de cálculo, etc.)
- Opcionalmente agrupa por fecha de modificación (año/mes)
- Modo de prueba (dry-run) para ver qué haría sin mover archivos
- Evita sobrescribir archivos duplicados (renombra automáticamente)

---

## 📁 Estructura del proyecto

organizador\_archivos/

├── organizador.py # Script principal

├── ejemplo\_archivos/ # Carpeta con archivos desordenados para pruebas

├── archivos\_organizados/ # Salida organizada (se crea al ejecutar el script)

├── requirements.txt

└── README.md

---

## 🚀 Uso

1. Abrí una terminal y navegá a la carpeta del proyecto:

```bash

cd organizador\_archivos



python organizador.py --origen ./ejemplo\_archivos --destino ./archivos\_organizados --por\_fecha --seco



--origen

Ruta a la carpeta con los archivos desordenados

--destino

Ruta donde se organizarán los archivos

--por\_fecha

Agrupa también por año y mes de modificación (opcional)

--seco

Modo prueba: no mueve archivos, solo muestra acciones

