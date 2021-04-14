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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.DataStructures import listiterator as lit
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'videos': None,
                'countries':None,
               'categories': None,
               'video_category':None,
               'tendency':None}
    catalog['videos'] = lt.newList('SINGLE_LINKED', compareViews)
    catalog['id'] = mp.newMap(maptype='CHAINING',
                                   loadfactor=1.5,
                                   comparefunction=compareMapVideoIds) #size para dias 
    catalog['categories'] = mp.newMap(34,
                                   maptype='CHAINING',
                                   loadfactor=1.5,
                                   comparefunction=compareMapVideoIds)
    catalog['countries'] = mp.newMap(10,
                                   maptype='CHAINING',
                                   loadfactor=1.5,
                                   comparefunction=compareMapCountry)
    catalog['video_category'] = mp.newMap(maptype='CHAINING',
                                   loadfactor=1.5,
                                   comparefunction=compareMapVideoIds)
    catalog['tendency'] = mp.newMap(maptype='PROBING',
                                   loadfactor=0.2,
                                   comparefunction=compareMapVideoIds)       
    return catalog
# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    #lt.addLast(catalog['videos'], video)
    countryname=video['country']
    exist = mp.contains(catalog['id'], video['video_id'])
    if exist:
        entry = mp.get(catalog['id'],video['video_id'])
        vid_id = me.getValue(entry)  
    else:
        mp.put(catalog['id'], video['video_id'], video)
        vid_id= mp.put(catalog['id'],  video['video_id'],video)
    lt.addLast(catalog['videos'], video)
    addVideoCountry(catalog,countryname, video)
    addTend(catalog,video)
    vid_cat=video['category_id']
    exist = mp.contains(catalog['video_category'], vid_cat)
    if exist:
        entry = mp.get(catalog['video_category'],vid_cat)
        li = me.getValue(entry)
    else:
        li=lt.newList('SINGLE_LINKED', compareViews)#ojo aca esto 
        mp.put(catalog['video_category'], vid_cat, li)
    lt.addLast(li,video)
  

def newId(video): 
    dic={}
    dic['title']=e['title']
    dic['channel_title']=e['channel_title']
    dic['category_id']=e['category_id']
    dic['days']=1
    lt.addLast(x,dic)
    lt.addLast(l,e['title'])
    return dic 


def addVideoCountry(catalog, countryname, video):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    countries = catalog['countries']
    exist = mp.contains(countries, countryname)
    if exist:
        entry = mp.get(countries, countryname)
        country = me.getValue(entry)
    else:
        country = newCountry(countryname)
        mp.put(countries, countryname, country)
    lt.addLast(country['videos'], video)    
    
# Funciones para creacion de datos
def newCountry(countryname):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    country = {'name': "", "videos": None}
    country['name'] = countryname
    country['videos'] = lt.newList('ARRAY_LIST')
    return country

def addCat(catalog, category):
    """
    Adiciona una categoria a la lista de categorias
    """
    cat = newCat(category['name'], category['id '])
    mp.put(catalog['categories'], cat['name'], cat['id'])   
    

def newCat(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    cat = {'name': '', 'id': ''}
    cat['name'] = name
    cat['id'] = id
    return cat
def newTend(e):
    dic={}
    dic['title']=e['title']
    dic['channel_title']=e['channel_title']
    dic['category_id']=e['category_id']
    dic['country']=e['country']
    dic['days']=1
    return dic
def addTend(catalog,video):
    tend = catalog['tendency']
    
    exist = mp.contains(tend, video['video_id'])
    if exist:
        entry = mp.get(tend, video['video_id'])
        ved = me.getValue(entry)
        vef=ved['elements']
        a=vef[0]
        a['days']+=1
    else:
        li=lt.newList('ARRAY_LIST',compareDays)
        ved = newTend(video)
        lt.addLast(li,ved)
        mp.put(tend, video['video_id'], li)   
# Funciones para creacion de datos
def getVideosByCountry(catalog, country):
    """
    Retorna un pais con sus videos a partir del nombre del pais
    """
    exist = mp.contains(catalog['countries'], country) 
    if exist:
        entry = mp.get(catalog['countries'], country)
        country1 = me.getValue(entry)
    else: 
        country1="No existe ese Pais"
    return country1

def getCat(catalog,category):
    exist = mp.contains(catalog['categories'], category)
    if exist:
        cati=mp.get(catalog['categories'],category)
        cat_id= me.getValue(cati)
    else: 
        cat_id=0
        
    return cat_id


# Funciones de consulta
def getVideosbyCatLikes(catalog,category):
    vid_cat=getCat(catalog,category)
    if vid_cat != 0:
        exist = mp.contains(catalog['video_category'], vid_cat)
        if exist:
            entry = mp.get(catalog['video_category'],vid_cat)
            li = me.getValue(entry)
    return li

def getVideosbyCat(catalog,countryname,category):
    country=getVideosByCountry(catalog,countryname) #o(1)/o(n)
    result=lt.newList('ARRAY_LIST',compareViews)
    cat_id=getCat(catalog,category)
    b=lit.newIterator(country['videos'])
    while lit.hasNext(b):
        video=lit.next(b)
        if video["category_id"]==cat_id: 
            lt.addLast(result, video)
    re=sortVideos(result)
    return re
def getTendencyTime(catalog,category):
    vid_cat=getCat(catalog,category)
    if vid_cat != 0:
        tend = catalog['tendency']
        a=tend['table']
        tendm=''
        tendtime=0
        for e in a['elements']:
            le=me.getValue(e)
            if le!=None:
                elements=le['elements']
                elements=elements[0]
                if elements['category_id']==vid_cat:
                    if elements['days']>tendtime:
                        tendm=elements
                        tendtime=elements['days']

    else: 
        tendm="No existe esa categoria"
    return tendm   
def Req2 (catalog, country):
    videosCountry= getVideosByCountry(catalog, country)
    if videosCountry!= None:
        tend = catalog['tendency']
        a=tend['table']
        tendm=''
        tendtime=0
        for e in a['elements']:
            le=me.getValue(e)
            if le!=None:
                elements=le['elements']
                elements=elements[0]
                if elements['country']==country:
                    if elements['days']>tendtime:
                        tendm=elements
                        tendtime=elements['days']
    else: 
        tendm="No existe esa categoria"
    return tendm

def Req4(catalog,country,tag):
    videosCountry= getVideosByCountry(catalog, country)
    result=lt.newList('ARRAY_LIST',compareLikes)
    b=lit.newIterator(videosCountry['videos'])
    while lit.hasNext(b):
        e=lit.next(b)
        if tag in e['tags']:
            dic={}
            r= lt.isPresent(result,e)
            if r==0:
                dic['title']=e['title']
                dic['channel_title']=e['channel_title']
                dic['publish_time']=e['publish_time']
                dic['views']=e['views']
                dic['likes']=e['likes']
                dic['dislikes']=e['dislikes']
                dic['tags']=e['tags']
                lt.addLast(result,dic)
    sort=sortLikes(result)
    #print(lt.getElement(dic_sort,1))
    return sort


           
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareViews (video1,video2):
    return (float(video1['views']) > float(video2['views']))
def compareLikes (video1,video2):
    return (float(video1['likes']) > float(video2['likes']))
def compareDays (video1,video2):
    return (float(video1['days']) > float(video2['days']))
def compareNames(video1, video2):
    if (video1['title'].lower() == video2['title'].lower()):
        return True
    return False
def compareMapVideoIds(id, entry):
    """
    Compara dos ids de videos, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if id ==identry :
        return 0
    elif id > identry:
        return 1
    else:
        return -1
def compareMapCountry(countryname, entry):
    """
    Compara dos ids de videos, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if countryname ==identry :
        return 0
    elif countryname > identry:
        return 1
    else:
        return -1


def sortLikes(catalog):
    sub_list = catalog.copy()
    sorted_list = qs.sort(sub_list, compareLikes)
    #stop_time = time.process_time()
    #elapsed_time_mseg = (stop_time - start_time)*1000
    return sorted_list

def sortVideos(catalog):
    sub_list = catalog.copy()
    sorted_list = qs.sort(sub_list, compareViews)
    #stop_time = time.process_time()
    #elapsed_time_mseg = (stop_time - start_time)*1000
    return sorted_list