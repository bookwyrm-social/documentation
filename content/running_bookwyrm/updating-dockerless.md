---
Title: Updating Without Docker
Date: 2023-01-29
Order: 4
---

Follow this guide if you have a BookWyrm installation without Docker and
there are changes available in the production branch.

This guide assumes that your setup followed the latest [Installation without Docker](/install-prod-dockerless.html) guide.

Run all the following commands, except otherwise noted, as the `bookwyrm` user:

1. Pull in the latest changes on the `production` branch with `git pull`
2. Install potential new Python dependencies:
   - `./venv/bin/pip3 install --upgrade "pip>=25.1.0"`
   - `./venv/bin/pip3 install --group main`
3. Compile the themes with `venv/bin/python3 manage.py compile_themes`
4. Collecting all the static files with `venv/bin/python3 manage.py collectstatic --no-input` – this also uploads them to [external storage](/external-storage.html) if you have this configured
5. Migrate the database (it's advisable to create a backup before) with `venv/bin/python3 manage.py migrate`
6. Restart the `systemd` services with `sudo systemctl restart bookwyrm bookwyrm-worker bookwyrm-scheduler`
