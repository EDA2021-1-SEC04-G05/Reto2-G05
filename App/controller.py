"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv

"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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




"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategories(catalog)

def loadVideos(catalog):
    """
    Carga los videos del archivo.
    """
    videofile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videofile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategories(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    catfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(catfile, encoding='utf-8'),delimiter="\t") 
    for category in input_file:
        model.addCat(catalog, category)
# Funciones de ordenamiento
def sortVideos(catalog, size,stype):
    """
    Ordena los libros por average_rating
    """
    return model.sortVideos(catalog, size,stype)
# Funciones de consulta sobre el catálogo
def Req2(catalog, country):
    return model.Req2(catalog, country)

def Req4(catalog, country, tag):
    return model.Req4(catalog, country, tag)
    
def getVideosbyCat(catalog,countryname,category):
    """
    Retrona los videos de un pais
    """
    videolist = model.getVideosbyCat(catalog, countryname, category)
    return videolist
def getTendencyTime(catalog,category):
    Tendtime= model.getTendencyTime(catalog, category)
    return Tendtime
def getVideosbyCatLikes(catalog,category):
    vidCat=model.getVideosbyCatLikes(catalog,category)
    return vidCat