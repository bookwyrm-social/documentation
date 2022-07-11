- - -
Title: Permissions Date: 2021-04-18 Order: 2
- - -

L'accès de l'utilisateur aux différentes fonctionnalités est contrôlé à l'aide du [système d'authentification intégré](https://docs.djangoproject.com/en/3.2/topics/auth/default/) de Django. Lorsqu'une instance est créée, le script `initdb` crée un ensemble de permissions, qui sont assignées aux groupes. Par défaut, tous les nouveaux utilisateurs sont assignés au groupe `éditeur` qui leur permet de modifier les métadonnées du livre.

L'administrateur de l'instance doit avoir le statut de `superutilisateur` qui leur donne accès à l'administration de Django (`/admin`) et confère toutes les permissions à cet utilisateur.

## Permissions et groupes
Ce tableau montre les quatre groupes (administrateur, modérateur, éditeur et utilisateur) et les permissions que les utilisateurs de ce groupe ont :

|                                       | admin | modérateur | éditeur | utilisateur |
| ------------------------------------- | ----- | ---------- | ------- | ----------- |
| modifier les paramètres de l'instance | ✔️    | -          | -       | -           |
| changer le niveau d'un utilisateur    | ✔️    | -          | -       | -           |
| gérer la fédération                   | ✔️    | ✔️         | -       | -           |
| créer des invitations                 | ✔️    | ✔️         | -       | -           |
| désactiver des utilisateurs           | ✔️    | ✔️         | -       | -           |
| supprimer des posts                   | ✔️    | ✔️         | -       | -           |
| modifier des livres                   | ✔️    | ✔️         | ✔️      | -           |
 mettre en ligne les pages couverture
