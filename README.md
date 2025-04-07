# 🧠 TextoInspector3000

¡Bienvenido a **TextoInspector3000**, el inspector de palabras definitivo!  
Este programa en Python analiza un párrafo de texto y revela información interesante como el número total de palabras, palabras únicas, la(s) palabra(s) más larga(s) y la frecuencia de cada palabra, ignorando mayúsculas, minúsculas y signos de puntuación.

---

## 🧾 ¿Qué hace este programa?

La función principal del programa se llama `procesar_texto` y recibe un párrafo en forma de cadena (`string`). Esta función devuelve un **diccionario** con la siguiente información:

- 📌 Número total de palabras  
- 📌 Lista de palabras únicas (sin repetir)  
- 📌 Palabra(s) más larga(s)  
- 📌 Número de veces que aparece cada palabra (ignorando mayúsculas, minúsculas y signos de puntuación)  

Además, el programa incluye un menú interactivo para elegir cómo ingresar el texto a analizar.

---

## 🧰 Funcionalidades del menú

Al ejecutar el programa, se presenta un menú con tres opciones:

1. ✍️ Ingresar el párrafo directamente desde la consola.  
2. 📄 Leer el párrafo desde un archivo `.txt`.  
   > ⚠️ **IMPORTANTE**: Esta opción solo funcionará si ejecutas el programa **pasando como argumento el nombre del archivo .txt**.  
   > Ejemplo: `python main.py parrafo.txt`
3. 🧪 Usar un párrafo de prueba incluido directamente en el código.

---

## ▶️ Cómo ejecutar el programa

### Requisitos
- Python 3.10 o superior (por el uso de `match-case`)
- Instalar la librería `regex` si no la tienes instalada:
```bash
pip install regex
