#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 7, 2014

@author: anroco

In python you can add an item to a tuple created?

En python ¿se puede agregar un elemento a una tupla creada?
'''

#create a tuple
tupla = (3, 6, 2, 7, 1)
print (tupla)

#tuples are immutable, so you can not adding new elements
#using merge of tuples with the + operator could add an item, create new tuple.
tupla = tupla + (10,)
print(tupla)

#adding items in a specific index
tupla = tupla[:2] + (20, 28, 24) + tupla[2:]
print(tupla)

#converting the tuple to list
lista = list(tupla)
#use different ways to add items in a list
lista.append(30)
#converting the tuple to list
tupla = tuple(lista)
print(tupla)
