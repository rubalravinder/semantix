# semantle_perso

## Etapes du projet :<br>
- Récupérer l'image docker <br>
        - https://hub.docker.com/r/insectatorious/word2vec-api : filée par Jérémie - en anglais (?) <br>
        - https://fauconnier.github.io/#data : en français <br>
- Créer une appli Flask
- Faire un docker-compose avec l'appli et l'image word2vec <br>
- ???
<br>

## Environnement virtuel
- python = 3.9.10
- pymagnitude (si tuto)
- gensim
- Flask-WTF
- WTForms
- Flask-Table (test pour test_similarity)


### Tuto déploiement d'un modèle
https://www.alibabacloud.com/blog/how-to-create-and-deploy-a-pre-trained-word2vec-deep-learning-rest-api_594064



17/03/2022
CHOSES A FAIRE : 
 - régler problèmes du dictionnaire français (Martin)
 - trouver des trucs beaux et stylés à rajouter en css (Martin)
 - rajouter bouton indice (Rubal) avec texte qui s'affiche
 - scaling du tableau des réponses (Rubal)
 - afficher mot inexistant sur la même page
 - Quand gagné, boutton rejouer et ça repart à zéro