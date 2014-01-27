CONVENTION  DE CODAGE
======================


NOMMAGE
--------
Toutes variables, fonctions, attributs et méthodes
doivent repsecter le camelCase. Ex: viePersonnage.
Les noms doivent tous décrire précisément à quoi la donnée se réfère.

Toutes les variables doivent contenir un minimum de 4 lettres sauf pourles itérateurs et coordonées.

## LANGUES

Le code devrait toujours être écrit en Anglais.



VARIABLES BOOLÉENNES ET FONCTIONS BOOLÉENNES.
----------------------------------------------
Le nom des variables booléennes doivent répondre à une question afin de mieux les reconnaître dans le code en utilisant les préfixe is, has.
Par exemple, la fonction retournant si le personnage d'un jeu est mort ou nom devrait être:
```
	personnage.isDead();
```

Dans le cas ou un personnage possèderait un objet ou non on obtiendrait:
```
	personnage.hasGun();
```


NOMS DE FICHIER
---------------
les fichiers doivent suivre la convention pour les Classes


NOMS DE TYPE
------------
le nom de tous les types que ce soit des classes, structs, typedefs, ou enums doivent
suivre le upper CamelCase. Ainsi ils commencent tous par une Majuscule et avoir une 
majuscule pour chaque nouveau mot. Aucune utilisation de underscore(_).

ex: 
```
class  Position { ...
class  MenuTitre{ ...
sturct InformationPerso{ ...
```

NOMS DE CONSTANTES
------------------
les constantes devraient toujours être en MAJUSCULE et spéraée par des underscore (_) pour chaque mot.
ex:
```
const int WINDOW_HEIGHT=800, WINDOW_WIDTH=600;
```

ESPACES DE NOMS
---------------

les espaces de noms devraient toujours être en minuscule et séprarés par 
des underscore (_) pour chaque mot:
example: 
```
badass_motherfucker
```

ENUMÉRATEUR
-----------
Les élément d'un enum devraient toujours êter en majuscule et spéarés par des underscore (_) 
ex.:
```
enum Color { RED, ORANGE, BLUE, YELLOW }
```











FICHIER ENTÊTE
==============
tous les fichiers d'entête doivent contenir l'extension ".hpp".

"#define" GUARD
--------------

le format des #define guards doit être : <DOSSIER_COURANT>_<FICHIER>_HPP

Les nom de variables, fonctions, classes, méthodes et attributs


LONGUEUR DES FONCTIONS ET MÉTHODES
==================================
chaque fonction ou méthode doit contenir un maximum de 30 lignes.


VARIABLES GLOBALES
==================
PAS DE VARIABLES globales.




CLASSES
========


CLASS vs STRUCT
---------------
Les struct ne doivent être utilisées seulement dans la cas d'objets passifs (i.e qui n'ont aucun comportement) qui ne font que contenir des données, 
dans les autres cas, on utilise des classes.


ATTRIBUTS
---------
Les attributs doivent toujours être préfixer de " m_"
example:
```
float m_healt;

```



ENCAPSULATION
--------------
Les attributs doivent toujours être private. Leur accès se fait à l'aide d'accesseurs et mutateurs.



ORDRE DES DÉCLARATIONS
----------------------
Tous les élément public: doivent être déclarés en premier, suivis des éléments protected et finalement par les éléments private:

À l'intérieur de chacune de ces section (public:, protected:, private:) les déclarations
devraient suivre l'ordre suivant:

* Typedefs et Enum
* Constantes (static const)
* Constructeurs
* Destructeurs
* Méthodes Statiques
* Méthodes
* Attributs (excepté les static const)






AUTRES
======

0 et nullptr/NULL
-------------------
Utiliser 0 pour les entiers, 0.0 pour les nombre réels et '\0' pour les chars.

Float
------
toujours suffixer les float par f 
```
ex: float var = 5.0f;
```

COMMENTAIRES
-------------
Il faut utiliser des commentaires afin que le code soit lisible pour une tierece personne.
Ne pas avoir peur de mettre des commentaires expliquant des attributs et des fonctions.


Commentaire de fichier
----------------------
Tous les fichiers devraient avoir en entête par ceci:
```
/////////////////////////////////////////////////////////////////////////////////
//  
//  Nom du Projet
//  Copyright (C) 2013 Team G.O.A.T
//  This program is free software; you can redistribute it and/or
//  modify it under the terms of the GNU General Public License
//	as published by the Free Software Foundation; either version 2
//	of the License, or (at your option) any later version.
//
//	This program is distributed in the hope that it will be useful,
//	but WITHOUT ANY WARRANTY; without even the implied warranty of
//	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//	GNU General Public License for more details.
//
//	You should have received a copy of the GNU General Public License
//	along with this program; if not, write to the Free Software
//	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
//  
//  Nom:    	 Nom du fichier
//  Auteur:     Auteurs
//  Description: Une description du contenu du fichier
//
//
/////////////////////////////////////////////////////////////////////////////////

```

COMMENTAIRE TODO
----------------
utiliser les commentaires TODO pour les section de code temporaires.




