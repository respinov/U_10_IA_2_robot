#/usr/bin/env python
# -*- coding: utf-8 -*-
# Vuelos con busqueda en amplitud

from arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):

    solucionado = False
    nodos_visitados = [] 
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        nodo=nodos_frontera[0]
        # Extraer todo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        
        if nodo.get_datos() == solucion:
          # solución encontrada   
          solucionado = True
          return nodo       #nodos_visitados  
        else:
          #Expandir nodos hijo   (ciudades con conexion)
          dato_nodo = nodo.get_datos()
          lista_hijos = []
          for un_hijo in conexiones[dato_nodo]:
             hijo = Nodo(un_hijo)
             lista_hijos.append(hijo)
             if not hijo.en_lista(nodos_visitados)\
             and not hijo.en_lista(nodos_frontera):
                 nodos_frontera.append(hijo)
          nodo.set_hijos(lista_hijos)    
         
    
if __name__=="__main__": 
    conexiones = {
        'inicio':{'a', 'c', 'd', 'e'},
        'a':{'b', 'c', 'inicio'},
        'b':{'a', 'c'},
        'c':{'a', 'b', 'inicio', 'l', 'k', 'h', 'd'},
        'd':{'inicio', 'c', 'e', 'g'},
        'e':{'inicio', 'd', 'f'},
        'f':{'g', 'i'},
        'g':{'h', 'i', 'd', 'f'},
        'h':{'c', 'k', 'g'},
        'i':{'h', 'g', 'f'},
        'j':{'k', 'm', 'fin', 'i'},
        'k':{'c', 'h', 'j', 'm', 'l'},
        'l':{'fin', 'm', 'k', 'c'},
        'm':{'l', 'j', 'fin'},
        'fin':{'l', 'm', 'j'}
        #'':{},
    
    
    
    }
    #Tesoro 1 h
    #Tesoro 2 f
    #Tesoro 3 i
     
    estado_inicial = 'inicio'
    solucion = 'i'
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)
    # mostrar resultado
    resultado =[]
    nodo = nodo_solucion
    while nodo.get_padre() != None:
      resultado.append(nodo.get_datos())
      nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print (resultado)
