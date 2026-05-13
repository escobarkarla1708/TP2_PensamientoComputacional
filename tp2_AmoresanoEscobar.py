from PIL import Image
import numpy as np
import os

PALETA = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# Abrimos la imagen y la convertimos a RGB
img = Image.open("marilyn.jpeg").convert('RGB') 

# La convertimos en una matriz de números
pixel_matrix = np.array(img)

# Creamos una copia de la matriz original para modificarla
resultado = pixel_matrix.copy()

# def main():
#     ruta = input("Ingrese la ruta del archivo de texto con las coordenadas: ")
#     if not os.path.exists(ruta):
#         print("No se encontró la imagen. Por favor, verifique la ruta e intente nuevamente.")
    
#     else:
#         imagen = Image.open(ruta) # Abrimos la imagen 
#         metodo = input ("Seleccione el método (pixel/ascii): ").lower()

#         if metodo == "pixel":
#             imagen = imagen.convert('RGB') # Convertimos la imagen a RGB
#             tam_bloque = int(input("Ingrese el tamaño del bloque (default=10): "))
#             if tam_bloque <= 0:
#                 print("Tamaño de bloque no válido, debe ser un número positivo. Usando tamaño por defecto de 10.")
#                 tam_bloque = 10
#             elif tam_bloque == '':
#                 tam_bloque = 10
            
#             #hacer las validaciones 


#             niveles_color = int(input("Ingrese el número de niveles de color (default=4): "))
#             if niveles_color <= 0:
#                 print("Número de niveles de color no válido, debe ser un número positivo. Usando niveles por defecto de 4.")
#                 niveles_color = 4
#             elif niveles_color == '':
#                 niveles_color = 4

#         resultado_pixel = pixel_art(imagen, tam_bloque, niveles_color) #esto va a ejecutar la función pixel_art con los parámetros ingresados por el usuario
#         ruta_salida = input("Seleccione la ruta para guardar la imagen procesada (ejemplo: resultado_pixel.png): ")
#         #if not ruta_salida.endswith(".png"):
#         #   ruta_salida += ".png"
#         # Validar que la ruta de salida sea válida es mejor controlar todo
        
#         resultado_pixel.save(ruta_salida)
#         print(f"Imagen editada guardada en: {ruta_salida}")

#         #if metodo == "ascii": continuarlo 

def validar_rutasalida(ruta, tipo):
    if ruta_salida == "":
        print("Debe ingresar una ruta de salida.")
        return
            
    # Extraemos solo la parte de las carpetas
    directorio = os.path.dirname(ruta_salida)
    # Verificamos si esa carpeta existe
    if directorio != "" and not os.path.isdir(directorio):
        print(f"Error: La carpeta '{directorio}' no existe en tu computadora.")
        return
    if not ruta_salida.lower().endswith(".png"):
        ruta_salida += ".png"
            
    # if os.path.exists(ruta_salida):
    #     print("El nombre del archivo ya existe.")
    #     ruta_salida+="(1)"
    
def pixel_art(imagen: Image, tam_bloque: int, niveles_color: int) -> Image:
    return

def ascii_art(imagen, ancho_ascii):
    return "ASCII ART RESULTANTE"

def guardar_ascii_art(ascii_art: str, ruta_salida: str): 
    with open(ruta_salida, 'w') as f:
        f.write(ascii_art)

def main():
    try:
        ruta = input("Ingrese la ruta de la imagen: ").strip()
        if not os.path.exists(ruta):
            print("No se encontró la imagen. Por favor, verifique la ruta e intente nuevamente.")
            return
        
        try:
            imagen = Image.open(ruta)
        except Exception as e:
            print(f"Error al abrir la imagen: {e}")
            return

        metodo = input("Seleccione el método (pixel/ascii): ").lower().strip()
        if metodo not in ["pixel", "ascii"]:
            print("Método no válido. Por favor, seleccione 'pixel' o 'ascii'.")
            return
        # TODO: Convertir metodos en def
        if metodo == "pixel":
            #Validando el tamaño del bloque.
            tam_bloque_ingresado = input("Ingrese el tamaño del bloque (default=10): ").strip()
            if tam_bloque_ingresado == "": 
                #El usuario no ingresó nada o solo espacios, se asigna el valor por defecto
                tam_bloque = 10
                print("Usando tamaño de bloque por defecto: 10")
            elif tam_bloque_ingresado.isdigit() and int(tam_bloque_ingresado) > 0: 
                #El usuario ingresó un número, se asigna ese valor
                tam_bloque = int(tam_bloque_ingresado)
            else:
                #El usuario ingresó un valor no válido, se asigna el valor por defecto
                print("Tamaño de bloque no válido, debe ser un número positivo. Usando tamaño por defecto de 10.")
                tam_bloque = 10
                #return?

            #Validando el número de niveles de color
            niveles_color_ingresado = input("Ingrese el número de niveles de color (default=4): ").strip()
            if niveles_color_ingresado == "": 
                #El usuario no ingresó nada o solo espacios, se asigna el valor por defecto
                niveles_color = 4
                print("Usando niveles de color por defecto: 4")
            elif niveles_color_ingresado.isdigit() and int(niveles_color_ingresado) > 0: 
                #El usuario ingresó un número, se asigna ese valor
                niveles_color = int(niveles_color_ingresado)
            else:
                #El usuario ingresó un valor no válido, se asigna el valor por defecto
                print("Número de niveles de color no válido, debe ser un número positivo. Usando niveles por defecto de 4.")
                niveles_color = 4
                #return?

            # TODO: hacer la funcion pixel
            resultado_pixel = pixel_art(imagen, tam_bloque, niveles_color)

            #Seleccionar ruta de salida de imagen editada.
            ruta_salida = input("Seleccione la ruta para guardar la imagen procesada: ").strip()
            if ruta_salida == "":
                print("Debe ingresar una ruta de salida.")
                return
            
            # Extraemos solo la parte de las carpetas
            directorio = os.path.dirname(ruta_salida)
            # Verificamos si esa carpeta existe
            if directorio != "" and not os.path.isdir(directorio):
                print(f"Error: La carpeta '{directorio}' no existe en tu computadora.")
                return
            if not ruta_salida.lower().endswith(".png"):
                ruta_salida += ".png"
            
            # if os.path.exists(ruta_salida):
            #     print("El nombre del archivo ya existe.")
            #     ruta_salida+="(1)"
            """PREGUNTAR"""

            resultado_pixel.save(ruta_salida)
            print(f"Imagen editada guardada en: {ruta_salida}")
        
        elif metodo == "ascii":
            # Validamos (...)
            ancho_ingresado = input("Ingrese el ancho de la imagen ASCII (default=100): ").strip()
            if ancho_ingresado == "": 
                #El usuario no ingresó nada o solo espacios, se asigna el valor por defecto
                ancho_ascii = 100
                print("Usando ancho de la imagen por defecto: 100")
            elif ancho_ingresado.isdigit() and int(ancho_ingresado) > 0: 
                #El usuario ingresó un número, se asigna ese valor
                ancho_ascii = int(ancho_ingresado)
            else:
                #El usuario ingresó un valor no válido, se asigna el valor por defecto
                print("El ancho de la imagen ASCII debe ser un número positivo. Usando valor por defecto de 100.")
                ancho_ascii = 100
                #return?

            # ancho_ascii = int(ancho_ingresado) if ancho_ingresado.isdigit() and int(ancho_ingresado) > 0 else 100
            # if ancho_ascii <= 0:
            #     print("El ancho de la imagen ASCII debe ser un número positivo.")
            #     return
            
            resultado_ascii = ascii_art(imagen, ancho_ascii)

            ruta_salida = input("Seleccione la ruta para guardar el resultado: ").strip()
            if ruta_salida == "":
                print("Debe ingresar una ruta de salida.")
                return
            # Extraemos solo la parte de las carpetas
            directorio = os.path.dirname(ruta_salida)
            # Verificamos si esa carpeta existe
            if directorio != "" and not os.path.isdir(directorio):
                print(f"Error: La carpeta '{directorio}' no existe en tu computadora.")
                return
            if not ruta_salida.lower().endswith(".txt"):
                ruta_salida += ".txt"
            # if os.path.exists(ruta_salida):
            #     print("El nombre del archivo ya existe.")
            #     ruta_salida+="(1)"
            """PREGUNTAR"""

            guardar_ascii_art(resultado_ascii, ruta_salida)
            print(f"Archivo ASCII guardado en: {ruta_salida}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")