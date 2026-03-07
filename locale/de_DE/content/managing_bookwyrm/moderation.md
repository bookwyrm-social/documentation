---
Title: Moderation
Date: 2021-04-18
Order: 3
---

## Nutzer\*innen-Aktionen

### Blockieren

Nutzer\*innen können andere Nutzer\*innen selbstständig blockieren, ohne dass ein\*e Moderator\*in eingreift. In der Verwaltungsansicht "Föderierte Instanzen" können Administrator\*innen einsehen, wie viele Nutzer\*innen einer Instanz von lokalen Nutzer\*innen blockiert worden sind.

### Melden

Nutzer\*innen können Beiträge oder Nutzer\*innen melden. Bei Beiträgen geht das über die Schaltfläche "Mehr Optionen" im Fußbereich eines Posts, bei Konten über die (Ent-)Folgen-Schaltfläche. Wenn eine Meldung eingeht, erhalten alle Nutzer\*innen mit Administrations-Berechtigungen eine Benachrichtigung.

Um Meldungen einzusehen, gehe zu `Administration > Moderation > Meldungen`.

Moderator\*innen haben unterschiedliche Optionen, auf Meldungen zu reagieren:

- Der gemeldeten Person eine Direktnachricht senden.
- Den gemeldeten Beitrag löschen.
- Das Konto deaktivieren. Bei lokalen Nutzer\*innen sorgt das dafür, dass sie sich nicht mehr einloggen können und ihr Konto nicht mehr in der Anwendung angezeigt wird. Für Nutzer\*innen anderer Instanzen wird der Server alle eingehenden Aktivitäten dieses Kontos ablehnen. Das Konto wird außerdem nicht in der Suche auftauchen.

## Automatisierte Moderation

Regeln für die automatisierte Moderation bewirken, dass Berichte erstellt werden über lokale Benutzer\*innen oder Beiträge, die die angegebene Zeichenkette in irgendeinem Feld nutzen. Nutzer\*innen und Beiträge, die schon gemeldet worden sind (unabhängig davon, ob die Meldung bearbeitet und abgeschlossen wurde), werden nicht markiert. Um Regeln für die automatisierte Moderation zu erstellen, gehe zu `Administration > Moderation > Regeln für automatisierte Moderation`.

## Moderation auf Instanzebene

### Instanzen händisch sperren

Moderator\*innen können gesamte Instanzen sperren. Das verhindert, dass Aktivitäten von dieser Instanz eintreffen, und deaktiviert alle Konten der Instanz lokal. Um eine Instanz zu sperren, gehe zu `Administration > Föderation > Föderierte Instanzen` und suche nach der Instanz, die du sperren möchtest. Weitere Informationen dazu gibt es unter `BookWyrm verwalten > Föderation`.

Wenn die Instanz entsperrt wird, werden alle deaktivierten Konten wieder aktiviert.

### FediBlock-Listen

Moderator\*innen können außerdem Sperrlisten im Format _FediBlock_ hochladen, um Server gesammelt zu sperren. Gehe hierfü zu `Föderation > Föderierte Instanzen` und klicke auf "Instanz hinzufügen".

### Sperrlisten für E-Mails und IPs

Du kannst Anmeldungen mit einer gegebenen E-Mail-Domain unter `Administration > Moderation > E-Mail-Sperrliste` sperren. Wenn jemand versucht, sich mit einer E-Mail-Adresse einer gesperrten Domain anzumelden, wird kein Account angelegt. Der Registrierungsprozess wird so wirken, als habe er funktioniert.

Eine Sperrliste für IP-Adressen wird sämtlichen Datenverkehr von dieser IP-Adresse sperren. Anfragen von dieser IP-Adresse nach jedem Teil deiner Instanz werden mit einer 404-Rückmeldung beantwortet.

### Link-Domains

Nutzer\*innen können jedem Buch einen Download-Link hinzufügen. Die Domains dieser Links müssen genehmigt werden, bevor sie auf den Buchseiten erscheinen, um Spam und bösartige Links zu vermeiden. Du kannst Link-Domains unter `Administration > Moderation > Link-Domains` genehmigen.

## Föderation deaktivieren

Administrator\*innen und Moderator\*innen können die Föderation komplett deaktivieren. Das wird die gesamte zukünftige eingehende und ausgehende Kommunikation unterbinden. Bestehende Daten bleiben allerdings in der Datenbank erhalten. Die Föderation zu deaktivieren hält die Konnektoren nicht davon ab, Bücher zu importieren, aber es beschränkt alle Beiträge (Rezensionen, Kommentare etc.) auf Nutzer\*innen deiner Instanz und das, was sie händisch importieren (z. B. von Goodreads durch einen CSV-Import).

Um die Föderation zu deaktivieren, gehe zu `Administration > Föderation > Föderationseinstellungen`.

