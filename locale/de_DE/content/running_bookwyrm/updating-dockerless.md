---
Title: Aktualisieren ohne Docker
Date: 2023-01-29
Order: 4
---

Folge dieser Anleitung, wenn du eine BookWyrm-Installation ohne Docker hast und Änderungen im `production`-Branch verfügbar sind.

Diese Anleitung nimmt an, dass du beim Aufsetzen der aktuellsten ["Installation ohne Docker"](/install-prod-dockerless.html)-Anleitung gefolgt bist.

Führe alle folgenden Befehle, sofern nicht anders angegeben, als `bookwyrm`-Nutzer aus:

1. Ziehe die neuesten Änderungen im `production`-Branch mit `git pull`
2. Installiere potenzielle neue Python-Abhängigkeiten:
   - `./venv/bin/pip3 install --upgrade "pip>=25.1.0"`
   - `./venv/bin/pip3 install --group main`
3. Kompiliere die Themes mit dem Befehl venv/bin/python3 manage.py compile_themes\`
4. Sammle alle statischen Dateien mit `venv/bin/python3 manage.py collectstatic --no-input` – dies lädt sie auch in [externe Speicher](/external-storage.html) hoch, sofern du dies eingerichtet hast
5. Migriere die Datenbank (es ist empfehlenswert, vorher eine Sicherung anzulegen) mit `venv/bin/python3 manage.py migrate`
6. Starte die `systemd`-Dienste neu mit `sudo systemctl restart bookwyrm bookwyrm-worker bookwyrm-scheduler`
