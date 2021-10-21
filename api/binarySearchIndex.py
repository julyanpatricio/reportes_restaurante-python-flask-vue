#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 00:35:34 2021
@author: julyanpatricio
"""
from datetime import date
# Estos codigos funcionan con lista ordenada de menor a mayor
# def bbinaria_index_menor_a(lista, fechaRecibida, partialIndexTrue = -1, referenceIndex=0):
#     ''' Devuelve el indice del elemento siguiente a la fecha recibida
#     requisito: lista ordenada
#     '''
#     if len(lista) == 0:
#         return -1
#     elif len(lista) == 1:
#         if date.fromisoformat(fechaRecibida) >= date.fromisoformat(lista[0]['date_closed'][:10]):
#             return referenceIndex
#         else:
#             return partialIndexTrue
#     else:
#         medio = len(lista)//2
#         if date.fromisoformat(fechaRecibida) >= date.fromisoformat(lista[medio]['date_closed'][:10]):
#             return bbinaria_index_menor_a(lista[:medio],fechaRecibida,referenceIndex + medio,referenceIndex)
#         else:
#             return bbinaria_index_menor_a(lista[medio:],fechaRecibida,partialIndexTrue,referenceIndex + medio )


# def bbinaria_index_menor_a(lista, e, referenceIndex=0):
#     ''' Devuelve el indice del elemento anterior a la fecha recibida
#     requisito: lista ordenada
#     '''
#     if len(lista) == 0:
#         return -1
#     elif len(lista) == 1:
#         if date.fromisoformat(fechaRecibida) >= date.fromisoformat(lista[0]['date_closed'][:10]):
#             return referenceIndex
#         else:
#             return -1
#     else:
#         medio = len(lista)//2
#         if date.fromisoformat(fechaRecibida) >= date.fromisoformat(lista[medio]['date_closed'][:10]):
#             return bbinaria_index_menor_a(lista[medio:],fechaRecibida,referenceIndex + medio )
#         else:
#             return bbinaria_index_menor_a(lista[:medio],fechaRecibida,referenceIndex)

# Estos codigos funcionan con lista ordenada de mayor a menor

def bbinaria_index_menor_a(lista, fechaRecibida, partialIndexTrue = -1, referenceIndex=0):
    ''' Devuelve el indice del elemento siguiente a la fecha recibida
    requisito: lista ordenada
    '''
    if len(lista) == 0:
        return -1
    elif len(lista) == 1:
        if date.fromisoformat(fechaRecibida) >= date.fromisoformat(lista[0]['date_closed'][:10]):
            return referenceIndex
        else:
            return partialIndexTrue
    else:
        medio = len(lista)//2
        if date.fromisoformat(fechaRecibida) >= date.fromisoformat(lista[medio]['date_closed'][:10]):
            return bbinaria_index_menor_a(lista[:medio],fechaRecibida,referenceIndex + medio,referenceIndex)
        else:
            return bbinaria_index_menor_a(lista[medio:],fechaRecibida,partialIndexTrue,referenceIndex + medio )

def bbinaria_index_mayor_a(lista, fechaRecibida, referenceIndex=0):
    ''' Devuelve el indice del elemento anterior a la fecha recibida
    requisito: lista ordenada
    '''
    if len(lista) == 0:
        return -1
    elif len(lista) == 1:
        if date.fromisoformat(fechaRecibida) <= date.fromisoformat(lista[0]['date_closed'][:10]):
            return referenceIndex
        else:
            return -1
    else:
        medio = len(lista)//2
        if date.fromisoformat(fechaRecibida) <= date.fromisoformat(lista[medio]['date_closed'][:10]):
            return bbinaria_index_mayor_a(lista[medio:],fechaRecibida,referenceIndex + medio )
        else:
            return bbinaria_index_mayor_a(lista[:medio],fechaRecibida,referenceIndex)