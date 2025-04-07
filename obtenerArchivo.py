import sys

def leer_archivo():
    #Comprobar que se envio como argumento solo el archivo .txt
    if  len(sys.argv) < 2 or len(sys.argv) > 2:
        print("ERROR Debe seguir el siguiente formato al ejecutar el codigo: python codigo_main.py nombre_archivo.txt")
        sys.exit(1)
    nombreArchivo = sys.argv[1]
    
    try:
        with open(nombreArchivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print(f"ERROR el archivo no existe, digite nuevamente el nombre: {nombreArchivo}")
        sys.exit(1)

    return contenido