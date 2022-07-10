- - -
Titel: Berechtigungen Datum: 2021-04-18 Bestellung: 2
- - -

Der Benutzerzugriff auf verschiedene Funktionen wird über das [integrierte Authentifizierungssystem von Django](https://docs.djangoproject.com/en/3.2/topics/auth/default/) gesteuert. Wenn eine Instanz erstellt wird, erstellt das `initdb`-Skript eine Reihe von Berechtigungen, die auf Gruppen übertragen werden. Standardmäßig wird allen neuen Benutzern die `-Editor-Gruppe` zugewiesen, die es ihnen erlaubt, Buch-Metadaten zu bearbeiten.

Der Instanzadministrator sollte `Superuser` Status haben, was Zugriff auf Django Admin (`/admin`) gibt und diesem Benutzer alle Berechtigungen überträgt.

## Berechtigungen und Gruppen
Diese Tabelle zeigt die vier Gruppen (Administrator, Moderator, Editor und Benutzer) und welche Berechtigungen Benutzer in dieser Gruppe haben:

|                                 | Administrator | Moderator | Editor | Benutzer |
| ------------------------------- | ------------- | --------- | ------ | -------- |
| Instanzeinstellungen bearbeiten | ✔️            | -         | -      | -        |
| ändere Benutzerlevel            | ✔️            | -         | -      | -        |
| verwalte Föderation             | ✔️            | ✔️        | -      | -        |
| sende Einladungen               | ✔️            | ✔️        | -      | -        |
| deaktiviere Benutzer            | ✔️            | ✔️        | -      | -        |
| entferne Beiträge               | ✔️            | ✔️        | -      | -        |
| bearbeite Bücher                | ✔️            | ✔️        | ✔️     | -        |
 lade Titelbilder hoch | ✔️ | ✔️ | ✔️ | ✔️
