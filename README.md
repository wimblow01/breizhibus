# Breizhibus

## Fonctionnement de l'appli

### Page d'accueil

Lorsque que l'on lance l'application on arrive sur la page d'accueil qui propose
- le header
  - le logo de l'appli
  - le nom de l'appli
  - un "menu" de bouton pour sélectionner la page que l'on veut
    - accueil
    - ajouter/supprimer
    - modifier
- le body
  - un espace d'affichage et de manipulation

Quand on clique sur le bouton d'une ligne (partie gauche), ça récupère et affiche les arrèts de cette ligne, leur adresse respective et les bus qui l'empruntent sous forme de tableau dans la partie droite.

![accueil.PNG](accueil.PNG) 

### Page de ajout/suppression

En cliquant sur le bouton *ajouter/supprimer* on arrive sur la page susnommée. \n
Cette dernière propose sur la partie gauche l'interface d'ajout proposant des champs dans lesquels il faut renseigner les informations nécessaires à la création du bus (numéro, immatriculation, nombre de places et la ligne sur laquelle il tourne). \n
Sur la partie droite, on a l'interface de suppression qui propose un menu déroulant dans lequel on peut choisir le bus à supprimer 

![ajout_suppr.PNG](ajouter_supprimer.PNG) 

### Page de modification

Cette page n'est pas encore tout à fait terminée. Malgré tout elle propose déjà sur la partie gauche un menu déroulant qui nous permet de choisir le bus à modifier et sur la partie droite les information sur ce bus que l'on veut remplacer (immatriculation, nombre de place, ligne)

![modifier.PNG](modif.PNG) 

## Choix techniques

Il reste encore quelques petites finitions comme un titre pour les pages d'accueil et de modification. De même, les pages d'ajout et modification peuvent être améliorées.

Pour la page d'accueil j'ai choisi de présenter une succession de boutons pour la sélection de lignes car je trouve cela plus visuel et plus aggréable à manipuler. La contrainte se trouve dans le nombre de lignes: je pense que si je devais avoir deux voire trois mignes de plus cet affichage poserait des problèmes et il faudrait sans doute passer par un menu déroulant. Quand on clique sur le bouton, cela renvoie sur un affichage simple car on veut juste présenter les données enregistrées.

Pour la page d'ajout, j'ai opté pour une succession de champs à remplir avec des placeholder afin de montrer quoi renseigner. La partie suppression est basée sur un menu déroulant proposant la liste des bus. Je suis parti du principe que la personne sur l'appli connaît déjà le bus à supprimer et n'a donc besoin que de son numéro.
Pour amélioreron peut imaginer des revoir la page pour afficher la liste des bus existants (affichage limité par le nombre total de bus). Pour terminer cette page, il faut que j'ajoute un message d'erreur si jamais le numéro de bus ou son immatriculation existe déjà, ainsi que mettre un champ sous le menu déroulant de suppression qui indiquerait les informations du bus à supprimer pour s'assurer que c'est le bon.

Pour la dernière page j'ai mis un menu déroulant pour sélectionner le bus pour sa praticité d'utilisation et des champs pour renseigner les informations à modifier. Pour cette page et celle d'ajout, je pense mettre par la suite, des menus déroulants pour sélectionner la ligne dans la liste de celles existantes (afin d'éviter des erreurs). De plus je dois mettre un place un affichage différent: actuellement, la page est affiché comme la capture d'écran; c'est à dire avec les menu déroulant et les champs. par la suite, je compte mettre en place un affichage différé: on n'aura au lancement de la page que le menu déroulant, puis losque l'on choisit un bus, les champs apparaîtraient pré-remplis avec les infos du bus.

## Difficulés rencontrées

J'ai rencontré pas mal de difficultés pour l'interface graphique car je n'en avais pas vraiment fait avant. Heureusement j'ai pu compter sur certains de mes collègues; je voudrais donc remercier Thomas, Pereg et Julien.
