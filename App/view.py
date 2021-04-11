"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp
from DISClib.DataStructures import listiterator as lit
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")

catalog = None

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("6- Funcion Lab: Video con mas likes por categoria")
    print("2- REQ. 1: Encontrar buenos videos por categoría y país")
    print("3- REQ. 2: Encontrar video tendencia por país")
    print("4- REQ. 3: Video con más días como tendencia")
    print("5- REQ. 4: Encontrar videos con mas likes")
    print("0- Salir")

def initCatalog():
    """
    Inicializa el catalogo de Videos
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    return controller.loadData(catalog)
    
    

def printinga(ordlist,total): 
    for i in range(0,total):
        video=lt.getElement(ordlist,i)
        print ("Titulo: {0}\nChannel_title:{1}\ntrending_date: {2}\nCountry: {3}\nViews: {4}\n Likes:{5}\n Dislikes:{6}\n ".format(video['title'],video['channel_title'],video['trending_date'],video['country'],video['views'],video['likes'],video['dislikes']))
        
def printing(ordlist,total,num): 
            for i in range(1,total+1):
                video=lt.getElement(ordlist,1)
                if num==2: 
                    print ("Title: {0}\nChannel_title:{1}\nPublish_Time:{2}\nViews: {3}\nLikes: {4}\nDislikes: {5}\nTags: {6}\n".format(video['title'],video['channel_title'],video['publish_time'],video['views'], video['likes'], video['dislikes'], video['tags']))
                elif num==1:
                    print ("Titulo: {0}\ntrending_date: {1}\n Nombre del canal:{2}\n publish_time: {3}\n Views: {4}\n Likes:{5}\n Dislikes:{6}\n ".format(video['title'],video['trending_date'],video['channel_title'],video['publish_time'],video['views'],video['likes'],video['dislikes']) )






catalog = None 

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        answer= loadData(catalog)
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
        "Memoria [kB]: ", f"{answer[1]:.3f}")
        #print(' El primer video cargado es:')
        #printinga(catalog['videos'],1)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categories'])))
    elif int(inputs[0]) == 6:
        category=" " + (str(input("Ingrese la categoria de eleccion:")))
        result=controller.getVideosbyCatLikes(catalog,category)
        printinga(result,3)
    elif int(inputs[0]) == 2:
        country=str(input("Ingrese el Pais de su eleccion:"))
        category=" " + (str(input("Ingrese la categoria de eleccion:")))
        number=int(input("Ingrese la cantidad de videos que quiere ver:"))
        result=controller.getVideosbyCat(catalog,country,category)
        printing(result[0],number,1)
    elif int(inputs[0]) == 3:
        country = input ("Ingrese el país para el cual desea realizar la consulta: ")
        answer = controller.Req2(catalog, country)
        ans=answer[0]
        data=answer[1]
        
        a= "Title: {0}\nChannel_title:{1}\nCountry:{2}\nDays: {3} ".format(ans['title'],ans['channel_title'],ans['country'],ans['days'])
        print(a)
        print("Tiempo [ms]: ", f"{data[0]:.3f}", "  ||  ",
        "Memoria [kB]: ", f"{data[1]:.3f}")

    elif int(inputs[0]) == 4:
        category=" " + (str(input("Ingrese la categoria de eleccion:")))
        answer= controller.getTendencyTime(catalog,category)
        ans=answer[0]
        data=answer[1]
        a="Title: {0}\nChannel_title:{1}\nCategory_id:{2}\nDays: {3} ".format(ans['title'],ans['channel_title'],ans['category_id'],ans['days'])
        print(a)
        print("Tiempo [ms]: ", f"{data[0]:.3f}", "  ||  ",
        "Memoria [kB]: ", f"{data[1]:.3f}")
        
    elif int(inputs[0])==5:
        country = input ("Ingrese el país para el cual desea realizar la consulta: ")
        tag=" " + (str(input("Ingrese el tag:")))
        size =int( input("Indique tamaño de la lista: "))
        
        answer= controller.Req4(catalog,country,tag)
        ans=answer[0]
        data=answer[1]
        printing(ans, size,2)
        print("Tiempo [ms]: ", f"{data[0]:.3f}", "  ||  ",
        "Memoria [kB]: ", f"{data[1]:.3f}")
        
    else:
        sys.exit(0)
sys.exit(0)