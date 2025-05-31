---
Title: Installation sans Docker
Date: 2022-10-02
Order: 2
---

Ce projet est encore jeune et n'est pas, pour le moment, très stable, faites preuve de prudence lors de son utilisation en production. Ce mode d'installation nécessite plus de travail, et est donc à réserver aux administrateurs plus expérimentés. L'installation via docker est recommandée Cette méthode d'installation suppose que vous ayez déjà configuré ssl, avec les certificats à votre disposition

## Configuration du serveur
- Obtenez un nom de domaine et configurez le DNS pour votre serveur. Vous devez faire pointer les serveurs de noms de domaine de votre fournisseur DNS vers le serveur où vous allez héberger BookWyrm. Voici les instructions pour [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Configurez votre serveur avec des pare-feu appropriés pour l'exécution d'une application web (ces instructions ont été testées avec Ubuntu 20.04). Voici les instructions pour [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Configurez un service de messagerie (tel que [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) et les paramètres SMTP/DNS appropriés. Utilisez la documentation du service pour la configuration de votre DNS
- Installez les dépendances. Sous debian, cela pourrait ressembler à `apt install postgresql redis nginx python3-venv python3-pip python3-dev libpq-dev`

## Installez et configurez BookWyrm

La branche `production` de BookWyrm contient un certain nombre d'outils qui ne sont pas sur la branche `main`, prévus pour fonctionner en production, tels que des modifications de `docker-compose` pour mettre à jour les commandes par défaut ou la configuration des conteneurs, ou des modifications spécifiques à des containers pour activer des fonctionnalités telles que SSL ou des sauvegardes régulières. Tous ces changements n'ont pas nécessairement un impact sur l'installation sans docker, mais la branche `production` est néanmoins recommandée

Instructions pour l'exécution de BookWyrm en production sans Docker :

- Créez et déplacez vous dans le répertoire où vous voulez installer BookWyrm. Par exemple `/opt/bookwyrm` : `mkdir /opt/bookwyrm && cd /opt/bookwyrm`
- Téléchargez le code de l'application : `git clone git@github.com:bookwyrm-social/bookwyrm.git ./`
- Passez sur la branche `production` : `git checkout production`
- Créez votre fichier de variables d'environnement, `cp .env.example .env`, et mettez à jour ce qui suit :
    - `SECRET_KEY` | Une chaîne de caractères secrète, difficile à deviner
    - `DOMAIN` | Votre domaine web
    - `POSTGRES_PASSWORD` | Utilisez un mot de passe sécurisé pour la base de données
    - `POSTGRES_HOST` | Mettez à `localhost` (la machine exécutant votre bdd)
    - `POSTGRES_USER` | Mettez à `bookwyrm` (recommendé) ou une valeur personnalisée (configurée plus tard)
    - `POSTGRES_DB` | Définir à `bookwyrm`
    - `REDIS_ACTIVITY_PASSWORD` | Laissez à blanc (adapté pour une machine locale avec un pare-feu)
    - `REDIS_ACTIVITY_HOST` | Mettez à `localhost` (la machine exécutant redis)
    - `REDIS_BROKER_PASSWORD` | Laissez à blanc (adapté pour une machine locale avec un pare-feu)
    - `REDIS_BROKER_HOST` | Mettez à `localhost` (la machine exécutant redis)
    - `EMAIL_HOST_USER` | L'adresse d'expéditeur de laquelle votre application enverra des emails
    - `EMAIL_HOST_PASSWORD` | Le mot de passe fourni par votre service d'emailing
- Configurez nginx
    - Copiez le fichier server_config vers le répertoire conf.d de nginx : `cp nginx/server_config /etc/nginx/conf.d/server_config`
    - Faites une copie du modèle de configurationde site de production et mettez le en place dans nginx&nbsp;: `cp nginx/production /etc/nginx/sites-available/bookwyrm.conf`
    - Mettez à jour le fichier `bookwyrm.conf` de nginx :
        - Remplacez `your-domain.com` par votre nom de domaine partout dans le fichier (y compris dans les lignes qui sont pour l'instant commentées)
        - Remplacez `/app/` avec votre chemin d'installation `/opt/bookwyrm/` partout dans le fichier (y compris dans les commentaires)
        - Décommentez les lignes 18 à 67 pour activer la redirection vers HTTPS. Vous devriez avoir deux blocs `server` actifs
        - Remplacez les chemins de `ssl_certificate` et `ssl_certificate_key` par ceux de votre fullchain et privkey
        - Modifiez la ligne 4 en `server localhost:8000`. Vous pouvez choisir un port différent si vous le souhaitez
        - Si vous exécutez un autre serveur web sur votre machine hôte, vous devrez suivre [les instructions pour serveur mandataire inverse](/reverse-proxy.html)
    - Activez la configuration nginx : `ln -s /etc/nginx/sites-available/bookwyrm.conf /etc/nginx/sites-enabled/bookwyrm.conf`
     - Rechargez la configuration nginx : `systemctl reload nginx`
- Configurez l'environnement virtuel python
    - Créez le répertoire venv python dans votre répertoire d'installation : `mkdir venv` `python3 -m venv ./venv`
    - Installez les dépendances python de bookwyrm avec pip : `./venv/bin/pip3 install -r requirements.txt`
- Créez la base de données postgresql de bookwyrm. Assurez-vous de remplacer le mot de passe par ce que vous avez défini dans la configuration `.env` :

    `sudo -i -u postgres psql`

```
CREATE USER bookwyrm WITH PASSWORD 'securedbypassword123';

CREATE DATABASE bookwyrm TEMPLATE template0 ENCODING 'UNICODE';

ALTER DATABASE bookwyrm OWNER TO bookwyrm;

GRANT ALL PRIVILEGES ON DATABASE bookwyrm TO bookwyrm;

\q
```

- Migrez le schéma de la base de données en exécutant `venv/bin/python3 manage.py migrate`
- Initialisez la base de données en exécutant `venv/bin/python3 manage.py initdb`
- Générez les static en exécutant `venv/bin/python3 manage.py collectstatic --no-input`
- Si vous souhaitez utiliser un stockage externe pour les ressources statiques et les fichiers multimédias (comme un service compatible S3), [suivez les instructions](/external-storage.html) jusqu'à être redirigé ici
- Créez et configurez votre utilisateur `bookwyrm`
    - Créez l'utilisateur système bookwyrm: `useradd bookwyrm -r`
    - Modifiez l’appartenance du répertoire d’installation de bookwyrm : `chown -R bookwyrm:bookwyrm /opt/bookwyrm`
    - Vous devriez maintenant exécuter les commandes liées à bookwyrm avec l'utilisateur de bookwyrm : `sudo -u bookwyrm echo I am the $(whoami) user`

- Générez le code administrateur avec `sudo -u bookwyrm venv/bin/python3 manage.py admin_code`, et copiez le pour l'utiliser lors de la création du compte administrateur.
- Vous pouvez obtenir ce code à n'importe quel moment en ré-exécutant la commande. Voici un exemple de sortie :

``` { .sh }
*******************************************
Use this code to create your admin account:
c6c35779-af3a-4091-b330-c026610920d6
*******************************************
```

- Créez et configurez le script d'exécution
    - Créez un fichier nommé dockerless-run.sh et remplissez le avec le contenu suivant

``` { .sh }
#!/bin/bash

# stop if one process fails
set -e

# bookwyrm
/opt/bookwyrm/venv/bin/gunicorn bookwyrm.wsgi:application --bind 0.0.0.0:8000 &

# celery
/opt/bookwyrm/venv/bin/celery -A celerywyrm worker -l info -Q high_priority,medium_priority,low_priority &
/opt/bookwyrm/venv/bin/celery -A celerywyrm beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler &
# /opt/bookwyrm/venv/bin/celery -A celerywyrm flower &
```
    - Remplacez `/opt/bookwyrm` par votre répertoire d'installation
    - Remplacez `8000` par votre numéro de port personnalisé
    - Flower a été ici désactivé parce qu'il n'est pas configuré automatiquement avec le mot de passe défini dans le fichier `.env`
- Vous pouvez à présent exécuter BookWyrm avec&nbsp;: `sudo -u bookwyrm bash /opt/bookwyrm/dockerless-run.sh`
- L'application devrait s'exécuter sur votre domaine. Lorsque vous chargez le domaine, vous devriez obtenir une page de configuration qui confirme vos paramètres d'instance, ainsi qu'un formulaire pour créer un compte d'administrateur. Utilisez votre code d'administration pour vous inscrire.
- Vous pouvez configurer BookWyrm pour qu'il s'exécute automatique à l'aide d'un service systemd. Voici un exemple :
```
# /etc/systemd/system/bookwyrm.service
[Unit]
Description=Bookwyrm Server
After=network.target
After=systemd-user-sessions.service
After=network-online.target

[Service]
User=bookwyrm
Type=simple
Restart=always
ExecStart=/bin/bash /opt/bookwyrm/dockerless-run.sh
WorkingDirectory=/opt/bookwyrm/

[Install]
WantedBy=multi-user.target
```
Vous devrez configurer une tâche Cron pour que le service démarre automatiquement au redémarrage du serveur.

Félicitations ! Vous y êtes arrivé !! Configurez votre instance comme vous le souhaitez.

## Participer

Voir [Participer](https://joinbookwyrm.com/get-involved/) pour plus de détails.
