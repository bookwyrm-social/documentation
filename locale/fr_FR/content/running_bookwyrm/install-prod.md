- - -
Title: Installing in Production Date: 2025-04-01 Order: 1
- - -

Ce projet est encore jeune et n'est pas, pour le moment, très stable, faites preuve de prudence lors de son utilisation en production.

## Configuration du serveur
- Obtenez un nom de domaine et configurez le DNS pour votre serveur. Vous devez faire pointer les serveurs de noms de domaine de votre fournisseur DNS vers le serveur où vous allez héberger BookWyrm. Voici les instructions pour [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Configurez votre serveur avec un pare-feu approprié pour les applications web (cette page de documentation est testée avec Ubuntu 20.04). Voici les instructions pour [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Configurez un service mail (comme [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) et les paramètres SMTP/DNS appropriés. Utilisez la documentation du service pour configurer vos DNS
- [Installez Docker et docker-compose](https://docs.docker.com/compose/install/)

## Installation et configuration de BookWyrm

There are several repos in the BookWyrm org, including documentation, a static landing page, and the actual Bookwyrm code. To run BookWyrm, you want the actual app code which is in [bookwyrm-social/bookwyrm](https://github.com/bookwyrm-social/bookwyrm).

La branche `production` de BookWyrm contient nombre d'outils qui ne sont pas sur la branche `main` prévus pour fonctionner en production. Par exemple des changements dans `docker-compose` pour mettre à jour les commandes par défaut ou la configuration des conteneurs et des changements individuels à la configuration des conteneurs pour activer des choses comme SSL ou les sauvegardes régulières.

Instructions pour lancer BookWyrm en production :

- Récupérez le code de l'application : `git clone git@github.com:bookwyrm-social/bookwyrm.git`
- Basculez sur la branche `production` : `git checkout production`
- Créez votre fichier de variables d'environnement, `cp .env.example .env`, et mettez à jour les valeurs suivantes :
    - `DOMAIN` | Votre nom domaine
    - `EMAIL` | L'adresse mail qui sera utilisée pour la vérification certbot
    - `FLOWER_USER` | Votre propre nom d'utilisateur·ice pour accéder à la surveillance des files d'attente Flower
    - `EMAIL_HOST_USER` | L'adresse "From" que l'application utilisera pour l'envoi de mail
    - `EMAIL_HOST_PASSWORD` | Le mot de passe fourni par votre service mail
- Initialize secrets by running `bw-dev create_secrets` or manually update following in `.env`:
    - `SECRET_KEY` | Une chaîne de caractères, difficile à deviner
    - `POSTGRES_PASSWORD` | Un mot de passe sécurisé pour la base de données
    - `REDIS_ACTIVITY_PASSWORD` | Un mot de passe sécurisé pour le Redis d'activités
    - `REDIS_BROKER_PASSWORD` | Un mot de passe sécurisé pour le Redis de files d'attente
    - `FLOWER_PASSWORD` | Votre propre mot de passe sécurisé pour accéder à la surveillance des files d'attente Flower
    - Si vous faites fonctionner un autre serveur web sur votre machine, vous devez suivre les [instructions de proxy inverse](/reverse-proxy.html)
- Setup ssl certificate via letsencrypt by running `./bw-dev init_ssl`
- Initialisez la base de données avec `./bw-dev migrate`
- Run the application with `docker-compose up --build`, and make sure all the images build successfully
    - Si vous faites fonctionner d'autres services sur votre machine, vous pourriez rencontrer des erreurs avec certains services tentant de s'attribuer un port. Consultez le [guide de dépannage](#port_conflicts) pour avoir des conseils de résolution à ce sujet.
- Une fois que les images docker sont construites avec succès, arrêtez le processus avec `CTRL-C`
- Si vous souhaitez utiliser un stockage externe pour les fichiers statiques et médias (comme un service compatible S3), [suivez les instructions](/external-storage.html) jusqu'à ce que celles-ci indiquent de revenir ici
- Initialisez l'application avec `./bw-dev setup` et copiez le code admin afin de l'utiliser pour créer votre compte admin.
    - La sortie de `./bw-dev setup` devrait se terminer par votre code admin. Vous pouvez récupérer votre code à tout moment en lançant `./bw-dev admin_code` depuis la ligne de commande. Voici un exemple du résultat :

``` { .sh }
*******************************************
Use this code to create your admin account:
c6c35779-af3a-4091-b330-c026610920d6
*******************************************
```

- Lancez docker-compose en arrière-plan avec : `docker-compose up -d`
- L'application devrait fonctionner sur votre nom de domaine. Quand vous chargez le nom de domaine, vous devriez arriver sur une page de configuration pour confirmer les paramètres de votre instance et un formulaire pour créer un compte admin. Utilisez votre code admin pour vous enregistrer.

Bravo ! Vous avez réussi !! Configurez votre instance comme vous le souhaitez.


## Sauvegardes

Le service db de BookWyrm créer une copie de sauvegarde de sa base de données dans le dossier `/backups` chaque jour à minuit UTC. Les sauvegardes sont nommées `backup__%Y-%m-%d.sql`.

Le service db possède un script optionnel pour nettoyer périodiquement le dossier des sauvegardes afin que les sauvegardes récentes soient conservées ainsi que les sauvegardes mensuelles et hebdomadaires. Pour activer ce script :

- Décommentez la dernière ligne dans `postgres-docker/cronfile`
- Reconstruisez votre instance `docker-compose up --build`

Vous pouvez copier les sauvegardes depuis le volume de sauvegardes vers votre machine avec `docker cp` :

- Lancez `docker-compose ps` pour vérifier le nom du service db (probablement `bookwyrm_db_1`).
- Lancez `docker cp <container_name>:/backups <host machine path>`

## Conflits de port

BookWyrm a plusieurs services fonctionnant sur leurs ports par défaut. Cela veut dire que, en fonction de ce qui fonctionne sur votre machine, vous pouvez rencontrer des erreurs à la construction et au lancement de BookWyrm lorsque les tentatives d'utiliser ces ports échouent.

Si cela arrive, vous devrez changer votre configuration pour lancer ces services sur des ports différents. Cela peut demander des modifications dans les fichiers suivants :

- `docker-compose.yml`
- `nginx/production.conf` or `nginx/reverse_proxy.conf` depending on NGINX_SETUP in .env-file
- `.env` (Vous créer ce fichier vous-même durant la configuration)

Si vous avez déjà un serveur web sur cette machine, vous devrez configurer un proxy inverse.

## Restez à l'affût

BookWyrm étant un projet jeune, nous travaillons toujours pour planifier une version stable et il y a beaucoup de bogues et de changements cassants. Il y a une équipe GitHub qui peut être mentionnée quand quelque chose d'important à propos d'une mise à jour se passe et que vous pouvez rejoindre en partageant votre nom d'utilisateur·ice GitHub. Il y a plusieurs manières d'entrer en contact :

 - Open an issue or pull request to add your instance to the [official list](https://joinbookwyrm.com/instances/)
 - Contacter le projet sur [Mastodon](https://tech.lgbt/@bookwyrm) ou [envoyer un mail au mainteneur·ice](mailto:mousereeve@riseup.net) directement avec votre nom d'utilisateur·ice GitHub
 - Rejoindre le salon de discussion [Matrix](https://matrix.to/#/#bookwyrm:matrix.org)
