import globales
import csv
import os
import math
import random
import json

os.system("cls")



productos = [ "Café Americano",
"Té Chai",
"Croissant",
"Jugo Naranja",
"Panini de Pavo y Queso",
"Pastel de Zanahoria",
"Espresso Doble",
"Ba;do de Frutas",
"Muffin",
"Ensalada",
"Chocolate Caliente",
"Tarta de Frambuesa",
"Sándwich de Huevo",
"Galletas de Avena",
"Frappé de Caramelo"
]
def montos_aleatorios():
    producto_random=globales.leer_archivo_json("productos.json")
    ventas=globales.leer_archivo_json("ventas.json")
    
    print("Datos añadidos") 
def estadisticas():
    print("hola")

    
def menu():
    
    print("1. Asignar montos aleatorios.")
    print("2. Ver estadíscas")
    print("3. Salir del programa.")
    opcion = globales.seleccionar_opcion(4)

    opcion == 1
    montos_aleatorios()
    opcion == 2
    
    opcion == 3     
    return

menu()



    
    





    
    