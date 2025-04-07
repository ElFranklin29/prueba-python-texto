from collections import Counter
from pprint import PrettyPrinter
import regex
from obtenerArchivo import leer_archivo
import sys

def menu():
    opcion = input("\n¡Bienvenido a TextoInspector3000 El inspector de palabras definitivo: cuenta, limpia y revela secretos del texto!\n"
            "\n¿Como deseas ingresar el parrafo?\n"
            "\n1. Ingresar parrafo desde consola"
            "\n2. Ingresar parrafo desde un archivo .txt"
            "\n3. Ingresar parrafo desde el codigo"
                
            "\n¡IMPORTANTE! Tenga en cuenta que para la opcion 2, el codigo debio ser ejecutado con un argumento, el cual debe ser el nombre del archivo .txt\n"
               
            "\nSelecciona una opcion: ")
    match opcion:
        case "1":
            parrafo=input("Ingrese el texto que quiere analizar: ")
        case "2":
            parrafo = leer_archivo()
        case "3":
            parrafo = "La evolución de la tecnología ha sido, sin lugar a dudas, un fenómeno imparable. Sin embargo, ¿hemos considerado realmente sus efectos a largo plazo? Algunos expertos, como la Dra. González, advierten sobre los riesgos de una dependencia excesiva. Otros, en cambio, celebran los avances como una muestra del ingenio humano." 
        case _:
            print("ERROR Ingrese una opcion valida")
            sys.exit(1)
    procesar_texto(parrafo)    
    
    

def procesar_texto(parrafo: str):  
    #Se eliminan signos de puntuacion con libreria regex e indicando categoria unicode
    textoLimpio = regex.sub(r"\p{P}","", parrafo.lower())

    #Obtener cada palabra del texto
    listaPalabras = textoLimpio.split()
    
    #Obtener numero de palabras mediante el tamaño de la lista
    numeroPalabras = len(listaPalabras)
    
    #Obtener todas las palabras sin repetir
    palabrasUnicas = set(listaPalabras)

    #Obtener palabra mas larga
    palabrasMasLargas = []
    tamPalabra = len(max(palabrasUnicas, key=len))
    for palabra in palabrasUnicas:
        if tamPalabra == len(palabra):
            palabrasMasLargas.append(palabra)
    
    #Obtener numero de veces que aparece cada palabra
    cantidadPorPalabra = Counter(listaPalabras)
    
    resultado = {
        "Parrafo": parrafo, 
        "Numero de palabras": numeroPalabras,
        "Lista de palabras (Sin repetir)": palabrasUnicas,
        "Palabra(s) mas larga": palabrasMasLargas,
        "Numero de veces que aparece cada palabra": dict(cantidadPorPalabra)
        }
    
    pp = PrettyPrinter(sort_dicts=False)
    print("\nTEXTO ANALIZADO\n")
    pp.pprint(resultado)
    
    

menu()





