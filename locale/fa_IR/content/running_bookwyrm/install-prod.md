- - -
Title: Installing in Production Date: 2025-04-01 Order: 1
- - -

This project is still young and isn't, at the moment, very stable, so please proceed with caution when running in production.

## Server setup
- Get a domain name and set up DNS for your server. You'll need to point the nameservers of your domain on your DNS provider to the server where you'll be hosting BookWyrm. Here are instructions for [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)
- Set your server up with appropriate firewalls for running a web application (this instruction set is tested against Ubuntu 20.04). Here are instructions for [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
- Set up an email service (such as [Mailgun](https://documentation.mailgun.com/en/latest/quickstart.html)) and the appropriate SMTP/DNS settings. Use the service's documentation for configuring your DNS
- [Install Docker and docker-compose](https://docs.docker.com/compose/install/)

## Install and configure BookWyrm

There are several repos in the BookWyrm org, including documentation, a static landing page, and the actual Bookwyrm code. To run BookWyrm, you want the actual app code which is in [bookwyrm-social/bookwyrm](https://github.com/bookwyrm-social/bookwyrm).

The `production` branch of BookWyrm contains a number of tools not on the `main` branch that are suited for running in production, such as `docker-compose` changes to update the default commands or configuration of containers, and individual changes to container config to enable things like SSL or regular backups.

Instructions for running BookWyrm in production:

- Get the application code: `git clone git@github.com:bookwyrm-social/bookwyrm.git`
- Switch to the `production` branch: `git checkout production`
- Create your environment variables file, `cp .env.example .env`, and update the following:
    - `DOMAIN` | Your web domain
    - `EMAIL` | Email address to be used for certbot domain verification
    - `FLOWER_USER` | Your own username for accessing Flower queue monitor
    - `EMAIL_HOST_USER` | The "from" address that your app will use when sending email
    - `EMAIL_HOST_PASSWORD` | The password provided by your email service
- Initialize secrets by running `./bw-dev create_secrets` or manually update following in `.env`:
    - `SECRET_KEY` | A difficult to guess, secret string of characters
    - `POSTGRES_PASSWORD` | Set a secure password for the database
    - `REDIS_ACTIVITY_PASSWORD` | Set a secure password for Redis Activity subsystem
    - `REDIS_BROKER_PASSWORD` | Set a secure password for Redis queue broker subsystem
    - `FLOWER_PASSWORD` | Your own secure password for accessing Flower queue monitor
    - If you are running another web-server on your host machine, you will need to follow the [reverse-proxy instructions](/reverse-proxy.html)
- Check that you have [all the required settings configured](/environment.html#required-environment-settings) before proceeding further
- Setup ssl certificate via letsencrypt by running `./bw-dev init_ssl`
- Initialize the database by running `./bw-dev migrate`
- Run the application with `docker-compose up --build`, and make sure all the images build successfully
    - If you are running other services on your host machine, you may run into errors where services fail when attempting to bind to a port. See the [troubleshooting guide](#port_conflicts) for advice on resolving this.
- When docker has built successfully, stop the process with `CTRL-C`
- If you wish to use an external storage for static assets and media files (such as an S3-compatible service), [follow the instructions](/external-storage.html) until it tells you to come back here
- Initialize the application with `./bw-dev setup`, and copy the admin code to use when you create your admin account.
    - The output of `./bw-dev setup` should conclude with your admin code. You can get your code at any time by running `./bw-dev admin_code` from the command line. Here's an example output:

``` { .sh }
*******************************************
Use this code to create your admin account:
c6c35779-af3a-4091-b330-c026610920d6
*******************************************
```

- Run docker-compose in the background with: `docker-compose up -d`
- The application should be running at your domain. When you load the domain, you should get a configuration page which confirms your instance settings, and a form to create an admin account. Use your admin code to register.

Congrats! You did it!! Configure your instance however you'd like.


## Backups

BookWyrm's db service dumps a backup copy of its database to its `/backups` directory daily at midnight UTC. Backups are named `backup__%Y-%m-%d.sql`.

The db service has an optional script for periodically pruning the backups directory so that all recent daily backups are kept, but for older backups, only weekly or monthly backups are kept. To enable this script:

- Uncomment the final line in `postgres-docker/cronfile`
- rebuild your instance `docker-compose up --build`

You can copy backups from the backups volume to your host machine with `docker cp`:

- Run `docker-compose ps` to confirm the db service's full name (it's probably `bookwyrm_db_1`.
- Run `docker cp <container_name>:/backups <host machine path>`

## Port Conflicts

BookWyrm has multiple services that run on their default ports. This means that, depending on what else you are running on your host machine, you may run into errors when building or running BookWyrm when attempts to bind to those ports fail.

If this occurs, you will need to change your configuration to run services on different ports. This may require one or more changes the following files:

- `docker-compose.yml`
- `nginx/production.conf` or `nginx/reverse_proxy.conf` depending on NGINX_SETUP in .env-file
- `.env` (You create this file yourself during setup)

If you are already running a web-server on your machine, you will need to set up a reverse-proxy.

## Get Connected

Because BookWyrm is a young project, we're still working towards a stable release schedule, and there are a lot of bugs and breaking changes. There is a GitHub team which can be tagged when there's something important to know about an update, which you can join by sharing your GitHub username. There are a few ways in get in touch:

 - Open an issue or pull request to add your instance to the [official list](https://joinbookwyrm.com/instances/)
 - Reach out to the project on [Mastodon](https://tech.lgbt/@bookwyrm) or [email the maintainer](mailto:mousereeve@riseup.net) directly with your GitHub username
 - Join the [Matrix](https://matrix.to/#/#bookwyrm:matrix.org) chat room
