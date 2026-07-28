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

