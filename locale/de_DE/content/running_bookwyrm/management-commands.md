---
Title: Verwaltungs-Befehle
Date: 2023-04-26
Order: 11
---

Im Verzeichnis `bookwyrm/management/commands` gibt es einige Befehle, um die Datenbank der Instanz zu bearbeiten. Einige davon werden hier dokumentiert.

## Objekte zusammenführen

Es geschieht recht oft, dass eine Instanz doppelte Bücher, Autor_innen oder Editionen vorhält, die zwar separat erscheinen, aber eigentlich nur verschiedene Editionen desselben Werks sind. Das passiert, wenn Editionen ohne gleichnamige Identifikationsmerkmale importiert werden oder Benutzer_innen Fehler machen. Es gab außerdem vor Version 0.7.5 einen Bug, der eine große Zahl doppelter Bücher, Editionen und Autor\*innen erstellte. Unglücklicherweise gibt es bis auf Weiteres keine Oberfläche, um dies zu korrigieren. In Fällen, in denen die Bücher wichtig für deine Instanz sind, kannst du aber diese Verwaltungs-Befehle nutzen, um manche der Probleme zu beheben. Voraussetzung hierfür ist Version 0.6.2 oder neuer.

Bitte sei besonders vorsichtig, wenn du diese Befehle ausführst, da es im Falle eines Fehlers keinen Weg gibt, die Aktion rückgängig zu machen.

### Editionen zusammenführen

Wenn eine Edition eines Buches zweimal in der Datenbank auftaucht und du sicher bist, dass sie tatsächlich dieselbe Edition meinen, kannst du sie mit einem Befehl wie diesem zusammenführen:

```
./bw-dev runweb python manage.py merge_editions --canonical=27 --other=38
```

Dies wird alle fehlenden Informationen von Edition 38 (die andere, engl. „other“) zu Edition 27 (die kanonische, engl. „canonical“) übertragen und dann die andere Edition löschen. Wenn es ein Feld in beiden Editionen gibt, werden die Daten der kanonischen Edition behalten. Wenn die andere Edition Teil einer Liste ist, Kommentare hat oder rezensiert wurde, werden diese Informationen künftig ebenfalls auf die kanonische Edition verweisen.

Du kannst die Nummern für den Befehl herausfinden, indem du die Seite eines Buches besuchst und die Zahl in der URL anschaust.

### Autor\*innen zusammenführen

Du kannst potenziell doppelte Autor\*innen mit `show_duplicate_authors` identifizieren:

```sh
./bw-dev runweb python manage.py show_duplicate_authors
```

Dies wird alle _potenziell_ doppelten Autor_innen-Datensätze auflisten, basierend ausschließlich auf ihrem Namen. Ebenfalls angeführt werden ihre Lebensdaten, sofern vorhanden, die Anzahl der Bücher beider Autor_innen und ein Link zu ihren Seiten auf deiner Instanz. Beachte dass **du prüfen musst, ob es sich tatsächlich um Duplikate handelt**, bevor du sie zusammenführst, da es sich um unterschiedliche Autor\*innen mit demselben Namen handeln könnte.

Sobald du dies geprüft hast, kannst du doppelte Autor\*innen mit einem Befehl wie diesem zusammenführen:

```sh
./bw-dev runweb python manage.py merge_authors --canonical=7 --other=46
```

Wie bei den Editionen werden zusätzliche Informationen des anderen Eintrags zum kanonischen Eintrag kopiert und dann wird der andere Eintrag gelöscht. Alle Bücher, die der_die andere Autor_in geschrieben hat, werden mit dem kanonischen Eintrag verknüpft. Du kannst die Nummern für den Befehl herausfinden, indem du die Seite der Autor\*innen besuchst und die Zahl in der URL anschaust.

## ISBNs berichtigen

In Version 0.8.0 gab es einen Bug, der unter bestimmten Bedingungen ISBN10-Einträge mit 11 Stellen generierte. Dies wurde in einer Datenmigration in Version 0.8.1 behoben, aber aus diversen Gründen kann es notwendig sein, händisch einen Aufräumbefehl auszuführen, um alle fehlerhaften ISBNs in deiner lokalen Datenbank zu berichtigen:

```sh
./bw-dev runweb python manage.py fix_isbn10_entries
```
