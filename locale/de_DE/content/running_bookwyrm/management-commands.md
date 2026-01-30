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

If an edition of a book appears twice in the database and you are sure they are actually both referring to same edition, you can combine them into one with a command like this:

```
./bw-dev runweb python manage.py merge_editions --canonical=27 --other=38
```

This will copy any missing information from edition 38 (the “other” edition) over to edition 27 (the “canonical” edition) and then delete the other edition. If any field of information is in both editions then the data from the canonical edition will be kept. If the other edition is in any lists or has any comments or reviews etc then these will all be updated to point to the canonical edition instead.

You can find the numbers to use in the command by visiting the page for a book and looking at the number in the URL.

### Merging authors

You can identify potential duplicate authors with `show_duplicate_authors`:

```sh
./bw-dev runweb python manage.py show_duplicate_authors
```

This will list all your _potential_ duplicate author records, based purely on their name, showing their birth and death dates if available, the count of books for each author, and a link to their page on your instance. Note that **you must check that these are actually duplicates** before merging them as they may be different authors with the same name.

Once confirmed, if an author is duplicated you can combine the two authors into one with a command like this:

```sh
./bw-dev runweb python manage.py merge_authors --canonical=7 --other=46
```

As for the editions, any extra information from the other author will be copied over to the canonical author and then the other author will be deleted. Any books written by the other author will be changed to be written by the canonical author. You can find the numbers to use in the command by visiting the page for an author and looking at the number in the URL.

## Fixing ISBNs

There was a bug in `v0.8.0` which erroneously created 11-digit ISBN10 entries in some circumstances. This was fixed in a data migration in `v0.8.1`, however for various reasons you may need to manually run a cleanup command to fix any incorrect ISBNs in your local database:

```sh
./bw-dev runweb python manage.py fix_isbn10_entries
```
