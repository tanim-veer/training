# 29/07

## Git

git status    → pour connaitre la situation des fichiers - À taper tout le temps
git add X     → zone 1 vers zone 2 (préparation) on prepare les fichiers dans status
git commit    → zone 2 vers zone 3 (dépôt local) envoie RIEN sur internet mais en local
git push      → zone 3 vers zone 4 (GitHub)
git log       → l'historique des commits

## SSH

ssh-keygen -t ed25519 -C "mail"  → crée la paire. -t = algo, -C = étiquette
ssh-add ~/.ssh/id_ed25519        → charge la clé dans l'agent (1 fois par session)
ssh -T git@github.com            → teste que GitHub me reconnaît

# 31/07

## Correction interro à froid n°1

schéma 4 zones : répertoire de travaille (PC) -> Préparation (staging) -> Depot local (.git) -> Depot distant (github)

Paire de clé > mdp : mdp voyage alors que clé privée reste fixe

chiffrer = illisible ;; signer = prouve grace à l'authentification (verif que c'est moi grace clé privé) & intégrité (si un bit change, verif échoue)

Trame config nouveau pc : AUTHENTIFICATION (générer la paire de clés, donner la publique à GitHub, charger la clé dans l'agent. Sans ça, le push est refusé et tu es bloqué)

## Linux
whoami, id
root = uid 0, ignore les permissions. $ = moi, # = root
sudo = exécute UNE commande en root, puis me rend la main. Trace + demande mon mdp
permissions : type + 3 blocs rwx, propriétaire/groupe/autres, notation chiffrée
se déplacer : cd, .., ~, Tab
