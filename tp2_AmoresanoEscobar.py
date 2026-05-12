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

def main():
    ruta = input("Ingrese la ruta del archivo de texto con las coordenadas: ")
    if not os.path.exists(ruta):
        print("No se encontró la imagen. Por favor, verifique la ruta e intente nuevamente.")
    
    else:
        imagen = Image.open(ruta) # Abrimos la imagen 
        metodo = input ("Seleccione el método (pixel/ascii): ").lower()

        if metodo == "pixel":
            imagen = imagen.convert('RGB') # Convertimos la imagen a RGB
            tam_bloque = int(input("Ingrese el tamaño del bloque (default=10): "))
            if tam_bloque <= 0:
                print("Tamaño de bloque no válido, debe ser un número positivo. Usando tamaño por defecto de 10.")
                tam_bloque = 10
            elif tam_bloque == '':
                tam_bloque = 10
            
            #hacer las validaciones 


            niveles_color = int(input("Ingrese el número de niveles de color (default=4): "))
            if niveles_color <= 0:
                print("Número de niveles de color no válido, debe ser un número positivo. Usando niveles por defecto de 4.")
                niveles_color = 4
            elif niveles_color == '':
                niveles_color = 4

        resultado_pixel = pixel_art(imagen, tam_bloque, niveles_color) #esto va a ejecutar la función pixel_art con los parámetros ingresados por el usuario
        ruta_salida = input("Seleccione la ruta para guardar la imagen procesada (ejemplo: resultado_pixel.png): ")
        #if not ruta_salida.endswith(".png"):
        #   ruta_salida += ".png"
        # Validar que la ruta de salida sea válida es mejor controlar todo
        
        resultado_pixel.save(ruta_salida)
        print(f"Imagen editada guardada en: {ruta_salida}")

        #if metodo == "ascii": continuarlo 