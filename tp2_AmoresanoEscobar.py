from PIL import Image
import numpy as np
import os
    
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
    # Convertimos la imagen a una cuadricula de píxeles RGB para procesarla (filas y columnas de color)
    cuadricula = np.array(imagen.convert('RGB'))
    alto, ancho, canales_RGB = cuadricula.shape
    resultado = cuadricula.copy() # Creamos una copia para no modificar la imagen original 

    # Recorremos la cuadricula saltando de bloque en bloque
    for y in range(0, alto, tam_bloque):
        for x in range(0, ancho, tam_bloque):
            # Cuadricula del bloque actual
            bloque = cuadricula[y : y + tam_bloque, x : x + tam_bloque]

            if bloque.size == 0: 
                continue
            # Obtenemos el color promedio del bloque
            color_promedio = bloque.mean(axis=(0, 1))
            # Calculamos la distancia entre los niveles de color permitidos
            distancia_tonos = 255 // (niveles_color - 1)
            # Asignamos el color predominante al bloque redondeando el color promedio al nivel de color más cercano
            color_predominante = np.round(color_promedio / distancia_tonos) * distancia_tonos 
            resultado[y : y + tam_bloque, x : x + tam_bloque] = color_predominante

    # Convertimos los números decimales a enteros sin signos de 8 bits (0-255) para evitar problemas de tipo al crear la imagen final
    resultado_final = resultado.astype(np.uint8)

    # Convertimos nuestra cuadrícula de números procesados en una imagen real de Pillow 
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
    # Paleta de caracteres ordenados de mayor a menor densidad visual (más oscuro a más claro)
    caracteres_ascii = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

    # Convertimos a escala de grises (L=luminancia) para obtener la intensidad de cada píxel
    imagen_gris = imagen.convert('L')
    ancho_original, alto_original = imagen_gris.size

    # Ajustamos la proporcion de la imagen para que no se vea distorsionada al convertir a ASCII, ya que los caracteres no son cuadrados
    proporcion = alto_original / ancho_original
    alto_ascii = int(ancho_ascii * proporcion * 0.5) # El numero 0.5 corrige la proporción de caracteres (porque sino la imagen quedaría muy alargada)
    
    # Redimensionamos la imagen para que se ajuste al ancho deseado
    imagen_redimensionada = imagen_gris.resize((ancho_ascii, alto_ascii))
        
    # Mapeamos 0-255 a los caracteres ASCII, dividiendo el rango de intensidad por la cantidad de caracteres disponibles
    div = 256 / len(caracteres_ascii)

    # Convertimos la imagen redimensionada a una cuadricula de píxeles
    pixeles = np.array(imagen_redimensionada)
    lineas_ascii = []  

    # Para cada fila, convertimos cada pixel en su caracter correspondiente
    for fila in pixeles:
        linea = "".join(caracteres_ascii[int(pixel / div)] for pixel in fila)
        lineas_ascii.append(linea)
    
    # Unimos todas las líneas con saltos de línea para formar la imagen ASCII completa.
    imagen_ascii = "\n".join(lineas_ascii)
    return imagen_ascii

def pedir_metodo()-> str:
    """
    Solicita al usuario elegir entre el efecto Pixel Art o ASCII Art.
    
    Utiliza un bucle infinito para garantizar que el usuario solo pueda avanzar 
    si ingresa una de las dos opciones válidas, evitando errores en las 
    etapas posteriores del procesamiento.

    Returns:
        str: El método seleccionado convertido a minúsculas ('pixel' o 'ascii').
    """
    while True:
        metodo = input("Seleccione el método (pixel/ascii): ").lower().strip()
        if metodo not in ["pixel", "ascii"]:
            print("Método no reconocido. Por favor, seleccione 'pixel' o 'ascii'.")
        else:
            break
    return metodo

def pedir_numero(mensaje: str, tipo: int, valor_default: int) -> int:
    """
    Solicita un número al usuario y valida que sea un entero positivo.
    
    Si el usuario deja la entrada vacía o ingresa un valor no válido 
    (letras, símbolos o números negativos), la función devuelve un 
    valor predeterminado para asegurar que el programa continúe.

    Argumentos:
        mensaje (str): El texto que se mostrará al usuario solicitando el dato.
        tipo (int): 1 para tamaño de bloque y ancho ASCII, 2 para niveles de color, 3 para ancho ASCII; para verificar los valores minimos y maximos de cada variable.
        valor_default (int): El número que se usará si la entrada es inválida.

    Returns:
        int: El número ingresado por el usuario o, en su defecto, el valor predeterminado.
    """    
    
    # Se recibe la entrada del usuario y se valida
    entrada = input(f"{mensaje} (default={valor_default}): ").strip()
    
    # Si el usuario no ingresa nada, se devuelve el valor por defecto
    if entrada == "":
        print(f"Usando valor por defecto: {valor_default}")
        return valor_default
    
    # Si la entrada es un número entero positivo, se devuelve ese numero ingresado
    if entrada.isdigit():
        if tipo == 1 and int(entrada) > 0:
            return int(entrada)
        if tipo == 2 and int(entrada) > 1 and int(entrada) <= 256:
            return int(entrada)
        if tipo == 3 and int(entrada) > 0 and int(entrada) <= 1000: # Limite superior para evitar problemas de rendimiento al generar ASCII Art muy ancho
            return int(entrada)

    # Si la entrada no es válida, se muestra un mensaje y se devuelve el valor por defecto
    print(f"Valor no válido. Usando defecto: {valor_default}")
    return valor_default

def ruta_salida_valida(extension: str) -> str:
    """
    Solicita al usuario una ruta de guardado y valida que sea factible.
    
    Asegura que el nombre no esté vacío, que la extensión sea correcta y que 
    la carpeta de destino exista. Si el archivo ya existe, añade un número 
    automáticamente para evitar sobrescribir datos.

    Argumentos:
        extension_requerida (str): La extensión que debe tener el archivo (ej: '.png' o '.txt').

    Returns:
        str: Una ruta de archivo válida y verificada.
    """

    # El bucle se mientras la ruta ingresada no sea válida
    while True:
        # Se solicita la ruta de salida al usuario
        ruta = input(f"Seleccione el nombre o ruta de salida ({extension}): ").strip()
        
        # Validamos que no esté vacío
        if not ruta:
            print("Error: El nombre del archivo no puede estar vacío.")
            continue  # Si esta vacio, vuelve a preguntar por la ruta hasta que no lo esté
        
        # Aseguramos que la ruta tenga la extensión correcta, si no la tiene, se la añadimos
        if not ruta.lower().endswith(extension):
            ruta += extension
            
        # Validamos que la carpeta exista
        directorio = os.path.dirname(ruta)
        # Si el directorio no es vacío y no existe, mostramos un error y volvemos a preguntar por la ruta
        if directorio != "" and not os.path.isdir(directorio):
            print(f"Error: La carpeta '{directorio}' no existe. Intente otra ruta.")
            continue
        
        # Verificamos si la ruta ingresada ya existe.
        if os.path.exists(ruta):
            # Separamos nombre de extensión para poder modificar el nombre sin cambiar la extensión
            nombre, ext = os.path.splitext(ruta)
            i = 1
            # Se añade un número entre paréntesis al nombre para evitar sobrescribirlo, y se incrementa el número hasta encontrar una ruta que no exista
            while os.path.exists(f"{nombre}({i}){ext}"):
                i += 1
            ruta = f"{nombre}({i}){ext}"
            print(f"Aviso: El archivo ya existía. Se renombró automáticamente a: {ruta}")
        
        return ruta

def guardar_ascii_art(ascii_art: str, ruta_salida: str): 
    with open(ruta_salida, 'w') as f:
        f.write(ascii_art)

#agregar docstrings y comentarios a metodos 
#y corregir algunos docstrings
def metodo_pixel(imagen: Image.Image):
    tam_bloque = pedir_numero("Ingrese el tamaño del bloque", 1, 10)
    niveles_color = pedir_numero("Ingrese los niveles de color", 2, 4)

    resultado = pixel_art(imagen, tam_bloque, niveles_color)

    ruta_salida = ruta_salida_valida(".png")
    if ruta_salida:
        resultado.save(ruta_salida)
        print(f"Imagen guardada en: {ruta_salida}")

def metodo_ascii(imagen: Image.Image):
    ancho_ascii = pedir_numero("Ingrese el ancho ASCII [1-1000]", 3, 100)

    resultado = ascii_art(imagen, ancho_ascii)
    
    ruta_salida = ruta_salida_valida(".txt")
    if ruta_salida:
        guardar_ascii_art(resultado, ruta_salida)
        print(f"Archivo guardado en: {ruta_salida}")

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
        
        metodo = pedir_metodo()

        if metodo == "pixel":
            metodo_pixel(imagen)

        elif metodo == "ascii":
            metodo_ascii(imagen)

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()