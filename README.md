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
 - si on a des soucis avec le déploiement, faire du javascript (caches de la page, etc)
 - formulaire pour envoyer des mails en python : https://www.tutorialspoint.com/python/python_sending_email.htm
 - liste de mots français courrants, voir ça : https://en.wikipedia.org/wiki/Swadesh_list

- import xtarfile dans main.py et dézip fr_core... et tar-filer le modèle et faire pareil



- récup le dico français des mots
- récup les mots les + fréquents
- transformer le .bin en .txt ou le lire le modèle en python
- on garde dans le modèle que les mots les + fréquents
- on sauvegarde le modèle en bin avec gensim

- ALTERNATIVE : faire une PCA sur les embeddings