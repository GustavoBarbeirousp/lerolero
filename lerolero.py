#!/usr/bin/python3
"""Gerador de lero-lero.

Gera frases de efeito sem significado real."""

import random

# Cada frase é composta por três partes aleatórias; aqui,
# Listas de possibilidades para cada uma das partes

parte1 = []
parte2 = []
parte3 = []

lingua = int(input("Escolha a lingua: 1 - português; 2 - inglês\n"))

if lingua == 2:
	parte1 = []
	parte2 = []
	parte3 = []

# Imprimi em ordem aleatória

print (random.choice(parte1), random.choice(parte2), rondom.choice(parte3))
