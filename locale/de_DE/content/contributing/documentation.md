---
Title: Dokumentation
Date: 2025-04-09
Order: 4
---

Die Dokumentation, die du gerade liest, wird von der BookWyrm-Community gepflegt. Jede Person kann zur Dokumentation beitragen.

## Eine Verbesserung vorschlagen

Du kannst einen **Fehler** (engl. error) melden, eine **Verbesserung** (engl. improvement) vorschlagen oder eine **Ergänzung** (engl. addition) zur Dokumentation anfragen, indem du [einen Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) im [Dokumentations-Repository](https://github.com/bookwyrm-social/documentation) anlegst.

## Wie die Dokumentation erstellt wird

Die Dokumentation [hat ihr eigenes GitHub-Repository](https://github.com/bookwyrm-social/documentation). Sie wird in Markdown verfasst und wir nutzen [Jinja](https://jinja.palletsprojects.com/en/stable) und ein Python-Skript, um sie in HTML umzuwandeln. Ein Jinja-Plugin wird gemeinsam mit Crowdin genutzt, um Übersetzungen zu erstellen. Alle Quelldateien der Dokumentation sollen in US-Englisch verfasst werden.

Alle Quelldatein werden im `content`-Verzeichnis abgelegt. Jeder Abschnitt hat darin ein Verzeichnis, wobei jede Seite durch eine einzelne Markdown-Datei abgebildet wird.

## Dokumentationsseiten bearbeiten oder anlegen

Um eine neue Seite anzulegen, ist Folgendes notwendig:

1. klone [das GitHub-Repository](https://github.com/bookwyrm-social/documentation)
2. arbeite im `content`-Verzeichnis, um deine Änderungen vorzunehmen – indem du entweder eine bestehende Markdown-Seite anpasst oder eine neue erstellst
3. erstelle eine neue Pull Request
4. nimm weitere Änderungen vor, wenn du Rückmeldungen erhältst
5. genieße, wie deine Änderungen sofort veröffentlicht werden, sobald deine Pull Request angenommen und gemerget wurde

Wenn du noch nie Git oder GitHub verwendet hast, mag das alles beängstigend klingen, aber lass es uns herunterbrechen:

### Klone das Repository

1. Stelle sicher, dass du [einen GitHub-Account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) hast.
2. Erstelle einen "Klon" oder "Fork" des Dokumentations-Repositorys:

   - Auf der **Web-Oberfläche** klicke "Fork" am oberen Rand [dieser Seite](https://github.com/bookwyrm-social/documentation)
   - Wenn du **GitHub Desktop** verwendest, folge [diesen Anweisungen](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop)
   - Wenn du die Kommandozeile nutzt, führe aus:

   `git clone https://github.com/bookwyrm-social/documentation.git`

### Einen neuen Branch erstellen und Änderungen vornehmen

Um Änderungen vorzunehmen:

1. [Erstelle einen neuen Branch](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue) in deinem Fork
2. Nimm deine Änderungen am `content`-Verzeichnis vor und **commite** sie:
   - [GitHub-Web-Oberfläche](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)
   - [GitHub Desktop](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop)
   - In der Kommandozeile, speichere deine Änderungen an den Dateien und führe `git commit` aus

An dieser Stelle wirst du vielleicht sehen wollen, wie deine Änderungen aussehen, wenn sie veröffentlicht werden. Schau dir [Dokumentation lokal bauen](#building-docs-locally) weiter unten an, um zu erfahren, wie du eine Vorschau deiner Änderungen ansehen kannst.

### Eine Pull Request erstellen

Wenn deine Änderungen abgeschlossen sind, [erstelle eine Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) an das Dokumentations-Repository.

Deine Pull Request wird überprüft werden und eines der drei folgenden Szenarien wird eintreten:

1. Sie wird ohne Änderungen **übernommen** (engl. merged)
2. Du wirst gebeten, **Änderungen** vorzunehmen
3. Sie wird **abgelehnt** und geschlossen

### Auf Überprüfungen reagieren

Wenn du gebeten wirst, Änderungen vorzunehmen, kannst du dies lokal erledigen und deine lokalen Änderungen an deinen Fork/Klon auf Github senden (engl. `push`). Sie werden dann automatisch in deine Pull Request übernommen. Lass den\*die Reviewer\*in wissen, wenn du mit deinen Anpassungen fertig bist, damit die Person eine weitere Überprüfung starten und dann hoffentlich deine Änderungen zu sich holen (engl. `pull`) kann.

Wir heißen alle Beiträge willkommen. Es wäre ungewöhnlich, wenn ein Beitrag zur Dokumentation direkt abgelehnt würde. Das würde nur dann geschehen, wenn deine Pull Request Informationen einfügt, die falsch oder irreführend ohne Aussicht auf Besserung sind oder wenn festgestellt wird, dass sie aus dem Rahmen fällt.

### Deine Änderungen werden veröffentlicht

Wenn deine Pull Request übernommen wird, wird [die Dokumentation](https://docs.joinbookwyrm.com/) automatisch aktualisiert. Es kann sein, dass du deinen Browser neu starten oder den "Inkognito-Modus" nutzen musst, um die Änderungen in deinem Browser zu sehen.

## Neue Seiten

Wenn du eine neue Seite hinzufügst, wirst du einige Metadaten angeben und andere Seite anpassen müssen.

Am Anfang jeder Markdown-Datei befindet sich die Titelei im `toml`-Format:

```toml
Title: Dokumentation
Date: 2025-04-09
Order: 4
```

Dieses Beispiel zeigt, dass die Seite "Dokumentation" heißt, in ihrem Abschnitt (in diesem Fall: "Wie mitmachen") an vierter Stelle angezeigt werden soll, und dass sie zuletzt am 9. April 2025 aktualisiert wurde. Wenn du die Seite nicht am Ende eines Abschnittes hinzufügst, wirst du die Reihenfolge (`order`) jeder Seite anpassen müssen, die unter deiner neuen Seite erscheinen soll.

Die Titelei wird von einem Paar dreifacher Bindestriche (`---`) umschlossen. In Markdown können dreifache Bindestriche auch für eine horizontale Trennlinie verwendet werden, allerdings kann dies den Parser für die BookWyrm-Dokumentation verwirren. Wenn du eine horizontale Trennlinie brauchst, nutze hierfür direkt den HTML-Code mit einer Leerzeile davor und danach:

```html

<hr/>

```

## Die Dokumentation lokal bauen

Bevor du eine Pull Request einreichst, wirst du dir anschauen wollen, wie deine Änderungen am Ende aussehen werden. Das Dokumentations-Repository enthält – wie das Haupt-Quelltext-Repository – ein Entwicklungs-Skript mit demselben Namen: `bw-dev`. Du kannst es benutzen, um zu testen, wie deine Änderungen aussehen werden.

Anders als im Hauptprojekt läuft die Dokumentation nicht in einem Docker-Container. Wenn du die Dokumentationsseite lokal kompilieren möchtest, wirst du alle Abhängigkeiten installieren müssen, und es ist empfehlenswert, [eine virtuelle Umgebung](https://docs.python.org/3/library/venv.html) zu nutzen:

```py
python -m venv /path/to/new/virtual/environment
source <venv>/bin/activate
pip install -r requirements.txt
```

Eine ganze Reihe von Befehlen ist verfügbar, wenn du `./bw-dev <command>` ausführst. Du wirst wahrscheinlich diese nutzen wollen:

### site:compile

Dieser Befehl wird deine Markdown-Dateien mithilfe des Skripts `generator.py` zu HTML kompilieren.

Wenn du `site:compile` ausführst, wird es im Verzeichnis `site` eine große Menge Dateien erzeugen. Checke diese nicht ein und füge sie nicht deiner Pull Request bei: Sie werden auf dem Dokumentations-Server neu generiert, wenn deine Pull Request übernommen wird.

### site:serve

Dieser Befehl startet einen lokalen Web-Server unter `http://[::1]:8080/`, damit du dir ansehen kannst, wie die Dokumentation aussehen wird.

### black

Dieser Befehl wird `black` ausführen, um deine Dateien zu analysieren und auftretende Probleme durch unsere automatischen Überprüfungen zu erkennen. Es ist unwahrscheinlich, dass du dies brauchen wirst, wenn du nur die Quelldateien der Dokumentation im Ordner `content` aktualisierst.

## Hinweise für Dokumentations-Maintainer

### Übersetzungen

Halte Übersetzungen konsistent, indem du sie regelmäßig von Crowdin aktualisierst:

1. Übersetzungen werden in Crowdin aktualisiert
2. Crowdin pusht neue Übersetzungen nach `l10n_main`, wenn sie verfügbar sind
3. in deinem Fork, pulle sowohl `main` als auch `l10n_main`, sodass dein lokales Repository aktuell ist
4. erstelle einen neuen Branch, der von `main` abzweigt (z. B. mit dem Namen `update_locales`), und checke ihn aus
5. merge das Verzeichnis `locale` von `l10n_main` in deinen Fork: `git checkout l10n_main -- locale`
6. nimm Änderungen vor, falls dies nötig ist
7. pushe deinen lokalen Branch zu deinem entfernten Repository und erstelle eine Pull Request
8. übernimm die Pull Request in `main`
9. es gibt nun eine neue Referenzdatei in `en_US`
10. mit den Änderungen in der neuen Referenzdatei werden die Übersetzungen in Crowdin angepasst ...

Die Lokalisierungen für die Sprachauswahl sind in `i18n.py` aufgeführt. Im Allgemeinen warten wir, bis eine Sprache in Crowdin zu 70 % abgedeckt ist, bevor wir sie zur Liste hinzufügen, um zu vermeiden, dass zu viel Inhalt unübersetzt bleibt.

### Updaten, wenn eine neue Version veröffentlicht wurde

Wenn eine neue Version von BookWyrm veröffentlicht wird, müssen wir eine neue Version der Dokumentation erstellen:

1. Füge einen Branch hinzu, dessen Name exakt dem neuen Versions-Tag in BookWyrm entspricht. Zum Beispiel `v0.x.y`.
2. Füge den Namen des neuen Branches zur Liste der Versionen in `generate.py` hinzu und pushe deinen neuen Branch zum Repository.
3. Wechsle nacheinander auf jede andere Version und merge die aktualisierte Datei `generate.py`, sodass sie alle den neuen Branch enthalten: `git checkout v0.x.y generate.py`. Dann commite diese Änderung, erstelle eine Pull Request, um die Änderung in den Branch dieser Version in der Dokumentation zu übernehmen, und übernimm sie. Das wird dafür sorgen, dass alle Seiten in allen Versionen der Dokumentation alle anderen Versionen im Auswahlmenü auflisten.
4. Merge die neue `generate.py` zuletzt in den `main`-Branch – nur Übernahmen in `main` lösen GitHub-Actions aus, um die Dokumentation auf den Web-Server auszurollen. Falls du dies also zuerst erledigst, werden die Änderungen in den anderen Branches keinen Effekt haben, bis du das nächste Mal `main` aktualisierst.