---
Title: Systemüberwachung
Date: 2021-04-18
Order: 4
---

Das Menü `Administration > System` bietet Instanz-Administrator\*innen eine Reihe an Funktionen für die Systemüberwachung sowie Konfigurationsoptionen für Aufgaben, die im Hintergrund ausgeführt werden.

## Importe

Auf der Seite **Importe** kannst du Buch-Importe sowie Exporte und Importe von Konten verwalten. Exporte von Konten sind standardmäßig deaktiviert. Auf dieser Seite kannst du Buch- und Konto-Importe überwachen und abbrechen, falls sie Fehler verursachen. Außerdem kannst du begrenzen, wie oft Nutzer\*innen Importe ausführen können. Das ist wichtig, wenn deine Instanz Performanzprobleme erleidet, weil im Hintergrund eine große Zahl an Import- und Exportprozessen läuft.

## Celery-Status

Die Seite **Celery-Status** gibt einen Überblick über die Celery-Aufgaben und kann anzeigen, welche Warteschlangen verantwortlich sein könnten, falls deine Instanz langsamer wird. Auf dieser Seite kannst du auch gesamte Warteschlagen und Aufgaben leeren – allerdings nur als allerletzte Option, weil es zu Datenverlust führen kann.

## Geplante Aufgaben

Du kannst Aufgaben unter `Administration > System > Geplante Aufgaben` überblicken. Aufgaben werden auf anderen Seiten ausgelöst.

## E-Mail-Konfiguration

Prüfe hier deine Konfigurationen für ausgehende E-Mails. Du kannst auch eine Test-E-Mail versenden. Es kann sein, dass diese Seite in Zukunft an eine andere Stelle umzieht.

## Konnektoren

Konnektoren sind Datenquellen für Bücher und Autor\*innen. Auf dieser Seite kannst du Konnektoren (de-)aktivieren und ihre Priorität festlegen. Andere BookWyrm-Server, Inventaier und Open Library sind standardmäßig aktiviert.

Die Priorität bestimmt, in welcher Reihenfolge Suchergebnisse erscheinen. Die höchste Priorität ist 1. Die Standardpriorität ist 2. Konnektoreneinstellungen bestimmen nur, ob ein Konnektor verwendet wird, um Suchergebnisse auszuliefern. Um die Föderation und Moderation zu konfigurieren, siehe `Administration > Föderation` oder `Administration > Moderation`.

## Dateiverwaltung

In diesem Bereich kannst du eine Reihe von Hintergrundaufgaben einrichten, die Import- und Exportdateien sowie Buch-Cover betreffen.

Unter **Löschung von Dateien planen** kannst du die regelmäßige Aufgabe einrichten, Dateien von Kontoim- und -exporten zu löschen, die ihr Verfallsdatum erreicht haben. Das Verfallsdatum wird unter **Ablaufdatum der Exportdateien** festgelegt.

Der Abschnitt **Titelbilder über Connectoren abrufen** kann dir helfen, zwei unterschiedliche aber verwandte Probleme zu lösen.

Mit **Fehlende Titelbilder finden** kannst du eine regelmäßige Aufgabe einrichten, in der lokalen Datenbank nach allen Büchern zu suchen, die keine Angabe zum Titelbild enthalten. Diese Aufgabe sucht über die Konnektoren nach Titelbildern, die sie zur Verfügung stellen können. Das erlaubt es beispielsweise, ein Titelbild einer verknüpften BookWyrm-Instanz zu nutzen, auf der es kürzlich hochgeladen wurde, ohne dass es eine Nachricht an deine Instanz gab, das aktualisierte Titelbild hinzuzufügen. Dieser Vorgang kann ressourcenintensiv sein, da er für jedes Buch in deiner Datenbank, das kein Titelbild hat, einen Suchprozess anstößt, also bedenke dies, wenn du einstellst, wie oft die Aufgabe ausgeführt werden soll.

**Finde fehlerhafte Dateipfade für Titelbilder** kann händisch ausgelöst werden, aber nicht als regelmäßige Aufgabe eingeplant werden. Die meisten Administrator\*innen werden diese Aufgabe nicht ausführen müssen. Sie wurde eingerichtet, um Probleme mit Server-Migrationen zu beheben, bei denen Buchdatensätze ein Titelbild aufführen, das nicht im Dateispeicher existiert.