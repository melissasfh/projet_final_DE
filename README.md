# Projet de Réduction de Dimension
## Aperçu
Ce projet final a été réalisé par une équipe de trois collaborateurs, visant à mettre en œuvre trois méthodes distinctes de réduction de dimension. Les principales méthodes implémentées sont l'Analyse en Composantes Principales (ACP), UMAP et t-SNE.

# 1. Organisation du Projet
Création du Répertoire GitHub

Nous avons initié ce projet en créant un dépôt GitHub central, auquel chaque membre de l'équipe a contribué. Nous avons ensuite cloné ce dépôt sur nos machines locales.

# 2. Travail sur les Branches Individuelles

Chaque membre a créé une branche dédiée sur sa machine locale. Nous avons développé des notebooks distincts pour chaque méthode de réduction de dimension (ACP, UMAP, t-SNE) dans ces branches respectives. Ces notebooks contiennent le prétraitement des données, l'application de la fonction de réduction de dimension, ainsi que l'évaluation finale avec l'algorithme KMeans et les métriques NMI et ARI.

# 3. Intégration du Code dans la Branche Principale

Dans un second temps, nous avons effectué des modifications sur les branches principales, en y incorporant le code des notebooks respectifs. Nous avons fusionné ces branches sur GitHub pour consolider l'ensemble des documents dans le dépôt principal.

# 4. Gestion des Conflits et Fusion des Branches

Durant le processus de fusion, un conflit est survenu. Nous l'avons résolu en sauvegardant une seule version du code, préservant ainsi l'intégralité des fonctionnalités de réduction de dimension.

# 5.Création du Container Docker
Pour rendre notre projet accessible sur Docker Hub, nous avons créé deux fichiers : requirements.txt, qui contient toutes les bibliothèques nécessaires au fonctionnement de notre code, et un Dockerfile. Nous avons procédé au build de notre image, puis au run de notre projet, affichant ainsi les résultats des trois méthodes via des impressions (print).

# 6. Sauvegarder les données pour ne pas les télécharger à chaque instanciation:
Pour ne pas charger les données à chaque instentiation, nous avons telechargé les données en format ('CSV') après l'etape de l'embedding, et nous avons mis à jour le code afin de charger les données en question directement en tant que dataframe. Cela dans le but de reduire la taille de notre image.

