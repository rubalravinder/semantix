# Projet SEMANTIX

## Environnement virtuel
- python = 3.9.10
- pandas
- gensim
- Flask-WTF
- WTForms
- Flask-Table (test pour test_similarity)
- spacy
- fr_core_news_md

## CHOSES A FAIRE : 
 - régler problèmes du dictionnaire français (Martin)
 - trouver des trucs beaux et stylés à rajouter en css (Martin)
 - highlight le dernier mot proposé dans la table (récup variable word_proposed et la modif en html? OU en javascript avec JQuery (semble plus simple))

## Règles du jeu

Un objectif : Trouver le mot secret !
Comment faire : En proposant des mots de plus en plus proches contextuellement du mot secret.
Comment savoir : Pour chaque mot proposé, un score de similarité avec le mot secret est calculé. Ce score, qui définit la proximité sémantique entre les deux mots, augmente lorsque les deux mots sont de plus en plus proche (il atteint 1 lorsque les deux mots sont identiques).

----------------------
En savoir plus :

Semantix est un jeu en ligne inspiré de son équivalent anglais Semantle dont le but est de trouver un mot secret tiré au sort dans une base de données de mots français.

Sémantique : 
Deux mots sont proches sémantiquement lorsqu'ils possèdent un grand nombre d'éléments en commun, et non pas car ils ont un grand nombre de lettres en commun. Par exemple, le score de similarité entre "voiture" et "véhicule" est de 0.73 tandis que celui entre "voiture" et "toiture" s'élève seulement à 0.10.

Fonctionnement : 
Ce jeu s'appuie sur un modèle d'intelligence artificielle pré-entrainé sur une grande base de données de textes, qui permet de transformer des mots en vecteurs. Pour calculer la distance entre deux mots, le modèle calcule la similarité cosinus (ou cosinus de l'angle) entre les deux vecteurs représentant respectivement chaque mot.

Pour simplifier le jeu, les verbes conjugués et les variantes féminines ou plurielles des mots ont été eliminées des mots à deviner (grâce à un deuxième modèle d'intelligence artificielle pré-entrainé). Cependant, les accents et les majuscules comptent lors de la saisie du texte.