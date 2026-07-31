# 29/07

## Git

- git status    → pour connaitre la situation des fichiers - À taper tout le temps
- git add X     → zone 1 vers zone 2 (préparation) on prepare les fichiers dans status
- git commit    → zone 2 vers zone 3 (dépôt local) envoie RIEN sur internet mais en local
- git push      → zone 3 vers zone 4 (GitHub)
- git log       → l'historique des commits
- git commit -am (Le -a fait le git add mais à faire que sur un fichier deja add pas un nouveau fichier créer car il va l'ignorer)
- phrase de passe -> chiffre et signe la clé privé (quand tu demandes à utiliser la clé (ssh-add, un push...), SSH doit d'abord déchiffrer le fichier, ce n'est pas "il vérifie un mot de passe puis te donne accès", c'est "il utilise ta phrase comme clé de déchiffrement"

## SSH

- ssh-keygen -t ed25519 -C "mail"  → crée la paire. -t = algo, -C = étiquette
- ssh-add ~/.ssh/id_ed25519        → charge la clé dans l'agent (1 fois par session)
- ssh -T git@github.com            → teste que GitHub me reconnaît

# 31/07

## Correction interro à froid n°1

- schéma 4 zones : répertoire de travaille (PC) -> Préparation (staging) -> Depot local (.git) -> Depot distant (github)

- Paire de clé > mdp : mdp voyage alors que clé privée reste fixe

- chiffrer = illisible ;; signer = prouve grace à l'authentification (verif que c'est moi grace clé privé) & intégrité (si un bit change, verif échoue)

- Trame config nouveau pc : AUTHENTIFICATION (générer la paire de clés, donner la publique à GitHub, charger la clé dans l'agent. Sans ça, le push est refusé et tu es bloqué)

## Linux
seikatsu@OZF:~/training$
    │      │      │     │
    │      │      │     └── le symbole d'invite $ = user normal et # = root
    │      │      └──────── TON RÉPERTOIRE COURANT
    │      └─────────────── le nom de la machine
    └────────────────────── ton nom d'utilisateur
- whoami, id
- root = uid 0, ignore les permissions
- sudo = exécute UNE commande en root, puis me rend la main. Trace + demande mon mdp
- permissions : type + 3 blocs rwx, propriétaire/groupe/autres, notation chiffrée
- se déplacer : pwd, ls, cd .. (parent), cd (retour ~), cd - (retour comme bouton précédent)
- chemin absolu : depuis la racine (commence par /) 
- chemin relatif : depuis ou je suis situé

## Python
- type(x) → donne la nature d'une donnée
- 4 types : int (entier), float (virgule), str (texte), bool (True/False)
- /  → toujours float     //  → quotient entier     %  → reste (modulo)
- guillemets = texte : "5" n'est PAS le nombre 5
- + colle le texte, sans espace. int + float = float
- float imprécis : ne jamais tester l'égalité stricte entre deux float
- = reçoit la valeur (action) > age = 22
- == est-il égal à ? (question)	> age == 22
- input() renvoie TOUJOURS un str, même si on tape un nombre
- int("5") convertit texte -> entier. int(nombre) SANS guillemets = le contenu de la boîte
- fonctions emboîtées : Python calcule de l'intérieur vers l'extérieur
- lire un traceback : fichier + ligne, puis la dernière ligne (TypeError, ValueError...)
- if condition:  puis bloc indenté (4 espaces). else: pour le cas contraire
- l'indentation EST le langage en Python : ce qui est décalé appartient au bloc
- comparateurs : ==  !=  >  <  >=  <=
- dans un if, toujours == (comparer), jamais = (affecter)
- % n donne toujours un résultat entre 0 et n-1
- prouver qu'un code marche pour TOUS les cas > le tester sur un cas

étape lors du code boucle / conditions : 
1. initialiser l'accumulateur AVANT la boucle
2. le mettre à jour À CHAQUE tour, dans la boucle
3. l'utiliser APRÈS la boucle
1. initialiser l'accumulateur AVANT la boucle
2. le mettre à jour À CHAQUE tour, dans la boucle
3. l'utiliser APRÈS la boucle
