from PIL import Image
import numpy as np
import os

PALETA = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def validar_ruta_salida(extension):
    """
    Pide la ruta de salida en un bucle hasta que sea válida.
    Maneja extensiones y autonumeración si el archivo ya existe.
    """
    while True:
        ruta = input(f"Seleccione el nombre o ruta de salida (.{extension}): ").strip()
        
        # Validamos que no esté vacío
        if not ruta:
            print("Error: El nombre del archivo no puede estar vacío.")
            continue  # Vuelve a preguntar
        
        # Aseguramos extensión antes de validar el directorio
        if not ruta.lower().endswith(extension):
            ruta += extension
            
        # Validamos que la carpeta exista
        directorio = os.path.dirname(ruta)
        # Si el directorio no es vacío y no existe, hay error
        if directorio != "" and not os.path.isdir(directorio):
            print(f"Error: La carpeta '{directorio}' no existe. Intente otra ruta.")
            continue  # Vuelve a preguntar
        
        # Si ya existe, lo nombramos con numeración automática
        if os.path.exists(ruta):
            # Separamos nombre de extensión (ej: 'resultado' y '.png')
            nombre, ext = os.path.splitext(ruta)
            i = 1
            while os.path.exists(f"{nombre}({i}){ext}"):
                i += 1
            ruta = f"{nombre}({i}){ext}"
            print(f"Aviso: El archivo ya existía. Se renombró automáticamente a: {ruta}")
        
        return ruta
    
def pixel_art(imagen: Image.Image, tam_bloque: int, niveles_color: int) -> Image.Image:
    """
    Transforma una imagen al estilo Pixel Art mediante el promedio de bloques y el color
    predominante de dicho bloque.

    Argumentos:
        imagen (Image.Image): Objeto de imagen de la librería PIL (Pillow).
        tam_bloque (int): Tamaño en píxeles del lado de cada bloque cuadrado.
        niveles_color (int): Cantidad de tonos permitidos por cada canal (R, G, B).

    Return:
        Image.Image: Una nueva imagen con el efecto de Pixel Art aplicado.
    """
    # Convertimos a RGB para procesar colores
    cuadricula = np.array(imagen.convert('RGB'))
    alto, ancho, canales_RGB = cuadricula.shape
    resultado = cuadricula.copy()

    for y in range(0, alto, tam_bloque):
        for x in range(0, ancho, tam_bloque):
            # Recorte del bloque actual
            bloque = cuadricula[y : y + tam_bloque, x : x + tam_bloque]
            if bloque.size == 0: 
                continue
            
            # Promedio de color y pintar del color predominante
            color_promedio = bloque.mean(axis=(0, 1))
            distancia_tonos = 255 // (niveles_color - 1)
            color_predominante = np.round(color_promedio / distancia_tonos) * distancia_tonos
            
            # Aplicar color al bloque
            resultado[y : y + tam_bloque, x : x + tam_bloque] = color_predominante

    # convertimos a uint8 para evitar problemas de tipo al crear la imagen final
    # Convertimos los números decimales a enteros de 8 bits (0-255)
    resultado_final = resultado.astype('uint8')
    # Creamos la imagen final a partir de la cuadricula resultante
    imagen_pixel_art = Image.fromarray(resultado_final)

    return imagen_pixel_art

def ascii_art(imagen: Image.Image, ancho_ascii: int = 100) -> str:
    """
    Transforma una imagen al estilo ASCII Art (en una cadena de caracteres ASCII).

    #Ajusta el tamaño de la imagen, la convierte a escala de grises y mapea 
    la intensidad de cada píxel a un carácter según su densidad visual.

    Argumentos:
        imagen (Image.Image): Objeto de imagen de la librería PIL (Pillow).
        ancho_ascii (int): Ancho en caracteres del resultado ASCII.

    Return:
        str: Cadena de texto con saltos de línea que forma la imagen en ASCII.
    """
    # Convertimos a escala de grises para procesar intensidad
    imagen_gris = imagen.convert('L')
    ancho_original, alto_original = imagen_gris.size
    proporcion = alto_original / ancho_original
    alto_ascii = int(ancho_ascii * proporcion) #ver eso del *0.55
    
    # Redimensionamos la imagen para que se ajuste al ancho deseado
    imagen_redimensionada = imagen_gris.resize((ancho_ascii, alto_ascii))
        
    # Mapeamos cada intensidad a un carácter ASCII
    caracteres_ascii = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    div = 256 / len(caracteres_ascii)

    # Convertimos la imagen redimensionada a una cuadricula de píxeles
    pixeles = np.array(imagen_redimensionada)
    lineas_ascii = []    
    # Por cada píxel, buscamos qué carácter le corresponde según su brillo
    for fila in pixeles:
        linea = "".join(caracteres_ascii[int(pixel / div)] for pixel in fila)
        lineas_ascii.append(linea)

    return "\n".join(lineas_ascii)

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
                print("Usando tamaño de bloque por default: 10")
            elif tam_bloque_ingresado.isdigit() and int(tam_bloque_ingresado) > 0: 
                #El usuario ingresó un número, se asigna ese valor
                tam_bloque = int(tam_bloque_ingresado)
            else:
                #El usuario ingresó un valor no válido, se asigna el valor por defecto
                print("Tamaño de bloque no válido, debe ser un número positivo. Usando tamaño por default de 10.")
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
                print("Número de niveles de color no válido, debe ser un número positivo. Usando niveles por default de 4.")
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
                print("Usando ancho de la imagen por default: 100")
            elif ancho_ingresado.isdigit() and int(ancho_ingresado) > 0: 
                #El usuario ingresó un número, se asigna ese valor
                ancho_ascii = int(ancho_ingresado)
            else:
                #El usuario ingresó un valor no válido, se asigna el valor por defecto
                print("El ancho de la imagen ASCII debe ser un número positivo. Usando valor por default de 100.")
                ancho_ascii = 100
                #return?
            
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