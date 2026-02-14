---
Title: Föderation
Date: 2026-01-18
Order: 2
---

## Föderationseinstellungen

Administrator\*innen und Moderator\*innen können die Föderation komplett deaktivieren. Das wird die gesamte zukünftige eingehende und ausgehende Kommunikation unterbinden. Bestehende Daten bleiben allerdings in der Datenbank erhalten. Die Föderation zu deaktivieren hält die Konnektoren nicht davon ab, Bücher zu importieren, aber es beschränkt alle Beiträge (Rezensionen, Kommentare etc.) auf Nutzer\*innen deiner Instanz und das, was sie händisch importieren (z. B. von Goodreads durch einen CSV-Import).

Um die Föderation zu deaktivieren, gehe zu `Admin > Federation > Federation Settings`.

## Föderierte Instanzen

At `Admin > Federation > Federated Instances` you can see all instances connected to yours via federation. This list may be quite long, as it will include every ActivityPub server that has sent or received a status or object. This list will show you the instance domain and software the instance is running.

You can click on the instance domain to find out more information about the instance including how many users have come from that instance. You can also block the instance completely from here.