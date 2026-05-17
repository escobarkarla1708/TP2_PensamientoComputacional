# README — Conversor de Imágenes a Pixel Art y ASCII Art
## Descripción general del trabajo

Este trabajo consiste en el desarrollo de un programa en Python capaz de transformar imágenes digitales en dos estilos artísticos diferentes: Pixel Art y ASCII Art. Para ello, se utilizan herramientas de procesamiento de imágenes y manipulación de matrices mediante las librerías Pillow y NumPy.

El objetivo principal del programa es permitir que el usuario cargue una imagen y elija cómo desea modificarla:
mediante un efecto visual pixelado similar al de videojuegos retro,
o convirtiéndola en una representación formada únicamente por caracteres de texto.

El sistema fue diseñado de manera modular, separando cada tarea en funciones específicas para mejorar la organización, reutilización y mantenimiento del código. Además, incorpora validaciones para controlar errores comunes, como rutas inexistentes, datos inválidos o problemas al guardar archivos.

El programa trabaja procesando los píxeles de la imagen original y aplicando distintos algoritmos según el método elegido. En el caso del Pixel Art, se simplifican colores y detalles visuales agrupando píxeles en bloques. En el caso del ASCII Art, los niveles de brillo de cada píxel son reemplazados por caracteres ASCII de distinta densidad visual.

Finalmente, el resultado puede guardarse:
como una nueva imagen .png,
o como un archivo de texto .txt.

## Funciones más importantes

### Función ‘pixel_art()’

Esta es una de las funciones centrales del programa y se encarga de transformar una imagen común en una imagen estilo Pixel Art.

La función recorre la imagen dividiéndola en bloques cuadrados de píxeles. Para cada bloque:
1. calcula el color promedio,
2. reduce la cantidad de tonos posibles,
3. y reemplaza todos los píxeles del bloque por un único color representativo.

De esta manera, la imagen pierde detalle y adquiere una apariencia simplificada y pixelada, característica de los videojuegos antiguos.

Además, la función utiliza matrices de NumPy para procesar grandes cantidades de píxeles de manera eficiente, mejorando el rendimiento del programa.

### Función ‘ascii_art()’

Esta función convierte una imagen en una representación hecha completamente con caracteres ASCII.

Primero, la imagen se transforma a escala de grises para analizar únicamente la intensidad de luz de cada píxel. Luego:
1. se redimensiona la imagen,
2. se analiza el brillo de cada píxel,
3. y cada nivel de intensidad se reemplaza por un carácter específico.

Los caracteres más “oscuros” representan zonas oscuras de la imagen, mientras que los más livianos representan zonas claras.

El resultado final es una cadena de texto que, al visualizarse completa, forma una versión textual de la imagen original.

### Función ‘main()’

La función main() coordina todo el funcionamiento del programa y controla la interacción con el usuario.

Sus tareas principales son:
solicitar la imagen,
validar datos ingresados,
permitir elegir el método de procesamiento,
ejecutar las funciones correspondientes,
y guardar el resultado final.

También incluye manejo de errores mediante bloques ‘try-except', evitando que el programa se cierre inesperadamente frente a entradas inválidas o problemas de ejecución.

Esta función actúa como el núcleo organizador del sistema, conectando todas las demás funciones entre sí.

## Tecnologías usadas 

- Python 3
- Pillow (PIL)
- NumPy
- os

## Ejemplos de uso

### Ejemplo Pixel Art:
Ingrese la ruta de la imagen: foto.jpg
Seleccione el método (pixel/ascii): pixel
Ingrese el tamaño del bloque: 10
Ingrese el número de niveles de color: 4

*Resultado:* 
- Imagen procesada en formato PNG.

### Ejemplo ASCII Art:

Ingrese la ruta de la imagen: paisaje.png
Seleccione el método (pixel/ascii): ascii
Ingrese el ancho ASCII: 100

*Resultado:* 
- Archivo TXT con representación ASCII.

## Licencia
Proyecto realizado con fines educativos y académicos.

## Autores
Karla Escobar Figuera & Isabella Amoresano




