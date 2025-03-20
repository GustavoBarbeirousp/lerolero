#!/usr/bin/python3
"""Gerador de lero-lero.

...Gera frases de efeito sem significado real."""

import random

# Cada frase é composta por três partes aleatórias;
# Listas de possibilidade para cada uma das partes.

parte1 = [
	"O sistema em desenvolvimento",
	"O novo protocolo de comunicação",
	"O algoritmo otimizado e"
	]
parte2 = [
	"possui excelente desenpenho",
	"oferece garantias de precisão acima da média"
	"preenche uma lacuna significatica"
	]
parte3 = [
	"nas aplicações a que se destina",
	"em relação às opções disponíveis no mercado",
	", promovendo ampla vantagem competitica a seus usuários"
	]

lingua = int(input("Escolha a lingua: 1 - português; 2 - inglês\n"))

if lingua == 2:
	parte1 = []
	parte2 = []
	parte3 = []

# Combina as partes aleatoriamente

print (random.choice(parte1), random.choice(parte2), rondom.choice(parte3))
